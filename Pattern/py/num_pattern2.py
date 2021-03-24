'''

Print the following pattern for the given N number of rows.
Pattern for N = 4

1
11
202
3003

Input format :Integer N (Total no. of rows)

Output format :Pattern in N lines

Sample Input :5

Sample Output :

1
11
202
3003
40004

'''
num=int(input('Enter the num for pattern : '))
for i in range(1,num+1):
    for j in range(0,i):
        x=i-1
        if x==0:
            print(1,end="")
        else:
            if x==j or j==0:
                print(x,end="")
            else:print(0,end="")
    print("")