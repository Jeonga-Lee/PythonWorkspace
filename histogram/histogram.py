# graphics module을 이용해 histogram graph를 생성하는 프로그램

from graphics import *

def createHistogram(range_list, part):
    # 창의 제목과 크기 설정
    title = "Quiz Score Histogram"
    width = 1000
    height = 600
    
    # GraphWin 객체 생성 및 변수 win에 할당
    win = GraphWin(title, width, height)
    
    # 창의 좌표 설정
    # 창의 좌표는 x = -1 → x = 21, y = -10 → y = (part 의 최대값 + 5)로 변화한다.
    win.setCoords(-1, -10, 21, max(part) + 5)
    
    # 히스토그램 바의 너비 설정
    barWidth = 0.8
    
    for i, count in enumerate(part):
        # Rectangle 객체 생성 및 변수 rect에 할당
        rect = Rectangle(Point(i, 0), Point(i + barWidth, count))
        rect.setFill('green')
        rect.draw(win)
        
        # 점수 구간 라벨 설정 및 그리기
        # 점수 구간 리스트에서 인덱스 i에 해당하는 구간을 변수 labelText에 저장한다.
        labelText = range_list[i]
        label = Text(Point(i + barWidth / 2, -2), labelText) # x좌표 막대 중앙, y좌표 -2
        label.setSize(8) # X축 라벨 글자크기
        label.draw(win)
        
        # 막대 상단의 count 표시 설정 및 그리기
        countLabel = Text(Point(i + barWidth / 2, count + 1), str(count)) # x좌표 막대 중앙, y좌표 막대 상단 +1
        countLabel.setSize(8)
        countLabel.draw(win)
    
    # 터미널 메시지 출력
    print("Click anywhere in the window to close.")
    
    # 사용자가 창을 클릭하면 창 종료
    win.getMouse()
    win.close()

# 프로그램 설명에서 제공된 데이터를 기반으로 히스토그램 생성
range_list = ['0-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49',
              '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80-84', '85-89', '90-94', '95-100']
part = [42, 18, 21, 23, 33, 25, 30, 29, 27, 26, 12, 15, 6, 17, 8, 1, 4, 1, 1, 1]

createHistogram(range_list, part)
