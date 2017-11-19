from storage.configuration import FileConfig, ParquetConfig, AvroConfig
from storage.spark_storage import FileStorage, ParquetStorage, AvroStorage


class StorageFactory:
    """
    Storage Factory
    """
    def __init__(self):
        """
        Constructor
        """
        pass

    @staticmethod
    def get(config):
        """
        Get Storage
        :param config: Configuration
        :return: Storage
        """
        return {
            FileConfig.__name__: FileStorage(config),
            ParquetConfig.__name__: ParquetStorage(config),
            AvroConfig.__name__: AvroStorage(config)
        }[config.__class__.__name__]
