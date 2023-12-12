## 완전 검색(Exhaustive Search)

- 문제의 해법으로 생각할 수 있는 모든 경우의 수를 나열해보고 확인하는 기법
- Brute-force 또는 Generate-and-Test 기법이라고도 불림
- 수행속도는 느리지만 해답을 찾아내지 못할 확률이 작다.
- 보통 완전 검색으로 접근하여 해답도출
- 그리고나서 성능 개선을 위한 다른 알고리즘을 사용해서 해답확인

ex) Baby-gin 게임
- 0~9 사이의 숫자 카드에서 임의이 카드 6장을 뽑았을 때, 3장의 카드가 연속적인 번호를
  갖는 경우를 run이라고 하고, 3장의 카드가 동일한 번호를 갖는 경우를 triplete이라고 함
  6장의 카드가 run과 triplete로만 구성된 경우를 Baby-gin으로 부름
  
- 667767 666,777 2triplete Baby-gin
- 054060 456,000 1run1triplete Baby-gin
- 101123 123,011 1run not Baby-gin

### 순열(Permutation)
- 서로 다른 것들 중 몇 개를 뽑아서 한 줄로 나열하는 것
- 서로 다른 n개 중 r개를 택하는 순열은 아래와 같이 표현
  nPr
- nPr은 다음과 같은 식이 성립
  nPr = n * (n-1) * (n-2) * ... * (n-r+1)
- nPn = n!이라고 표기하며 Factorial이라 부름

ex) {1,2,3} 을 포함하는 모든 순열을 생성하는 함수
```python
for i1 in range(1,4):
  for i2 in range(1,4):
    if i2 != i1:
      for i3 in range(1,4):
        if i3 != i1 and i3 != i2:
          print(i1,i2,i3)
```
