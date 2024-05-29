# Time Complexity
# - Average : O(nlogn)
# - Worst   : O(nlogn)
# 리스트를 반으로 분할해 정렬하고, 정렬된 서브 리스트를 합병하는 작업을 반복
# 정렬된 리스트를 보관할 추가적인 저장공간이 필요함

def sort(num, left, right):
    if left < right:
        mid = (left+(right-left)//2)
        sort(num, left, mid)
        sort(num, mid+1, right)
        merge(num, left, mid, right)
        print(num)

def merge(num, left, mid, right):
    pos = left
    left_end = mid
    right_start = mid+1
    n = right-left+1
    temp = [None]*len(num)
    while left <= left_end and right_start <= right:
        if num[left] <= num[right_start]:
            temp[pos] = num[left]
            pos+=1
            left+=1
        else:
            temp[pos] = num[right_start]
            pos+=1
            right_start+=1
        while left <= left_end:
            temp[pos] = num[left]
            pos+=1
            left+=1
        while right_start <= right:
            temp[pos] = num[right_start]
            pos+=1
            right_start+=1
        for i in range(n):
            num[right]=temp[right]
            right-=1

num = [31, 10, 9, 23, 49, 15, 11, 7]
sort(num, 0, len(num)-1)



