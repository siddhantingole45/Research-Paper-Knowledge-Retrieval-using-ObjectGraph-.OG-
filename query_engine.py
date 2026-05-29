import json

with open("objectgraph_paper_nodes.json", "r", encoding="utf-8") as file:
    data = json.load(file)


def get_all_nodes():
    return list(data.keys())


def get_node(node_name):
    return data.get(node_name)


def calculate_token_savings(node_name):
    """
    Simulated token comparison
    """

    full_document_tokens = 6000

    node = get_node(node_name)

    if not node:
        return None

    node_tokens = len(str(node).split())

    savings = (
        (full_document_tokens - node_tokens)
        / full_document_tokens
    ) * 100

    return {
        "full_document_tokens": full_document_tokens,
        "retrieved_tokens": node_tokens,
        "savings_percentage": round(savings, 2)
    }