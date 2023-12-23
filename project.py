import cv2
import numpy
import tensorflow
import tensorflow_hub
import sys
import os


def main():
    # Create image variable 
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check valid command-line arguments
    check_command_line()

    # Check valid input file
    original_image = import_image(input_file)

    # Convert image to reflection
    reflection_image = (original_image)

    cv2.imwrite(output_file, reflection_image)


def check_command_line():

    valid_file = [".jpg", ".jpeg", ".png"]

    try:
        # Check lenght of argv
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line argument")
        
        # Check valid input and output 
        else:
            input_file = os.path.splitext(sys.argv[1])[1].lower()
            output_file = os.path.splitext(sys.argv[2])[1].lower()

            if input_file and output_file not in valid_file:
                sys.exit("Invalid input and output")
            elif input_file not in valid_file:
                sys.exit("Invalid input file")
            elif output_file not in valid_file:
                sys.exit("Invalid output file")
            elif input_file != output_file:
                sys.exit("Input file and output file have diffirent extensions")
    except IndexError:
        sys.exit("Out of range")


def import_image(image):

    # Check input image is exist or not
    try:
        image = cv2.imread(image)

        if image is None:
            sys.exit("Error: Unable to read the image file")
        
        # Return the image if image is not None
        else:
            return image
    
    except Exception as e:
        sys.exit(f"Error: {e}")


def reflection(image):

    # Return relection image
    return  cv2.flip(image,1) # 1 denotes horizontal flip


def grayscale(image):

    # Return grayscale image
    return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)  

def sepia(image):

    # Define matrix of RGB 
    matrix = numpy.array([[0.393, 0.769, 0.189],
	[0.349, 0.686, 0.168],
	[0.272, 0.534, 0.131]])

    # Return sepia image with matrix
    return cv2.transform(image, matrix)


if __name__ == "__main__":
    main()
