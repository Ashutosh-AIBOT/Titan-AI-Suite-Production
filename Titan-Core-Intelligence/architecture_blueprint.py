"""
📚 AGNO LEARNING NOTES & SNIPPETS
----------------------------------
This file contains essential concepts for building production-ready agents 
using Agno and NVIDIA NIM.
"""

from agno.agent import Agent
from agno.models.nvidia import Nvidia
from agno.tools.duckduckgo import DuckDuckGoTools

# 1. CORE CONCEPT: The Agent
# An agent is an LLM with 'Instructions', 'Tools', and 'Memory'.
def basic_agent_example():
    agent = Agent(
        model=Nvidia(id="meta/llama-3.1-8b-instruct"),
        instructions="You are a helpful assistant.",
        markdown=True
    )
    # agent.print_response("Hello!")
    return agent

# 2. CORE CONCEPT: Tools
# Tools allow the agent to interact with the world.
def tool_agent_example():
    agent = Agent(
        model=Nvidia(id="meta/llama-3.1-8b-instruct"),
        tools=[DuckDuckGoTools()],
        instructions="Use web search to find the latest info.",
        show_tool_calls=True
    )
    return agent

# 3. CORE CONCEPT: Memory (Sessions)
# Agno supports persistent storage using SQL.
# Example: Using SQLite to save chat history.
"""
from agno.storage.agent.sqlite import SqlAgentStorage
storage = SqlAgentStorage(table_name="agent_sessions", db_file="agents.db")
agent = Agent(storage=storage, add_history_to_messages=True)
"""

# 4. CORE CONCEPT: Knowledge (RAG)
# You can attach a Knowledge Base (PDFs, URLs) to an agent.
"""
from agno.knowledge.pdf import PDFUrlKnowledgeBase
knowledge_base = PDFUrlKnowledgeBase(urls=["https://example.com/file.pdf"])
agent = Agent(knowledge_base=knowledge_base, search_knowledge=True)
"""

# 🚀 PRO TIP: Use 'debug_mode=True' to see exactly what the LLM is thinking!
# agent = Agent(model=llm, debug_mode=True)

if __name__ == "__main__":
    print("Agno Learning Notes Loaded. Run individual functions to test concepts.")
