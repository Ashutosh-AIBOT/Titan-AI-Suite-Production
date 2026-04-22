# 📊 Titan-Analytics-Pro

An autonomous **Data Science & Analytics Suite** powered by Agno and NVIDIA Llama 3.1. This suite manages a team of specialized agents to automate the entire machine learning pipeline.

---
### 🙏 Credits
Inspired by the multi-agent orchestration patterns shared by the **CampusX** YouTube channel. 
---

## 🌟 Advanced Features (Production Ready)
- **Multi-Agent Orchestration**: Specialized agents for loading, cleaning, visualizing, and coding.
- **Agentic State Management**: Maintains complex session states across the entire ML lifecycle.
- **Error-Correcting Python REPL**: The coding agent can execute, debug, and fix its own code.
- **REST API Deployment**: Built-in FastAPI integration for enterprise consumption.
- **Observability**: Latency tracking and structured logs for every agentic decision.

## 🚀 Execution
1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Serve the API:
   ```bash
   python analytics_orchestrator.py
   ```
3. The API will be available at `http://localhost:7777`.

## 📂 Project Structure
- `src/`: Clean, modularized Python tools for data manipulation and plotting.
- `data/`: Raw and processed data storage.
- `models/`: Fitted preprocessors and ColumnTransformers.
- `plots/`: Automated visualization outputs.
- `reports/`: Generated markdown analysis reports.
