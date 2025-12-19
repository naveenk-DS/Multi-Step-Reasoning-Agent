import streamlit as st
from agent.agent import solve

st.set_page_config(
    page_title="Multi-Step Reasoning Agent",
    page_icon="🧠",
    layout="wide"
)

# ---------- SESSION STATE ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- TITLE ----------
st.markdown("<h2 style='text-align:center;'>🧠 Multi-Step Reasoning Agent</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Planner → Executor → Verifier</p>", unsafe_allow_html=True)
st.divider()

# ---------- CHAT HISTORY ----------
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown("### 🧑 User")
        st.info(msg["content"])
    else:
        st.markdown("### 🤖 Agent")
        for line in msg["content"]:
            st.write(line)

# ---------- BOTTOM INPUT ----------
st.divider()
question = st.chat_input("Ask a math or logic question...")

if question:
    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    agent_output = []

    # -------- PLANNER --------
    agent_output.append("**🧠 Planner:**")
    agent_output.append("Thinking of a plan...")

    with st.spinner("Planner is working..."):
        result = solve(question)

    agent_output.append("✅ Plan created.")

    # -------- STEP-BY-STEP PLAN --------
    plan = result.get("metadata", {}).get("plan", [])
    if plan:
        agent_output.append("")
        agent_output.append("**📋 Step-by-Step Plan:**")
        for i, step in enumerate(plan, 1):
            agent_output.append(f"{i}. {step}")

    # -------- EXECUTOR --------
    agent_output.append("")
    agent_output.append("**⚙️ Executor:**")
    agent_output.append("Executing steps...")

    # -------- FINAL ANSWER --------
    agent_output.append("")
    agent_output.append("**✅ Final Answer:**")
    agent_output.append(f"**{result['answer']}**")
    agent_output.append(result["reasoning_visible_to_user"])

    # Save agent response
    st.session_state.messages.append({
        "role": "assistant",
        "content": agent_output
    })

    # Rerun to display new messages
    st.rerun()
