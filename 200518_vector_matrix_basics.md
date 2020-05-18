# 200518_ Vector, Matrix의 표현

시작하기에 앞서, 2주 정도 경황이 전혀 없었음을 밝힌다.

반쯤 차였고, 반쯤 깨진 여자 사람과의 문제에 멘탈이 날라갔었다.

다시 공부하는 습관을 조금씩 들이고 다시하려고 한다.

그런 의미로 오늘은 짧게라도 한다.

참고도서 : 밑바닥부터 시작하는 데이터과학 2E 4장

python으로 어떻게, 벡터와 행렬을 표현할 수 있을지 정리하고자 한다.



## 벡터

선형대수에서 정의되는 벡터를 표현하기 위한 가장 좋은 자료형은 당연히 List.

float 객체를 가지고 있는 리스트로 표현을 하려고 한다.

추가로, 새로 맞이한 코드의 기능을 추가로 정리한다.



```python
from typing import List

Vector = List[float]

height_weight_age = [70,
                    170,
                    40]
grades = [95,
         80,
         75,
         62]

# 벡터의 덧셈 : 성분합으로 정의하니까
def add(v: Vector, w: Vector) -> Vector:  # 타입 명시 표현
    assert len(v) == len(w), "vectors must be the same length"
    #assert는 좌측의 조건이 충족되지 않았을 경우 출력하는 방식이다.
    
    return [v_i + w_i for v_i, w_i inn zip(v,w)]

# 벡터의 스칼라배
def scalar_multiply(c: float, v: Vector) -> Vector:
    return [c * v_i for v_i in v]

# 벡터의 내적
def dot(v: Vector, w: Vector) -> float:
    assert len(v) == len(w), "vectors must be the same length"
    
    return sum(v_i*w_i for v_i, w_i in zip(v,w))
    #zip은 리스트를 같은 성분끼리 묶어주는 역할을 한다. 따라서 저리씀

# 벡터의 크기
def sum_of_squares(v: Vector) -> float:
    return dot(v,v)  # 제곱합부터 정의하고
def magnitude(v : Vector) -> float:
    return math.sqrt(sum_of_squares(v))  # import math 필요

# 두 벡터간의 거리
def distance(v: Vector, w: Vector) -> float:
    return magnitude(subtract(v, w))
```



## 행렬

이번장의 내용은 행렬을 표현하는 법만 담겨있다. 이를 정리한다.

A라는 행렬에서 `A[i][j]`는 i번째 행과 j번째 열에 속한 숫자를 의미한다.



형태에 맞는 행렬을 생성하고, 각 원소를 채워넣는 함수를 다음과 같이 구현한다.

```python
# 타입 명시를 위한 별칭 부여
Matrix = List[List[float]]
from typing import Callable

def make_matrix(num_rows: int,
               num_cols: int,
               entry_fn: Callable[[int, int], float]) -> Matrix:
    return [[entry_fn(i,j)
           for j in range(num_cols)]
            for i in range(num_rows)] 
    
```

