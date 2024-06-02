from DPFCore.LaunchDPF.DPF.DPFPreprocessor.DPFSeasonalProcessor.DPFSeasonalDecomposeProcessor import (
    DPFSeasonalDecomposeProcessor)


class SeasonalProcessorFactory:

    @staticmethod
    def get_processor(seasonal_processor, *params):
        if seasonal_processor == 'seasonal decompose':
            return DPFSeasonalDecomposeProcessor(*params)