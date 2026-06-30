"""
OctopusX Unified Multi-LLM Client
Lightweight universal gateway for multiple LLM providers
Unify OpenAI & Gemini request schema, standardize input/output format
Local deployment ready, eliminate repetitive SDK integration work
"""
import openai
import google.generativeai as genai

class UnifiedLLMClient:
    """
    Core unified client class for cross-provider LLM calling
    Automatically route requests to matched model provider, return consistent text response format
    """
    def chat(self, model_name: str, prompt: str):
        """
        Universal chat completion entrypoint
        :param model_name: Target model identifier, e.g. gpt-4o / gemini-1.5-flash
        :param prompt: Raw user input query text
        :return: Plain text generation output from LLM
        """
        # Keep all your original code below this line
