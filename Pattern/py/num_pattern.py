'''

Print the following pattern for the given N number of rows.
Pattern for N = 4

1234
123
12
1

Input format :

Integer N (Total no. of rows)

Output format :

Pattern in N lines

Sample Input : 5
Sample Output :

12345
1234
123
12
1


'''


num = int(input('Enter the value pattern number : '))
for i in range(0,num):
    for j in range(1,num+1-i):
        print(j,end="")

    print()