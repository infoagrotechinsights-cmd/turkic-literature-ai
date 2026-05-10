from core.embeddings import embed_text
from core.vector_db import search_vectors
from core.similarity import cosine_similarity
from core.motif_engine import extract_motifs


LANG_PRIORITY = ["az", "tr", "fa"]

def align_poem(poem, target_languages=["tr", "fa"], top_k=5):

    query_vec = embed_text(poem)
    query_motifs = extract_motifs(poem)

    aligned_results = []

    for lang in target_languages:

        results = search_vectors(
            query_vec,
            top_k=top_k,
            filter_lang=lang
        )

        for r in results:

            score = cosine_similarity(query_vec, r["vector"])
            motifs = extract_motifs(r["text"])

            shared_motifs = len(
                set([m["term"] for m in motifs]) &
                set([m["term"] for m in query_motifs])
            )

            aligned_results.append({
                "language": lang,
                "text": r["text"],
                "author": r.get("author", "unknown"),
                "score": float(score),
                "shared_motifs": shared_motifs,
                "alignment_score": float(score + shared_motifs * 0.15)
            })

    return sorted(aligned_results, key=lambda x: x["alignment_score"], reverse=True)
