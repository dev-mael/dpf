from sklearn import linear_model


class LinearModelModelDefiner:
    def __init__(self):
        pass

    def define(self):
        self._model = linear_model.LinearRegression()

        return self._model
