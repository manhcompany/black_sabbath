class InternalDeDuplication:
    """
    Abstract internal deduplication
    """
    def __init__(self):
        """
        Constructor
        """
        pass

    def deduplicate(self, df):
        """
        Abstract deduplication function, default is do not nothing
        :param df: DataFrame
        :return: DataFrame
        """
        return df
