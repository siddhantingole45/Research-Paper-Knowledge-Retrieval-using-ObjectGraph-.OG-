import streamlit as st

from query_engine import (
    get_all_nodes,
    get_node,
    calculate_token_savings
)

st.set_page_config(
    page_title="Research Paper ObjectGraph Demo",
    layout="wide"
)

st.title("Research Paper Knowledge Retrieval using ObjectGraph (.OG)")

st.markdown(
    """
    Demonstration of the ObjectGraph concept proposed in the paper.
    
    Instead of loading the entire paper,
    retrieve only the required knowledge node.
    """
)

st.divider()

nodes = get_all_nodes()

selected_node = st.selectbox(
    "Select Knowledge Node",
    nodes
)

if st.button("Retrieve Node"):

    node_data = get_node(selected_node)

    st.subheader("Retrieved Node")

    st.json(node_data)

    stats = calculate_token_savings(selected_node)

    st.divider()

    st.subheader("Token Savings Comparison")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Full Paper Tokens",
            stats["full_document_tokens"]
        )

    with col2:
        st.metric(
            "Retrieved Node Tokens",
            stats["retrieved_tokens"]
        )

    with col3:
        st.metric(
            "Savings %",
            f"{stats['savings_percentage']}%"
        )
