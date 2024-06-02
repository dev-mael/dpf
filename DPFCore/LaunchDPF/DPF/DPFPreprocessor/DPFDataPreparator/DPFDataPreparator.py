from datetime import datetime

from DPFCore.LaunchDPF.DPF.dpf_config import DPFDataPreparatorConfig


class DPFDataPreparator:
    def __init__(self, dayahead_df):
        self._prepared_dayahead_df = dayahead_df.copy()
        self._DATE = DPFDataPreparatorConfig.DATE
        self._HOUR = DPFDataPreparatorConfig.HOUR
        self._DAY = DPFDataPreparatorConfig.DAY
        self._DOW = DPFDataPreparatorConfig.DOW

    def prepare(self):
        if self._HOUR not in self._prepared_dayahead_df.columns:
            self._prepared_dayahead_df[self._HOUR] = self._prepared_dayahead_df.apply(
                lambda row: row[self._DATE].hour + 1, axis='columns')
        self._prepared_dayahead_df[self._DAY] = self._prepared_dayahead_df.apply(
            lambda row: datetime.date(row[self._DATE]), axis='columns')
        self._prepared_dayahead_df[self._DOW] = self._prepared_dayahead_df.apply(
            lambda row: row[self._DATE].dayofweek, axis='columns')

        return self._prepared_dayahead_df
