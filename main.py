def main():
    print("hello")

    # Chapter 7 strings
    # strings are a collection data type in python
    # furthermore, they are also considered ordered collections
    # getting length of string
    text = "How much wood could a woodchuck chuck, if a woodchuck could chuck wood?"
    print(len(text))
    # we can use '', "" or """"""/'''''' so long as we start adn end with same type
    # """""" can span multiple lines too

    # Bracket Notation
    # index starts at zero.
    sample_string = "This is a sample string."
    print(sample_string[-1])
    print(sample_string[0])

    # Slicing strings
    # remember that slicing is exclusive
    print("\nSlicing Strings section:")
    print(sample_string[0:4])
    print(sample_string[5:])

    # String immutability
    # strings cannot have individually characters of their string changed
    # ex:) sample_string[0]='t' would throw an error. doesn't apply to variables though, we can reassignt them

    # String methods:
    # good list at: https://education.launchcode.org/lchs/chapters/strings/string-methods.html

    # Other characters (unicode)
    # unicode table: https://unicode-table.com/en/
    print('\u25E8     \u26BD     \u26A1')

    # format method (template literals)
    new_string = "and I'm adding a new string to it."
    print("{} This is some more text. {}".format(sample_string, new_string))

    # fstring (python 3.6 and later)
    fstring_example = f"example of a format string. {sample_string}"
    print(fstring_example)

    # Checking types
    my_var = 42
    if type(my_var) == str:
        print("The value '{0}' is a string.".format(my_var))
    else:
        print("The value {0} is NOT a string.".format(my_var))

    # in and not in
    text = "Armadillos or anteaters"
    vowels = 'aeiou'
    vowel_count = 0
    for char in text.lower():
        if char in vowels:
            vowel_count += 1
    print(f"'{text}' contains {vowel_count} vowels.")

    # checking case
    character = 'a'
    word = "yep!"
    non_letters = '$10.75'
    print(character.isupper())
    print(word.islower())
    print(non_letters.isupper())

    # string module
    # provides us with some checks and constants
    # https://education.launchcode.org/lchs/chapters/strings/string-module.html


if __name__ == "__main__":
    main()
