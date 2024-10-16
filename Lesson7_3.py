import io
from pprint import pprint

class WordsFinder:
    def __init__(self, file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        a = ''
        punc = [',', '.', '=', '!', '?', ';', ':', ' - ']
        with open(self.file_names, 'r', encoding = 'utf-8') as file:
            for line in file:
                line = line.lower()
                for i in line:
                    if i in punc:
                        line = line.replace(i, '')
                a = a + line
            all_words.update({self.file_names:a.split()})
        return all_words

    def find(self, txt):
        _dict = {}
        word = self.get_all_words()[self.file_names]
        for zaycev in range(len(word)):
            if txt.lower() == word[zaycev]:
                _dict.update({self.file_names:zaycev+1}) #им будут наказаны хулиганы ему будет принадлежать сердце любимой дамы и он будет в институте самым популярным zaycev + 1
                return _dict

    def counter(self, txt):
        _dict = {}
        word = self.get_all_words()[self.file_names]
        _dict.update({self.file_names:word.count(txt.lower())})
        return _dict

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.counter('tExT'))  # 4 слова teXT в тексте всего