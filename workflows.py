from ai_client import generate_response


def summarize_workflow(user_input: str) -> str:
    prompt = f"""
You are a professional assistant.
Summarize the following text clearly and concisely in bullet points:

Text:
{user_input}
"""
    result = generate_response(prompt)

    if result.startswith("DEMO_MODE::"):
        cleaned = user_input.strip()

        if not cleaned:
            return "Demo mode: No content provided to summarize."

        sentences = [s.strip() for s in cleaned.split(".") if s.strip()]

        if len(sentences) == 1:
            return (
                "Demo mode summary:\n"
                f"- Main point: {sentences[0].capitalize()}.\n"
                "- Suggested next step: review and organize the key details."
            )

        bullets = "\n".join(f"- {s.capitalize()}." for s in sentences[:3])
        return f"Demo mode summary:\n{bullets}"

    return result


def email_reply_workflow(user_input: str) -> str:
    prompt = f"""
You are a professional workplace assistant.
Write a polite, clear email reply based on the following message.

Message:
{user_input}
"""
    result = generate_response(prompt)

    if result.startswith("DEMO_MODE::"):
        return (
            "Demo mode email reply:\n\n"
            "Hi,\n\n"
            "Thank you for your message. I appreciate the update and would be happy to follow up. "
            "Please let me know a time that works best for you.\n\n"
            "Best regards,\n"
            "Mouhamadou Kane"
        )

    return result


def action_items_workflow(user_input: str) -> str:
    prompt = f"""
You are a productivity assistant.
Extract the key action items from the following text.
Format the response as a numbered list.

Text:
{user_input}
"""
    result = generate_response(prompt)

    if result.startswith("DEMO_MODE::"):
        parts = [p.strip() for p in user_input.replace("\n", " ").split(",") if p.strip()]
        if not parts:
            return "Demo mode: No action items found."
        numbered = "\n".join(f"{i+1}. {item}" for i, item in enumerate(parts[:5]))
        return f"Demo mode action items:\n{numbered}"

    return result


def run_workflow(workflow_type: str, user_input: str) -> str:
    workflow_type = workflow_type.strip().lower()

    if workflow_type == "summarize":
        return summarize_workflow(user_input)
    if workflow_type == "email":
        return email_reply_workflow(user_input)
    if workflow_type == "actions":
        return action_items_workflow(user_input)

    return "Invalid workflow type. Choose: summarize, email, or actions."