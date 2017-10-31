class Storage:
    def __init__(self):
        pass

    def load(self):
        pass

    def save(self, data):
        pass


class SparkStorage(Storage):
    def __init__(self):
        super().__init__()


class NoSqlStorage(Storage):
    def __init__(self):
        super().__init__()


class PlainTextFileStorage(Storage):
    def __init__(self, config, handle):
        super().__init__()
        self.__config = config
        self.__handle = handle

    def load(self):
        with open(self.__config.get_source_path()) as f:
            lines = f.readlines()
            for line in lines:
                self.__handle.handle(line)

    def save(self, lines):
        with open(self.__config.get_target_path()) as f:
            for line in lines:
                f.write(line)
