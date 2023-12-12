# 전역함수
def menu():
    print("==== 학생관리 프로그램 ====")
    print("1.신규 학생 등록")
    print("2.학생 정보 조회")
    print("3.전체 학생 조회")
    print("4.프로그램 종료")
    

# 전역변수
stuList = []

# 학생정보를 관리할 클래스 선언
class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        
    def get_tot(self):
        return self.kor + self.eng + self.math
    
    def get_avg(self):
        return self.get_tot()/3
    
    def disp(self):
        print(f"{self.name}\t{self.get_tot()}\t{self.get_avg()}")
        
# 실행파일
def main():
    print()
    
    while True:        
        menu()
        ch = int(input("메뉴 = "))
        
        if ch == 1:
            name = input("이름 = ")
            kor = int(input("국어 = "))
            eng = int(input("영어 = "))
            math = int(input("수학 = "))
            stu = Student(name, kor, eng, math)
            stuList.append(stu)
            print("학생 등록이 완료되었습니다.")
            
        elif ch == 2:
            print("== 학생정보 조회 ==")
            print("[1]학번  [2]이름  [3]뒤로")
            a = int(input("메뉴 = "))
            if a == 1:
                pass
            elif a == 2:
                pass
            elif a == 3:
                continue
            else:
                print("메뉴의 선택이 올바르지 않습니다.")
        elif ch == 3:
            pass
        elif ch == 4:
            print("\n프로그램을 종료합니다.")
            break
        else:
            print("메뉴의 선택이 올바르지 않습니다.")
            
            
# 진입점
if __name__ == '__main__':
    main()
        
        
        
        
        
        
        