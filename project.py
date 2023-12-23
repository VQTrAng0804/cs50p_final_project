import cv2
import numpy
import sys
import os
from rembg import remove
from pyfiglet import Figlet


# Transform the image with artistic effects
def main():
    
    # Check valid command-line arguments
    check_command_line()

    # Create image variable 
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check valid input file
    original_image = import_image(input_file)

    # Convert image to new mode
    image = chosoe(original_image)

    # Save or save and show
    output(original_image, image, output_file)


def check_command_line():

    valid_file = [".jpg", ".jpeg", ".png"]

    # Check lenght of argv
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
        
    # Check valid input and output 
    else:
        input_file = os.path.splitext(sys.argv[1])[1].lower()
        output_file = os.path.splitext(sys.argv[2])[1].lower()

    if input_file not in valid_file and output_file not in valid_file:
        sys.exit("Invalid input and output")
    elif input_file not in valid_file:
        sys.exit("Invalid input file")
    elif output_file not in valid_file:
        sys.exit("Invalid output file")
    elif input_file != output_file:
        sys.exit("Input file and output file have diffirent extensions")


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

    # Convert the input image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Normalize the grayscale image to a range of [0, 1]
    normalized_gray = numpy.array(gray, numpy.float32) / 255

    # Create a sepia filter matrix with predefined intensity values
    sepia = numpy.ones(image.shape)
    sepia[:, :, 0] *= 153  # B
    sepia[:, :, 1] *= 204  # G
    sepia[:, :, 2] *= 255  # R

    # Multiply the sepia filter with the normalized grayscale image
    sepia = numpy.multiply(sepia, normalized_gray[:, :, numpy.newaxis])

    # Convert the resulting sepia image back to uint8 format
    sepia = numpy.array(sepia, numpy.uint8)

    # Return sepia image
    return sepia


def pencil_sketch(image):

    # Get input blur from the user
    while True:
        try:
            count = int(input("Get the blur of image (use integer), recommend 265: "))

            # Check valid condition
            if isinstance(count, int) and count % 2 == 1 and count > 0:
              break  

            #  Check valid integer
            print("Count divide 2 remainded 1, and Count > 0 ")

        # Check invalid value
        except ValueError:
            print("The input have to be an integer")
    
    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    invert_grayscale = cv2.bitwise_not(grayscale_image)

    # Apply Gaussian blur to the inverted image 
    blur = cv2.GaussianBlur(invert_grayscale, (count,count), 0)

    # Invert the blurred image 
    invert_blur = cv2.bitwise_not(blur)

    # Return the blending the original color image with the inverted and blurred image 
    return cv2.divide(grayscale_image, invert_blur, scale=256.0)


def blur(image):
    # Get input blur from the user
    while True:
        try:
            blur_level = int(input("Get the blur of image (use integer): "))

            # Check valid condition
            if isinstance(blur_level, int) and blur_level % 2 == 1 and blur_level > 0:
              break  

            #  Check valid integer
            print("Count divide 2 remainded 1, and Count > 0 ")

        # Check invalid value
        except ValueError:
            print("The input have to be an integer")

    # Return blur image
    return cv2.GaussianBlur(image, (blur_level,blur_level), 0)


def delete_back(image):
    
    # Return remove background
    return remove(image)


def negative(image):

    # Return negative image
    return 255 - image


def vintage(image):

    # Define the vintage filter matrix
    vintage_filter = numpy.array([[0.393, 0.769, 0.189],
                             [0.349, 0.686, 0.168],
                             [0.272, 0.534, 0.131]])

    # Apply the vintage filter to the image
    sepia_image = cv2.transform(image, vintage_filter)

    # Clip values to be in the valid range [0, 255]
    vintage_image = numpy.clip(sepia_image, 0, 255).astype(numpy.uint8)

    # Return vintage image
    return vintage_image


def fresh(image):

    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Increase the saturation for a more vibrant look
    hsv_image[:, :, 1] = numpy.clip(hsv_image[:, :, 1] * 1.5, 0, 255)

    # Increase the value (brightness) to brighten the colors
    hsv_image[:, :, 2] = numpy.clip(hsv_image[:, :, 2] * 1.2, 0, 255)

    # Convert the image back to BGR color space
    fresh_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

    # Return fresh image
    return fresh_image


def edges(image):
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise and improve edge detection
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Apply Canny edge detection
    edges_image = cv2.Canny(blurred_image, 50, 150)

    # Convert edges image to BGR color space
    edges_image_bgr = cv2.cvtColor(edges_image, cv2.COLOR_GRAY2BGR)

    # Combine the edges with the original image
    edges_effect_image = cv2.addWeighted(image, 0.7, edges_image_bgr, 0.3, 0)
    return edges_effect_image


def bland(image):

    # Return bland image
    return  cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def chosoe(image):

    # Greeting
    figlet = Figlet()
    figlet.getFonts()
    figlet.setFont()
    print(figlet.renderText("Welcome!"))
    print("May your days be filled with joy 😊, laughter 😄, and moments of genuine happiness 😇.")
    print("This is a tool to convert an image to some kind of image which is attracted today!")
    print("I hope you like this tool 💌 ✋ 💗 ")
    print("")
    print("This is 3 steps you will do: ")
    print("- First, choose the effect of image.")
    print("- Second, choose the blur count (This step is for pencil sketch, blur)")
    print("- Finally, choose save and show image or just save the image")
    print("")
    print("Have fun🥰🤗💞👋")
    print("")
    print("")
    print("These are these image effects:")
    print("- Reflection")
    print("- Grayscale")
    print("- Sepia")
    print("- Pencil sketch")
    print("- Blur")
    print("- Delete background")
    print("- Negative")
    print("- Vintage")
    print("- Fresh")
    print("- Edges")
    print("- Bland")
    print("Note📝: Deleting background is ideal for objects but not landscapes.")

    # Get input from user to choose the image
    while True:
        choose_effect = input("Choose your image effect you want to change: ").lower()

        # Return the image effect that the user chooseed
        # Relection
        if choose_effect == 'reflection':
            return reflection(image)
        
        # Grayscale
        elif choose_effect == 'grayscale':
            return grayscale(image)
        
        # Sepia
        elif choose_effect == 'sepia':
            return sepia(image)
        
        # Pencil sketch
        elif choose_effect == 'pencil sketch':
            return pencil_sketch(image)
        
        # Blur
        elif choose_effect == 'blur':
            return blur(image) 
        
        # Delete background
        elif choose_effect == 'delete background':
            return delete_back(image)

        # Negative
        elif choose_effect == 'negative':
            return negative(image)

        # Vintage
        elif choose_effect == 'vintage':
            return vintage(image)

        # Fresh
        elif choose_effect == 'fresh':
            return fresh(image)
        # Edges
        elif choose_effect == 'edges':
            return edges(image)
        
        # Colorful
        elif choose_effect == 'bland':
            return bland(image)
        
        # Reprompt the user to choose the right mode
        print(("Please choose these image effects below 🥺:"))
        print("Reflection, grayscale, sepia, pencil sketch, blur, delete background, negative, vintage, fresh, edges, and bland.")
        print("")


def output(image,convert_image,name):

    # Instruction
    print("")
    print("")
    print("Do you want to show save and show the image or just save? ")
    print("Please type '1' if you want to save.")
    print("Please type '2' if you want to save and show.")

    # Chosing
    while True:
        choose = input("Here is your choose: ")
        if choose == '1':
            cv2.imwrite(name, convert_image)
            print("")
            print("Image saved successfully!")
            break
        elif choose == '2':
            cv2.imwrite(name,convert_image)
            cv2.imshow("Original Image", image)
            cv2.imshow("Effect Image", convert_image)
            cv2.waitKey(0)  # Wait for any key press
            cv2.destroyAllWindows()
            print("")
            print("Image saved and displayed successfully!")
            break

        # Promp the user to choose the right and choose again
        print("Please just type 1 or 2!")



if __name__ == "__main__":
    main()
