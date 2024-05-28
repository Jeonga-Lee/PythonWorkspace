# Time Complexity
# - Worst   : O(n²)
# 최솟값을 찾는데 n번 비교하고, 이 과정을 n번 반복

# 탐색범위
# Outer : O -> n-1
# 마지막 element 제외
# Inner : O -> i+1
# 이미 정렬된 부분 제외

def swap(a, b):
    lst[a], lst[b] = lst[b], lst[a]

def selectionSort(lst):
    n = len(lst)
    for i in range(n-1):
        smallest=i
        for j in range(i+1, n):
            if lst[j] < lst[smallest]:
                smallest = j
        swap(i, smallest)
        print(lst)

lst = [31, 10, 9, 23, 49, 15, 11 ,7]
selectionSort(lst)