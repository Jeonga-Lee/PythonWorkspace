# Time Complexity
# - Worst   : O(n²)
# 원소들이 역순으로 되어있는 경우
# - Best    : O(n) 
# 이미 정렬이 되어있는 경우

# 탐색범위
# Outer : 1 -> n
# 정렬된 어레이를 유지할 때 시작 사이즈를 2로 설정
# Inner : j >= 0 && lst[i] > key
# 정렬된 어레이를 끝까지 탐색하지 않았고, 
# 현재 값보다 키가 더 작으면 왼쪽으로 이동

def sort(lst):
    n = len(lst)
    for i in range(1, n):
        pivot = lst[i]
        j = i - 1
        # 정렬된 list중 제일 큰 숫자
        while j >= 0 and lst[j] > pivot: 
            # j 인덱스가 0 이상이고 j가 pivot보다 크면 
            lst[j+1] = lst[j]
            # j값 pivot에 덮어씌우기
            j-=1
            # j를 감소하여 반복
        lst[j+1] = pivot
        # while문 종료 전 j-=1 했기 때문에 
        # j+1 자리에 pivot 할당

        print(lst)

lst = [31, 10, 9, 23, 49, 15, 11, 7]
sort(lst)