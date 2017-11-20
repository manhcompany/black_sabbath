from data_flows.model import Model
from utils.converter import StringConverter


class PhoneNumber(Model):
    def __init__(self):
        super().__init__()
        self.phone_number = ''
        self.activation_date = []
        self.deactivation_date = []
        self.actual_activation_date = ''

    @staticmethod
    def load(data, **kwargs):
        data_list = data.split(',')
        if len(data_list) < 2:
            return None
        result = PhoneNumber()
        result.phone_number = data_list[0]
        result.activation_date = [data_list[1]]
        try:
            if len(data_list[2]):
                result.deactivation_date = [data_list[2]]
            else:
                result.deactivation_date = []
        except IndexError as e:
            result.deactivation_date = []
        return result

    @staticmethod
    def add(x, y):
        result = PhoneNumber()
        result.phone_number = x.phone_number
        result.activation_date = x.activation_date + y.activation_date
        result.deactivation_date = x.deactivation_date + y.deactivation_date
        return result

    def transform(self):
        return self

    def get_str(self):
        return '%s,%s' % (self.phone_number, self.actual_activation_date)

    def find_actual_activation(self):
        activation_timestamp = [StringConverter.convert_string2timestamp(i) for i in self.activation_date]
        deactivation_timestamp = [StringConverter.convert_string2timestamp(i) for i in self.deactivation_date]
        activation_timestamp.sort()
        deactivation_timestamp.sort()
        results = [t for t in activation_timestamp]
        i = 0
        j = 0
        while i < len(activation_timestamp) and j < len(deactivation_timestamp):
            if activation_timestamp[i] == deactivation_timestamp[j]:
                results[i] = -1.0
                i += 1
                j += 1
                continue
            if activation_timestamp[i] > deactivation_timestamp[j]:
                j += 1
                continue
            if activation_timestamp[i] < deactivation_timestamp[j]:
                i += 1
                continue

        index = len(results) - 1
        while results[index] == -1.0 and index > 0:
            index -= 1
        self.actual_activation_date = StringConverter.convert_timestamp2string(results[index])
        self.activation_date = results
        return self
