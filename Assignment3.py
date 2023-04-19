# sun and avaerage of a given list of items

list = [10,20,50,25,70,80,55,5,15]
sum = 0
average = 0
for price in list:
    sum = sum + price
    average = sum / len(list)
print ('The SUM and AVERAGE value are',sum,'and',average,'respectively')