'''

Print the following pattern for the given N number of rows.
Pattern for N = 3

 A
 BB
 CCC

Input format :

Integer N (Total no. of rows)

Output format :

Pattern in N lines

Constraints 0 <= N <= 26
Sample Input 1:7

Sample Output 1:

A
BB
CCC
DDDD
EEEEE
FFFFFF
GGGGGGG

Sample Input 2: 6

Sample Output 2:

A
BB
CCC
DDDD
EEEEE
FFFFFF




'''

l=['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num=int(input())
c=0
for i in range(1,num+1):
    for j in range(0,i):
        print(l[i-1],end="")
    print()
    c=c+1