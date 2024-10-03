//
Write a program to sort the given list and print it.
Sample Input:
30 20 10 50 40
Sample Output:
10 20 30 40 5
//
my_list = list(map(int, input().split()))
my_list.sort()
print(*my_list) 
