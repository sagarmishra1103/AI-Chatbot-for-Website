import re

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text.split()

def score_chunk(chunk, query_words):
    chunk_words = preprocess(chunk)
    return sum(chunk_words.count(word) for word in query_words)

def get_top_chunks(query, chunks, top_k=3):
    query_words = preprocess(query)

    scored = []
    for chunk in chunks:
        score = score_chunk(chunk, query_words)
        if score > 0:
            scored.append((chunk, score))

    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:top_k]