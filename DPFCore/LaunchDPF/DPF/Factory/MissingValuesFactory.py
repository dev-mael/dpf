from DPFCore.LaunchDPF.DPF.DPFPreprocessor.DPFMissingValuesFiller.DPFSmoothedSimilarDayFiller import (
    DPFSmoothedSimilarDayFiller)


class MissingValuesFactory:

    @staticmethod
    def get_filler(missing_values_filler, *params):
        if missing_values_filler == 'smoothed similar day':
            return DPFSmoothedSimilarDayFiller(*params)