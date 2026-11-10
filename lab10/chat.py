"""Terminal chatbot for the library's study-room desk."""

import os
import uuid

from pydantic_ai import Agent
from pydantic_ai.exceptions import AgentRunError
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider


agent = Agent(
    OpenAIChatModel(
        os.environ["LLM_MODEL"],
        provider=OpenAIProvider(
            base_url=os.environ["LLM_BASE_URL"],
            api_key=os.environ["LLM_API_KEY"],
        ),
    ),
    instructions=(
        "You are the assistant at the library's study-room desk. "
        "Answer questions about studying and study rooms in at most three sentences. "
        "Do not invent room availability or library policies."
    ),
)


def main():
    """Chat until /quit or end of input, keeping successful turns in memory."""
    print("Study-room desk. Type /new for a new conversation and /quit to leave.")
    history = []
    session_id = uuid.uuid4().hex

    while True:
        try:
            text = input("you> ").strip()
        except (EOFError, KeyboardInterrupt):
            break

        if not text:
            continue
        if text == "/quit":
            break
        if text == "/new":
            history = []
            session_id = uuid.uuid4().hex
            print("New conversation.")
            continue

        try:
            result = agent.run_sync(
                text,
                message_history=history,
                model_settings={"extra_headers": {"X-Session-ID": session_id}},
            )
        except AgentRunError as error:
            print(f"desk> no usable answer: {error}")
            continue

        history = result.all_messages()
        print(f"desk> {result.output}")


if __name__ == "__main__":
    main()
