from collections import namedtuple

DataIngestionArtifact = namedtuple("DataIngestionArtifact",["train_file_path","test_file_path","is_ingested","message"])
DataValiationArtifact = namedtuple("DataValiationArtifact",['schema_file_path','report_file_path','report_page_file_path','is_validated','message']) 