from string import punctuation


def count_letters_and_punctuation(text):
    total_letters = sum(1 for char in text if char.isalpha())
    total_punctuations = sum(1 for char in text if char in punctuation)
    return total_letters, total_punctuations


def process_file(input_, output_):
    with open(input_, "r") as input_file, open(output_, "w") as output_file:
        for line_number, line in enumerate(input_file, start=1):
            total_letters, total_punctuations = count_letters_and_punctuation(line)
            output_file.write(f"Line {line_number}: {line.strip()} ({total_letters})({total_punctuations})\n")


process_file("text.txt", "output.txt")