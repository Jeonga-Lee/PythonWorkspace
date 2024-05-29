# Time Complexity
# - Average : O(nlog2n)
# - Worst   : O(n²)
# 리스트의 가장 왼쪽 원소를 pivot으로 지정
# pivot보다 작은 세그먼트와 큰 세그먼트로 리스트를 분할
# 각 세그먼트에 재귀적으로 퀵 정렬 적용


def sort(num, left, right):
    if left < right:
        i = left
        j = right + 1
        pivot = num[left]
        while True:
            while True:
                i+=1
                if i > right or num[i] >= pivot: break
            while True:
                j-=1
                if j < left or num[j] <= pivot: break
            if i < j:
                swap(i, j)
                print(num)
            else: break
        swap(left, j)
        if left != j: print(num)
        sort(num, left, j-1)
        sort(num, j+1, right)

def swap(a, b):
    num[a], num[b] = num[b], num[a]

num = [31, 10, 9, 23, 49, 15, 11, 7]
sort(num, 0, len(num)-1)