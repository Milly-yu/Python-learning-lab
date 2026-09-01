percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]

resps = []
for per in percent_rain:
    if per > 90:
        resps.append('Bring an umbrella.')
    elif per > 80:
        resps.append('Good for the flowers?')
    elif per > 50:
        resps.append('Watch out for clouds!')
    else:
        resps.append('Nice day!')
print(resps)
# reminder: nothing special, just pay attention to some details: 1)the format of the nested if-elif-else; 2)don't forget the period, question mark, and exclamation mark after each string.
