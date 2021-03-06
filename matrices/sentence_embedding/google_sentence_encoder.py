from sklearn.metrics.pairwise import cosine_similarity


def run_gse_benchmark(sentences1, sentences2, embed):
    raw_sentences1 = [sent1.raw for sent1 in sentences1]
    raw_sentences2 = [sent2.raw for sent2 in sentences2]

    embeddings1 = embed(raw_sentences1)
    embeddings2 = embed(raw_sentences2)

    gse_sims = []
    for (emb1, emb2) in zip(embeddings1, embeddings2):
        sim = cosine_similarity(emb1.reshape(1, -1), emb2.reshape(1, -1))[0][0]
        gse_sims.append(sim)

    return gse_sims
