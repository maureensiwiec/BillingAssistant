import streamlit as st

st.set_page_config(
    page_title="AI Billing Workflow Assistant",
    page_icon="💸",
    layout="wide"
)

st.title("AI Billing Workflow Assistant")
st.caption("Demo concept: improve invoice clarity, follow-up communication, and AR risk visibility.")

with st.sidebar:
    st.header("Demo Scenarios")
    if st.button("Load Late Payer Example"):
        st.session_state.client = "ABC Advisory Group"
        st.session_state.amount = "$8,500"
        st.session_state.days = "25"
        st.session_state.notes = "Historically pays late. Invoice description is vague. Client may need follow-up."
    if st.button("Load Healthy Account Example"):
        st.session_state.client = "North Ridge Tax"
        st.session_state.amount = "$3,200"
        st.session_state.days = "6"
        st.session_state.notes = "Usually pays on time. Minimal current concern."

client_default = st.session_state.get("client", "")
amount_default = st.session_state.get("amount", "")
days_default = st.session_state.get("days", "")
notes_default = st.session_state.get("notes", "")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Input")
    client = st.text_input("Client Name", value=client_default)
    amount = st.text_input("Invoice Amount", value=amount_default)
    days = st.text_input("Days Outstanding", value=days_default)
    notes = st.text_area("Notes", value=notes_default, height=160)

    generate = st.button("Generate Insights", type="primary")

with col2:
    st.subheader("What this demo shows")
    st.markdown(
        """
        - Clearer invoice language  
        - Smarter follow-up communication  
        - Early AR risk visibility  
        - Workflow-oriented AI support
        """
    )

if generate:
    try:
        d = int(days) if days else 0
    except ValueError:
        d = 0

    st.markdown("---")
    st.subheader("Output")

    out1, out2, out3 = st.columns(3)

    with out1:
        st.markdown("### Improved Invoice Description")
        st.info(
            "Q3 financial workflow optimization and reporting improvements, "
            "including reconciliation support and process efficiency updates."
        )

    with out2:
        st.markdown("### Suggested Follow-Up Email")
        st.success(
            f"Hi {client or '[Client]'}, just checking in on the outstanding invoice "
            f"for {amount or '[Amount]'}. Let me know if you need any clarification on the work completed. "
            "Happy to walk through it."
        )

    with out3:
        st.markdown("### Risk Insight")
        if d >= 25:
            st.warning("Elevated collection risk. Recommend follow-up within 2 days.")
        elif d >= 10:
            st.info("Monitor closely. Consider a reminder this week.")
        else:
            st.success("Low current risk based on days outstanding.")

    st.markdown("---")
    st.subheader("Why this matters")
    st.write(
        "The value is not just automation. It is improving invoice clarity, making follow-up timing more consistent, "
        "and surfacing AR risk earlier in the billing workflow."
    )
