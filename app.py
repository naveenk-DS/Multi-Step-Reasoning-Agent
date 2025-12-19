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
if "chat" not in st.session_state:
    st.session_state.chat = []

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
for msg in st.session_state.chat:
    if msg["role"] == "user":
        st.markdown("### 🧑 User")
        st.info(msg["content"])
    else:
        st.markdown("### 🤖 Agent")
        for block in msg["blocks"]:
            block()

# ---------------- CHAT INPUT ----------------
question = st.chat_input("Ask a math or logic question...")

if question:
    # Save user question
    st.session_state.chat.append({
        "role": "user",
        "content": question
    })

    # Placeholders
    planner_box = st.empty()
    plan_box = st.empty()
    executor_box = st.empty()
    json_box = st.empty()

    # ---------------- PLANNER (THINKING) ----------------
    planner_box.markdown("### 🧠 Planner")
    planner_box.info("🤔 Thinking of a plan...")
    time.sleep(1.2)

    # Run agent ONCE
    result = solve(question)

    planner_box.success("✅ Plan created")

    # ---------------- STEP-BY-STEP PLAN (REAL) ----------------
    plan = result.get("metadata", {}).get("plan", [])
    if plan:
        plan_box.markdown("### 📋 Step-by-Step Plan")
        for i, step in enumerate(plan, 1):
            plan_box.write(f"{i}. {step}")
            time.sleep(0.5)

    # ---------------- EXECUTOR ----------------
    executor_box.markdown("### ⚙️ Executor")
    executor_box.info("⏳ Executing steps...")
    time.sleep(1.2)
    executor_box.success("✅ Execution completed")

    # ---------------- FINAL JSON (REAL OUTPUT) ----------------
    json_box.markdown("### 📦 Final Output (JSON)")
    time.sleep(0.5)
    json_box.json(result)

    # Save clean renderable blocks
    st.session_state.chat.append({
        "role": "agent",
        "blocks": [
            lambda: st.markdown("### 🧠 Planner\nPlan created"),
            lambda: st.markdown("### 📋 Step-by-Step Plan"),
            lambda: st.write(plan),
            lambda: st.markdown("### ⚙️ Executor\nExecution completed"),
            lambda: st.markdown("### 📦 Final Output (JSON)"),
            lambda: st.json(result)
        ]
    })

    time.sleep(0.3)
    st.rerun()
