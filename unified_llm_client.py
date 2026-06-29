# Unified LLM client for GPT & Gemini single entry call
import os

class UnifiedLLMClient:
    def __init__(self):
        self.openai_key = os.getenv("OPENAI_API_KEY")
        self.gemini_key = os.getenv("GEMINI_API_KEY")

    def chat(self, model_name: str, prompt: str) -> str:
        """
        Unified chat entry
        :param model_name: target llm, e.g. gpt-4o, gemini-1.5-flash
        :param prompt: user input text
        :return: llm response string
        """
        if model_name.startswith("gpt"):
            return self._call_gpt(prompt, model_name)
        elif model_name.startswith("gemini"):
            return self._call_gemini(prompt, model_name)
        return "unsupported model"

    def _call_gpt(self, prompt: str, model: str) -> str:
        return f"[{model}] GPT response: {prompt}"

    def _call_gemini(self, prompt: str, model: str) -> str:
        return f"[{model}] Gemini response: {prompt}"

if __name__ == "__main__":
    client = UnifiedLLMClient()
    print(client.chat("gpt-4o", "what is llm api aggregator"))
    print(client.chat("gemini-1.5-flash", "benefits of unified llm interface"))
