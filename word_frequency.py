STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as praise_song:
        text = praise_song.read()
    word_list = text.split(" ")
    word_list_copy = text.replace("-","")
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for element in text:
            if element in punctuations:
                text = text.replace(element, "")
        # text = text.replace("\n", " ")
    word_list_copy 
    word_list_copy = word_list.copy()
    for word in word_list:
        if word in STOP_WORDS:
            word_list_copy.remove(word)
    word_frequency = {}
    for word in word_list_copy:
        if word in word_frequency.keys():
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    print(word_frequency)


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
