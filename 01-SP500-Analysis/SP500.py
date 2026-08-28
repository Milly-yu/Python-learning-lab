fileref = open('SP500.txt', 'r')
lines = fileref.readlines()
sum_SP = 0
max_interest = float(lines[6].split(',')[5]) # remeber to invert the data type to float
for line in lines[6:18]: # iterate from June 2016 through May 2017    
    sum_SP += float(line.split(',')[1])
    if float(line.split(',')[5]) > max_interest:
        max_interest = float(line.split(',')[5])
mean_SP = sum_SP / 12
print(mean_SP, max_interest)
