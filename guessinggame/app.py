import streamlit as st
import random

# Load the CSS file
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title of the app
st.title("Number Guessing Game")

# Instructions
st.markdown("""
<div style="text-align: center;">
    Welcome to the Number Guessing Game!  
    <br>I have selected a random number between 1 and 100.  
    <br>Can you guess it?  
</div>
""", unsafe_allow_html=True)

# Generate a random number and store it in session state
if "target" not in st.session_state:
    st.session_state.target = random.randint(1, 100)
    st.session_state.attempts = 0

# User input for guessing
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1, key="user_guess")

# Button to submit guess
if st.button("Check"):
    st.session_state.attempts += 1
    if guess < st.session_state.target:
        st.warning("❌ Too low! Try again.")
    elif guess > st.session_state.target:
        st.warning("❌ Too high! Try again.")
    else:
        st.success(f"🎉 Congratulations! You guessed the number in {st.session_state.attempts} attempts.")
        # Reset game
        if st.button("Play Again"):
            st.session_state.target = random.randint(1, 100)
            st.session_state.attempts = 0

# Footer
st.markdown("<footer>Created with ❤️ using Streamlit</footer>", unsafe_allow_html=True)
