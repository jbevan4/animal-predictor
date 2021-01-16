class Model:

    def __init__(self, processed_images):
        self.compiled = False
        self.trained = False
        self.processed_images = processed_images

    def compile(self):
        self.compiled = True
        return self.compiled

    def train(self):
        self.trained = True
        return self.trained
