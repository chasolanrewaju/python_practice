# Averaage of first n natural numbers

n = input('The nth term value: ')
n = int(n)
sum = 0
average = 0
for num in range (0,n+1,1):
    sum = sum + num
    average = sum/n
print ('The sum of nth term is:', sum)
print ('The average value is:', average)
