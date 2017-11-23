from data_flows.internal_deduplication import InternalDeDuplication

from data_flows.cleaning import Cleaning

from data_flows.model import Model
from utils.coder import SHA256Encoder
from utils.converter import StringConverter


class CallHistory(Model):
    def __init__(self):
        super().__init__()
        self.from_phone_number = ''
        self.to_phone_number = ''
        self.start_time = ''
        self.call_duration = 0
        self.imei = ''
        self.location = ''
        self.call_id = ''
        self.start_timestamp = 0.0
        self.hour = 0

    @staticmethod
    def load(data):
        data_split = data.split(';')
        result = CallHistory()
        try:
            result.from_phone_number = data_split[0]
            result.to_phone_number = data_split[1]
            result.start_time = data_split[2]
            result.call_duration = int(data_split[3])
            result.imei = data_split[4]
            result.location = data_split[5]
        except IndexError:
            return None
        return result

    def transform(self):
        try:
            self.start_timestamp = StringConverter.convert_string2timestamp(self.start_time, "%d/%m/%Y %H:%M:%S")
            self.hour = CallHistory.get_hour_from_datetime(self.start_time)
            self.call_id = SHA256Encoder\
                .hash("%s-%s-%s" % (self.from_phone_number, self.to_phone_number, self.start_time))
        except Exception:
            return None
        return self

    def get_id(self):
        return self.call_id

    def get_str(self):
        # TODO
        pass

    @staticmethod
    def get_hour_from_datetime(datetime_str):
        return int(datetime_str.split(" ")[1].split(":")[0])


class CallHistoryCleaning(Cleaning):
    def __init__(self):
        super().__init__()

    def cleaning(self, df):
        return df.dropna()


class CallHistoryInternalDeDuplication(InternalDeDuplication):
    def __init__(self):
        super().__init__()

    def deduplicate(self, df):
        return df.drop_duplicates()
