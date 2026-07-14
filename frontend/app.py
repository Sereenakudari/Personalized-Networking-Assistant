import streamlit as st
import requests
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
from io import BytesIO

st.set_page_config(
    page_title="Personalized Networking Assistant",
    layout="wide"
)
def create_pdf(bio, event, interests, conversation):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>Personalized Networking Assistant</b>", styles["Title"]))

    story.append(Paragraph(f"<b>Bio:</b> {bio}", styles["BodyText"]))

    story.append(Paragraph(f"<b>Event:</b> {event}", styles["BodyText"]))

    story.append(Paragraph(f"<b>Interests:</b> {interests}", styles["BodyText"]))

    story.append(Paragraph("<b>Conversation Starters</b>", styles["Heading2"]))

    story.append(Paragraph(conversation.replace("\n", "<br/>"), styles["BodyText"]))

    doc.build(story)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf

# ---------------- Session State ----------------

if "bio" not in st.session_state:
    st.session_state.bio = ""

if "event" not in st.session_state:
    st.session_state.event = ""

if "interests" not in st.session_state:
    st.session_state.interests = ""

if "response" not in st.session_state:
    st.session_state.response = ""

# ---------------- Sidebar ----------------

st.sidebar.title("Personalized Networking Assistant")

if st.sidebar.button("New Chat", use_container_width=True):
    st.session_state.bio = ""
    st.session_state.event = ""
    st.session_state.interests = ""
    st.session_state.response = ""
    st.rerun()

page = st.sidebar.radio(
    "Navigation",
    [
        "AI Assistant",
        "Wikipedia Fact Checker",
        "Conversation History",
        "Feedback History"
    ]
)

# ============================================================
# AI EVENT COPILOT
# ============================================================

if page == "AI Assistant":

    st.title("AI Event Copilot")

    st.caption("Describe your upcoming networking event in one prompt and let AI prepare you.")

    user_prompt = st.text_area(
        "Describe your event (Event overview, your background, and your networking goals)",
        height=180,
        placeholder="""
Example:

I'm attending Google I/O next week.
I'm a Computer Science student interested in AI and Cybersecurity.
I want to meet recruiters for internship opportunities and build my professional network.
"""
    )

    if st.button("Prepare My Networking Plan", use_container_width=True):

        if user_prompt.strip() == "":
            st.warning("Please describe your event.")
        else:

            with st.spinner("Preparing your networking plan..."):

                try:

                    response = requests.post(
                        "http://127.0.0.1:8000/event-copilot",
                        json={
                            "prompt": user_prompt
                        }
                    )

                    if response.status_code == 200:

                        data = response.json()

                        st.session_state.response = data["response"]

                    else:
                        st.error("Could not connect to backend.")

                except Exception:
                    st.error("Backend is not running.")

    if st.session_state.response:

        st.success("Your Personalized Networking Plan")

        st.markdown(st.session_state.response)

        st.divider()

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            if st.button("👍", key="like"):

                requests.post(
                    "http://127.0.0.1:8000/feedback",
                    json={
                        "response": st.session_state.response,
                        "feedback": "Like"
                    }
                )

                st.toast("Thanks for your feedback!")

        with c2:

            if st.button("👎", key="dislike"):

                requests.post(
                    "http://127.0.0.1:8000/feedback",
                    json={
                        "response": st.session_state.response,
                        "feedback": "Dislike"
                    }
                )

                st.toast("Feedback recorded.")

        with c3:

            st.download_button(
                "📄 Download",
                data=st.session_state.response,
                file_name="NetworkingPlan.txt",
                mime="text/plain",
                key="download_plan"
            )

        with c4:

            if st.button("🔄 Regenerate", key="regen"):

                st.rerun()
# ============================================================
# Conversation History
# ============================================================

elif page == "Conversation History":

    st.title("Conversation History")

    try:

        response = requests.get(
            "http://127.0.0.1:8000/history"
        )

        if response.status_code == 200:

            history = response.json()

            if len(history) == 0:

                st.info("No conversation history available.")

            else:

                for item in history:

                    with st.expander("Conversation"):

                        st.markdown("### Event")
                        st.write(item["event"])

                        st.markdown("### AI Response")
                        st.write(item["response"])

            st.divider()

            if st.button("Generate AI Conversation Summary"):

                summary = requests.get(
                    "http://127.0.0.1:8000/history-summary"
                )

                if summary.status_code == 200:

                    st.subheader("AI Conversation Analysis")

                    st.markdown(summary.json()["summary"])

                else:

                    st.error("Could not generate summary.")

        else:

            st.error("Could not load conversation history.")

    except Exception as e:

        st.error(f"Backend Error: {e}")

# ============================================================
# WIKIPEDIA
# ============================================================

elif page == "Wikipedia Fact Checker":

    st.title("Wikipedia Fact Checker")

    st.write("Verify any topic using Wikipedia.")

    fact_query = st.text_input(
        "Enter a topic",
        placeholder="Example: Blockchain in Healthcare"
    )

    if st.button("🔍 Verify Fact"):

        try:

            response = requests.get(
                "http://127.0.0.1:8000/fact-check",
                params={"query": fact_query}
            )

            if response.status_code == 200:

                result = response.json()

                st.success("Wikipedia Summary")

                st.write(result["summary"])

                if result["url"]:

                    st.markdown(
                        f"###  [Read Full Article]({result['url']})"
                    )

            else:
                st.error("Could not fetch Wikipedia information.")

        except Exception:
            st.error("Backend is not running.")

# ============================================================
#  feedback HISTORY
# ============================================================

# ============================================================
# FEEDBACK HISTORY
# ============================================================

elif page == "Feedback History":

    st.title("Feedback History")

    try:

        response = requests.get("http://127.0.0.1:8000/feedback")

        if response.status_code == 200:

            feedback = response.json()

            if len(feedback) == 0:

                st.info("No feedback available.")

            else:

                for item in feedback:

                    with st.expander(item["feedback"]):

                        st.markdown("### AI Response")
                        st.write(item["response"])

                        st.markdown("### User Feedback")
                        st.success(item["feedback"])

            st.divider()

            if st.button("Generate AI Feedback Analysis"):

                with st.spinner("Analyzing feedback..."):

                    summary = requests.get(
                        "http://127.0.0.1:8000/feedback-summary"
                    )

                    if summary.status_code == 200:

                        st.subheader("AI Feedback Analysis")

                        st.markdown(summary.json()["summary"])

                    else:

                        st.error("Could not analyze feedback.")

        else:

            st.error("Could not load feedback.")

    except Exception as e:

        st.error(f"Backend Error: {e}")
# ============================================================
# HISTORY
# ============================================================
