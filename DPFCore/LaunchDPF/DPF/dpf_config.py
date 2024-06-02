

class DPFBaseConfig:
    DATE = 'Date'
    HOUR = 'Hour'
    PRICE = 'Price'
    DAY = 'Day'
    COUNTRY = 'Country'
    DOW = 'Day of week'


class DPFDataPreparatorConfig(DPFBaseConfig):
    pass


class DPFMissingValuesFillerConfig(DPFBaseConfig):
    pass


class DPFOutlierDetectorConfig(DPFBaseConfig):
    MEDIAN_PRICE = 'Median Price'
    DEMEDIANED_PRICE = 'Demedianed Price'
    BT_PLUS = 'Bt+'
    BT_MINUS = 'Bt-'


class DPFTransformatorConfig(DPFBaseConfig):
    MEAN = 'Mean'
    STD = 'Std'
    MOD_PRICE = 'Mod Price'
    TRANS_PRICE = 'Trans Price'
    UNMOD_PRICE = 'Unmod Price'
    FORECAST_PRICE = 'Forecast Price'
    INV_TRANS_PRICE = 'Inv Trans Price'


class DPFSeasonalProcessorConfig(DPFTransformatorConfig, DPFBaseConfig):
    WEEKLY_SEAS = 'Weekly Seas'
    ANNUAL_SEAS = 'Annual Seas'
    SEAS_PRICE = 'Seas Price'
    DESEAS_PRICE = 'Deseas Price'
    UNPRO_PRICE = 'Unpro Forecast Price'


class DPFProcessedPlotterConfig(DPFSeasonalProcessorConfig, DPFTransformatorConfig, DPFBaseConfig):
    pass


class DPFModellerConfig(DPFTransformatorConfig, DPFBaseConfig):
    pass


class DPFLinearModelVariablesPreparatorConfig(DPFBaseConfig):
    COUNTRY_HOLIDAY_DICT = {'DE-LU': 'DE', 'FR': 'FR'}


class DPFBacktestingConfig(DPFTransformatorConfig, DPFBaseConfig):
    pass


class DPFPredictedResultsConfig(DPFSeasonalProcessorConfig, DPFBaseConfig):
    FORECAST_PRICE = 'Forecast Price'


class DPFMetricComputerConfig:
    metric_dict = {'MAPE': 'DPFMAPEComputer', 'MAE': 'DPFMAEComputer', 'RMSE': 'DPFRMSEComputer'}