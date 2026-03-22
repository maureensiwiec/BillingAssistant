import streamlit as st

st.set_page_config(page_title="AI Billing Workflow Assistant", layout="centered")

st.title("AI Billing Workflow Assistant")
st.write("Demo: improve invoice clarity, follow-up communication, and AR risk visibility.")

client = st.text_input("Client Name")
amount = st.text_input("Invoice Amount")
days = st.text_input("Days Outstanding")
notes = st.text_area("Notes")

if st.button("Generate Insights"):
    st.subheader("Improved Invoice Description")
    st.write(
        "Q3 financial workflow optimization and reporting improvements, "
        "including reconciliation support and process efficiency updates."
    )

    st.subheader("Suggested Follow-Up Email")
    st.write(
        f"Hi {client or '[Client]'}, just checking in on the outstanding invoice "
        f"for {amount or '[Amount]'}. Let me know if you need any clarification on the work completed. "
        "Happy to walk through it."
    )

    st.subheader("Risk Insight")
    try:
        d = int(days) if days else 0
    except ValueError:
        d = 0

    if d >= 25:
        st.warning("Elevated collection risk. Recommend follow-up within 2 days.")
    elif d >= 10:
        st.info("Monitor closely. Consider a reminder this week.")
    else:
        st.success("Low current risk based on days outstanding.")

    if notes:
        st.subheader("Context Used")
        st.write(notes)
