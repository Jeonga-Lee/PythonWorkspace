# Time Complexity
# - Worst   : O(n²)
# 최댓값을 오른쪽으로 이동시키는 데 O(n)의 시간이 걸리고, n번 반복

# 탐색범위
# Outer : O -> n-1
# 마지막 element 제외
# Inner : O -> n-1-i
# 이미 정렬된 부분 제외

def swap(a, b):
    lst[a], lst[b] = lst[b], lst[a]

def sort(lst):
    n = len(lst)
    for i in range(n-1):
        flag = 0
        for j in range(n-1-i):
            if lst[j] > lst[j+1]:
                swap(j, j+1)
                flag = 1
        if flag == 0: break
        # 이전 단계에서 원소의 교환이 없었다면 빠져나옴
        print(lst)

lst = [31, 10, 9, 23, 49, 15 ,11 ,7]
sort(lst)
