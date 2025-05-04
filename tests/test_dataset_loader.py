import pytest
from rag.dataset_loader import load_dataset

def test_load_dataset():
    dataset = load_dataset('rag/data/plants.txt')
    assert len(dataset) > 0, "Dataset should not be empty"
    assert isinstance(dataset, list), "Dataset should be a list"