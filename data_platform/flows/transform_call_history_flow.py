from data_flows.transformation import Transformation
from models.call_history import CallHistory, CallHistoryCleaning, CallHistoryInternalDeDuplication


class TransformCallHistoryFlow:
    def __init__(self, source, target, deduplication=None):
        self.source = source
        self.target = target
        self.deduplication = deduplication

    def start(self):
        data = self.source.load()
        model = CallHistory()
        cleaning = CallHistoryCleaning()
        internal_deduplication = CallHistoryInternalDeDuplication()
        transformation = Transformation(model=model,
                                        external_deduplication=self.deduplication,
                                        cleaning=cleaning,
                                        internal_deduplication=internal_deduplication)
        result = transformation.start(data)
        self.target.save(data=result, coalesce=1)
