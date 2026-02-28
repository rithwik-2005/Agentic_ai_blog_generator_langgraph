from langgraph.graph import StateGraph, START, END
from src.states.blogstate import BlogState
from src.nodes.blog_node import BlogNode

class GraphBuilder:
    def __init__(self, llm):
        self.graph = StateGraph(BlogState)
        self.llm = llm

    def build_topic_graph(self):
        node = BlogNode(self.llm)

        self.graph.add_node("title_creation", node.title_creation)
        self.graph.add_node("content_generation", node.content_creation)

        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_generation")
        self.graph.add_edge("content_generation", END)

        return self.graph.compile()