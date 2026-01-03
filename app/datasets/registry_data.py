from app.datasets.parallel_dataset import ParallelDataset

DATASETS: dict[str, ParallelDataset] = {}

def load_dataset(name: str, path: str) -> None:
    dataset = ParallelDataset(path)
    dataset.load()
    DATASETS[name] = dataset
    print(f"✅ Loaded dataset: {name} with {len(dataset.pairs)} pairs")



def get_dataset(name: str) -> ParallelDataset:
    return DATASETS[name]

def list_datasets() -> list[str]:
    return list(DATASETS.keys())

# Auto-load datasets on module import
try:
    load_dataset("healthcare", "datasets/healthcare_base.csv")
    load_dataset("education", "datasets/education_base.csv")
    load_dataset("general", "datasets/general_base.csv")
    load_dataset("government", "datasets/test_data.csv")
    print(f"📚 Total datasets loaded: {len(DATASETS)}")
except Exception as e:
    print(f"❌ Error loading datasets: {e}")