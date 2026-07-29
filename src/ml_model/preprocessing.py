"""
preprocessing.py
----------------
Data loading, cleaning, and graph construction for cloud resource abuse detection.
Author: D.Ebenezer Paul Leon (Student 3 - feature/student3)
"""

import os
import argparse


def load_data(input_dir: str):
    """Load raw dataset files from input_dir."""
    # TODO: Implement data loading
    print(f"[INFO] Loading data from: {input_dir}")
    return None


def clean_data(df):
    """Handle missing values, normalize, encode features."""
    # TODO: Implement cleaning pipeline
    print("[INFO] Cleaning data...")
    return df


def build_graph(df):
    """Convert tabular tenant activity data into a graph structure."""
    # TODO: Construct adjacency matrix / edge list
    print("[INFO] Building graph from tenant activity data...")
    return None


def save_processed(data, output_dir: str):
    """Save processed data and graph to output_dir."""
    os.makedirs(output_dir, exist_ok=True)
    # TODO: Save files
    print(f"[INFO] Processed data saved to: {output_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Preprocess cloud resource abuse dataset")
    parser.add_argument("--input", required=True, help="Path to raw data directory")
    parser.add_argument("--output", required=True, help="Path to save processed data")
    args = parser.parse_args()

    raw_data = load_data(args.input)
    cleaned = clean_data(raw_data)
    graph = build_graph(cleaned)
    save_processed(graph, args.output)
