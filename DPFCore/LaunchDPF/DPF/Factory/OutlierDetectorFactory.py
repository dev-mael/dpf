from DPFCore.LaunchDPF.DPF.DPFPreprocessor.DPFOutlierDetector.DPFRunningMedianDetector import DPFRunningMedianDetector


class OutlierDetectorFactory:

    @staticmethod
    def get_detector(outlier_detector, *params):
        if outlier_detector == 'running median':
            return DPFRunningMedianDetector(*params)