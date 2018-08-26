class MD:
    @staticmethod
    def to_title(words):
        return r'# {}'.format(words)

    @staticmethod
    def to_subtitle(words):
        return r'### {}'.format(words)

    @staticmethod
    def to_question_title(words):
        return r'#### {}'.format(words)
