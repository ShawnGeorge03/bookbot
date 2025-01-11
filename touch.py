def read_file(path_to_file):
    file_content = ''

    with open(path_to_file) as f:
        file_content = f.read()

    return file_content

def word_count(file_content):
    words = file_content.split()
    print(f"Number of Words: {len(words)}")

def character_count(file_content):
    cleaned_file_content = file_content.lower()

    for char_id in range(ord('a'), ord('z') + 1):
        char = chr(char_id)
        char_count = cleaned_file_content.count(char)
        print(f"The {char} character was found {char_count} times")

def main():
    path_to_file = "books/frankenstein.txt"
    file_content = ""

    file_content = read_file(path_to_file)
    print(f"--- Begin report of {path_to_file} --")

    word_count(file_content)

    print("Character Count")
    character_count(file_content)

main()
