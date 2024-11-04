def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = word_count(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")

    chars = char_count(file_contents)

    for char, count in chars.items():
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")


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