# 🚀 Directive-Orchestrated AI Engine (DOE)

A deterministic, multi-agent AI workflow engine built with **FastAPI + Async OpenAI**, designed to execute structured AI pipelines using directive-controlled orchestration instead of uncontrolled LLM chaining.

---

## 🧠 What This Project Is

This project implements a **Directive-Orchestrated Executable (DOE)** — a structured AI execution engine where:

* Execution order is controlled by code
* Agents operate via shared structured state
* Retry logic is rule-driven
* Critic-based evaluation enables iterative refinement
* The system is fully asynchronous

Instead of letting the LLM decide flow dynamically, the engine enforces deterministic execution through a defined workflow.

---

## 🏗 Architecture Overview

```
FastAPI (Async API Layer)
        ↓
Directive Engine
        ↓
Execution Engine (Async)
        ↓
Agents (Planner → Researcher → Writer → Critic → Finalizer)
        ↓
Shared State Object
```

---

## 🔄 Execution Flow

1. User sends request to `/chat`
2. Directive defines execution steps
3. Engine executes agents sequentially
4. Critic evaluates output
5. If not approved → retry loop (max_iterations)
6. Final output returned

---

## 📦 Features

* ✅ Async OpenAI integration
* ✅ Deterministic multi-agent orchestration
* ✅ Structured state management
* ✅ Retry loop with approval logic
* ✅ Critic-based quality control
* ✅ Modular agent architecture
* ✅ FastAPI API layer
* ✅ Swagger auto-docs
* ✅ Expandable for parallelism and tools

---

## 🗂 Project Structure

```
backend/
│
├── main.py
├── config.py
│
├── directives/
│   ├── schema.py
│   ├── generator.py
│   └── executor.py
│
├── agents/
│   ├── base.py
│   ├── planner.py
│   ├── researcher.py
│   ├── writer.py
│   ├── critic.py
│   └── finalizer.py
│
├── execution/
│   └── store.py
│
└── utils/
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd multi-agent/backend
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Mac/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Create `.env`

```
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Running the Server

```bash
uvicorn main:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Example API Call

### Request

```json
POST /chat

{
  "message": "Write a blog about AI in healthcare"
}
```

### Response

```json
{
  "plan": "...",
  "research": "...",
  "draft": "...",
  "critique": {
    "feedback": "...",
    "approved": false
  },
  "approved": false
}
```

---

## 🧠 Agent Roles

### Planner

Creates structured outline from user input.

### Researcher

Generates structured research notes from plan.

### Writer

Produces full draft using plan + research.

### Critic

Evaluates draft and returns:

```
{
  "feedback": "...",
  "approved": true/false
}
```

### Finalizer

Outputs final version.

---

## 🔁 Retry Logic

If:

```
retry_if_not_approved = True
```

The system will:

* Re-run writer with critic feedback
* Re-evaluate with critic
* Stop after `max_iterations`

This enables iterative refinement.

---

## 🔐 Why Directive-Orchestrated?

Most AI apps:

```
LLM → LLM → LLM → LLM
```

Flow is uncontrolled.

This system:

* Separates orchestration from intelligence
* Enforces deterministic execution
* Applies loop constraints
* Supports future branching & parallelism
* Is production-extendable

---

## 🚀 Future Improvements

* Parallel agent execution
* Tool-calling integration
* Cost & token tracking
* Redis-based state persistence
* Workflow templates
* Execution timeline visualization
* Scoring instead of binary approval
* Multi-critic voting

---

## 🏆 Use Cases

* AI content pipelines
* Research automation
* Structured report generation
* Enterprise AI orchestration
* Controlled multi-agent experimentation

---

## 📌 Current Limitations

* In-memory state store
* No persistent database
* No horizontal scaling
* No job queue
* Limited evaluation scoring
* Single-process execution

---

## 🧩 Tech Stack

* Python 3.11+
* FastAPI
* AsyncOpenAI
* Pydantic
* Uvicorn

---

## 📄 License

MIT License

---

# 🎯 Summary

This project demonstrates how to build a deterministic AI execution engine using structured directives and modular agent orchestration — moving beyond naive prompt chaining toward production-grade AI architecture.

