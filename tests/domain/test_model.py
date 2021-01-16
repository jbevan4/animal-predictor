from predictor.domain.model import Model


def test_model_init():
    processed_images = ["./image.png", "./image.jpeg"]
    model = Model(processed_images)
    assert isinstance(model, Model)
    assert model.processed_images == processed_images


# def test_model_can_train():
#     model = Model()
