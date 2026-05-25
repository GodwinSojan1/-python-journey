from datetime import date
today = date.today()
entry = input("Write your diary entry: ")

with open("D:/git/git hub/diary.txt", "a") as file:
    file.write(f"{today}: {entry}\n")

print("Entry saved!")
print("\n--- All Diary Entries ---")

with open("D:/git/git hub/diary.txt", "r") as file:
    content = file.read()
    print(content)
    