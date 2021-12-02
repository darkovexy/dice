#Write a python function to remove a given word from a string and strip it at the same time.
def remove_and_strip(str,word):
    new_str = str.replace(word," ")
    return new_str.strip()

string = "      Hi this is chinmay    "
n = remove_and_strip(string,"Hi")
print(n)