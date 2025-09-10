from langchain.callbacks.base import BaseCallbackHandler

class TokenUsageHandler(BaseCallbackHandler):
    def __init__(self):
        self.prompt_tokens = 0
        self.completion_tokens = 0
        self.total_tokens = 0

    def on_llm_end(self, response, **kwargs):
        # Gemini returns metadata instead of token_usage
        metadata = response.llm_output or {}
        usage = metadata.get("usage_metadata", {})  # Gemini key

        prompt_tokens = usage.get("prompt_token_count", 0)
        completion_tokens = usage.get("candidates_token_count", 0)  # text output tokens
        total_tokens = usage.get("total_token_count", prompt_tokens + completion_tokens)

        self.prompt_tokens += prompt_tokens
        self.completion_tokens += completion_tokens
        self.total_tokens += total_tokens

        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Completion tokens: {completion_tokens}")
        print(f"Total tokens: {total_tokens}")
