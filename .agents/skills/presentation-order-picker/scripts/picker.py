import random


names = ["Lucia", "Shichao", "Shiyi", "Yizhou", "Xingcheng"]


random.shuffle(names)

print("Presentation Order:")
for i, name in enumerate(names, 1):
    print(f"{i}. {name}")