NAME_MIN_CHARACTERS: dict[str, int] = {
    "English": 3, "Japanese": 1
}

NAME_MAX_CHARACTERS: dict[str, int] = {
    "English": 26, "Japanese": 6
}

def name_them(question: str = "Name:") -> str:
    language: str = language_name()
    prompt: str = question.strip() + " "

    while True:
        name: str = str(input(prompt))
        if not name:
            print("Whitespaces only are not accepted.")
            continue
        if not all(c.isalpha() or c.isspace() for c in name):
            print("Only alphabetic letters are accepted.")
            continue

        language_characters: int = get_key_from_value(value = language)
        language_min_characters: int = LANGUAGE_NAMES[language_characters]
        if len(name) < NAME_MIN_CHARACTERS[language]:
            print(f"That name is too short to be a real {language_min_characters} name.")
            continue

        language_max_characters: int = LANGUAGE_NAMES[language_characters]
        if len(name) > NAME_MAX_CHARACTERS[language]:
            print(f"That name is too long to be a real {language_max_characters} name.")
            continue

        complete_name = name.split()
        if len(complete_name[0]) > 26:
            print(f"A {language_max_characters} first name can not have more than 26 characters.")

        return name

LANGUAGE_NAMES: dict[int, str] = {
    1: "English",
    2: "Japanese"
}

def language_name(question: str | None = None) -> str:
    if question is None:
        choice: int = 1
        return LANGUAGE_NAMES[choice]

    while True:
        print("----------\nSELECT YOUR NAME'S LANGUAGE:\n----------\n")
        print(
            " [1] English\n",
            "[2] Japanese\n"
        )
        try:
            choice = int(input("Choice: "))

            if not choice:
                print("Empty spaces are not allowed.")
                continue

            print(f"You have a {LANGUAGE_NAMES[choice]} name.")
            return LANGUAGE_NAMES[choice]
        except ValueError as e:
            print(f"Invalid input {e}")

def get_key_from_value(dictionary: dict[object, object] = LANGUAGE_NAMES, value: object | None = None) -> object | None:
    for k, v in dictionary.items():
        if v == value:
            return k
    return None

if __name__ == "__main__":
    name: str = name_them(" Enter your name: ")
    print(f"Yourname is {name}.")
