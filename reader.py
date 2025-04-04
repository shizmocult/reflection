class LongWordIterator:
    def __init__(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        for ch in ",.!?;:()":
            text = text.replace(ch,"")
        self.words = [word for word in text.split() if len(word) > 3]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise Stopiteration

        word = self.words[self.index]
        self.index += 1
        return word

file_path = "reflection.txt"
for word in LongWordIterator(file_path):
print (word)