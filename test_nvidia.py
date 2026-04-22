import os
from agno.agent import Agent
from agno.models.nvidia import Nvidia
from dotenv import load_dotenv

load_dotenv()

def test_nvidia():
    agent = Agent(
        model=Nvidia(id="meta/llama-3.1-8b-instruct"),
        instructions="You are a helpful assistant.",
    )
    agent.print_response("Say hello in 5 words.")

if __name__ == "__main__":
    test_nvidia()
