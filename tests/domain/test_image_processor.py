from predictor.domain.image_processor import ImageProcessor


def test_predictor_init():
    image_proccessor = ImageProcessor()
    assert isinstance(image_proccessor, ImageProcessor)
