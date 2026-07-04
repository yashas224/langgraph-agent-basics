from dotenv import load_dotenv
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()


@tool()
def tripple(num: float) -> float:
    """
    param num: a number to triple

    returns: the triple of the input number
    """
    return num * 3


tavily_search_tool = TavilySearch(
    max_results=1,
    topic="general",
)

tools = [tripple, tavily_search_tool]

llm = ChatOpenAI(model="gpt-5.5", temperature=0)
llm = llm.bind_tools(tools=tools)


def main():
    print("Hello from langgraph-agent-basics!")


if __name__ == "__main__":
    main()
