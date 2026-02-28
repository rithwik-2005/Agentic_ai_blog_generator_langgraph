from src.states.blogstate import BlogState, Blog

class BlogNode:
    def __init__(self, llm):
        self.llm = llm

    def title_creation(self, state: BlogState):
        prompt = f"""
        You are an expert blog writer.
        Generate ONE SEO-friendly blog title for:
        {state['topic']}
        Return only the title.
        """

        response = self.llm.invoke(prompt)

        return {
            **state,
            "blog": Blog(title=response.content.strip())
        }

    def content_creation(self, state: BlogState):
        prompt = f"""
        You are an expert blog writer.
        Write a detailed markdown blog for:
        {state['topic']}
        """

        response = self.llm.invoke(prompt)

        return {
            **state,
            "blog": Blog(
                title=state["blog"].title,
                content=response.content
            )
        }