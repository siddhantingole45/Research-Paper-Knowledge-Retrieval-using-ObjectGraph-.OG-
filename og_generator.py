import re

def generate_nodes(text):

    nodes = {}

    sections = [
        "abstract",
        "introduction",
        "methodology",
        "methods",
        "dataset",
        "results",
        "discussion",
        "conclusion"
    ]

    text_lower = text.lower()

    positions = []

    for section in sections:

        match = re.search(rf"\b{section}\b", text_lower)

        if match:
            positions.append(
                (section, match.start())
            )

    positions.sort(key=lambda x: x[1])

    for i in range(len(positions)):

        section_name = positions[i][0]

        start = positions[i][1]

        if i < len(positions) - 1:
            end = positions[i + 1][1]
        else:
            end = len(text)

        nodes[section_name] = text[start:end].strip()

    return nodes