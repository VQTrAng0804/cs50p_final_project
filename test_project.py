import sys
import pytest
from project import check_command_line, import_image, reflection, grayscale, sepia, pencil_sketch, blur
from project import delete_back, negative ,vintage, fresh, chosoe, output, edges, bland
import cv2
import numpy as np
from unittest.mock import patch



def test_check_command_line(capsys):
    # Test too few command-line arguments
    with pytest.raises(SystemExit) as e:
        sys.argv = ["test_project.py"]
        check_command_line()
    assert str(e.value) == "Too few command-line arguments"

    # Test too many command-line arguments
    with pytest.raises(SystemExit) as a:
        sys.argv = ["test_project.py", "input.jpg", "output.jpg", "extra_argument"]
        check_command_line()
    assert str(a.value) == "Too many command-line arguments"

    # Test invalid input and ouput
    with pytest.raises(SystemExit) as b:
        sys.argv = ["test_project.py", "input.mp3", "output.mp4"]
        check_command_line()
    assert str(b.value) == "Invalid input and output"

    # Test invalid input
    with pytest.raises(SystemExit) as b:
        sys.argv = ["test_project.py", "input.mp3", "output.jpg"]
        check_command_line()
    assert str(b.value) == "Invalid input file"

    # Test invalid output
    with pytest.raises(SystemExit) as c:
        sys.argv = ["test_project.py", "input.jpeg", "output.mp3"]
        check_command_line()
    assert str(c.value) == "Invalid output file"


def test_import_image(tmp_path):
    # Create a temporary image file for testing
    test_image_path = tmp_path / "test.jpg"
    cv2.imwrite(str(test_image_path), (255 * np.random.rand(100, 100, 3)).astype(np.uint8))

    # Test reading a valid image file
    result_image = import_image(str(test_image_path))
    assert result_image is not None

    # Test reading an invalid image file
    with pytest.raises(SystemExit) as e:
        import_image("non_existent_image.jpg")
    assert str(e.value) == "Error: Unable to read the image file"

    # Test handling other exceptions
    with pytest.raises(SystemExit) as e:
        import_image(123)  # passing an invalid argument (not a file path)
    assert "Error: " in str(e.value)

def test_reflection(tmp_path):
    # Create a temporary image file for testing
    test_image_path = tmp_path / "test.jpg"
    cv2.imwrite(str(test_image_path), (255 * np.random.rand(100, 100, 3)).astype(np.uint8))

    # Read the test image
    original_image = cv2.imread(str(test_image_path))

    # Test reflection function
    reflected_image = reflection(original_image)

    # Ensure the reflected image is not None
    assert reflected_image is not None


def test_grayscale(tmp_path):

    # Create a temporary image file for testing
    test_image_path = tmp_path / "test.jpg"
    cv2.imwrite(str(test_image_path), (255 * np.random.rand(100, 100, 3)).astype(np.uint8))

    # Read the test image
    original_image = cv2.imread(str(test_image_path))

    # Test grayscale function
    grayscale_image = grayscale(original_image)

    # Ensure the grayscale image is not None
    assert grayscale_image is not None


def test_sepia(tmp_path):

    # Create a temporary image file for testing
    test_image_path = tmp_path / "test.jpg"
    cv2.imwrite(str(test_image_path), (255 * np.random.rand(100, 100, 3)).astype(np.uint8))

    # Read the test image
    original_image = cv2.imread(str(test_image_path))

    # Test sepia function
    sepia_image = sepia(original_image)

    # Ensure the sepia image is not None
    assert sepia_image is not None


def test_pencil_sketch(monkeypatch, tmp_path):

    # Create a temporary image file for testing
    test_image_path = tmp_path / "test.jpg"
    cv2.imwrite(str(test_image_path), (255 * np.random.rand(100, 100, 3)).astype(np.uint8))

    # Read the test image
    original_image = cv2.imread(str(test_image_path))

    # Set the user input for the count value
    monkeypatch.setattr('builtins.input', lambda _: '111')

    # Test pencil_sketch function
    sketch_image = pencil_sketch(original_image)

    # Ensure the sketch image is not None
    assert sketch_image is not None


def test_blur(monkeypatch, tmp_path):
    # Create a temporary image file for testing
    test_image_path = tmp_path / "test.jpg"
    cv2.imwrite(str(test_image_path), (255 * np.random.rand(100, 100, 3)).astype(np.uint8))

    # Read the test image
    original_image = cv2.imread(str(test_image_path))

    # Set the user input for the blur level
    monkeypatch.setattr('builtins.input', lambda _: '5')

    # Test blur function
    blurred_image = blur(original_image)

    # Ensure the blurred image is not None
    assert blurred_image is not None


def test_delete_back(monkeypatch, tmp_path):
    # Create a temporary image file for testing
    test_image_path = tmp_path / "test.jpg"
    cv2.imwrite(str(test_image_path), (255 * np.random.rand(100, 100, 3)).astype(np.uint8))

    # Read the test image
    original_image = cv2.imread(str(test_image_path))

    # Mock the remove function to avoid actual API calls during testing
    with patch('rembg.remove') as mock_remove:
        # Set the mock return value
        mock_remove.return_value = original_image

        # Test delete_back function
        result_image = delete_back(original_image)

        # Ensure the result image is not None
        assert result_image is not None


def test_negative(tmp_path):
    # Create a temporary image file for testing
    test_image_path = tmp_path / "test.jpg"
    cv2.imwrite(str(test_image_path), (255 * np.random.rand(100, 100, 3)).astype(np.uint8))

    # Read the test image
    original_image = cv2.imread(str(test_image_path))

    # Test negative function
    negative_image = negative(original_image)

    # Ensure the negative image is not None
    assert negative_image is not None


def test_vintage(tmp_path):
    # Create a temporary image file for testing
    test_image_path = tmp_path / "test.jpg"
    cv2.imwrite(str(test_image_path), (255 * np.random.rand(100, 100, 3)).astype(np.uint8))

    # Read the test image
    original_image = cv2.imread(str(test_image_path))

    # Test vintage function
    vintage_result = vintage(original_image)

    # Ensure the vintage result is not None
    assert vintage_result is not None



def test_fresh(tmp_path):
    # Create a temporary image file for testing
    test_image_path = tmp_path / "test.jpg"
    cv2.imwrite(str(test_image_path), (255 * np.random.rand(100, 100, 3)).astype(np.uint8))

    # Read the test image
    original_image = cv2.imread(str(test_image_path))

    # Test fresh function
    fresh_result = fresh(original_image)

    # Ensure the fresh result is not None
    assert fresh_result is not None



def test_edges(tmp_path):
    # Create a temporary image file for testing
    test_image_path = tmp_path / "test.jpg"
    cv2.imwrite(str(test_image_path), (255 * np.random.rand(100, 100, 3)).astype(np.uint8))

    # Read the test image
    original_image = cv2.imread(str(test_image_path))

    # Test edges function
    edges_result = edges(original_image)

    # Ensure the edges result is not None
    assert edges_result is not None


def test_bland(tmp_path):
    # Create a temporary image file for testing
    test_image_path = tmp_path / "test.jpg"
    cv2.imwrite(str(test_image_path), (255 * np.random.rand(100, 100, 3)).astype(np.uint8))

    # Read the test image
    original_image = cv2.imread(str(test_image_path))

    # Test bland function
    bland_result = bland(original_image)

    # Ensure the bland result is not None
    assert bland_result is not None


def test_chosoe(tmp_path):
    # Create a temporary image file for testing
    test_image_path = tmp_path / "mage.jpg"
    cv2.imwrite(str(test_image_path), (255 * np.random.rand(100, 100, 3)).astype(np.uint8))

    # Read the test image
    original_image = cv2.imread(str(test_image_path))

    # Set the user input for the chosen effect
    with patch('builtins.input', side_effect=['grayscale']):
        # Test chosoe function
        result_image = chosoe(original_image)

    # Ensure the result image is not None
    assert result_image is not None

    # Check if the result image has the correct dimensions
    assert result_image.shape == original_image.shape[:-1]

    # Check if the result image is not the same as the original image
    assert not np.array_equal(result_image, original_image)


def test_output(tmp_path):
    # Create a temporary image file for testing
    test_image_path = tmp_path / "test.jpg"
    cv2.imwrite(str(test_image_path), (255 * np.random.rand(100, 100, 3)).astype(np.uint8))

    # Read the test image
    original_image = cv2.imread(str(test_image_path))

    # Set the user input for the output choice
    with patch('builtins.input', side_effect=['1']):
        # Test output function
        output(original_image, original_image, str(tmp_path / "output_image.jpg"))

    with patch('builtins.input', side_effect=['2']):
        # Test output function
        output(original_image, original_image, str(tmp_path / "output_image.jpg"))
        