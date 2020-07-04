from collections import defaultdict
import NOD
import random

# 1) Подсчет количества повторений биграмм

f = open('output.txt', 'r', encoding="utf-8");

output = '';

for num, line in enumerate(f):
    output = output + line.strip();
    # if (num == 15):
    #     break;

frequency = {};
trigrMass = [];

i = 0;
j = 1;
k = 2;

while (i < len(output) - 2):
    ss = output[i] + output[j] + output[k];
    i += 1;
    j += 1;
    k += 1;

    if (ss in trigrMass):
        continue;
    else:
        trigrMass.append(ss);


for word in trigrMass:
    frequency[word] = 0;

print(frequency);

i = 0;
j = 1;
k = 2;
kol = 5;

while (i < len(output) - 2):
    ss = output[i] + output[j] + output[k];

    i += 1;
    j += 1;
    k += 1;

    frequency[ss] += 1;


frequency = sorted(frequency.items(), key=lambda item: item[1], reverse=True);

print(frequency);

# На данном этапе есть количества всех биграмм в отсортированном порядке

# 2) Анализ самой частой биграммы и поиск d

for m in range(0, 1):

    i = 0;
    j = 1;
    k = 2;
    trigram = frequency[m][0];
    kolTrig = frequency[m][1];

    pos = [];

    while (i < len(output) - 2):
        if (kolTrig == 0):
            break;

        ss = output[i] + output[j] + output[k];

        if (ss == trigram):
            pos.append(i);
            kolTrig -= 1;

        i += 1;
        j += 1;
        k += 1;

    print(pos);
    posDiff = [];

    for n in range(0, len(pos) - 1):
        m = n + 1;
        posDiff.append(pos[m] - pos[n]);

    print(posDiff);


# 3)можно сделать вывод насчет d и попытаться продолжить расшифровку
#  разбиваем исходный текст на d строк
test = [];
for i in range(0, 10):
    a = random.randint(0, len(posDiff) - 1);
    b = random.randint(0, len(posDiff) - 1);
    test.append(NOD.NOD(posDiff[a], posDiff[b]));

print("Вычислительно сдвиг равен: ", test);

d = input("Введите предпологаемый свдиг: ");
d = int(d);

splitMass = [];

j = 1;

for i in range(1, d + 1):
    l = '';

    while (j < len(output)):
        l += output[j];
        j += d;

    j = i + 1;
    splitMass.append(l);


# 4) Сейчас текст разбит на d строк. теперь в каждой строке проводим частотный анализ
Alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', '_'];
alphNumd = [];

for i in range(0, len(splitMass)):
    alphNumd.append(0);
    alphNumd[i] = defaultdict(int);

    for j in range(0, len(splitMass[i])):
         alphNumd[i][splitMass[i][j]] += 1;

    alphNumd[i] = sorted(alphNumd[i].items(), key=lambda item: item[1], reverse=True);
    print(alphNumd[i]);


# 5) Отталкиваясь от того, что самый частый символ - пробел,
# начинаем искать сдвиг для каждой строки

shift = [];
for i in range(0, len(splitMass)):
    shift.append(0);
    shift[i] = (1 + Alphabet.index(alphNumd[i][0][0])) % 31;
print(shift);
# 6) Зная сдвиг можно преобразовать каждую из строк

newText = [];

for i in range(0, len(splitMass)):
    s = '';
    for j in range(0, len(splitMass[i])):
        k = splitMass[i][j];
        kk = Alphabet.index(k);
        newK = (kk - shift[i]) % 31;
        k = Alphabet[newK];
        s += k;

    splitMass[i] = s;


for i in range(0, len(splitMass)):
    print(splitMass[i]);

# 7)Запись новых строк в файл
try:
    j = 0;
    ss = '';
    print(len(output));
    while j < len(output) // d:
        i = 0;
        while (i < d):
            ss += splitMass[i][j];
            i += 1;
        j += 1;
except:
    pass

input = open('input.txt', 'w');

input.write(ss);

f.close();
input.close();

# 8)Шифровальное слово
print();

s = '';
try:
    for i in shift:
        s += Alphabet[i];
except:
    pass
print(s);
print(len(ss));
kol = 0;


