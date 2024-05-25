import math

class ReadFile:
    def __init__(self, inputFile):
        """
        ReadFile 클래스의 생성자.
        
        인스턴스 변수:
        - inputFile: 입력 파일의 이름을 저장하는 변수
        - numList: 파일에서 읽은 양의 정수들로 이루어진 리스트 (초기값: 빈 리스트)
        """
        self.inputFile = inputFile
        self.numList = []

    def readNum(self):
        """
        파일에서 양의 정수만 읽어 numList 리스트에 추가하는 함수.

        Return:
        - numList: 파일에서 읽은 양의 정수들의 리스트
        """
        try:
            with open(self.inputFile, 'r') as file:
                for line in file:
                    try:
                        num = int(line.strip())
                        if num > 0:
                            self.numList.append(num)
                    except ValueError:
                        print(f"Warning: Skipping non-integer value in line: {line.strip()}")
        except FileNotFoundError:
            print(f"Error: The file '{self.inputFile}' was not found.")
        
        return self.numList

class Operate:
    def __init__(self, numList):
        """
        Operate 클래스의 생성자.

        인스턴스 변수:
        - inputList: numList 리스트를 저장하는 변수
        """
        self.inputList = numList

    def sumUnique(self):
        uniqueList=list(set(self.inputList))
        uniqueSum=sum(uniqueList)
        return uniqueSum

    def avgNum(self):
        """
        리스트 내 숫자들의 평균을 구하는 함수.

        Return:
        - average: 리스트 내 숫자들의 평균
        """
        if not self.inputList:
            return 0
        average = sum(self.inputList) / len(self.inputList)
        return average

    def varNum(self):
        """
        리스트 내 숫자들의 분산을 구하는 함수.

        Return:
        - variance: 리스트 내 숫자들의 분산
        """
        if not self.inputList:
            return 0
        mean = self.avgNum()
        variance = sum((x - mean) ** 2 for x in self.inputList) / len(self.inputList)
        return variance

    def stdNum(self):
        """
        리스트 내 숫자들의 표준편차를 구하는 함수.

        Return:
        - std_dev: 리스트 내 숫자들의 표준편차
        """
        variance = self.varNum()
        std_dev = math.sqrt(variance)
        return std_dev

    def writeToFile(self, average, variance, std_dev):
        """
        파일에 평균, 분산, 표준편차 값을 작성하는 함수.

        매개변수:
        - average: 평균
        - variance: 분산
        - std_dev: 표준편차
        """
        with open("result.txt", 'w') as file:
            file.write(f"Average: {average:.2f}\n")
            file.write(f"Variance: {variance:.2f}\n")
            file.write(f"Standard Deviation: {std_dev:.2f}\n")

def main():
    # ReadFile 클래스에 대한 객체 reader 를 생성한다.
    reader = ReadFile("test2.txt")
    
    # reader 에서 받아 오는 숫자 리스트를 numbers 에 저장한다.
    numbers = reader.readNum()
    
    # Operate 클래스에 대해 numbers 를 인자로 하는 객체 calculator 를 생성한다.
    calculator = Operate(numbers)
    
    # calculator 를 통해 평균, 분산, 표준편차 값을 구한다.
    average = calculator.avgNum()
    variance = calculator.varNum()
    std_dev = calculator.stdNum()
    
    unique = calculator.sumUnique()
    print(f"unique: {unique:.2f}")
    # 구한 평균, 분산, 표준편차를 파일에 작성한다.
    calculator.writeToFile(average, variance, std_dev)
    
    # 평균, 분산, 표준편차를 터미널에 출력한다. (단, 소수점 2 번째 자리까지 출력해야 한다.)
    print(f"Average: {average:.2f}")
    print(f"Variance: {variance:.2f}")
    print(f"Standard Deviation: {std_dev:.2f}")

if __name__ == "__main__":
    #module이 import가 아니고 독립으로 실행될 때만 코드 실행
    main()
