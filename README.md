# multi-llm-api-starter
A lightweight unified API starter, use single API key to request GPT-5 / Gemini 3 / MiniMax simultaneously.

## Features
- Single key management for 3 mainstream LLMs
- OpenAI compatible request format
- Simple switch model without rewriting request logic
- Minimal dependency, fast deployment

## Quick Start Code Example
```python
from openai import OpenAI

# Unified endpoint & global key
client = OpenAI(
    api_key="YOUR_UNIFIED_KEY",
    base_url="https://octopusx.ai/v1"
)

# Call GPT-5
gpt_response = client.chat.completions.create(
    model="gpt-5",
    messages=[{"role": "user", "content": "your prompt"}]
)

# Call Gemini 3
gemini_response = client.chat.completions.create(
    model="gemini-3",
    messages=[{"role": "user", "content": "your prompt"}]
)

# Call MiniMax
minimax_response = client.chat.completions.create(
    model="minimax-01",
    messages=[{"role": "user", "content": "your prompt"}]
)

print(gpt_response.choices[0].message.content)
Links
Official Site: https://octopusx.ai
Documentation: https://doc.octopusx.ai/en
Contact: hello@octopusx.ai
