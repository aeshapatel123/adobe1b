PDF Document Intelligence Pipeline (Round 1B)
This project is designed to process a collection of PDFs, analyze their contents, and generate structured JSON outputs that summarize the most relevant sections and subsections.
It was built to support multiple use cases (Travel Planner, Research Reviews, Business Analysis, Education) without hardcoding any specific domain.

Features
Automatically scans all collections of PDFs inside the input/ folder.

Generates clean JSON outputs in the output/ folder for each collection.

Extracts:

Metadata (input documents, detected persona, job to be done, timestamp)

Top relevant sections (title, page number, importance rank)

Subsection summaries (refined text for deeper insights)

Fully supports Docker deployment.

Scales across multiple domains, not just travel-related documents.

Project Structure
graphql
Copy code
├── input/                # Place your collections of PDFs here
│   ├── collection1/
│   ├── collection2/
│   ...
├── output/               # JSON outputs will be generated here
├── src/                  # Core Python modules
│   ├── pipeline.py
│   ├── extractor.py
├── run.py                # Main entry point
├── Dockerfile            # Docker setup
├── requirements.txt      # Python dependencies
└── README.md             # This file
How to Run
1. Local (without Docker)
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the pipeline:

bash
Copy code
python run.py
Check the output/ folder for the generated JSON files.

2. Using Docker
Build the Docker image:

bash
Copy code
docker build -t pdf-intelligence .
Run the container:

bash
Copy code
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output pdf-intelligence

Why This Project?
Automates manual document review for faster insights.

Works for multi-domain use cases (Travel, Research, Business, Education, etc.).

Can be easily extended for advanced ML-based classification and summarization.

Next Steps
Improve ranking mechanism for better accuracy.

Add NER & classification models for even more context-aware outputs.
