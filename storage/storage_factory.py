from storage.configuration import FileConfig, ParquetConfig, AvroConfig

from storage.spark_storage import FileStorage, ParquetStorage, AvroStorage


class StorageFactory:
    def __init__(self):
        pass

    @staticmethod
    def get(config):
        return {
            FileConfig.__name__: FileStorage(config),
            ParquetConfig.__name__: ParquetStorage(config),
            AvroConfig.__name__: AvroStorage(config)
        }[config.__class__.__name__]
