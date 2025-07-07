from src.langgraphagenticai.state.state import state
from src.langgraphagenticai.tools.search_tool import get_tools 
class ChatbotwithToolNode:

    def __init__(self,model):
        self.llm = model
    

    def process(self,state:state):

        user_input = state['messages'][-1] if state['messages'] else ''
        llm_response=self.llm.inoke([{'role':'user','content':user_input}])


        tools_response = f"Tool integration for: '{user_input}'"

        return {"messages":[llm_response,tools_response]}
    
    def create_chatbot(self,tools):
        #tools=get_tools()
        llm_with_tools=self.llm.bind_tools(tools)
        def chatbot_node(state):
            return {'messages':[llm_with_tools.invoke(state['messages'])]}
        return chatbot_node