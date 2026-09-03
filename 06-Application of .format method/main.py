inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

for item in inventory:
    name = item.split(',')[0] # Remember to split the string, or else the indexing will be by character, not word.
    qty = item.split(',')[1]
    price = item.split(',')[2]
    print('The store has{} {}, each for{} USD.'.format(qty, name, price))
    # A sentence will be printed out for every item, so the print() function should be included in every loop; adjust the format of the printed sentence.

