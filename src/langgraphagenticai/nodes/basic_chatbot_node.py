from src.langgraphagenticai.state.state import state


class BasicChatbotNode:

    def __init__(self,model):
        self.llm=model

    def process(self,state:state):

        return {'messages':self.llm.invoke(state['messages'])} 