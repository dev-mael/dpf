from DPFCore.LaunchDPF.DPF.DPFModeller.LinearModel.LinearModelVariablesPreparator.AR1.AR1VariablesPreparator import (
    AR1VariablesPreparator)
from DPFCore.LaunchDPF.DPF.DPFModeller.LinearModel.LinearModelVariablesPreparator.AR1h.AR1hVariablesPreparator import (
    AR1hVariablesPreparator)
from DPFCore.LaunchDPF.DPF.DPFModeller.LinearModel.LinearModelVariablesPreparator.AR1hm.AR1hmVariablesPreparator import (
    AR1hmVariablesPreparator)
from DPFCore.LaunchDPF.DPF.DPFModeller.LinearModel.LinearModelVariablesPreparator.AR2.AR2VariablesPreparator import (
    AR2VariablesPreparator)
from DPFCore.LaunchDPF.DPF.DPFModeller.LinearModel.LinearModelVariablesPreparator.AR2h.AR2hVariablesPreparator import (
    AR2hVariablesPreparator)
from DPFCore.LaunchDPF.DPF.DPFModeller.LinearModel.LinearModelVariablesPreparator.AR2hm.AR2hmVariablesPreparator import (
    AR2hmVariablesPreparator)
from DPFCore.LaunchDPF.DPF.DPFModeller.LinearModel.LinearModelVariablesPreparator.mAR1.mAR1VariablesPreparator import (
    mAR1VariablesPreparator)
from DPFCore.LaunchDPF.DPF.DPFModeller.LinearModel.LinearModelVariablesPreparator.mAR1h.mAR1hVariablesPreparator import (
    mAR1hVariablesPreparator)
from DPFCore.LaunchDPF.DPF.DPFModeller.LinearModel.LinearModelVariablesPreparator.mAR1hm.mAR1hmVariablesPreparator import (
    mAR1hmVariablesPreparator)
from DPFCore.LaunchDPF.DPF.DPFModeller.LinearModel.LinearModelModelDefiner.AR1.AR1ModelDefiner import AR1ModelDefiner
from DPFCore.LaunchDPF.DPF.DPFModeller.LinearModel.LinearModelModelDefiner.AR1h.AR1hModelDefiner import AR1hModelDefiner
from DPFCore.LaunchDPF.DPF.DPFModeller.LinearModel.LinearModelModelDefiner.AR1hm.AR1hmModelDefiner import \
    AR1hmModelDefiner
from DPFCore.LaunchDPF.DPF.DPFModeller.LinearModel.LinearModelModelDefiner.AR2.AR2ModelDefiner import \
    AR2ModelDefiner
from DPFCore.LaunchDPF.DPF.DPFModeller.LinearModel.LinearModelModelDefiner.AR2h.AR2hModelDefiner import \
    AR2hModelDefiner
from DPFCore.LaunchDPF.DPF.DPFModeller.LinearModel.LinearModelModelDefiner.AR2hm.AR2hmModelDefiner import \
    AR2hmModelDefiner
from DPFCore.LaunchDPF.DPF.DPFModeller.LinearModel.LinearModelModelDefiner.mAR1.mAR1ModelDefiner import \
    mAR1ModelDefiner
from DPFCore.LaunchDPF.DPF.DPFModeller.LinearModel.LinearModelModelDefiner.mAR1h.mAR1hModelDefiner import \
    mAR1hModelDefiner
from DPFCore.LaunchDPF.DPF.DPFModeller.LinearModel.LinearModelModelDefiner.mAR1hm.mAR1hmModelDefiner import \
    mAR1hmModelDefiner

class ModellerFactory:
    @staticmethod
    def get_variables_preparator(model, *params):
        if model == 'AR1':
            return AR1VariablesPreparator(*params)
        elif model == 'AR1h':
            return AR1hVariablesPreparator(*params)
        elif model == 'AR1hm':
            return AR1hmVariablesPreparator(*params)
        elif model == 'AR2':
            return AR2VariablesPreparator(*params)
        elif model == 'AR2h':
            return AR2hVariablesPreparator(*params)
        elif model == 'AR2hm':
            return AR2hmVariablesPreparator(*params)
        elif model == 'mAR1':
            return mAR1VariablesPreparator(*params)
        elif model == 'mAR1h':
            return mAR1hVariablesPreparator(*params)
        elif model == 'mAR1hm':
            return mAR1hmVariablesPreparator(*params)

    @staticmethod
    def get_model_definer(model):
        if model == 'AR1':
            return AR1ModelDefiner()
        elif model == 'AR1h':
            return AR1hModelDefiner()
        elif model == 'AR1hm':
            return AR1hmModelDefiner()
        elif model == 'AR2':
            return AR2ModelDefiner()
        elif model == 'AR2h':
            return AR2hModelDefiner()
        elif model == 'AR2hm':
            return AR2hmModelDefiner()
        elif model == 'mAR1':
            return mAR1ModelDefiner()
        elif model == 'mAR1h':
            return mAR1hModelDefiner()
        elif model == 'mAR1hm':
            return mAR1hmModelDefiner()