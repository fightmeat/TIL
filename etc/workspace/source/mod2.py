PI = 3.141592

class Math:
    def solv(self, r):
        return PI * ( r ** 2)
    
    def sum(a, b):
        return a + b
    
print("Math 모듈이 로딩되었습니다.")

if __name__ == "__main__":
    print(PI)
    a = Math()
    print(a.solv(2))
    print(sum(PI, 4.2))