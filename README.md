## Tales by AI

An interactive story creation app that transforms your character descriptions into engaging stories using AI.

## What it does

- Enter character descriptions
- AI detects your story intent
- Shows the AI's thinking process
- Generates a complete story based on your characters
- Toggle to show/hide the AI's creative process

## Features

- Intent Recognition: Understands what kind of story you want
- AI Thinking Steps: Shows how the story is planned
- Story Generation: Creates engaging narratives
- Interactive UI: Simple Streamlit interface
- Customizable Display: Show or hide the AI process

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/<your-username>/tales-by-ai.git
   cd tales-by-ai
   ```

2. Create virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate    # Windows
   source venv/bin/activate # macOS/Linux
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up API key:
   Create a `.env` file and add:
   ```
   GEMINI_API_KEY=your_google_gemini_api_key_here
   ```

5. Run the app:
   ```
   streamlit run app.py
   ```

## How to use

1. Enter your character descriptions in the input box
2. Click "Generate Story"
3. Read your AI-generated story
4. Optional: Click "Show Intent & Thinking Process" to see how the AI created the story

## Example

**Input:**
"Two astronauts stranded on Mars, one optimistic and one sarcastic, trying to find a way home."

**Output:**
- Intent: Survival and teamwork story about astronauts on Mars
- Thinking: AI plans the setting, conflict, character dynamics, and resolution
- Story: Complete narrative featuring your characters

## Requirements

- Python 3.10+
- Google Gemini API key
- Internet connection

## Project Structure

```
tales-by-ai/
├── app.py           # Streamlit frontend
├── backend.py       # AI logic with Gemini API
├── config.py        # API key configuration
├── requirements.txt # Dependencies
├── README.txt       # This file
└── .env            # Environment variables
```

## Notes

- Free Google Gemini API key available
- Daily usage quotas apply on free tier
- Default model: gemini-1.5-flash
- Works on Windows, macOS, and Linux

## Built with

- Python
- Streamlit
- Google Gemini API
