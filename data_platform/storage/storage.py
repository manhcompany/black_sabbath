class Storage:
    """
    Storage abstract class
    """
    def __init__(self):
        """
        Constructor
        """
        pass

    def load(self):
        """
        Load data from source path
        :return: Data
        """
        pass

    def save(self, data):
        """
        Save data into target path
        :param data: data
        :return: void
        """
        pass


class SparkStorage(Storage):
    """
    Spark Storage abstract class. Include Parquet and Avro
    """
    def __init__(self):
        """
        Constructor
        """
        super().__init__()


class NoSqlStorage(Storage):
    """
    Nosql Storage abstract class.
    """
    def __init__(self):
        super().__init__()


class PlainTextFileStorage(Storage):
    """
    Plain text storage
    """
    def __init__(self, config, handle):
        """
        Constructor
        :param config: config (source, target)
        :param handle: handle function for each line
        """
        super().__init__()
        self.__config = config
        self.__handle = handle

    def load(self):
        """
        Load data from data source
        :return: void
        """
        with open(self.__config.get_source_path()) as f:
            lines = f.readlines()
            for line in lines:
                self.__handle.handle(line)

    def save(self, lines):
        """
        Save data into target
        :param lines:
        :return:
        """
        with open(self.__config.get_target_path()) as f:
            for line in lines:
                f.write(line)
