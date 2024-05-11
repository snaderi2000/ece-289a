import cv2
import numpy as np
from tensorflow.keras.datasets import mnist

def save_mnist_row(digit=5, num_images=1, output_file='mnist_row.jpg'):
    # Load MNIST dataset
    (train_images, train_labels), (_, _) = mnist.load_data()
    
    # Filter images for the specified digit
    images_of_digit = train_images[train_labels == digit]
    
    # Select the first 'num_images' instances
    if images_of_digit.shape[0] < num_images:
        raise ValueError("Not enough images of the specified digit in the dataset")
    selected_images = images_of_digit[:num_images]
    
    # Concatenate images horizontally
    concatenated_image = np.hstack(selected_images)
    
    # Resize the concatenated image to have a uniform height of 50 pixels
    target_height = 50
    scale_factor = target_height / concatenated_image.shape[0]
    target_width = int(concatenated_image.shape[1] * scale_factor)
    resized_image = cv2.resize(concatenated_image, (target_width, target_height), interpolation=cv2.INTER_LINEAR)
    
    # Convert the image from grayscale to a format suitable for saving in JPEG format
    resized_image = cv2.cvtColor(resized_image, cv2.COLOR_GRAY2BGR)
    
    # Save the resized image as a JPEG file
    cv2.imwrite(output_file, resized_image)
    
    print(f"Image saved as {output_file}, Dimensions: {target_width}x{target_height}")

if __name__ == "__main__":
    # Specify the digit, number of images, and output filename here
    save_mnist_row(digit=5, num_images=1, output_file='one_five.jpg')

