"""
Deterministic Reasoning Demo
Inspired by the Scientific Copilot experiment (EDCA-LAB)
"""

steps = [
    "R1: Clarify the scientific question.",
    "R2: Identify variables and constraints.",
    "R3: Describe mechanisms or hypotheses.",
    "R4: Provide a stable, domain-independent reasoning path.",
    "R5: Produce a concise, reproducible scientific explanation.",
]

def deterministic_reasoning(question: str):
    trace = []
    trace.append(("input", question))

    explanation = []

    for s in steps:
        trace.append(("step", s))
        explanation.append(f"{s} → done")

    conclusion = (
        "This is a deterministic reasoning trace showing "
        "how a scientific question is broken into stable, "
        "repeatable phases without hallucinated steps."
    )

    trace.append(("output", conclusion))

    return conclusion, trace


if __name__ == "__main__":
    q = "Why does a cell need energy?"
    result, trace = deterministic_reasoning(q)

    print("QUESTION:", q, "\n")
    print("RESULT:", result, "\n")
    print("TRACE:")
    for item in trace:
        print(item)
