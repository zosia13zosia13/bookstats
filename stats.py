def get_count_of_words(filepath: str) -> None:
    count = 0
    with open(filepath, "r") as file:
        for line in file:
            count += len(line.split()) #podzielimy po spacji
    print(f"Found {count} total words")


def count_characters(filepath: str) -> dict:
    symbols = {}
    with open(filepath, "r") as file:
        for line in file:
            for letter in line.lower():
                symbols[letter] = symbols.get(letter, 0) + 1 #jeśli nie ma litery to wsadzamy 0, w innym wypadku +1
    return symbols

def sort_dictionary(dictionary: dict) -> None:
    sorted_symbols = []
    for key, value in dictionary.items():
        sorted_symbols.append({"char": key, "num": value})

    sorted_symbols.sort(reverse=True, key = lambda item: item["num"])

    for item in sorted_symbols:
        print(f"{item["char"]}: {item["num"]}")

## Do books trzeba dodać 2 ksiązki
## Za pomocą sys.argv wczytać plik python main.py books/name_ksiazki.txt