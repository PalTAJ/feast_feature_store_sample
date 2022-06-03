
# Importing dependencies
import pandas as pd
from feast import FeatureStore
from feast.infra.offline_stores.file_source import SavedDatasetFileStorage

# Getting our FeatureStore
store = FeatureStore(repo_path="breast_cancer/")

# Reading our targets as an entity DataFrame
entity_df = pd.read_parquet(path="breast_cancer/data/target_df.parquet")

