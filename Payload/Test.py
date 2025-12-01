import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def load_and_combine_bands(red_file, green_file, blue_file):
    # Loads the raw R, G, and B band data from CSV files, ensures they are of
    # the same dimensions, and combines them into a single RGB image.

    green = np.loadtxt(green_file, delimiter=",", skiprows=1)[1:]   #read file, and then skip the first row and column
    blue = np.loadtxt(blue_file, delimiter=",", skiprows=1)[1:]
    red = np.loadtxt(red_file, delimiter=",", skiprows=1)[1:]

    if green.shape == blue.shape and green.shape == red.shape:      #check if the file shapes are the same size
        combined = np.dstack((red, green, blue))                    #if they are stack them
        combined = combined.astype(np.uint8)                        #ensure proper type
        return combined
    else:
        print("CSV files must have the same shape")
        return None

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
        plt.xlim(0, radiance_values.shape[1])                               #x axis limited to size of shape
        plt.ylim(0, radiance_values.shape[0])                               #y axis limited to size of shape
        radiance_values = np.flipud(radiance_values)                              #flip values as it is read upside down
        plt.imshow(radiance_values)                                               #plot the values as an image
        plt.show()


if __name__ == "__main__":
    main()