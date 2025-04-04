class WordIterator:
    def __init__(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            self.words = self.extract_words(text)
            self.index = 0
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def extract_words(self, text):
        word = ""
        words = []
        for char in text:
            if char.isalnum():
                word += char
            elif word:
                words.append(word)
                word = ""
        if word:
            words.append(word)
        return words

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        word = self.words[self.index]
        self.index += 1
        return word


file_path = "reflection.txt"

try:
    iterator = WordIterator(file_path)
    for word in iterator:
        print(word)
except Exception as e:
    print(f"An error occurred: {e}")



