
from typing import List
from .client import OllamaClient
from .logger import logger

class ChatService:
    def __init__(self, client: OllamaClient):
        self.client = client
        # in-memory conversation history; small list of dicts
        self.history: List[dict] = []

    def send(self, user_text: str) -> str:
        prompt = self._build_prompt(user_text)
        try:
            out = self.client.generate(prompt, stream=True)
            self.history.append({"user": user_text, "bot": out})
            return out
        except Exception as exc:
            logger.error(f"Error generating response: {exc}")
            return "Sorry, something went wrong."


    def _build_prompt(self, user_text: str) -> str:
        # Simple multi-turn prompt builder for local LLMs
        history_text = "\n".join([f"User: {h['user']}\nAssistant: {h['bot']}" for h in self.history])
        if history_text:
            return f"{history_text}\nUser: {user_text}\nAssistant:"
        return f"User: {user_text}\nAssistant:"
