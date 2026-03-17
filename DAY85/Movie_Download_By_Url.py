import argparse
import requests
import os
import time

# Create command line parser
parser = argparse.ArgumentParser(description="Movie/File downloader with resume support")

# URL argument (required)
parser.add_argument("url", help="Direct URL of the movie/file")

# Optional filename
parser.add_argument("-n", "--name", help="Name of the downloaded file", default="downloaded_movie.mp4")

# Optional path argument (where to save the file)
parser.add_argument("-p", "--path", help="Folder where file will be saved", default=".")

# Parse arguments
args = parser.parse_args()

url = args.url
filename = args.name
path = args.path

# Create folder if it does not exist
os.makedirs(path, exist_ok=True)

# Create full file path
save_path = os.path.join(path, filename)

# Check if file already exists (for resume support)
file_size = 0
if os.path.exists(save_path):
    file_size = os.path.getsize(save_path)

headers = {"Range": f"bytes={file_size}-"}

# Request file
response = requests.get(url, headers=headers, stream=True)

total_size = int(response.headers.get("content-length", 0)) + file_size

start_time = time.time()

# Open file in append mode (important for resume)
with open(save_path, "ab") as f:

    downloaded = file_size

    for chunk in response.iter_content(chunk_size=1024 * 1024):
        if chunk:
            f.write(chunk)
            downloaded += len(chunk)

            # Calculate progress
            percent = (downloaded / total_size) * 100 if total_size > 0 else 0

            # Calculate speed
            elapsed = time.time() - start_time
            speed = downloaded / elapsed / 1024 / 1024 if elapsed > 0 else 0

            print(f"\rProgress: {percent:.2f}% | Speed: {speed:.2f} MB/s", end="")

print("\nDownload completed!")


#  python Movie_Download_By_Url.py https://samplelib.com/lib/preview/mp4/sample-5s.mp4 -n film.mp4 -p D:\Movies

# just run above command in terminal to download the movies