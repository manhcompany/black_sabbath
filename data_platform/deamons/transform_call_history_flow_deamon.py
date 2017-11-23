import sys

from data_flows.external_deduplication import ExternalDeDuplication
from flows.transform_call_history_flow import TransformCallHistoryFlow
from storage.configuration import FileConfig, ParquetConfig
from storage.storage_factory import StorageFactory

if __name__ == '__main__':
    source_path = sys.argv[1]
    target_path = sys.argv[2]
    deduplication_path = sys.argv[3]

    source_storage = StorageFactory.get(FileConfig(source_path=source_path, target_path=''))
    target_storage = StorageFactory.get(ParquetConfig(source_path='', target_path=target_path))
    deduplication_storage = StorageFactory.get(ParquetConfig(source_path=deduplication_path, target_path=''))
    deduplication = ExternalDeDuplication(parquet_storage=deduplication_storage, key="call_id")

    flow = TransformCallHistoryFlow(source=source_storage, target=target_storage, deduplication=deduplication)
    flow.start()