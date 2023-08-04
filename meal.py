child = input('how much for child?')
adult = input('and for adults?')

kids = input('how many kids are there?')
old = input('how many adult are there?')

Fkids = float(child) * float(kids)
Fadults = float(adult) * float(old)

total = Fkids + Fadults

print(f'the total amount of you bill is {total}')