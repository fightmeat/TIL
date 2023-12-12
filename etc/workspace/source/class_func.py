class Student:
    # 멤버 필드 : 클래스 변수
    count = 0 # 학생수를 카운팅할 목적으로 사용
    students = []
    
    # 클래스 함수
    @classmethod
    def print(cls):
        print("------- 학생목록 출력 -------")
        print("이름", "총점", "평균", sep="\t")
        for student in cls.students:
            print(str(student)) 
        print("------- ----------- -------")
        
    # 생성자 메서드
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math        
        
    # 멤버 메서드 : getter(get), setter(set)
    ## 총점을 계산하여 반환하는 메서드
    def get_sum(self):
        return self.kor + self.eng + self.math
    
    ## 평균을 계산하여 반환하는 메서드
    def get_average(self):
        return self.get_sum() / 3
    
    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())    
    
    
# 학생 리스트 선언
Student('aaa', 88, 97, 65) 
Student('bbb', 92, 94, 90) 
Student('ccc', 85, 88, 84) 
Student('ddd', 79, 89, 88) 
Student('eee', 80, 76, 92)    

# 현재 생성된 학생 출력
Student.print()    