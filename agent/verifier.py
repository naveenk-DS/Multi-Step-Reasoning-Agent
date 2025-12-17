import json
from agent.llm.openai_llm import OpenAILLM
from agent.llm.mock_llm import MockLLM
from agent.config import LLM_PROVIDER

def _choose_llm():
    return MockLLM() if LLM_PROVIDER == "mock" else OpenAILLM()

def run_verifier(question: str, intermediate: str, final_answer: str):
    llm = _choose_llm()
    with open("agent/prompts/verifier_prompt.txt") as f:
        template = f.read()

    payload = {
        "question": question,
        "intermediate_solution": intermediate,
        "final_answer": final_answer
    }

    prompt = template + "\n\n" + json.dumps(payload)
    response = llm.generate(prompt)

    return json.loads(response)
