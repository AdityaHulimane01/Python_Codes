import os

Images = os.listdir("Images")

count = 1

for i in Images:
    print(i)
    if i.endswith(".png"):
        os.rename(f"Images/{i}", f"Images/{count}.png")
        count += 1
