from MLMCPy.model.Model import Model


class ModelForTesting(Model):

    def __init__(self, model_type='ones'):

        self._model_type = model_type

    def evaluate(self, sample):

        if self._model_type == 'ones':

            return 1.

        if self._model_type == 'repeat':

            return sample
