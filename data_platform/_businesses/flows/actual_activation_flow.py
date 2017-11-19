from _businesses.models.phone_number import PhoneNumber
from data_flows.ingestion import Ingestion


class ActualActivationFlow:
    def __init__(self, source, target):
        self.source = source
        self.target = target

    def start(self):
        data = self.source.load()
        model = PhoneNumber()
        ingestion = Ingestion(model=model)
        rdd_data = ingestion.start(data)
        result_data = ActualActivationFlow.find_actual_activation_flow(rdd_data)
        self.target.save(data=result_data, coalesce=1)

    @staticmethod
    def find_actual_activation_flow(data):
        data.map(lambda x: (x.phone_number, x))\
            .reduceByKey(lambda x, y: PhoneNumber.add(x, y))\
            .map(lambda x: x[1].find_actual_activation())\
            .map(lambda x: x.to_str())
