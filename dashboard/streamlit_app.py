import streamlit as st

from workflows.incident_workflow import (
    run_incident_workflow
)

st.set_page_config(
    page_title="CyberIntelAI",
    layout="wide"
)

st.title(
    "🛡️ CyberIntelAI"
)

st.markdown(
    """
    AI-Powered SOC Assistant

    Educational Use Only
    """
)

alert = st.text_area(
    "Paste Security Alert"
)

if st.button(
    "Analyze"
):

    with st.spinner(
        "Investigating..."
    ):

        result = (
            run_incident_workflow(alert)
        )

    st.success(
        "Analysis Complete"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Threat Type")
        st.write(
            result["classification"]
        )

        st.subheader("Risk")
        st.write(
            result["risk"]
        )

        st.subheader("MITRE ATT&CK")
        st.json(
            result["mitre"]
        )

    with col2:

        st.subheader("Extracted IOCs")
        st.json(
            result["iocs"]
        )

    st.subheader(
        "Threat Hunting"
    )

    st.write(
        result["threat_hunting"]
    )

    st.subheader(
        "Incident Response Plan"
    )

    st.write(
        result["response_plan"]
    )

    st.subheader(
        "SOC Report"
    )

    st.write(
        result["report"]
    )
