'''
Print the following pattern for the given N number of rows.
Pattern for N = 4

1
11
121
1221

Input format :

Integer N (Total no. of rows)

Output format :

Pattern in N lines

Sample Input :

5

Sample Output :

1
11
121
1221
12221

'''

num=int(input('enter the number :'))
for i in range(1,num+1):
    for j in range(0,i):
        x=i-1
        if x==0:
            print(1,end="")
        else:
            if x==j or j==0:
                print(1,end="")
            else:print(2,end="")
    print("")