class SingletonMeta(type):
    """
    Singleton Meta
    """
    def __init__(cls, *args, **kwargs):
        """
        Constructor
        :param args:
        :param kwargs:
        """
        cls._instance = None
        super(SingletonMeta, cls).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instance
