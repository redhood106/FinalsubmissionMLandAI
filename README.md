# FinalsubmissionMLandAI

# Hyperparameter Optimization for Cyberattack Detection

This repository contains code and resources for detecting cyberattacks through network traffic analysis using hyperparameter optimization techniques.

## Repository Structure

- `data/`: Contains raw and processed datasets.
- `notebooks/`: Jupyter Notebooks for data preprocessing, model training, and hyperparameter optimization.
- `models/`: Directory to save trained models.
- `reports/`: Contains model card and datasheet for documenting the model and dataset.
- `scripts/`: Python scripts for data preprocessing, model training, and hyperparameter optimization.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `README.md`: Overview and instructions for the repository.
- `requirements.txt`: List of dependencies required to run the project.

## Getting Started

### Prerequisites

- Python 3.x
- Jupyter Notebook
- Install dependencies: `pip install -r requirements.txt`

### Dataset

The dataset used for this project is available in the `data/` directory. Ensure the raw data is placed in `data/raw_data.csv`.

### Running the Project

1. **Data Preprocessing**:
   - Use `notebooks/01_data_preprocessing.ipynb` or run `python scripts/data_preprocessing.py`.

2. **Model Training**:
   - Use `notebooks/02_model_training.ipynb` or run `python scripts/train_model.py`.

3. **Hyperparameter Optimization**:
   - Use `notebooks/03_hyperparameter_optimization.ipynb` or run `python scripts/hyperparameter_optimization.py`.

### Documentation

- `reports/model_card.md`: Detailed information about the model.
- `reports/datasheet.md`: Detailed information about the dataset.
