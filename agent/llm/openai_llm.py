import os
from openai import OpenAI

from agent.llm.base import LLMBase
from agent.config import OPENAI_MODEL


class OpenAILLM(LLMBase):
    def __init__(self):
        # OpenAI client MUST be created here
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content
