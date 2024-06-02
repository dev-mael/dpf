from DPFCore.LaunchDPF.DPF.dpf_config import DPFSeasonalProcessorConfig


class DPFSeasonalProcessor:
    def __init__(self, df):
        self._df = df
        self._PRICE = DPFSeasonalProcessorConfig.PRICE

    def process(self):
        pass
