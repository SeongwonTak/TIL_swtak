# 200502 파이썬 몰랐던 내용들 학습

Python 을 쓰면서 늘 헷갈렸거나, 혹은 잘 모르고 넘어갔던 내용들,

혹은 그냥 제대로 모르고 썼던 내용 등등을 공부하고 정리하려고 한다.

참고 : 점프 투 파이썬 위키독스, 파이썬 코딩 도장

## Class

#### 생성자(constructor)

먼저 Class 구조의 기초를 다시 한번 복습.

``` python
class Plus:
    def setdata(self, first, second):  # 객체에 데이터를 저장할 수 있게
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

a = Plus()  # 메서드 호출
a.setdata(4,2)
b.setdata(3,7)

print(a.first)  # 4
print(b.first)  # 3
print(a.first)  # 4 클래스로 만든 객체의 객체변수는 \
# 다른 객체의 객체변수에 상관없이 독립적인 값을 유지한다.
print(a.add())  # 4 + 2 = 6
```

잠깐! 메서드란? 클래스 안에 구현된 함수!

이제 생각해 볼 문제는 다음과 같다.

```python
a = Plus()
a.add()  # setdata를 수행하지 않아, Attribue Error 발생.
```

객체에 초기값을 설정해야 하는 경우, setdata 대신 생성자를 구현하는 것이 좋은 방법.

**생성자(Constructor)란 객체가 생성될 때 자동으로 호출되는 메서드를 의미한다.**

```python
class Minus:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def minus(self):
        result = self.first - self.second
        return result

a = Minus()  # __init__이 호출되면서 first, second에 값 전달 X. 오류.
b = Minus(3, 5)  # 이러면 first = 3, second = 5
```



## 상속과 오버라이딩

#### 상속(Inheritance)

하나의 클래스를 만들 때, 다른 기존 클래스의 기능을 물려받도록 해준다.

```python
class MinDiv(Minus):  # 상속을 실시시 괄호 안에 상속할 애를 넣음
    def div(self):
        return self.first / self.second
    
a = MinDiv(10, 5)
a.minus()  # 10 - 5 = 5
a.div()  # 10 // 5 = 2
```

###### 상속을 왜 해야 할까?

상속은 기존 클래스를 변경하지 않고 기능을 추가하거나, 기존 기능을 변경(!) 할 때 사용한다. 기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않을 경우 상속을 사용해야만 한다.



아무튼 위의 코드는 무언가 이상하다. **0으로 나눌 수 없는데..**? div를 수정하면 된다고는 하지만...  위의 질문의 답처럼, 수정을 할 수 없다면?  이에 대한 해결책이 바로 **메서드 오버라이딩** 이다.



#### 메서드 오버라이딩(Method Overriding)

오버라이딩은 덮어쓰기를 의미한다. 부모 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것을 의미한다. 이 경우, 부모클래스 메서드 대신 오버라이딩한 메서드가 호출된다. 예시 코드는 다음과 같다.

```python
class SafeMinDiv(MinDiv):  # 위에서 작성한 것을 상속시켜오자
    def div(self):  # div를 재작성 할거다.
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = SafeMinDiv(3, 0)
b = MinDiv(5, 0)
a.div()  # 오버라이딩을 해놓은 결과로 0
b.div()  # Error! 0으로 나눌 수 없다.
```



## 모듈

모듈의 기본 내용부터 재복습.

```python
# mod.py
PI = 3.14

class CircleArea:
    def Area(self, r):
        return PI * (r ** 2)
    
def add(a, b):
    return a + b


# 실행결과
import mod
print(mod.PI)  # 3.14
a = mod.CircleArea()
print(a.Area(10))  # 314
print(mod.add(mod.PI, 5))  # 8.14

```



##  `if __name__ == "__main__"`의 의미

결론부터 정리하면, `__name__`의 의미는 모듈의 이름이 저장되는 변수이다.

어떤 스크립트 파일이던, 파이썬 인터프리터가 최초로 실행한 스크립트 파일의 `__name__`에는 `__main__`이 들어간다. 예시를 통해 이해해보자.

```python
# add.py
def add(a,b):
    return a + b

if __name__ == "__main__":
    print(add(9, 99))
```

위와 같은 상황이다. 우선은 add.py를 실행하면, 프로그램의 시작점이기에, 하단의 if문이 만족되어 108이라는 결과값이 print된다.

하지만 `import add`를 실시했을 경우, 하단의 if문이 만족되지 않아, 108이 출력되지 않는다. 



## 내장함수  map

그동안 여러 BOJ 문제를 풀면서 아무생각없이 `list(map(int, input().split()))` 해왔는데 이 구문에 대한 의미를 정확하게 정리하자.

 먼저 `map(f, interable)`은 함수와 반복 가능한 자료형을 입력으로 받는다. map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려준다. 즉 다시말해, 자료형에 있는 모든 요소에 f를 각각 모두 적용시켜주는 함수이다.

기본적으로 input()으로 받으면 문자열 형태로 지정이되는데, int(input()) 과정을 통해서 입력한 값을 정수 변수로 저장해버린다.

따라서 `list(map(int, input().split()))`의 진짜 의미는 

- 공백으로 구분될 수 있는 입력으로 들어온 각 요소를
- 정수형으로 변환해서
- 각 구분된 요소마다 list의 한 칸씩 넣어준다.

가 된다.

다른 예시를 들면 다음과 같다.

```python
def nine_times(x):
    return x * 9

list(map(nine_times, [1, 11, 111, 1111]))
# 출력결과는 [9, 99, 999. 9999]
```



## 람다 표현식(lambda expression)

###### 기초사항

람다 표현식은 이름이 없는 함수를 만든다. 따라서 람다 표현식을 anonymous function이라고 부르기도 한다. 람다 표현식은 다음과 같이 지정하고 사용한다.

```python
lambda x: x + 10
# 이 상태로 실행할 경우 함수를 호출할 수 없다.

plus_ten = lambda x: x + 10
plus_ten(9)  # 19

(lambda y : y * 7)(5)  # 35, 이런식으로 한번에 호출도 가능하다.
```

주의사항 하나는, **람다 표현식 안에서는 변수를 만들 수 없다. **예시는 다음과 같다.**

```python
(lambda x: y = 9; x + y)(9)
# 람다 표현식 안에서는 변수 선언이 불가. 즉 syntax error 발생

z = 10
(lambda w : w - z)(25)  # 15
# 단, 람다 표현식 바깥에 있는 변수는 사용 가능하다.
```

람다 표현식은 함수의 인수 부분에서 간단하게 함수를 만들기 위해 사용한다.

```python
list(map(lambda z : z * 9, [1, 11, 111, 1111]))
```

위의 9배 만드는 예제, nine_times 같은 경우는 함수를 직접 사용했는데 상단과 같은 방법 편리한 방법도 가능하다.



###### lambda와 조건부 표현식

기본 구문은 다음과 같다.

* lambda 매개변수들: 식1 if 조건식 else 식 2

```python
a = [1, 2, 3, 4, 5, 6]
list(map(lambda x: str(x) if x % 3 == 0 else x, a))

# 출력결과
[1, 2, '3', 4, 5, '6']
```

3의 배수일때는 문자열로 만들어서 변환이 되고, 아닐 때는 그대로 된다.

식1은 조건식이 참 일때, 식2는 조건식이 거짓일때 사용하게 된다.



**주의사항!** if를 사용시 else는 반드시 사용해야 하며 elif는 사용할 수 없다.



###### lambda와 filter함수, reduce 함수

먼저 filter함수는 

* filter(함수, 반복 가능한 객체)

로 정의되며, 특정 조건에 맞는 요소만 가져오게 한다. 함수가 들어가므로 lambda를 또 쓸 수 있다. 예시는 다음과 같다.

```python
a = [6, 10, 5, 9, 2, 4]
list(filter(lambda x : x > 5 and x < 10, a))

# 출력결과
[6, 9]
```

다음 reduce함수는 python3에서는 **내장함수가 아님에 주의**하자.

이 함수는 반복 가능한 객체의 각 요소를 지정된 함수로 처리한 뒤 **이전 결과에 누적해서 변환한다.**

* from functools import reduce

* reduce(함수, 반복가능한 객체)

  

역시 lambda와 결합해서 사용가능하다.

```python
a = [3, 5, 10, 12]
from functools import reduce
reduce(lambda x, y : x * y, a)

# 출력결과
1800  # 3 * 5 * 10 * 12
```



다음번에는 이터레이터와 제너레이터에 대해 정리하고자 한다.