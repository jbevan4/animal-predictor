class Model:

    def __init__(self, processed_images):
        self.compiled = False
        self.processed_images = processed_images

    def compile(self):
        self.compiled = True
        return self.compiled
