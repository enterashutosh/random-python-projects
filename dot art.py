'''
this program converts an image into an ASCII version with only white space and dot characters used. it is like black and white, but different.
have fun with it.
'''


from PIL import Image
import numpy as np
import random
hexdigits = '0123456789abcdef'



def dot_art(image_path, output_name):
    # load the image and convert it to grayscale
    if image_path[0] == '"':
        image = Image.open(image_path[1:-1]).convert("L")
    else:
        image = Image.open(image_path).convert("L")

    # resize the image
    original_width, original_height = image.size
    resized_image = image.resize((230,original_height//(original_width//230)))


    # convert the image to a NumPy array
    image_array = np.array(resized_image)

    # define a threshold for binarization (adjust as needed)
    threshold = 128

    # create a binary matrix (1 for white, 0 for black)
    binary_matrix = (image_array > threshold).astype(int)

    # define characters for white and black pixels
    white_space = " "

    # convert the binary matrix to a text representation
    text_representation = "\n".join(["".join([random.choice(hexdigits) if pixel == 1 else white_space for pixel in row]) for row in binary_matrix])



    # save the text representation to a text file
    with open(output_name, "w") as text_file:
        text_file.write(text_representation)


while True:
    if __name__ == "__main__":
        p = input("paste image path ('q' to quit): ")
        if p == "q":
            break
        else:
            q = input("choose an output file name: ") + ".txt"
            dot_art(p,q)
            print("dot file succesfully created!\n")