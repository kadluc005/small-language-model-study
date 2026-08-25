from src.import_data import names

print("Number of names:",len(names))


smallest_name = names[0]
longest_name = names[0]
for name in names:
    if len(name) < len(smallest_name):
        smallest_name = name
    if len(name) > len(longest_name):
        longest_name = name    

print("Smallest name:", smallest_name)
print("Length:", len(smallest_name))

print("Longest name:", longest_name)
print("Length:", len(longest_name))

chars = sorted(list(set("".join(names))))

print("Characters:", chars)
print("Number of characters:", len(chars))

lengths = [len(name) for name in names]

print("Average name length:", sum(lengths) / len(lengths))