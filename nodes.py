from dotenv import load_dotenv
from langchain.messages import SystemMessage
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode

load_dotenv()


from react import llm, tools

system_message = "You are a helpful assistant that can use tools to answer Questions"


def run_agent_reasoning(state: MessagesState) -> MessagesState:
    """
    Run The agent reasoning Node
    """
    response = llm.invoke([SystemMessage(content=system_message), *state["messages"]])

    return {"messages": [response]}


tool_node = ToolNode(tools=tools)
