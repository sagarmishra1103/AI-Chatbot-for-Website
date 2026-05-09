def format_chat_history(chat_history, max_turns=4):
    history = chat_history[-max_turns:]
    return "\n".join([f"{role}: {text}" for role, text in history])

def build_prompt(question, top_chunks, chat_history):
    context = "\n\n".join([c for c, _ in top_chunks])
    history = format_chat_history(chat_history)

    return f"""
You are a precise assistant.

Rules:
- Answer ONLY from the provided context.
- If not found, say: "Information not available in the provided content."

Previous Conversation:
{history}

Context:
{context}

Question:
{question}
"""