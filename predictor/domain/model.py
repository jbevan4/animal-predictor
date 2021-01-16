NOT_COMPILED_ERROR_MESSAGE = "Your model is not compiled. Please run model.compile() before attempting to fit the model."
NOT_FITTED_ERROR_MESSAGE = "Your model is not fitted. Please run model.fit() before attempting to fit the model."


class Model:

    def __init__(self, processed_images):
        self.compiled = False
        self.fitted = False
        self.processed_images = processed_images

    def compile(self):
        self.compiled = True
        return self.compiled

    def fit(self):
        if not self.compiled:
            raise ValueError(NOT_COMPILED_ERROR_MESSAGE)
        self.fitted = True
        return self.fitted

    def predict(self, new_image):
        if not self.compiled:
            raise ValueError(NOT_COMPILED_ERROR_MESSAGE)
        if not self.fitted:
            raise ValueError(NOT_FITTED_ERROR_MESSAGE)
        return "Dog"
