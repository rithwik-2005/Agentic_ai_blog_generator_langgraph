import streamlit as st
from src.llms.openaillm import OpenAILLM
from src.graphs.graph_builder import GraphBuilder
from src.states.blogstate import Blog

# ---------- Page Config ----------
st.set_page_config(
    page_title="AI Blog Generator",
    layout="wide"
)

st.title("📝 AI Blog Generator")
st.write("Generate a complete blog using **OpenAI + LangGraph**")

# ---------- Initialize LLM & Graph (ONCE) ----------
@st.cache_resource
def load_graph():
    llm = OpenAILLM().get_llm()
    graph = GraphBuilder(llm).build_topic_graph()
    return graph

graph = load_graph()

# ---------- UI ----------
topic = st.text_input(
    "Enter blog topic",
    placeholder="e.g. Future of Artificial Intelligence"
)

generate = st.button("🚀 Generate Blog")

# ---------- Action ----------
if generate:
    if not topic.strip():
        st.warning("Please enter a topic")
    else:
        with st.spinner("Generating blog..."):
            result = graph.invoke({
                "topic": topic,
                "blog": Blog(),
                "current_language": "en"
            })

        blog = result["blog"]

        st.success("Blog generated successfully!")

        st.subheader("📌 Title")
        st.markdown(f"### {blog.title}")

        st.subheader("📖 Content")
        st.markdown(blog.content)