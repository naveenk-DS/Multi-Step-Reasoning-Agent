import json
from agent.llm.openai_llm import OpenAILLM
from agent.llm.mock_llm import MockLLM
from agent.config import LLM_PROVIDER

def _choose_llm():
    return MockLLM() if LLM_PROVIDER == "mock" else OpenAILLM()

def run_planner(question: str):
    llm = _choose_llm()
    with open("agent/prompts/planner_prompt.txt") as f:
        template = f.read()

    prompt = template + f'\n\nQuestion: "{question}"\nPlan:'
    response = llm.generate(prompt)

    return json.loads(response)["plan"]
