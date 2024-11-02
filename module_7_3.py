
class WordsFinder:
    file_names = []
    all_words = {}
    def __init__(self, *texts_name):
        for i in range(len(texts_name)):
            self.file_names.append(texts_name[i])

    def get_all_words(self):
        for i in range(len(self.file_names)):
            with open(self.file_names[i], encoding='utf-8') as file:
                str1 = file.read().lower()
                for j in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    str1 = str1.replace(j, ' ')
                str2 = str1.split()
                self.all_words.update({self.file_names[i] : str2})
        return self.all_words

    def find(self, word):
        WordsFinder.get_all_words(self)
        word1 = word.lower()
        words1 = {}
        for i in range(len(self.file_names)):
            text1 = self.all_words.get(self.file_names[i])
            for j in range(len(text1)):
                if word1 == text1[j]:
                    words1.update({self.file_names[i] : j + 1})
                    break
                else:
                    continue
        return words1

    def count(self, word):
        WordsFinder.get_all_words(self)
        word2 = word.lower()
        words2 = {}
        for i in range(len(self.file_names)):
            text2 = self.all_words.get(self.file_names[i])
            number = 0
            for j in range(len(text2)):
                if word2 == text2[j]:
                    number += 1
                else:
                    continue
            words2.update({self.file_names[i] : number})
        return words2
    
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего