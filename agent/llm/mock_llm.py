import json
from agent.llm.base import LLMBase


class MockLLM(LLMBase):
    """
    Deterministic mock LLM for offline testing.
    Always returns valid JSON in the expected format.
    """

    def generate(self, prompt: str) -> str:

        # ---------- PLANNER ----------
        if "Planner module" in prompt or "generate a concise numbered plan" in prompt:
            return json.dumps({
                "plan": [
                    "Extract relevant quantities",
                    "Handle time or arithmetic logic",
                    "Perform calculation",
                    "Format final answer"
                ]
            })

        # ---------- EXECUTOR ----------
        if "Executor" in prompt or "Follow the plan EXACTLY" in prompt:

            # Overnight movie case
            if "23:40" in prompt and "01:10" in prompt:
                return json.dumps({
                    "intermediate_solution": (
                        "Movie crosses midnight. "
                        "From 23:40 to 24:00 = 20 min, "
                        "from 00:00 to 01:10 = 70 min, "
                        "total = 90 min"
                    ),
                    "final_answer": "1 hour 30 minutes"
                })

            # Train case
            if "14:30" in prompt:
                return json.dumps({
                    "intermediate_solution": "14:30=870m, 18:05=1085m, diff=215m",
                    "final_answer": "3 hours 35 minutes"
                })

            # Apples case
            if "apples" in prompt:
                return json.dumps({
                    "intermediate_solution": "Green apples = 6, Total = 9",
                    "final_answer": "9"
                })

            return json.dumps({
                "intermediate_solution": "Mock calculation",
                "final_answer": "Mock answer"
            })

        # ---------- VERIFIER ----------
        if "Verifier module" in prompt:
            return json.dumps({
                "passed": True,
                "issues": ""
            })

        return json.dumps({})
