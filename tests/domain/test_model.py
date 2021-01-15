from predictor.domain.model import Model


def test_model_init():
    model = Model()
    assert isinstance(model, Model)
