from pathlib import Path

# A tiny "corpus" (for demo)
corpus = [
    "Apple releases a new research paper on self-supervised vision.",
    "Tesla introduces an autonomous planning module.",
    "DeepMind publishes a breakthrough in protein folding.",
    "OpenAI improves the function-calling architecture in GPT models.",
]

def deterministic_retrieval(query: str, corpus: list[str]):
    """
    Minimal deterministic retrieval:
    - NOT vector search
    - NOT top-k
    - NOT cosine similarity
    - NOT graph traversal
    - NOT embedding

    Pure expression-guided scoring:
    - exact match > keyphrase > token overlap
    - stable scoring rules
    - no randomness
    """
    key = query.lower().strip()

    def score(doc: str):
        doc_l = doc.lower()

        if key in doc_l:
            return 3  # strongest
        if key.split()[0] in doc_l:
            return 2
        return 1 if any(w in doc_l for w in key.split()) else 0

    scored = [(score(d), d) for d in corpus]
    scored.sort(key=lambda x: (-x[0], corpus.index(x[1])))  # stable tie-breaker

    trace = [{"doc": d, "score": s} for (s, d) in scored]
    best = scored[0][1]

    return best, trace


if __name__ == "__main__":
    query = "openai gpt architecture"
    best, trace = deterministic_retrieval(query, corpus)

    print("QUERY:", query)
    print("\nBEST MATCH:")
    print(best)

    print("\nTRACE:")
    for t in trace:
        print(t)
