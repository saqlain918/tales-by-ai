project:
  name: "Tales by AI"
  description: >
    Tales by AI is an interactive story creation app built with Python, Streamlit, and the Google Gemini API.
    It allows users to input their character descriptions, then:
      1. Detects the intent of the user.
      2. Shows the thinking process of how the story will be created.
      3. Generates a final story based on the given characters.

features:
  - Intent Recognition: Understands what the user is aiming for based on the provided characters.
  - AI Thinking Steps: Displays the AI's creative process in human-readable bullet points.
  - Story Generation: Produces an engaging story that matches the intent and characters.
  - Toggle Display: Users can choose to show or hide the intent and thinking process after the story is generated.
  - Streamlit Frontend: Simple and interactive UI.

technologies_used:
  - Python 3.10+
  - Streamlit
  - Google Gemini API
  - PyCharm (optional)

installation_and_setup:
  - step: Clone the repository
    commands:
      - git clone https://github.com/<your-username>/tales-by-ai.git
      - cd tales-by-ai

  - step: Create and activate a virtual environment
    commands:
      - python -m venv venv
      - "# On Windows"
      - venv\Scripts\activate
      - "# On macOS/Linux"
      - source venv/bin/activate

  - step: Install dependencies
    commands:
      - pip install -r requirements.txt

  - step: Set up environment variables
    instructions: |
      Create a `.env` file in the project root and add:
      GEMINI_API_KEY=your_google_gemini_api_key_here

  - step: Run the app
    commands:
      - streamlit run app.py

usage_steps:
  - Enter your character descriptions in the input box.
  - Click "Generate Story".
  - View the final AI-generated story.
  - (Optional) Click "Show Intent & Thinking Process" to see how the AI developed the story.

example:
  input: |
    Two astronauts stranded on Mars, one optimistic and one sarcastic, trying to find a way home.

  output:
    intent: |
      The user wants a survival and teamwork-themed story about astronauts on Mars.

    thinking_steps:
      - Identify setting: Mars
      - Determine main conflict: survival and escape
      - Assign character dynamics: optimism vs sarcasm
      - Plan key events: resource search, communication attempts, emotional moments
      - Build a satisfying conclusion

    story: |
      [Full AI-generated story here]

notes:
  - Ensure you have a valid Google Gemini API key.
  - Free-tier API usage is limited; daily quotas may apply.
  - Default model: gemini-1.5-flash (can be changed in the backend).
