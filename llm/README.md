# LLM Module

The `llm` package manages communication with external Large Language Models.

ResearchMind-AI currently uses the Groq API to perform AI-powered reasoning and text generation.

## Responsibilities

- Connect to Groq API
- Build prompts
- Send requests
- Receive responses
- Handle model configuration

## Files

### groq_client.py

Provides a reusable client for interacting with the configured Groq model.

## Supported Model

- Llama 3.3 70B Versatile

The implementation is modular, allowing other LLM providers to be integrated in the future with minimal changes.
