MAX_NUM_BELL_PEPPERS = 1
MAX_NUM_CAULIFLOWERS = 2
MAX_NUM_CARROTS = 4
MAX_NUM_CELERIES = 3


class JarIterator:
    def __init__(self, content):
        self.content = content
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.content):
            self.index += 1
            return self.content[self.index - 1]
        else:
            raise StopIteration()


# def jars_content(jars, bell_peppers, cauliflowers, carrots, celeries):
#     while bell_peppers and cauliflowers and carrots and celeries:
#         for jar in jars:
#
a = JarIterator([1, 3, 4])
print(next(a))
print(a)
