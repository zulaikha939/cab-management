import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import wiener

# Set the image path (make sure "image.jpg" is in the same folder as this script)
image_path = "image.jpg"

# Load the image in grayscale mode
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Error: Could not read the image. Check the path!")
    exit()

# Apply the Wiener filter.
# The scipy.signal.wiener function returns a floating-point array.
filtered_image = wiener(image)

# Convert the filtered image to uint8 for display
filtered_image_uint8 = np.clip(filtered_image, 0, 255).astype(np.uint8)

# Display the original and Wiener filtered images side by side using matplotlib
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(filtered_image_uint8, cmap='gray')
plt.title("Wiener Filtered Image")
plt.axis("off")

plt.show()






    










