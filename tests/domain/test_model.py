from predictor.domain.model import Model

from pytest import fixture
from unittest.mock import MagicMock


@fixture
def model():
    processed_images = ["./image.png", "./image.jpg", "./image.jpeg"]
    model = Model(processed_images)
    return model


def test_model_init(model):
    assert isinstance(model, Model)


def test_model_can_be_compiled(model):
    model.compile()
    assert model.compiled == True


def test_model_can_be_trained_after_being_compiled(model):
    model.compile()
    model.train()
    assert model.trained == True
