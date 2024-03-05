from collections import Counter

def anagrama(string1, string2):
    if Counter(string1) == Counter(string2):
        return True
    
    return False

print(anagrama("america", "iracema"))
print(anagrama("estudo", "duetos"))
print(anagrama("estudar", "duetar"))