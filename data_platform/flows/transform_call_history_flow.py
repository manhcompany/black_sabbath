from data_flows.transformation import Transformation
from models.call_history import CallHistory


class TransformCallHistoryFlow:
    def __init__(self, source, target, deduplication=None):
        self.source = source
        self.target = target
        self.deduplication = deduplication

    def start(self):
        data = self.source.load()
        model = CallHistory()
        transformation = Transformation(model=model, deduplication=self.deduplication)
        result = transformation.start(data)
        self.target.save(data=result, coalesce=1)