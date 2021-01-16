from predictor.domain.model import Model

from unittest.mock import MagicMock

from pytest import fixture
from pytest import raises


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


def test_model_can_be_fitted_after_being_compiled(model):
    model.compile()
    model.fit()
    assert model.fitted == True


def test_model_errors_when_fitted_without_compiling(model):
    with raises(ValueError) as not_compiled_error:
        model.fit()
    assert "Your model is not compiled. Please run model.compile() before attempting to fit the model." == str(
        not_compiled_error.value)


def test_model_can_predict_a_new_image(model):
    model.compile()
    model.fit()
    classification = model.predict("new_image")
    assert classification == "Dog"


def test_model_will_error_if_attempting_to_predict_without_compiling(model):
    with raises(ValueError) as not_compiled_error:
        model.predict("new_image")
    assert "Your model is not compiled. Please run model.compile() before attempting to fit the model." == str(
        not_compiled_error.value)
