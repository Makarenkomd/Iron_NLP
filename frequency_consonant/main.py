import os

cons = set(['б', 'в', 'г', 'гъ', 'д', 'дж', 'дз','ж', 'з', 'й', 'к', 'къ', 'л', 'м', 'н', 'п', 'пъ', 'р', 'с', 'т', 'тъ', 'ф', 'х', 'хъ', 'ц', 'цъ', 'ч', 'чъ', 'ш', 'щ'])

# преобразыем слово в список списков подряд идущих согласных
def word_to_list_cons(word):
    double_symbol = 'гдкптцчх'
    list_continuals = list()
    continual = list()
    i = 0
    while i < len(word):
        if word[i] in cons:
            if word[i] in double_symbol :
                if i + 1 < len(word):
                    double_cons = word[i:i + 2]
                    if double_cons in cons:         # двойная буква
                        continual.append(double_cons)
                        #is_double = True
                        i += 1
                    else:                           # одинарная буква
                        continual.append(word[i])
                else:
                    continual.append(word[i])       # одинарная буква в конце слова
            else:
                continual.append(word[i])           # одинарная буква
        else:
            if continual: list_continuals.append(continual)
            continual = list()
        i += 1
    if continual: list_continuals.append(continual)
    return  list_continuals


# считать все файлы из папки дата
count_word = 0
files = list(os.walk("data"))[0][2]
print("Всего файлов", len(files))
freq_cons = dict()
for file in files:
    path_text = 'data/' + file
    with open(path_text, "r", encoding="utf-8") as file_text:
        for line in file_text.readlines():
            for word in line.lower().split():
                count_word += 1
                # возвращает список списков
                list_consonants = word_to_list_cons(word)
                #print(word, list_consonants)
                for list_ in list_consonants:
                    if len(list_) > 1:          # более 1 согласной подряд
                        key = '/'.join(list_)
                        if key in freq_cons:
                            freq_cons[key][0] +=1
                        else:
                            freq_cons[key] = [1]
                        freq_cons[key].append(word)
        print(len(freq_cons))



print("Всего различных сочетаний согласных", len(freq_cons))
print("Всего обработано слов", count_word)
#print(freq_cons.items())
freq_cons_sort = sorted(freq_cons.items(), key=lambda x: - x[1][0])
#print(freq_cons_sort)
all_tuple_consonant = sum([freq_cons[key][0] for key in freq_cons])
print("Всего сочетаний согласных", all_tuple_consonant)
file_analysis = 'statistics_analysis_of_consonants.txt'
with open(file_analysis, "w", encoding="utf-8") as file_out:
    for el in freq_cons_sort:
        unic_words = set(el[1])
        temp = f"{el[0]} {el[1][0]}|{round(el[1][0]/all_tuple_consonant * 100, 3)} {len(unic_words)} {list(unic_words)[:10]}"
        #print(temp)
        print(temp, file=file_out)



