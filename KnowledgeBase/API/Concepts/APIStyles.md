# 6 API Styles — REST Isn't Always the Answer

Most teams default to REST for everything, then fight it for months.

The skill isn't knowing the styles. It's knowing **when each one earns its place**.

---

## 1. REST — Resources over plain HTTP

**The right default when:**

- Public APIs
- Lots of consumers
- Caching matters

**Skip it when:** one screen needs 5 round-trips to render.

---

## 2. GraphQL — The client asks for exactly the fields it needs

**Great when:** web, mobile, and partners all want different shapes.

**Not worth it when:** a single client has stable needs. You're buying a caching headache you don't have yet.

---

## 3. gRPC — Binary, schema-first, fast

**Best for:** internal service-to-service where you own both ends.

**Don't:** hand it to a browser without a proxy in front.

---

## 4. WebSocket — A persistent two-way pipe

**Use for:** chat, collaborative editing, live cursors.

**Overkill when:** "the dashboard refreshes every 30 seconds."

---

## 5. SSE (Server-Sent Events) — One-way server push over normal HTTP

**Use for:** notifications, feeds, streaming LLM tokens.

> **The most underrated one here.** Most "real-time" features need this, not WebSocket.

---

## 6. Webhooks — The server calls you when something happens

**Use for:** payments, CI events, integrations.

**Watch out:** now you own retries, ordering, and idempotency.

---

## Quick Reference

| Style | Direction | Best for |
|-------|-----------|----------|
| REST | Request/response | Public APIs, caching, many consumers |
| GraphQL | Client-shaped queries | Multiple clients, different data needs |
| gRPC | Request/response (binary) | Internal microservices |
| WebSocket | Two-way, persistent | Live collaboration, chat |
| SSE | Server → client push | Feeds, notifications, LLM streaming |
| Webhooks | Server → your endpoint | Event-driven integrations |

<img width="569" height="730" alt="Screenshot 2026-07-23 at 11 15 44 AM" src="https://github.com/user-attachments/assets/b5e94fa6-4b7b-4adc-b3a7-495bee9bc9af" />

