## UV Installation

In Windows, install uv with ps1 and then add to PATH
setx PATH "%PATH%;C:\Users\xxxx\.local\bin"

init project:
1) uv init .

load deps - ipykernel is for Jupiter notebooks
2) uv add python-dotenv langgraph "langchain[anthropic]" ipykernel

3) Add .env file to store LLM Keys
  ash-langgraph-api-key

## Build a simple Chatbot with user input using Claude Sonnet