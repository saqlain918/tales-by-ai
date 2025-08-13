import google.generativeai as genai
from config import GEMINI_API_KEY

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def safe_get_text(response):
    """Safely extract text from Gemini API response."""
    try:
        if response and hasattr(response, "candidates") and len(response.candidates) > 0:
            candidate = response.candidates[0]
            if hasattr(candidate, "content") and hasattr(candidate.content, "parts"):
                parts = candidate.content.parts
                if len(parts) > 0 and hasattr(parts[0], "text"):
                    return parts[0].text.strip()
        return "⚠️ No valid text generated."
    except Exception as e:
        return f"⚠️ Error extracting text: {e}"

def analyze_intent(user_characters: str) -> str:
    """Recognize what user wants based on character description."""
    prompt = f"You are an intent recognizer. User characters: {user_characters}. Explain in one sentence what they want."
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt, request_options={"timeout": 60})
    return safe_get_text(response)

def generate_thinking_steps(user_characters: str) -> list:
    """Simulate thinking steps in human-readable form."""
    steps_prompt = f"""
    You are a creative assistant. Break down in 4-5 short bullet points how you would create a story
    based on these characters: {user_characters}.
    Do NOT write the story yet — only list the thought steps.
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(steps_prompt, request_options={"timeout": 60})
    text = safe_get_text(response)
    # Remove empty lines and trim whitespace
    return [line.strip() for line in text.split("\n") if line.strip()]

def create_story(user_characters: str) -> str:
    """Create the final story."""
    story_prompt = f"Write a creative, engaging short story based on these characters: {user_characters}."
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(story_prompt, request_options={"timeout": 60})
    return safe_get_text(response)

