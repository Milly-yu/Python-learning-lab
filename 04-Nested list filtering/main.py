athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]
t = []
other = []
for lst in athletes:
    for name in lst:
        if 't' in name:
            t.append(name)
        else:
            other.append(name)
print("Names with 't':", t)
print("Other names:", other)
