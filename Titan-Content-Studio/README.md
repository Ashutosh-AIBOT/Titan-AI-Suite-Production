# ✍️ Titan-Content-Studio

An autonomous **Research & Content Generation Factory**. This suite leverages a team of research specialists across Arxiv, YouTube, Reddit, and X to create high-impact articles.

---
### 🙏 Credits
This project architecture draws inspiration from the agentic research workflows taught by **CampusX**.
---

## 🌟 Advanced Features
- **Cross-Platform Cognitive Research**: Orchestrates 10+ research agents simultaneously.
- **Context-Aware Drafting**: Uses RAG-based retrieval to ensure factual accuracy in generated articles.
- **Asynchronous Processing**: Optimized for high-throughput research.
- **Enterprise Tooling**: Includes Gmail integration for automated newsletter drafting and outreach.
- **Performance Monitoring**: Built-in tracking for API latency and token efficiency.

## 🚀 Execution
1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Serve the API:
   ```bash
   python content_creation_engine.py
   ```

## 📂 Architecture
- `research_papers/`: Local repository for downloaded academic resources.
- `medium_articles/`: Production-ready Markdown drafts.
- **Orchestrator**: A specialized Team Leader agent that delegates tasks based on topic complexity.
