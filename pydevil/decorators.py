from typing import Callable

from functools import wraps

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


def scatter(func: Callable) -> Callable:
    @wraps(func)
    def plot(
        data: pd.DataFrame,
        *args,
        **kwargs
    ) -> matplotlib.figure.Figure:
        x, y = func(data, *args, **kwargs)
        f = plt.figure()
        plt.scatter(x, y)
        return f
    return plot
