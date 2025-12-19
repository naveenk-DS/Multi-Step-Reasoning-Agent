import streamlit as st
from agent.agent import solve
import uuid

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Multi-Step Reasoning Agent",
    page_icon="🧠",
    layout="wide"
)

# ---------------- SESSION STATE ----------------
if "chats" not in st.session_state:
    st.session_state.chats = {}

if "active_chat" not in st.session_state:
    st.session_state.active_chat = None

# ---------------- HELPERS ----------------
def new_chat():
    chat_id = str(uuid.uuid4())
    st.session_state.chats[chat_id] = {
        "title": "New Chat",
        "messages": []
    }
    st.session_state.active_chat = chat_id

def add_message(role, content):
    st.session_state.chats[
        st.session_state.active_chat
    ]["messages"].append({
        "role": role,
        "content": content
    })

# ---------------- SIDEBAR (CHATGPT STYLE) ----------------
with st.sidebar:
    st.markdown("## 💬 Chats")

    if st.button("➕ New Chat", use_container_width=True):
        new_chat()

    st.divider()

    for chat_id, chat in st.session_state.chats.items():
        if st.button(chat["title"], key=chat_id, use_container_width=True):
            st.session_state.active_chat = chat_id

    st.divider()
    st.caption("🧠 Multi-Step Reasoning Agent")

# ---------------- MAIN AREA ----------------
st.markdown("### 🧠 Multi-Step Reasoning Agent")
st.caption("Planner → Executor → Verifier")

if not st.session_state.active_chat:
    st.info("Start a new chat from the sidebar")
    st.stop()

chat = st.session_state.chats[st.session_state.active_chat]

# ---------------- RENDER CHAT ----------------
for msg in chat["messages"]:
    with st.chat_message(msg["role"]):
        if isinstance(msg["content"], list):
            for line in msg["content"]:
                st.markdown(line)
        else:
            st.markdown(msg["content"])

# ---------------- INPUT (BOTTOM LIKE CHATGPT) ----------------
question = st.chat_input("Ask a math or logic question...")

if question:
    # User message
    add_message("user", question)

    # Auto title
    if len(chat["messages"]) == 1:
        chat["title"] = question[:30] + "..." if len(question) > 30 else question

    agent_lines = []

    # ---------- PLANNER ----------
    agent_lines.append("**🧠 Planner**")
    agent_lines.append("Thinking of a plan...")

    with st.spinner("Agent is working..."):
        result = solve(question)

    agent_lines.append("✅ Plan created.")

    # ---------- PLAN ----------
    plan = result.get("metadata", {}).get("plan", [])
    if plan:
        agent_lines.append("")
        agent_lines.append("**📋 Step-by-Step Plan**")
        for i, step in enumerate(plan, 1):
            agent_lines.append(f"{i}. {step}")

    # ---------- EXECUTOR ----------
    agent_lines.append("")
    agent_lines.append("**⚙️ Executor**")
    agent_lines.append("Executing the plan...")

    # ---------- FINAL ----------
    agent_lines.append("")
    agent_lines.append("**✅ Final Answer**")
    agent_lines.append(f"**{result['answer']}**")
    agent_lines.append(result["reasoning_visible_to_user"])

    add_message("assistant", agent_lines)

    st.rerun()
