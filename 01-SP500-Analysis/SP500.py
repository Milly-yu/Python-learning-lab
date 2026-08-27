fileref = open('SP500.txt', 'r')
lines = fileref.readlines()
sum_SP = 0
max_interest = float(lines[6].split(',')[5])
for line in lines[6:18]:
    sum_SP += float(line.split(',')[1])
    if float(line.split(',')[5]) > max_interest:
        max_interest = float(line.split(',')[5])
mean_SP = sum_SP / 12
print(mean_SP, max_interest)
