from src.pipeline import run_pipeline

if __name__ == "__main__":
    input_root = "input"      # Folder containing collections
    output_root = "output"    # Output folder

    run_pipeline(input_root, output_root)
