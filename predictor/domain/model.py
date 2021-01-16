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
            raise ValueError(
                "Your model is not compiled. Please run model.compile() before attempting to fit the model.")
        self.fitted = True
        return self.fitted
