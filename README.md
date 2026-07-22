# AI_Demo

## Knowledge Base

- [Learning Theory](./KnowledgeBase/ICanStudy/README.md) — growth mindset, time management, deep processing, note taking, and more
- [SupportDesk RAG Workshop](./week2/SupportDesk-RAG-Workshop/README.md) — hands-on RAG project with LangChain, LlamaIndex, and OpenAI

---

## Retrieval-Augmented Generation (RAG)

### Pure Prompt vs. RAG

A **pure prompt** sends only the user's question to the LLM. The model generates an answer from what it already learned during training — it cannot see your private documents, tickets, or up-to-date data.

**RAG does not teach the model new data** via fine-tuning or retraining. Instead, it retrieves relevant information at query time and puts that context into the prompt. The model stays the same; what changes is the **context** you give it.

| Approach | How the model gets knowledge | Updates new data? |
|----------|------------------------------|-------------------|
| Pure prompt | Training data only | No — stale or missing |
| Fine-tuning | Retrain weights on new data | Yes — expensive, slow |
| **RAG** | Retrieve chunks at query time | Yes — update the index, not the model |

---

### What RAG Is

RAG has three steps:

#### 1. Retrieval

Search your **private knowledge base** using the user's question.

- Convert the query into an embedding (vector)
- Find the most similar document **chunks** in a vector store
- Return the top-K relevant pieces of information

> *Example:* User asks *"How do I fix login issues after a password reset?"* → retrieve support ticket chunks about authentication and session errors.

#### 2. Augmentation

Plug the retrieved chunks and the user's question into a **prompt template**.

```
You are a support assistant. Answer using ONLY the context below.

Context:
{retrieved_chunk_1}
{retrieved_chunk_2}

Question: {user_question}

Answer:
```

The LLM now has grounded facts to work with instead of guessing.

#### 3. Generation

Send the augmented prompt to the LLM and generate an answer **using the correct context**.

- The model synthesizes a natural-language response
- Good RAG systems cite or trace back to source chunks
- Safeguards can refuse to answer when context is insufficient (anti-hallucination)

---

### End-to-End RAG Pipeline

Before retrieval works, you build the knowledge base once (offline):

```
Documents → Chunking → Embeddings → Vector Store
```

At query time (online):

```
User Question → Embed Query → Retrieve Chunks → Augment Prompt → LLM → Answer
```

| Stage | Purpose | Workshop module |
|-------|---------|-----------------|
| Embeddings | Turn text into vectors for semantic search | `1_embeddings` |
| Chunking | Split documents into retrievable pieces | `2_chunking` |
| Indexing | Organize and search the vector store | `3_indexing` |
| RAG pipeline | Wire retrieval + generation together | `4_rag_pipeline` |
| Evaluation | Measure retrieval and answer quality | `5_evaluation` |
| Agentic RAG | Multi-step reasoning with tools | `6_agentic_rag` |

---

### Why Use RAG?

- **Factual accuracy** — answers grounded in your data, not hallucinations
- **Up-to-date** — add new documents without retraining the model
- **Private data** — use internal tickets, docs, and knowledge bases safely
- **Traceable** — show which chunks supported the answer
- **Cost-effective** — no fine-tuning required

---

### Setup (this repo)

**Install dependencies** (from project root):

```bash
# activate venv first (see below)
python -m pip install -r requirements.txt
```

> Use `-r` to install *from* a requirements file.  
> `pip install requirements.txt` tries to install a package literally named "requirements.txt" — that is not what you want.

**Environment** — this project uses [direnv](https://direnv.net/) with a venv at `~/venvs/AI_Demo`:

```bash
cd AI_Demo
direnv allow          # loads OPENAI_API_KEY and puts venv on PATH
which pip             # should show ~/venvs/AI_Demo/bin/pip
pip install -r requirements.txt
```

> **Note:** The RAG workshop requires **Python 3.12** (not 3.13/3.14) because `chromadb` depends on libraries that break on newer Python versions. See the [workshop README](./week2/SupportDesk-RAG-Workshop/README.md) for full setup.

**Run the first module:**

```bash
cd week2/SupportDesk-RAG-Workshop/modules/1_embeddings
python demo.py
```
