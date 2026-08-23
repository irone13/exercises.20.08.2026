#1
grades = {}
grades['math'] = int(input('Math grade : '))
grades['english'] = int(input('English grade : '))
grades['literature'] = int(input('literature grade : '))
grades['python'] = int(input('Python grade : '))
print(f"1 : grades = {grades}")
#2
grades['avg'] = (grades['math'] + grades['english'] + grades['literature'] + grades['python'])//len(grades)
print(f"2 : {grades}")

#3
grades['max'] = max(grades.values())
grades['min'] = min(grades.values())
print(f"3 : {grades}")

#4
grades.pop('literature')
print(f"4 : {grades}")

#irone Zaoui



