import sys

from flows.actual_activation_flow import ActualActivationFlow
from storage.configuration import FileConfig
from storage.storage_factory import StorageFactory

if __name__ == '__main__':
    source_path = sys.argv[1]
    target_path = sys.argv[2]

    data_storage = StorageFactory.get(FileConfig(source_path=source_path, target_path=target_path))
    
    flow = ActualActivationFlow(data_storage, data_storage)
    flow.start()
