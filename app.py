import streamlit as st

from models.crisis_detector import detect_crisis
from rag.setup_rag import initialize_rag
from rag.rag_pipeline import rag_response
from models.mental_state_detector import detect_mental_state


from database.memory import (
    initialize_memory,
    save_memory,
    get_memories
)

from database.mood_tracker import (
    initialize_db,
    save_mood
)

from models.memory_extractor import (
    should_store_memory
)

initialize_memory()
initialize_db()

if "rag_ready" not in st.session_state:

    index, chunks = initialize_rag()

    st.session_state.index = index
    st.session_state.chunks = chunks

    st.session_state.rag_ready = True

st.set_page_config(
    page_title="MindMate AI",
    page_icon="🧠"
)

st.title("🧠 MindMate AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input(
    "How are you feeling today?"
)

if prompt:

    if detect_crisis(prompt):

        st.error(
            """
            If you are in immediate danger or thinking about harming yourself,
            please contact emergency services, a crisis helpline,
            or a trusted friend/family member immediately.
            """
        )

        st.stop()

    emotion = detect_mental_state(prompt)

    save_mood(
        prompt,
        emotion
    )

    if should_store_memory(prompt):
        save_memory(prompt)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    answer, sources = rag_response(
        query=prompt,
        emotion=emotion,
        index=st.session_state.index,
        chunks=st.session_state.chunks
    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):

        st.markdown(answer)

        with st.expander(
            "Retrieved Context"
        ):

            for source in sources:
                st.write(source)