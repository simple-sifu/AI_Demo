# RAG Workshop — Class Notes

---

## 1. Why RAG Exists (The Motivation)

The instructor framed this around three concrete problems with using a raw LLM alone:

### Knowledge cutoff

Every LLM is trained on data scraped up to a specific date. After that, it has **zero awareness** of new events — not "outdated knowledge," but literally no information at all.

> **Example:** GPT-3.5, with a cutoff around September 2021.

### Private / internal data

No public model has ever seen your company's internal wikis, tickets, or docs, so it **structurally can't** answer questions about them.

### Business control over outputs

Using a Walmart search example — a customer searching **"jam"** might technically get a relevant but undesired result (e.g., a competitor's private-label product like Kirkland/Costco jam).

The business wants to **bias retrieval** toward its own inventory / high-margin products, not just "technically correct" matches.

---

## 2. What "Retrieval" Really Means

The instructor pushed back on a common misconception:

> **Retrieval ≠ vector databases or embeddings**

Retrieval is defined **functionally** — any mechanism that surfaces relevant information for a query counts, including:

- Google search
- E-commerce search bars
- A human doing manual lookup

**Vector search** is just one popular implementation.

---

## 3. Embeddings, Explained Geometrically

- An embedding model converts text into a **numeric vector** (in production, often 1,000+ dimensions).
- The key property: **semantically similar text** produces vectors pointing in similar directions.
- This is measured via **cosine similarity** — the cosine of the angle between two vectors:

| Angle | Cosine | Meaning |
|-------|--------|---------|
| 0° | 1 | Identical direction — highly similar meaning |
| 90° | 0 | Unrelated |
| 180° | -1 | Opposite |

This lets a system match **"car insurance"** to a document titled **"vehicle insurance"** even though no words overlap — something a traditional exact-match SQL query would fail at:

```sql
WHERE title = 'car insurance'  -- misses "vehicle insurance"
```

---

## 4. Why Chunking Matters

A big theme: embedding a huge, topically diverse document (the **"Encyclopedia problem"**) produces a vague, generic vector that ends up superficially matching almost every query — which is **useless for retrieval**.

### Example: Elon Musk's Wikipedia page

If a user asks only about his **political affiliations**, embedding the entire page (business, politics, wealth, public image, etc. all mixed together) gives poor results.

**Instead:** split the page into sections — politics, legal affairs, business — and embed each separately. The system can then retrieve just the relevant section.

> **Chunking** = breaking documents into smaller, topically focused pieces before embedding.

---

## 5. Vector Databases

Once chunks are embedded, they're stored in a **vector database**, which has essentially two jobs:

1. **Store** large volumes of vectors
2. **Perform similarity search** against a query vector extremely fast — even across billions of records

### Scale example

The instructor cited **Walmart's scale**: with ~2 billion products, their vector index is roughly that size, and searches still return in a fraction of a second.

### Top-K

A **top-k** parameter (e.g., `k=3`) controls how many of the closest-matching chunks get returned as context. Choosing the right **k** is treated as an empirical tuning decision (to be covered in the next session).

---

## 6. Offline vs. Online Stages

A useful distinction was drawn with color-coding in the diagram:

| Stage | Color | What happens | Latency concern? |
|-------|-------|--------------|------------------|
| **Offline** | Green | Chunking, generating embeddings, refreshing the vector DB | No — no customer waiting |
| **Online** | Yellow | Embed query → retrieve matches → generate answer | Yes — customer is waiting |

### Offline (green)

- Chunk documents, generate embeddings, refresh the vector DB
- Can run on a schedule
- **Walmart example:** nightly batch refresh, since product titles/descriptions change constantly as merchants update listings

### Online (yellow)

- Embed the incoming user query, retrieve matches, generate the final answer
- Happens live while a customer waits
- Bigger/slower embedding models or bloated vector DBs **directly hurt user experience**

### Student Q&A: Avoiding downtime during vector DB updates

Real-time streaming updates are technically possible, but **cost** (continuous compute for embedding on-the-fly) is the tradeoff against doing periodic batch refreshes.

---

## 7. Assembling the Final Prompt (Augmentation)

Once top-k chunks are retrieved, they're combined with:

- The original user query
- Explicit instructions (e.g., "be concise," "only use the provided context")
- Formatting guidance
- Citation requirements

…into a single **augmented prompt**, which is then passed to the LLM for the **generation** step.

---

## 8. Hands-On Setup (Practical Portion)

For the coding exercise — a customer support bot using ~20 historical tickets as a knowledge base — the environment setup involved:

### Environment

| Item | Details |
|------|---------|
| Python | 3.12 |
| Package manager | **uv** — fast, Rust-based; creates `.venv` and installs from `requirements.txt` in parallel |
| Secrets | `.env` file (renamed from `.env.example`) holding the OpenAI API key |

### OpenAI embedding models

| Model | Dimensions | Cost | Notes |
|-------|------------|------|-------|
| `text-embedding-ada-002` | 1536 | — | Older, legacy model |
| `text-embedding-3-small` | 1536 | ~$0.02 / 1M tokens | Good default choice |
| `text-embedding-3-large` | 3072 | ~6× cost of small | High-stakes domains only (medical, financial) |

### Demo dataset

A JSON knowledge base of **20 support tickets**, each with fields like:

- Ticket ID
- Title
- Description
- Resolution
- Category
- Priority
- Timestamps

Intended to simulate a real customer-support RAG use case.
