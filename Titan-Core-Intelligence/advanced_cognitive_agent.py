import logging
import time
import os
from functools import wraps
from typing import Optional, List
from agno.agent import Agent
from agno.models.nvidia import Nvidia
from agno.db.sqlite import SqliteDb
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.file import FileTools
from pathlib import Path
from dotenv import load_dotenv

# --- CONFIGURATION & LOGGING ---
load_dotenv()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("TitanCore")

# Create exports directory
# Modified to use consolidated outputs/exports folder
export_path = Path(__file__).parent.parent / "outputs" / "exports"
export_path.mkdir(parents=True, exist_ok=True)

# --- ADVANCED FEATURE: RATE LIMITING ---
def rate_limit(calls_per_minute: int):
    interval = 60.0 / calls_per_minute
    last_called = [0.0]
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            if elapsed < interval:
                wait_time = interval - elapsed
                logger.warning(f"Rate limit hit. Waiting {wait_time:.2f}s...")
                time.sleep(wait_time)
            result = func(*args, **kwargs)
            last_called[0] = time.time()
            return result
        return wrapper
    return decorator

# --- ADVANCED FEATURE: USAGE & LATENCY TRACKING ---
class TitanAgent(Agent):
    def print_response(self, *args, **kwargs):
        start_time = time.time()
        result = super().print_response(*args, **kwargs)
        latency = time.time() - start_time
        
        # Calculate word count for "Token Simulation"
        word_count = len(str(result).split())
        logger.info(f"--- TITAN METRICS ---")
        logger.info(f"Latency: {latency:.2f}s | Est. Words: {word_count} | Status: Success")
        return result

# --- DATABASE SETUP ---
# Modified to use database folder
db_path = Path(__file__).parent.parent / "database" / "session_storage.db"
db_path.parent.mkdir(parents=True, exist_ok=True)
db = SqliteDb(db_file=str(db_path))

# --- MASTER AGENT FACTORY ---
@rate_limit(calls_per_minute=20)
def get_advanced_agent(session_id: Optional[str] = "titan_master"):
    return TitanAgent(
        model=Nvidia(id="meta/llama-3.1-8b-instruct"),
        name="Titan-Master-Agent",
        session_id=session_id,
        db=db,
        instructions=[
            "You are a production-grade AI assistant. Accuracy and speed are your top priorities.",
            "You have the ability to save your research into the 'exports' folder using your file tools.",
            "Always structure your output in professional Markdown.",
            "If a query requires extensive research, save a summary to a file named 'research_report.md'."
        ],
        tools=[
            DuckDuckGoTools(), 
            FileTools(base_dir=export_path)
        ],
        add_history_to_context=True,
        add_session_state_to_context=True,
        markdown=True,
        stream=True
    )

if __name__ == "__main__":
    master_agent = get_advanced_agent()
    logger.info("Titan Master Agent initialized with File Export capability.")
    master_agent.print_response("Research the latest news on SpaceX Starship and save a summary to 'spacex_report.md'")
