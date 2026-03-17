import requests

print("Which news you want to see choose:")
print("1. Tesla\n2. Apple\n3. Business")

choice1 = int(input("Enter Choice: "))

if choice1 == 1:
    response = requests.get("https://newsapi.org/v2/everything?q=tesla&apiKey=1137c5d0d12b4cf28c4898c5340ac759")
    data = response.json()

elif choice1 == 2:
    response = requests.get("https://newsapi.org/v2/everything?q=apple&from=2026-03-13&to=2026-03-13&sortBy=popularity&apiKey=1137c5d0d12b4cf28c4898c5340ac759")
    data = response.json()

elif choice1 == 3:
    response = requests.get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=1137c5d0d12b4cf28c4898c5340ac759")
    data = response.json()

else:
    print("Invalid choice")
    exit()

# Show articles
for i, article in enumerate(data["articles"][:10]):
    print(i, article["title"])

choice2 = int(input("Enter the article number you want to read: "))

print("\nSelected Article:")
print(data["articles"][choice2]["title"])