import os, json
from datetime import datetime

base_folder = "input"
collections = [c for c in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, c))]

for collection in collections:
    pdf_folder = os.path.join(base_folder, collection)
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]

    persona = input(f"Enter persona for {collection}: ")
    job = input(f"Enter job to be done for {collection}: ")

    data = {
        "challenge_info": {
            "challenge_id": f"round_1b_{datetime.now().strftime('%Y%m%d%H%M')}",
            "test_case_name": collection,
            "description": f"Auto-generated challenge for {collection}"
        },
        "documents": [{"filename": f, "title": os.path.splitext(f)[0]} for f in pdf_files],
        "persona": {"role": persona},
        "job_to_be_done": {"task": job}
    }

    output_json = os.path.join(pdf_folder, "challenge_input.json")
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"✅ Created input JSON for {collection}: {output_json}")
