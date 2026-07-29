# src/ml_model — Graph Intelligence Model (Student 3: D.Ebenezer Paul Leon)

This directory contains the machine learning pipeline for the Explainable Graph Intelligence model.

## Files

| File | Description |
|------|-------------|
| `preprocessing.py` | Data loading, cleaning, and graph construction |
| `train.py` | Model training script |
| `predict.py` | Inference / prediction script |
| `model.pkl` | Saved trained model artifact (generated after training) |

## Usage

```bash
# Step 1: Preprocess data
python preprocessing.py --input ../../dataset/raw/ --output ../../dataset/processed/

# Step 2: Train model
python train.py --data ../../dataset/processed/ --output model.pkl

# Step 3: Predict
python predict.py --model model.pkl --input <sample_data>
```
