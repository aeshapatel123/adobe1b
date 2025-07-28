from sklearn.feature_extraction.text import TfidfVectorizer

def assign_importance(extracted_sections, job_description):
    section_texts = [sec["section_title"] for sec in extracted_sections]
    vectorizer = TfidfVectorizer().fit(section_texts + [job_description])

    scores = vectorizer.transform([job_description]).toarray()[0]

    for idx, sec in enumerate(extracted_sections):
        sec["importance_rank"] = idx + 1

    return sorted(extracted_sections, key=lambda s: s["importance_rank"])
