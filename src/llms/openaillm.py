from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

class OpenAILLM:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not found")

    def get_llm(self):
        return ChatOpenAI(
            model="gpt-4o-mini",
            api_key=self.api_key,
            temperature=0.7
        )