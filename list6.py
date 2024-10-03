Write a Python Program to find the smallest number in a list
Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the size of the list.
Output consists of the largest element.
Sample Input:
5
1
2
3
6
5
Sample Output:
1
//
n = int(input())
my_list = []
for _ in range(n):
    my_list.append(int(input()))
min_num = my_list[0]
for num in my_list:
    if num < min_num:
        min_num = num
print(min_num)
