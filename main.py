def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    words = word_count(file_contents)
    print("***********************************************")
    print(f"This text have {words} words")

    chars = char_count(file_contents)
    print("***********************************************")
    print(f"Characters count: {chars}")

def word_count(file_contents):
    words = file_contents.split()
    return len(words)

def char_count(file_contents):
    words = file_contents.split()
    chars = dict()
    for word in words:
        word = word.lower()
        for char in word:
            if char in chars:
                chars[char] = chars[char] + 1
            else:
                chars[char] = 1
    return chars

main()