from pydantic import BaseModel
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from typing import Annotated,List



class state(TypedDict):
    messages:Annotated[List,add_messages]