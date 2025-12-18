import streamlit as st
import requests

st.set_page_config(page_title="CrossExam", layout="centered")

st.title("CrossExam")
st.markdown("*A skeptical interview simulator*")

FLASK_URL = "http://localhost:5000"

if 'submitted' not in st.session_state:
    st.session_state.submitted = False
    st.session_state.result = None

st.markdown("---")

question = "Tell me about a challenging project you worked on and how you approached it."
st.markdown(f"**Question:** {question}")

answer = st.text_area(
    "Your Answer",
    height=200,
    placeholder="Type your answer here...",
    key="answer_input"
)

col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    submit = st.button("Submit Answer", use_container_width=True)

if submit:
    if not answer.strip():
        st.error("Please provide an answer before submitting.")
    else:
        with st.spinner("Evaluating your answer..."):
            try:
                response = requests.post(
                    f"{FLASK_URL}/evaluate",
                    json={"answer": answer},
                    timeout=30
                )

                if response.status_code == 200:
                    st.session_state.result = response.json()
                    st.session_state.submitted = True
                else:
                    st.error(f"Server error: {response.status_code}")

            except requests.exceptions.ConnectionError:
                st.error("Cannot connect to Flask server. Make sure server.py is running on port 5000.")
            except Exception as e:
                st.error(f"Error: {str(e)}")

if st.session_state.submitted and st.session_state.result:
    result = st.session_state.result

    st.markdown("---")
    st.markdown("### Evaluation Results")

    st.markdown("**Rule-Based Analysis**")
    for flag in result['flags']:
        st.markdown(f"• {flag}")

    st.markdown("")
    st.markdown("**Adversarial Feedback**")

    # FIX: display the string directly (horizontal text)
    st.markdown(result['gemini_counter'])

    st.markdown("")
    st.markdown(f"**Word Count:** {result['word_count']}")
    st.markdown(f"**Final Score:** {result['score']}/100")

    verdict = result['verdict']
    if verdict == "HIRE":
        st.success(f"**Verdict: {verdict}**")
    elif verdict == "BORDERLINE":
        st.warning(f"**Verdict: {verdict}**")
    else:
        st.error(f"**Verdict: {verdict}**")

    st.markdown("")
    if st.button("Try Another Answer"):
        st.session_state.submitted = False
        st.session_state.result = None
        st.rerun()
