import time
import streamlit as st
from agent.agent import solve

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Multi-Step Reasoning Agent",
    page_icon="🧠",
    layout="wide"
)

# ---------------- SESSION STATE ----------------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- TITLE ----------------
st.markdown(
    "<h2 style='text-align:center;'>🧠 Multi-Step Reasoning Agent</h2>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center;'>Planner → Executor → Verifier</p>",
    unsafe_allow_html=True
)
st.divider()

# ---------------- CHAT HISTORY ----------------
for item in st.session_state.history:
    if item["role"] == "user":
        st.markdown("### 🧑 User")
        st.info(item["content"])
    else:
        st.markdown("### 🤖 Agent")
        for line in item["content"]:
            st.write(line)

# ---------------- BOTTOM INPUT ----------------
question = st.chat_input("Ask a math or logic question...")

if question:
    # Save user message
    st.session_state.history.append({
        "role": "user",
        "content": question
    })

    # Placeholders for video-like thinking
    planner_box = st.empty()
    plan_box = st.empty()
    executor_box = st.empty()
    json_box = st.empty()

    # ---------------- PLANNER ----------------
    planner_box.markdown("### 🧠 Planner")
    planner_box.info("🤔 Thinking of a plan...")
    time.sleep(1.2)

    # Call agent ONCE
    result = solve(question)

    planner_box.success("✅ Plan created")
    time.sleep(0.8)

    # ---------------- STEP-BY-STEP PLAN ----------------
    plan = result.get("metadata", {}).get("plan", [])
    if plan:
        plan_box.markdown("### 📋 Step-by-Step Plan")
        for i, step in enumerate(plan, 1):
            plan_box.write(f"{i}. {step}")
            time.sleep(0.6)

    # ---------------- EXECUTOR ----------------
    executor_box.markdown("### ⚙️ Executor")
    executor_box.info("⏳ Executing steps...")
    time.sleep(1.5)
    executor_box.success("✅ Execution completed")

    # ---------------- FINAL JSON OUTPUT ----------------
    json_box.markdown("### 📦 Final Output (JSON)")
    time.sleep(0.5)
    json_box.json(result)

    # Save clean history (for re-render)
    st.session_state.history.append({
        "role": "agent",
        "content": [
            "🧠 Planner: Thinking and plan created",
            "📋 Step-by-step plan shown",
            "⚙️ Executor: Execution completed",
            "📦 Final JSON output generated"
        ]
    })

    time.sleep(0.3)
    st.rerun()
