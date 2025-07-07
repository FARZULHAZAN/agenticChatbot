from langgraph.graph import StateGraph,START,END
from src.langgraphagenticai.state.state import state
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.tools.search_tool import get_tools,create_tool_node
from langgraph.prebuilt import ToolNode,tools_condition
from src.langgraphagenticai.nodes.chatbotwithweb import ChatbotwithToolNode



class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(state)
        
    def basic_chatbot_builde_graph(self):

        self.basic_chat_bot=BasicChatbotNode(self.llm)

        self.graph_builder.add_node('chatbot',self.basic_chat_bot.process)
        self.graph_builder.add_edge(START,'chatbot')
        self.graph_builder.add_edge('chatbot',END)
    
    def chatbot_with_tools(self):
        tools=get_tools()
        tool_node=create_tool_node(tools)


        llm=self.llm
        self.chatbot_with_tools=ChatbotwithToolNode(llm)
        self.graph_builder.add_node('chatbot',self.chatbot_with_tools.create_chatbot(tools))
        self.graph_builder.add_node('tools',tool_node)

        self.graph_builder.add_edge(START,'chatbot')
        self.graph_builder.add_conditional_edges('chatbot',tools_condition)
        self.graph_builder.add_edge('tools','chatbot')
        self.graph_builder.add_edge('chatbot',END)

    def setup_graph(self,usecase):

        if usecase=='Basic Chatbot':
            self.basic_chatbot_builde_graph()
        elif usecase=='Chat Bot with web':
            self.chatbot_with_tools()
        return self.graph_builder.compile()