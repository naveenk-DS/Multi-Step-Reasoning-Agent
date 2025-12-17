import json
from agent.llm.openai_llm import OpenAILLM
from agent.llm.mock_llm import MockLLM
from agent.config import LLM_PROVIDER

def _choose_llm():
    return MockLLM() if LLM_PROVIDER == "mock" else OpenAILLM()

def run_executor(question: str, plan: list):
    llm = _choose_llm()
    with open("agent/prompts/executor_prompt.txt") as f:
        template = f.read()

    payload = {
        "question": question,
        "plan": plan
    }

    prompt = template + "\n\n" + json.dumps(payload)
    response = llm.generate(prompt)

    return json.loads(response)
