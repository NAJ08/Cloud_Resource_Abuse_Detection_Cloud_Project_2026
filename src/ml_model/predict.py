"""
predict.py
----------
Run inference using the trained Explainable Graph Intelligence model.
Author: D.Ebenezer Paul Leon (Student 3 - feature/student3)
"""

import argparse
import pickle


def load_model(model_path: str):
    """Load a saved model from disk."""
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    print(f"[INFO] Model loaded from: {model_path}")
    return model


def predict(model, input_data):
    """Run prediction on input data and return results with explanations."""
    # TODO: Run inference + generate XAI explanation
    print("[INFO] Running prediction...")
    result = None
    explanation = None
    return result, explanation


def format_output(result, explanation):
    """Pretty-print prediction result and explanation."""
    print("=== Prediction Result ===")
    print(f"Abuse Detected: {result}")
    print(f"Explanation: {explanation}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Predict cloud resource abuse")
    parser.add_argument("--model", default="model.pkl", help="Path to trained model")
    parser.add_argument("--input", required=True, help="Input data (file or JSON string)")
    args = parser.parse_args()

    model = load_model(args.model)
    result, explanation = predict(model, args.input)
    format_output(result, explanation)
