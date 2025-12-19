import streamlit as st
from agent.agent import solve

st.set_page_config(
    page_title="Multi-Step Reasoning Agent",
    page_icon="🧠",
    layout="wide"
)

# ---------- SESSION STATE ----------
if "chat" not in st.session_state:
    st.session_state.chat = []

# ---------- TITLE ----------
st.markdown(
    "<h2 style='text-align:center;'>🧠 Multi-Step Reasoning Agent</h2>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center;'>Planner → Executor → Verifier</p>",
    unsafe_allow_html=True
)
st.divider()

# ---------- CHAT HISTORY ----------
for msg in st.session_state.chat:
    if msg["role"] == "user":
        st.markdown("### 🧑 User")
        st.info(msg["content"])
    else:
        st.markdown("### 🤖 Agent")
        for line in msg["content"]:
            st.write(line)

# ---------- BOTTOM INPUT (CHATGPT STYLE) ----------
question = st.chat_input("Ask a math or logic question...")

if question:
    # Store user message
    st.session_state.chat.append({
        "role": "user",
        "content": question
    })

    agent_lines = []

    # ---------- PLANNER ----------
    agent_lines.append("**🧠 Planner**")
    agent_lines.append("Thinking of a plan...")

    with st.spinner("Agent is working..."):
        result = solve(question)

    agent_lines.append("✅ Plan created.")

    # ---------- STEP-BY-STEP PLAN ----------
    plan = result.get("metadata", {}).get("plan", [])
    if plan:
        agent_lines.append("")
        agent_lines.append("**📋 Step-by-Step Plan**")
        for i, step in enumerate(plan, 1):
            agent_lines.append(f"{i}. {step}")

    # ---------- EXECUTOR ----------
    agent_lines.append("")
    agent_lines.append("**⚙️ Executor**")
    agent_lines.append("Executing the plan and computing result...")

    # ---------- FINAL ANSWER ----------
    agent_lines.append("")
    agent_lines.append("**✅ Final Answer**")
    agent_lines.append(f"**{result['answer']}**")
    agent_lines.append(result["reasoning_visible_to_user"])

    # Store agent response
    st.session_state.chat.append({
        "role": "agent",
        "content": agent_lines
    })

    st.rerun()
