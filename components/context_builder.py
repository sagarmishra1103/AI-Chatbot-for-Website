import re

def clean_text(text: str) -> str:
    return re.sub(r'\s+', ' ', text).strip()

def split_into_sentences(text: str):
    return re.split(r'(?<=[.!?]) +', text)

def build_chunks(text, chunk_size=700, overlap=100):
    text = clean_text(text)
    sentences = split_into_sentences(text)

    chunks = []
    current_chunk = []
    current_len = 0

    for sentence in sentences:
        words = sentence.split()
        if current_len + len(words) > chunk_size:
            chunk_text = " ".join(current_chunk)
            chunks.append(chunk_text)

            overlap_words = chunk_text.split()[-overlap:]
            current_chunk = [" ".join(overlap_words)]
            current_len = len(overlap_words)

        current_chunk.append(sentence)
        current_len += len(words)

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks