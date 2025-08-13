import streamlit as st
from backend import analyze_intent, generate_thinking_steps, create_story

st.set_page_config(page_title="AI Story Creator", layout="centered")

st.title("AI Story Creator")
st.write("Enter your characters, and watch the AI create a story!")

# Initialize toggle state
if "show_details" not in st.session_state:
    st.session_state.show_details = False

# User input
user_characters = st.text_area("Enter your characters and details", height=150)

if st.button("Generate Story"):
    if user_characters.strip():
        with st.spinner("Creating your story..."):
            st.session_state.story = create_story(user_characters)

        # Store intent thinking (but hidden at first)
        st.session_state.intent = analyze_intent(user_characters)
        st.session_state.thinking_steps = generate_thinking_steps(user_characters)
        st.session_state.show_details = False
    else:
        st.warning("Please enter character details first.")

# Show toggle_story if exists
if "story" in st.session_state:
    # Toggle button ABOVE story
    if st.button("Show/Hide Intent & Thinking"):
        st.session_state.show_details = not st.session_state.show_details

    # Show details if toggled
    if st.session_state.show_details:
        st.subheader("Intent Recognition")
        st.info(st.session_state.intent)

        st.subheader("AI's Thinking Process")
        for step in st.session_state.thinking_steps:
            st.markdown(f"✅ **{step}**")  # Clean display

    # Story below
    st.subheader("Story")
    st.write(st.session_state.story)
