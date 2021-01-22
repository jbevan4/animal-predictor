from predictor.domain.image_loader import ImageLoader
from tensorflow.keras.utils import get_file
import pathlib

from unittest.mock import MagicMock, patch


def test_image_loader_init():
    url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
    image_loader = ImageLoader(url, get_file)
    assert isinstance(image_loader, ImageLoader)


# TODO: get this test working properly
@patch('six.moves.urllib.request')
def test_can_load_images_from_a_url(mock_urlopen):
    url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
    mocked_images_path = "path_to_directory_of_images"
    image_loader = ImageLoader(url, get_file)
    directory_of_images = image_loader.load('pets')
    assert directory_of_images == mocked_images_path
