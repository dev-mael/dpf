from DPFCore.LaunchDPF.DPF.dpf_config import DPFMissingValuesFillerConfig


class DPFMissingValuesFiller:
    def __init__(self, cleaned_df):
        self._cleaned_dayahead_df = cleaned_df
        self._PRICE = DPFMissingValuesFillerConfig.PRICE
        self._DOW = DPFMissingValuesFillerConfig.DOW

    def fill(self):
        pass