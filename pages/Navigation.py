import streamlit as st

def show_sidebar():
    with st.sidebar:
        st.image("assets/logo.png", width=120)
        st.title("Navigation")
        
        # Page selection
        page = st.radio(
            "Go to:",
            options=["🏠 Home", "🔍 Filters", "📊 Overview", "ℹ️ About"],
            horizontal=False
        )
        
        # Store selection in session state
        st.session_state.current_page = page
        