class WordStartsWithIterator(Iterator):
    def __init__(self, text: str, letter: str):
        self.word_iterator = WordIterator(text)
        self.letter = letter.lower()
        self.next_word = None

    def __next__(self) -> str:
        if self.next_word is not None:
            word = self.next_word
            self.next_word = None
            return word

        while True:
            word = next(self.word_iterator)
            if word and word[0].lower() == self.letter:
                return word

with open("reflection.txt", "r", encoding="utf-8") as f:
    file_text = f.read()
it = WordStartsWithIterator(file_text, 'a')
for word in it:
    print(word)


