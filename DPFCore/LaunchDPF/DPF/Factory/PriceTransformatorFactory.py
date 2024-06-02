from DPFCore.LaunchDPF.DPF.DPFPriceTransformator.DPFAsinhTransformator import DPFAsinhTransformator
from DPFCore.LaunchDPF.DPF.DPFPriceTransformator.DPFLogisticTransformator import DPFLogisticTransformator
from DPFCore.LaunchDPF.DPF.DPFPriceTransformator.DPFBoxCoxTransformator import DPFBoxCoxTransformator
from DPFCore.LaunchDPF.DPF.DPFPriceTransformator.DPFPolyTransformator import DPFPolyTransformator
from DPFCore.LaunchDPF.DPF.DPFPriceTransformator.DPFMLogTransformator import DPFMLogTransformator
from DPFCore.LaunchDPF.DPF.DPFPriceTransformator.DPF3SigmaTransformator import DPF3SigmaTransformator
from DPFCore.LaunchDPF.DPF.DPFPriceTransformator.DPF3SigmaLogTransformator import DPF3SigmaLogTransformator


class PriceTransformatorFactory:

    @staticmethod
    def get_transformator(price_transformator, *params):
        if price_transformator == 'asinh':
            return DPFAsinhTransformator(*params)
        elif price_transformator == 'logistic':
            return DPFLogisticTransformator(*params)
        elif price_transformator == 'boxcox':
            return DPFBoxCoxTransformator(*params)
        elif price_transformator == 'poly':
            return DPFPolyTransformator(*params)
        elif price_transformator == 'mlog':
            return DPFMLogTransformator(*params)
        elif price_transformator == '3sigma':
            return DPF3SigmaTransformator(*params)
        elif price_transformator == '3sigmaLog':
            return DPF3SigmaLogTransformator(*params)