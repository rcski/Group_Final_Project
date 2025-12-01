# Note: Students might need to install matplotlib if they don't have it
# pip install matplotlib
import matplotlib.pyplot as plt
import numpy as np



def load_and_combine_bands(red_file, green_file, blue_file):
    
    #Loads the raw R, G, and B band data from CSV files, ensures they are of
    #the same dimensions, and combines them into a single RGB image.

    green = np.loadtxt(green_file, delimiter=",") # read file, and then skip the first row and column headers
    blue = np.loadtxt(blue_file, delimiter=",")
    red = np.loadtxt(red_file, delimiter=",")

    if green.shape == blue.shape and green.shape == red.shape:  # check if the file shapes are the same size
        combined = np.dstack((red, green, blue))  # if they are stack them
          # make type for plt.imshow
        return combined
    else:
        print("CSV files must have the same shape")
        return None



def convert_radiance_to_reflectance(rgb_image, k=0.8, b=0.1):
    #Converts radiance values to reflectance.
    rgb_image = rgb_image.astype(np.float64)    #convert to float to be able to create a ratio
    reflectance_array = rgb_image * k + b #convert to ratio and then multiply by scalar and add additive factor
    return reflectance_array


def rescale_to_8bit(reflectance_image):
    
    #Converts the floating point reflectance values to 8-bit integers (0-255).

    rescale = reflectance_image * 255           #scale back to 0-255
    rescale_int = rescale.astype(np.uint8)      #convert to integers
    return rescale_int

def save_image(image, filename):

   # Saves the image to a file.

    plt.imsave(filename, image)
    pass

def main():

    #Main function to process the remote sensing data.

    # File paths for the CSV data
    red_file = r"C:\Users\zachm\SS1011 Final Project\red.csv"
    green_file = r"C:\Users\zachm\SS1011 Final Project\green.csv"
    blue_file = r"C:\Users\zachm\SS1011 Final Project\blue.csv"

    # Task 1: Load and combine bands
    radiance_values = load_and_combine_bands(red_file, green_file, blue_file)
    if radiance_values is not None:
        print("Successfully loaded and combined image bands.")
        # Optional: visualize the raw radiance image
        plt.title("Radiance Image")
        plt.xlim(0, radiance_values.shape[1])  # x axis limited to size of shape
        plt.ylim(0, radiance_values.shape[0])  # y axis limited to size of shape
        radiance_values = np.flipud(radiance_values)  # flip values as it is read upside down
        plt.imshow(radiance_values)  # plot the values as an image
        plt.show()
    else:
        print("Failed to load bands.")

    # "Check Plus" Tasks

    # Task 2: Convert to reflectance

    reflectance_image = convert_radiance_to_reflectance(radiance_values)
    if reflectance_image is not None:
        print("Successfully converted to reflectance.")
    else:
        print("Failed to convert to reflectance.")

    #Task 3: Rescale to 8-bit

    final_image = rescale_to_8bit(reflectance_image)
    if final_image is not None:
        print("Successfully rescaled to 8-bit.")
    else:
        print("Failed to rescale to 8-bit to reflectance.")

    # Task 4: Visualize and save the final image

    if final_image is not None:
        plt.title("Final Processed Image")
        plt.xlim(0, final_image.shape[1])  # x axis limited to size of shape
        plt.ylim(0, final_image.shape[0])  # y axis limited to size of shape
        plt.axis('off')                          # remove unnecessary axis
        final_image = np.flipud(final_image)     # flip values as it is read upside down
        plt.imshow(final_image)
        save_image(final_image, r'C:\Users\zachm\SS1011 Final Project\final_image.png')
        print("Saved final image to final_image.png")

if __name__ == "__main__":
    main()
