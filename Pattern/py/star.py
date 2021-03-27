'''

Print the following pattern
Pattern for N = 4

Star Pattern
The dots represent spaces.
Input Format :

N (Total no. of rows)

Output Format :

Pattern in N lines

Constraints :

0 <= N <= 50

Sample Input 1 : 3

Sample Output 1 :

   *
  *** 
 *****

Sample Input 2 : 4
Sample Output 2 :

    *
   *** 
  *****
 *******

'''

num=int(input('enter the number : '))
i=1
while num>=i:
    spaces=1
    while spaces<=(num-i):
        print(" ",end="")
        spaces=spaces+1
    k=i
    while k>=1:
        print("*",end="")
        k=k-1
    j=2
    while j<=i:
        print("*",end="")
        j=j+1

    print()
    i += 1