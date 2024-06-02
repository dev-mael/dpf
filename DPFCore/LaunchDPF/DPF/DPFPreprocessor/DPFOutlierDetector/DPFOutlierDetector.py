from DPFCore.LaunchDPF.DPF.dpf_config import DPFOutlierDetectorConfig


class DPFOutlierDetector:
    def __init__(self, prepared_df):
        self._prepared_dayahead_df = prepared_df
        self._PRICE = DPFOutlierDetectorConfig.PRICE

    def detect(self):
        pass
