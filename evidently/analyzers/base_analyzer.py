#!/usr/bin/env python
# coding: utf-8
import abc
from typing import Optional

import pandas as pd

from evidently.options import OptionsProvider
from evidently.pipeline.column_mapping import ColumnMapping


class Analyzer:
    @abc.abstractmethod
    def calculate(self,
                  reference_data: pd.DataFrame,
                  current_data: Optional[pd.DataFrame],
                  column_mapping: ColumnMapping) -> object:
        raise NotImplementedError()

    options_provider: OptionsProvider
