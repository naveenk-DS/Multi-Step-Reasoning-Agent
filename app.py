import streamlit as st
from agent.agent import solve

st.set_page_config(
    page_title="Multi-Step Reasoning Agent",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Multi-Step Reasoning Agent")
st.caption("Planner → Step-by-Step Plan → Executor")

question = st.text_input(
    "",
    placeholder="Ask a math or logic question..."
)

if question:
    # User message
    st.markdown("### 🧑 User")
    st.info(question)

    # Agent working
    st.markdown("### 🤖 Agent")
    with st.spinner("Agent is working..."):
        result = solve(question)

    # Planner
    st.markdown("### 🧠 Planner")
    st.success("Plan created")

    plan = result.get("metadata", {}).get("plan", [])
    if plan:
        st.markdown("**Step-by-step plan:**")
        for i, step in enumerate(plan, 1):
            st.write(f"{i}. {step}")

    # Executor
    st.markdown("### ⚙️ Executor")
    st.info("Executing the plan...")

    # Final Answer
    st.markdown("### ✅ Final Answer")
    st.success(result["answer"])

    st.caption(result["reasoning_visible_to_user"])
