"""Shared LLM factory for all agents."""

import os

from langchain_openai import ChatOpenAI


def get_llm() -> ChatOpenAI:
    """Return a ChatOpenAI client using OpenAI credentials."""
    return ChatOpenAI(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        temperature=0.3,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
    )