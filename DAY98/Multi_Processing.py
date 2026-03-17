import multiprocessing
import requests

# Function to download image
def download(url , name):
    print(f"Started process {name}")

    response = requests.get(url)   # fetch image from internet

    # Save image to file
    open(f"Files/file{name}.jpg" , "wb").write(response.content)

    print(f"Finished process {name}")


# Windows safety entry point
if __name__ == "__main__":

    url = "https://picsum.photos/200/300"   # correct URL
    pros = []   # list to store processes

    # Step 1: start all processes 🚀
    for i in range(5):
        p = multiprocessing.Process(target=download , args=[url , i])
        p.start()
        pros.append(p)

    # Step 2: wait for all processes ⏳
    for p in pros:
        p.join()