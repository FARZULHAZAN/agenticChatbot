import streamlit as st
from src.langgraphagenticai.UI.streamlit.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMs.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.UI.streamlit.display_result import DisplayResultStreamlit

def load_langgraph_agenticai_app():
    """
    Loads and runs the langgraph app with streamlit
    """

    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Erro: Failed to load user input from the UI")
        return
    
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe
    else:
        user_message = st.chat_input('Enter your message:')
    if user_message:
        try:
            obj_llm_config=GroqLLM(user_controls_input=user_input)
            model=obj_llm_config.get_llm_models()

            if not model:
                st.error('Error: no model found')
                return

            usecase=user_input.get("selected_usecase")
            if not usecase:
                st.error('Error: no usecase')
                return
            
            graph_builder=GraphBuilder(model)
            try:
                graph=graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
            except Exception as e:
                st.error(f'Error graph setup fail {e}')
                return
            
        except Exception as e:
            st.error(f'Error graph setup fail {e}')
            return

        
    