first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = ((len(f) - len(s)) for f, s in zip(first, second) if len(f) - len(s) != 0)
second_result = (len(first[x]) == len(second[x]) for x in range(len(first)))

print(list(first_result))
print(list(second_result))

