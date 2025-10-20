import sys
from stats import get_count_of_words
from stats import count_characters
from stats import sort_dictionary

def main():
    # sys.arg - lista wszytskich argumentów z terminalu; python - część polecenia systemowego, a nie scryptu (?)
    if len(sys.argv) == 1:
        print("Podaj poprawną śiezkę pliku")
        return
    else:
        filepath = sys.argv[1] #0 argument - main.py, argument 1- ściezka

    get_count_of_words(filepath)

    char_count = count_characters(filepath)
    sort_dictionary(char_count)

if __name__ == "__main__":
    main()

