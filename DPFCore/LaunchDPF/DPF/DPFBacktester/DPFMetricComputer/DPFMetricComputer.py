import pandas as pd

from DPFCore.LaunchDPF.DPF.DPFBacktester.DPFMetricComputer.DPFMAPEComputer import DPFMAPEComputer
from DPFCore.LaunchDPF.DPF.DPFBacktester.DPFMetricComputer.DPFMAEComputer import DPFMAEComputer
from DPFCore.LaunchDPF.DPF.DPFBacktester.DPFMetricComputer.DPFRMSEComputer import DPFRMSEComputer
from DPFCore.LaunchDPF.DPF.dpf_config import DPFMetricComputerConfig


class DPFMetricComputer:
    def __init__(self, predicted_df):
        self._predicted_df = predicted_df
        self._metric_dict = DPFMetricComputerConfig.metric_dict
        self._metric_df = pd.DataFrame(columns=self._metric_dict.keys())

    def compute(self):
        for metric in self._metric_dict.keys():
            metric_value = eval(self._metric_dict[metric]).compute(self._predicted_df)
            self._metric_df.loc[0, metric] = metric_value

        return self._metric_df
