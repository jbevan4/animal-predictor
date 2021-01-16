class Model:

    def __init__(self, processed_images):
        self.compiled = False
        self.trained = False
        self.processed_images = processed_images

    def compile(self):
        self.compiled = True
        return self.compiled

    def train(self):
        if not self.compiled:
            raise ValueError(
                "Your model is not compiled. Please run model.compile() before attempting to train the model.")
        self.trained = True
        return self.trained
