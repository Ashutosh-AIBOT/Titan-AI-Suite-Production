---
title: Titan AI Suite Production
emoji: 🧠
colorFrom: blue
colorTo: indigo
sdk: docker
app_file: app.py
pinned: false
---

# Titan AI Suite: Unified Multi-Agent Ecosystem

[![Framework: Agno](https://img.shields.io/badge/Framework-Agno-blueviolet)](https://agno.com)
[![Model: NVIDIA NIM](https://img.shields.io/badge/Model-NVIDIA%20NIM-green)](https://build.nvidia.com)
[![Streamlit: Unified UI](https://img.shields.io/badge/UI-Streamlit-FF4B4B)](https://streamlit.io)

Welcome to the **Titan AI Suite**, a high-end, production-grade consolidation of three specialized AI engines. This project leverages the **Agno (formerly Phidata)** framework and **NVIDIA NIM** to deliver an autonomous agentic experience for research, analytics, and content creation.

---

## Acknowledgments & Credits

This project was built as a deep-dive into the world of agentic AI. 
- **Inspiration & Learning**: Huge credit to **CampusX**. I have learned immensely about the **Agno** framework and the potential of multi-agent systems through their high-quality educational content. This suite is a culmination of those learnings, optimized and consolidated into a professional-grade repository.

---

## Key Features

### 1. Titan Core Intelligence (The Cognitive Brain)
*   **Autonomous Research**: Uses DuckDuckGo and local file tools for deep-web exploration.
*   **Resilient Reasoning**: Built-in rate limiting and latency tracking to ensure stable operation.
*   **Persistent Memory**: Uses SQLite to maintain session context across multiple runs.

### 2. Titan Analytics Pro (Automated Data Science)
*   **Multi-Agent Pipeline**: A specialized team (Data Loader, Viz Agent, Coding Agent) that automates the entire ML lifecycle.
*   **EDA & Visualization**: Automatically generates Matplotlib/Seaborn charts and provides statistical summaries.
*   **Code Generation**: Writes and executes Python code for data cleaning and model training.

### 3. Titan Content Studio (Research & Content Engine)
*   **Multi-Source Harvesting**: 9+ specialized agents scraping Arxiv, YouTube, Reddit, X (Twitter), Wikipedia, and HackerNews.
*   **Article Generation**: Synthesizes research into professional, publication-ready Medium-style articles.
*   **File Management**: Automatically saves drafts as Markdown files for easy export.

---

## 🛠 Project Structure

```bash
├── Titan-Core-Intelligence/  # Core reasoning & CLI agents
├── Titan-Analytics-Pro/      # ML & Data Science team orchestrators
├── Titan-Content-Studio/     # Research agents & Content pipelines
├── titan_app.py              # The Unified Streamlit Master UI
├── notes.md                  # Comprehensive Interview Prep & Technical Notes
├── HLD.md                    # High-Level Design & Architecture Diagrams
└── requirements.txt          # Deployment dependencies
```

---

## Quick Start

### 1. Environment Setup
```bash
# Activate your conda environment
conda activate agent

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration
Create a `.env` file in the root directory:
```env
NVIDIA_API_KEY=your_nvidia_api_key_here
```

### 3. Launch the Master Suite
The suite features a unified UI that integrates all engines into one dashboard:
```bash
python titan_suite.py ui
```

---

## System Architecture
For a deep-dive into the technical flow and agent interaction maps, please refer to the [High-Level Design (HLD.md)](./HLD.md) and the interactive **Architecture Map** available directly within the Streamlit UI.

---

## ☁️ Deployment Ready
This repository is pre-configured for **Hugging Face Spaces**. 
- **Entry Point**: `app.py`
- **Configuration**: See [deployment_guide.md](./deployment_guide.md) for step-by-step instructions.

---
**Titan AI Suite** | *Built with Agno, NVIDIA NIM, and a passion for agentic systems.*
