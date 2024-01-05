class promptGenerator:

    def __init__(self, theme_words = None, words = None, answer_format=None, limits=None):
        self.num_sentences_limit = limits[0]
        self.num_characters_limit = limits[1]
        self.string_limit = self.generateStringLimit()
        self.answer_format = answer_format
        self.words = words
        self.collection_of_words = self.generateStringWords()
        self.theme_words = theme_words
        self.prompt = self.generatePrompt()

    def generateStringLimit(self):
        if self.num_sentences_limit is None and self.num_characters_limit is None:
            return "No limit"
        string_limit = "The maximum number of "
        if self.num_sentences_limit is not None:
            string_limit += "sentences is " + str(self.num_sentences_limit) + " and "
        if self.num_characters_limit is not None:
            string_limit += "characters is " + str(self.num_characters_limit) + " and "
        string_limit = string_limit[:-5]
        return string_limit

    def generateStringWords(self):
        collection_of_words = ""
        counter = 0
        for word in self.words:
            counter += 1
            collection_of_words += f"Word/Phrase {counter}: " + word + ", "
        return collection_of_words[:-2]
    def generatePrompt(self):
        template_prompt = (
            f"I will give you a collection of words or phrases, which will from now on be called QWERTY.\n"
            f"Please provide an answer to each QWERTY in a quizlet style with the format being {self.answer_format}.\n"
            f"The answers must be in accordance to the theme of: {self.theme_words}.\n"
            f"Each QWERTY must be with this prescribed limit: {self.string_limit}.\n\n"
            f"The collection of words or phrases is:\n{self.collection_of_words}\n"
        )
        return template_prompt


# theme_words = "Answer the questions academically in terms of chemistry"
# words = ["water", "phosphorus", "the types of carbon sequestration"]
# answer_format = "you display your answer, then you enter three times and then your next answer, and so on so forth"
# num_sentences_limit = None
# num_characters_limit = 50
# limits = [num_sentences_limit, num_characters_limit]
# example = promptGenerator(theme_words, words, answer_format, limits)
# # print(example.answer_format)
# # print(example.theme_words)
# # print(example.string_limit)
# # print(example.collection_of_words)
#
# print("prompt: ", example.prompt)