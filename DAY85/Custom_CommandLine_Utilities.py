import argparse
import requests

# Create the parser object
parser = argparse.ArgumentParser(description="Download an image from a URL")

# Argument 1 → image URL (required)
parser.add_argument("url", help="URL of the image you want to download")

# Argument 2 → image name (optional)
# If user does not give it, default name will be used
parser.add_argument("-n", "--name", help="Name of the image file", default="downloaded_image.jpg")

# Parse the arguments given in terminal
args = parser.parse_args()

# Extract values
image_url = args.url
image_name = args.name

# Send request to the URL
response = requests.get(image_url)

# Check if download was successful
if response.status_code == 200:
    
    # Open a file in write-binary mode
    with open(image_name, "wb") as file:
        file.write(response.content)   # write image data into file

    print(f"Image downloaded successfully as '{image_name}'")

else:
    print("Failed to download image")


# python Custom_CommandLine_Utilities.py https://dlib.indiana.edu/images/IUScholarWorks.jpg 

# run above command in terminal 