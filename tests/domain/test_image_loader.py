from predictor.domain.image_loader import ImageLoader


def test_image_loader_init():
    image_loader = ImageLoader()
    assert isinstance(image_loader, ImageLoader)
