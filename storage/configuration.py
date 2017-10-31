class Configuration:
    def __init__(self):
        pass


class FileConfig(Configuration):
    __source_path = ''
    __target_path = ''

    def get_source_path(self):
        return self.__source_path

    def get_target_path(self):
        return self.__target_path

    def __init__(self, source_path, target_path):
        super().__init__()
        self.__source_path = source_path
        self.__target_path = target_path


class ParquetConfig(FileConfig):
    def __init__(self, source_path, target_path):
        super().__init__(source_path=source_path, target_path=target_path)


class AvroConfig(FileConfig):
    def __init__(self, source_path, target_path):
        super().__init__(source_path=source_path, target_path=target_path)


class ElasticSearchConfig(Configuration):
    __config = {}

    def __init__(self, config):
        super().__init__()
        self.__config = config
        self.host = config['host']
        self.port = config['port']
        self.access_key = config['access_key']
        self.secret_key = config['secret_key']
        self.region = config['region']


class DynamoDBConfig(Configuration):
    __config = {}

    def __init__(self, config):
        super().__init__()
        self.__config = config

    def get_config(self):
        return self.__config
