# multi-llm-api-starter

Lightweight unified multi-LLM API gateway.

Unify OpenAI and Gemini interface, one set of code calls all mainstream large models.

- Unified request format, compatible with OpenAI standard SDK
- Support local rapid deployment, zero complex configuration
- Low resource consumption, suitable for backend service integration

## Install Dependencies

```bash
pip install openai google-generativeai
```

## Env Config

```bash
# Mac / Linux
export OPENAI_API_KEY=your_key_here
export GEMINI_API_KEY=your_key_here

# Windows CMD
set OPENAI_API_KEY=your_key_here
set GEMINI_API_KEY=your_key_here
```
## Local Client Usage (unified_llm_client.py)

```python
from unified_llm_client import UnifiedLLMClient

client = UnifiedLLMClient()

# Call OpenAI GPT
gpt_res = client.chat("gpt-4o", "your question")
print(gpt_res)

# Call Google Gemini
gem_res = client.chat("gemini-1.5-flash", "your question")
print(gem_res)
```

## Params Explain

- `model_name`: Specify target LLM model
- `prompt`: Input query for model generation
- `Return`: Raw text output from LLM

## Supported Models

### OpenAI Series
- `gpt-4o`
- `gpt-4-turbo`
- `gpt-3.5-turbo`

### Google Gemini Series
- `gemini-1.5-flash`
- `gemini-1.5-pro`
