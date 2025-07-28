def refine_text(sub_section_analysis):
    refined = []
    for sub in sub_section_analysis:
        text = " ".join(sub["refined_text"].split())
        if text.strip():
            refined.append({
                "document": sub["document"],
                "refined_text": text,
                "page_number": sub["page_number"]
            })
    return refined
