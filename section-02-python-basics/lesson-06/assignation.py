# Copy the contents of one file to another
# Counts the number of occurrences of a specific word in a text file
# Log messages with timestamps into a file

import datetime


def copy_option():
    try:
        file_1 = input("Copy from file: ")
        file_2 = input("Destination file: ")
        with open(file_1, "r") as file:
            lines = file.readlines()
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)
            print(f"Number of lines: {line_count}")
            print(f"Number of words: {word_count}")
            with open(file_2, "w+") as dest_file:
                dest_file.write("".join(lines))
                dest_file.write(f"\nNumber of lines: {line_count}")
                dest_file.write(f"\nNumber of words: {word_count}")
    except FileNotFoundError:
        print(f"File {file_1} not found!")


def summarize_words(file_name):
    try:
        wordsList = dict()
        file_1 = input("Input file: ")
        file_1 = file_name
        with open(file_1, "r") as file:
            lines = file.readlines()
            line_count = len(lines)
            # word_count = sum(len(line.split()) for line in lines)
            for line in lines:
                for word in line.lower().split():
                    wordsList[word] = wordsList.get(word, 0) + 1
            print(f"Number of lines: {line_count}")
            result = "\n".join(
                (f"'{key}' = {value}") for key, value in wordsList.items()
            )
            print(f"Occurrences by word: \n{result}")

    except FileNotFoundError:
        print(f"File {file_1} not found!")


def log_in_file_option():
    try:
        file_1 = input("File to write from file: ")
        text = input("Text to append: ")
        with open(file_1, "a+") as file:
            file.write(f"\n{datetime.datetime.now()}: {text}")
    except FileNotFoundError:
        print(f"File {file_1} not found!")


while True:
    print(
        """
  System options
  e: exit
  1: Copy the contents of one file to another
  2: Counts the number of occurrences of a specific word in a text file
  3: Log messages with timestamps into a file
  """
    )

    option = input("Select an option /> ")

    if option == "e":
        break
    elif option == "1":
        print("COPY FROM 1 FILE TO ANOTHER")
        copy_option()
    elif option == "2":
        print("SUMMARIZE WORDS")
        summarize_words("sample.txt")
    elif option == "3":
        print("LOG IN FILE")
        log_in_file_option()
    else:
        print("Option not found")
