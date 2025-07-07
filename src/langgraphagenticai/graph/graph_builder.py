from langgraph.graph import StateGraph,START,END
from src.langgraphagenticai.state.state import state
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.tools.search_tool import get_tools,create_tool_node
from langgraph.prebuilt import ToolNode,tools_condition
from src.langgraphagenticai.nodes.chatbotwithweb import ChatbotwithToolNode
from src.langgraphagenticai.nodes.AI_news import AINewsNode


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
        chatbot_with_tools=ChatbotwithToolNode(llm)
        self.graph_builder.add_node('chatbot',chatbot_with_tools.create_chatbot(tools))
        self.graph_builder.add_node('tools',tool_node)

        self.graph_builder.add_edge(START,'chatbot')
        self.graph_builder.add_conditional_edges('chatbot',tools_condition)
        self.graph_builder.add_edge('tools','chatbot')
        self.graph_builder.add_edge('chatbot',END)
    
    def AI_News_Builder_graph(self):
        
        ai_news=AINewsNode(self.llm)
        
        self.graph_builder.add_node('fetch_news',ai_news.fetch_news)
        self.graph_builder.add_node('summarize_news',ai_news.summarize_news)
        self.graph_builder.add_node('save_result',ai_news.save_result)

        self.graph_builder.set_entry_point('fetch_news')
        self.graph_builder.add_edge('fetch_news','summarize_news')
        self.graph_builder.add_edge('summarize_news','save_result')
        self.graph_builder.add_edge('save_result',END)


    def setup_graph(self,usecase):

        if usecase=='Basic Chatbot':
            self.basic_chatbot_builde_graph()
        if usecase=='Chat Bot with web':
            self.chatbot_with_tools()
        if usecase=='AI News':
            self.AI_News_Builder_graph()

        return self.graph_builder.compile()