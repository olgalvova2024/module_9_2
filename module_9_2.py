first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
first_result = [str_ for str_ in first_strings if len(str_) > 5]
print(first_result)
second_result = [(str1, str2) for str1 in first_strings for str2 in second_strings if len(str1) == len(str2)]
print(second_result)
third_result = {str_: len(str_) for str_ in (first_strings + second_strings) if (len(str_)%2 != 1)}
print(third_result)
