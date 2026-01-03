"""from fastapi import FastAPI
from app.datasets.registry_data import load_dataset

app = FastAPI()

@app.on_event("startup")
def load_all_datasets():
    load_dataset("government", "datasets/test_data.csv")
    load_dataset("healthcare", "datasets/healthcare_base.csv")
    load_dataset("education", "datasets/education_base.csv")
    load_dataset("general", "datasets/general_base.csv")
"""
