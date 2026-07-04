from langchain_core.messages import AIMessage, HumanMessage
from langgraph.graph import END, START, MessagesState, StateGraph

from nodes import run_agent_reasoning, tool_node

AGENT_REASON = "agent_reason"
ACT = "act"
LAST = -1

flow = StateGraph(MessagesState)

flow.add_node(AGENT_REASON, run_agent_reasoning)

# Equivalent to calling `add_edge(START, AGENT_REASON)
flow.set_entry_point(AGENT_REASON)

flow.add_node(ACT, tool_node)


def should_continue(state: MessagesState) -> str:
    lastMessage: AIMessage = state["messages"][LAST]

    if lastMessage.tool_calls:
        return ACT
    else:
        return END


flow.add_conditional_edges(AGENT_REASON, should_continue, {ACT: ACT, END: END})


flow.add_edge(ACT, AGENT_REASON)

graph = flow.compile()
graph.get_graph().draw_mermaid_png(output_file_path="flow.png")


def main():
    print("Executing a ReAct Agent using LangGraph")
    res = graph.invoke({"messages" : HumanMessage(content="What is the Weather in Bangalore? List it and tripple it ")})
    print(res["messages"][LAST].content)

if __name__ == "__main__":
    main()
