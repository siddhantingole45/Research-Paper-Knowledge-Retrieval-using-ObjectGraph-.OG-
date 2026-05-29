import streamlit as st
import os
from parser import extract_text
from og_generator import generate_nodes

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

st.set_page_config(
    page_title="Research Paper Knowledge Retrieval using ObjectGraph (.OG)",
    layout="wide"
)

st.title("Research Paper Knowledge Retrieval using ObjectGraph (.OG)")

st.write(
    "Upload a research paper PDF and convert it into ObjectGraph-style knowledge nodes."
)

st.divider()

# PDF Upload Section

uploaded_file = st.file_uploader(
    "Upload Research Paper PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    file_path = os.path.join(
        UPLOAD_FOLDER,
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(
        f"PDF Uploaded Successfully: {uploaded_file.name}"
    )

    st.code(file_path)

    # --------------------
    # Extract Text
    # --------------------

    paper_text = extract_text(file_path)
    nodes = generate_nodes(paper_text)

    st.divider()

    st.subheader("Extracted Text Preview")

    st.text_area(
        "First 3000 Characters",
        paper_text[:3000],
        height=300
    )

# ---------------------------------
# Generated Nodes
# ---------------------------------

    st.divider()

    st.subheader("Generated Knowledge Nodes")

    st.json(list(nodes.keys()))

# ---------------------------------
# Nodes Retrieval
# ---------------------------------

    st.divider()

    st.subheader("Retrieve Specific Node")

    selected_node = st.selectbox(
        "Select a Node",
        list(nodes.keys())
    )

    if st.button("Retrieve Node"):

        st.subheader(f"Node: {selected_node}")

        st.text_area(
            "Node Content",
            nodes[selected_node][:3000],
            height=300
        )

        # ==========================
        # Token Calculation
        # ==========================

        full_tokens = len(paper_text.split())

        node_tokens = len(
            nodes[selected_node].split()
        )

        savings = (
            (full_tokens - node_tokens)
            / full_tokens
        ) * 100

        # ==========================
        # Display Token Savings
        # ==========================

        st.divider()

        st.subheader("Token Savings Comparison")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Full Paper Tokens",
            full_tokens
        )

        col2.metric(
            "Retrieved Node Tokens",
            node_tokens
        )

        col3.metric(
            "Savings %",
            f"{savings:.2f}%"
        )