class TextProcessor:
    def __init__(self, text):
        self.text = text
        self.banned_words = ["example_banned_word"]

    def word_count(self):
        return len(self.text.split())

    def reverse_words(self):
        return ' '.join(self.text.split()[::-1])

    def to_uppercase(self):
        return self.text.upper()

    def contains_banned_word(self):
        return any(banned_word in self.text for banned_word in self.banned_words)

# 使用示例
if __name__ == "__main__":
    text = "Hello world, this is an example text with example_banned_word"
    processor = TextProcessor(text)
    
    print("Original Text:", text)
    print("Word Count:", processor.word_count())
    print("Reversed Words:", processor.reverse_words())
    print("Uppercase:", processor.to_uppercase())
    print("Contains Banned Word:", processor.contains_banned_word())
