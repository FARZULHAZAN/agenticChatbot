import streamlit as st
from src.langgraphagenticai.UI.streamlit.loadui import LoadStreamlitUI


def load_langgraph_agenticai_app():
    """
    Loads and runs the langgraph app with streamlit
    """

    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Erro: Failed to load user input from the UI")
        return
    
    user_message = st.chat_input('Entr your message:')
        
    