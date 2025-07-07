from langgraph.graph import StateGraph,START,END
from src.langgraphagenticai.state.state import state
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode

class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(state)
        
    def basic_chatbot_builde_graph(self):

        self.basic_chat_bot=BasicChatbotNode(self.llm)

        self.graph_builder.add_node('chatbot',self.basic_chat_bot.process)
        self.graph_builder.add_edge(START,'chatbot')
        self.graph_builder.add_edge('chatbot',END)
    
    def setup_graph(self,usecase):

        if usecase=='Basic Chatbot':
            self.basic_chatbot_builde_graph()
        return self.graph_builder.compile()