# load model
class text_cleaning:
    """

    """
    def __init__(self):

        """


        """
        #define stopwords
        self.__stopwords = [
            '!',
            '?',
            ',',
            '.',
            '“',
            '”',
            '‘',
            '’',
            '•',
            '・',
            '…',
            ':',
            ';',
            '(',
            ')',
            '{',
            '}',
            '[',
            ']',
            '<',
            '>',
            '\'',
            '\/',
            '"',
            '#',
        ]

        #special stopwords that needed to be replaced by space
        self.__stopwords_special = [
            '-',
            '_',
            '\n',
            '\r'
        ]

    def preprocessing_text(self, text):
        """

        :param text: string, parsed text data
        :return:
        """

        # apply lowercasing
        text = text.lower()

        # remove punctuation
        text = self.__arrange_words(text)

        return text


    # The function to remove noisy marks in text
    def __arrange_words(self, text):
        """
        input: text - string, needed to be processed
        input: text - string, pocessed
        """
        for i in self.__stopwords:
            if i in self.__stopwords_special:
                text = text.replace(i, ' ')
            else:
                text = text.replace(i, '')

        return text