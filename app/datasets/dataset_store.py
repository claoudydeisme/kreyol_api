from app.datasets.parallel_dataset import ParallelDataset
import logging





logger = logging.getLogger("dataset")

parallel_dataset = ParallelDataset("datasets/healthcare_base.csv")
parallel_dataset.load()

logger.warning(
    f"DATASET LOADED: {len(parallel_dataset.pairs)} pairs"
)
