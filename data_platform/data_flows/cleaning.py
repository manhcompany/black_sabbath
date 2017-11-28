class Cleaning:
    """
    Abstract cleaning
    """
    def __init__(self):
        """
        Constructor
        """
        pass

    def cleaning(self, df):
        """
        Abstract cleaning function
        :param df: dataframe
        :return: cleaned dataframe
        """
        return df
