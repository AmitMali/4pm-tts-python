'''
print("Enter any two numbers")
no1 = int(input())
no2 = int(input())

if no1 > no2:
    temp = no1
    no1 = no2
    no2 = temp

while no1 <= no2:
    if no1 % 2 == 0:
        print(no1,end=', ')
    no1 = no1 + 1
'''

'''
take letter from user and print following pattern
a
aa
aaa
aaaa
aaaaa
aaaaaa
aaaaaaa
'''

for x in range(0,10):print('a'*x)