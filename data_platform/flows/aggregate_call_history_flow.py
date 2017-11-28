from data_flows.data_flow import DataFlow
import queries.call_history_queries as cq


class AggregateCallHistoryFlow:
    def __init__(self,source, target, func_name):
        self.source = source
        self.target = target
        self.func_name = func_name

    def start(self):
        data = self.source.load()
        if self.func_name == 'aggregate_call_duration':
            flow = DataFlow(handle=cq.aggregate_call_duration)
        elif self.func_name == 'aggregate_number_of_call':
            flow = DataFlow(handle=cq.aggregate_number_of_call)
        elif self.func_name == 'aggregate_number_of_call_in_working_hour':
            flow = DataFlow(handle=cq.aggregate_number_of_call_in_working_hour, first_hour=8, second_hour=17)
        elif self.func_name == 'find_imei_most_call':
            flow = DataFlow(handle=cq.find_imei_most_call)
        elif self.func_name == 'find_top_2_localtion':
            flow = DataFlow(handle=cq.find_top_2_localtion)

        df_result = flow.start(data=data)

        self.target.save(data=df_result, coalesce=1)

