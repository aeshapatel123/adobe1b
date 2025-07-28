from pathlib import Path
from datetime import datetime
import json

from src.extractor import extract_sections, extract_subsections


def run_pipeline(input_root, output_root):
    input_root = Path(input_root)
    output_root = Path(output_root)
    output_root.mkdir(parents=True, exist_ok=True)

    # Loop through each collection folder inside input_root
    for collection_folder in input_root.iterdir():
        if collection_folder.is_dir():
            print(f"🔎 Processing collection: {collection_folder.name}")

            all_sections = []
            all_subsections = []

            # Iterate over PDFs in this collection
            pdfs = sorted(collection_folder.glob("*.pdf"))
            for pdf_path in pdfs:
                sections = extract_sections(pdf_path)
                all_sections.extend(sections)

                for section in sections:
                    all_subsections.extend(extract_subsections(section))

            # Sort and take top 5 sections
            all_sections = sorted(all_sections, key=lambda x: x["importance_rank"])[:5]

            output_data = {
                "metadata": {
                    "input_documents": [pdf.name for pdf in pdfs],
                    "persona": "Travel Planner",
                    "job_to_be_done": "Plan a trip for a group",
                    "processing_timestamp": datetime.now().isoformat()
                },
                "extracted_sections": all_sections,
                "subsection_analysis": all_subsections
            }

            output_file = output_root / f"{collection_folder.name}_output.json"
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(output_data, f, indent=4)

            print(f"✅ Output saved: {output_file}")
