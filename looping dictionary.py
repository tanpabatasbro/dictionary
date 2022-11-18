friends = {
    "cup": "ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
    "sep":"asep si kasyep",
    "cuy":"cuy surucuy"
}
print("="*20)
for friend in friends:
    print(friend)
print("="*20)
keys = friends.keys()
print(keys)
print("="*20)
for key in friends.keys():
    print(friends.get(key))
print("="*20)
values = friends.values()
print(values)
print("="*20)
for value in friends.values():
    print(value)
print("="*20)
items = friends.items()
print(items)
print("="*20)
for item in friends.items():
    print(item)

for key,value in friends.items():
    print(f"key = {key},value ={value}")
