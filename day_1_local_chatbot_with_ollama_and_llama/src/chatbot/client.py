from rich.console import Console
from typing import Optional
import subprocess
import httpx
import json
from .config import settings
from .logger import logger

console = Console()

class OllamaClient:
    def __init__(self, model: Optional[str] = None):
        self.model = model or settings.model_name
        self.base_url = f"http://{settings.ollama_host}:{settings.ollama_port}"

    def run_via_http(self, prompt: str, stream: bool = True) -> str:
        url = f"{self.base_url}/api/generate"
        payload = {"model": self.model, "prompt": prompt, "stream": True}
        output_chunks = []

        try:
            with httpx.stream("POST", url, json=payload, timeout=None) as r:
                console.print("[magenta]Bot: [/magenta]", end="")
                r.raise_for_status()
                for line in r.iter_lines():
                    if not line:
                        continue
                    try:
                        data = json.loads(line)
                        chunk = data.get("response") or data.get("output") or data.get("text")
                        if chunk:
                            if stream:
                                print(chunk, end="", flush=True)
                            output_chunks.append(chunk)
                        if data.get("done"):
                            break
                    except json.JSONDecodeError as je:
                        logger.debug(f"Could not parse line: {line} ({je})")

            if stream:
                print()
            return "".join(output_chunks)

        except Exception as e:
            logger.debug(f"HTTP call failed: {e}")
            raise


    def run_via_subprocess(self, prompt: str) -> str:
        try:
            console.print("[magenta]Bot: [/magenta]", end="")
            result = subprocess.run(
                ["ollama", "run", self.model, prompt],
                capture_output=True,
                text=True,
                check=True,
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as exc:
            logger.error(f"Subprocess call failed: {exc.stderr}")
            raise

    def generate(self, prompt: str, stream: bool = True) -> str:
        """
        Generate text using the Ollama model.
        If stream=True, print chunks live and return final text without reprinting.
        """
        try:
            return self.run_via_http(prompt, stream=stream)
        except Exception as e:
            logger.warning(f"HTTP API failed, falling back to subprocess: {e}")
            return self.run_via_subprocess(prompt)
