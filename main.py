from dotenv import load_dotenv
from typing import Annotated, Literal
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field
from typing_extensions import TypedDict
import os

load_dotenv()

anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

llm = init_chat_model(
    "anthropic:claude-sonnet-4-20250514"  
)

# Define the state structure
class State(TypedDict):
    messages: Annotated[list, add_messages]
   
# Build the state graph
graph_builder = StateGraph(State)

# Define the chatbot node
def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}

# Add nodes and edges to the graph
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

# Compile the graph
graph = graph_builder.compile()

# Run the graph with user input
user_input = input("Enter a message: ")
state = graph.invoke({"messages": [{"role": "user", "content": user_input}]})

# Print the chatbot's response
print(state["messages"][-1].content)