import requests

# -------------------------------
# 1. Basic GET Request
# -------------------------------
print("\n--- Basic GET Request ---")
url = "https://httpbin.org/get"
response = requests.get(url)

print("Status Code:", response.status_code)
print("Text:", response.text[:100])   # print first 100 characters


# -------------------------------
# 2. GET Request with Parameters
# -------------------------------
print("\n--- GET Request with Parameters ---")
params = {
    "username": "john123",
    "id": 45
}

response = requests.get("https://httpbin.org/get", params=params)

print("Final URL:", response.url)
print("Response:", response.text[:100])


# -------------------------------
# 3. POST Request
# -------------------------------
print("\n--- POST Request ---")
data = {
    "name": "John",
    "password": "12345"
}

response = requests.post("https://httpbin.org/post", data=data)

print("Status Code:", response.status_code)
print("Response:", response.text[:100])


# -------------------------------
# 4. JSON Response
# -------------------------------
print("\n--- JSON Request ---")
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

json_data = response.json()

print("JSON Data:", json_data)
print("Title:", json_data["title"])


# -------------------------------
# 5. Send Headers
# -------------------------------
print("\n--- Headers Example ---")
headers = {
    "User-Agent": "MyPythonRequestsScript/1.0"
}

response = requests.get("https://httpbin.org/headers", headers=headers)

print("Headers Response:", response.text[:100])


# -------------------------------
# 6. Download File
# -------------------------------
print("\n--- File Download ---")
file_url = "https://httpbin.org/image/png"

response = requests.get(file_url)

with open("downloaded_image.png", "wb") as f:
    f.write(response.content)

print("File downloaded as downloaded_image.png")


# -------------------------------
# 7. Streaming Large File
# -------------------------------
print("\n--- Streaming Download ---")
stream_url = "https://httpbin.org/bytes/2048"

response = requests.get(stream_url, stream=True)

with open("big_file.bin", "wb") as f:
    for chunk in response.iter_content(chunk_size=512):
        if chunk:
            f.write(chunk)

print("Streaming download complete")


# -------------------------------
# 8. Timeout Example
# -------------------------------
print("\n--- Timeout Example ---")
try:
    response = requests.get("https://example.com", timeout=5)
    print("Website responded with:", response.status_code)
except requests.exceptions.Timeout:
    print("Request timed out")