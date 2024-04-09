# Get multiple values from a dictionary in Python

my_dict = {
    'name': 'Borislav Hadzhiev',
    'site': 'bobbyhadz.com',
    'id': 1,
    'topic': 'Python'
}

keys = ['name', 'site']

values = [my_dict[key] for key in keys]
print(values)  # 👉️ ['Borislav Hadzhiev', 'bobbyhadz.com']

# ----------------------------------------

# 👇️ using dict.get()

values = [my_dict.get(key) for key in keys]
print(values)  # 👉️ ['Borislav Hadzhiev', 'bobbyhadz.com']