from predictor.domain.model import Model
from unittest.mock import MagicMock


def test_model_init():
    processed_images = ["./image.png", "./image.jpg", "./image.jpeg"]
    model = Model(processed_images)
    assert isinstance(model, Model)
    assert model.processed_images == processed_images


def test_model_can_be_compiled():
    processed_images = ["./image.png", "./image.jpg", "./image.jpeg"]
    model = Model(processed_images)
    model.compile()
    assert model.compiled == True
