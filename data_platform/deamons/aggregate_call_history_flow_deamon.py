import sys

from flows.aggregate_call_history_flow import AggregateCallHistoryFlow
from storage.configuration import ParquetConfig
from storage.storage_factory import StorageFactory

if __name__ == '__main__':
    source_path = sys.argv[1]
    target_path = sys.argv[2]
    func_name = sys.argv[3]

    data_storage = StorageFactory.get(ParquetConfig(source_path=source_path, target_path=target_path))

    flow = AggregateCallHistoryFlow(source=data_storage, target=data_storage, func_name=func_name)
    flow.start()