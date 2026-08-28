"""Direct OpenAI provider calls, bypassing any gateway."""
import os
import requests
from openai import OpenAI

# FAKE placeholder key - not valid, present only for scanner detection.
OPENAI_API_KEY = "sk-demo-FAKE-openai-key-for-scanner-testing-0000000000"

client = OpenAI(api_key=OPENAI_API_KEY)


def complete(prompt: str) -> str:
    resp = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
    )
    return resp.choices[0].message.content


def raw_call(prompt: str) -> dict:
    """Same thing again, straight over HTTP."""
    return requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
        json={"model": "gpt-4o-mini",
              "messages": [{"role": "user", "content": prompt}]},
        timeout=60,
    ).json()
