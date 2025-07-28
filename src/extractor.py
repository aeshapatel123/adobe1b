import fitz  # PyMuPDF

def extract_sections(pdf_path):
    """
    Extract sections from a single PDF. Returns list of dicts:
    {document, section_title, page_number, importance_rank}
    """
    sections = []
    doc = fitz.open(pdf_path)

    for page_num, page in enumerate(doc, start=1):
        text = page.get_text("text").strip()

        # Split into lines and treat each as a possible section heading
        for line in text.split("\n"):
            clean_line = line.strip()

            # Filter out junk / bullet points
            if not clean_line or len(clean_line.split()) < 3:
                continue
            if any(bullet in clean_line for bullet in ["•", "-", "–"]):
                continue

            sections.append({
                "document": pdf_path.name,
                "section_title": clean_line,
                "page_number": page_num,
                "importance_rank": len(clean_line)  # shorter = higher importance
            })

    doc.close()
    return sections


def extract_subsections(section):
    """
    For now, returns a very short refined_text for the given section.
    This avoids repeating full paragraphs.
    """
    return [{
        "document": section["document"],
        "refined_text": f"{section['section_title']} → Summary ready",
        "page_number": section["page_number"]
    }]
