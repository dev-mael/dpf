from DPFCore.LaunchDPF.DPF.DPFModeller.LinearModel.LinearModelVariablesPreparator.LinearModelVariablesPreparator import \
    LinearModelVariablesPreparator


class AR1VariablesPreparator(LinearModelVariablesPreparator):
    def __init__(self, transformed_dayahead_df, hour):
        super().__init__(transformed_dayahead_df, hour)
