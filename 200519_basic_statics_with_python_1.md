# 200519 통계 기초 구현(1)

수학적으로는 모르는 내용은 아니나, 한번 더 정리할겸, 파이썬에서 기본적으로 어떻게 구현하는지를 한 번 정리한다.

참고 : 밑바닥부터 시작하는 데이터 과학 2편

※ 굳이, Numpy등의 패키지등도 있는데, 이런 식의 공부를 하는 이유는 그 밑바닥에 깔린 가장 기본을 보려는 것이 의도이다. 그런 의미로 책을 고른거기도 하고, 패키지의 활용은 그 다음단계로 본격적인 프로젝트를 하면서 배우는 것이 좋다고 본다.



## 대표값의 구현 : 평균, 중앙값, 분위수, 최빈값

평균은 합계/자료의 수,  중앙값은 당연히 중간값, 분위수는 몇%에 있는 자료를 확인, 최빈값은 가장 많이 등장하는 값이다.  당연히 평균은 이상치 즉, Outlier의 영향을 크게 받을 것이다.

코드를 통해 내용을 확인 및 복습한다.

```python
# 평균의 구현
def mean(xs : List[float]) -> float:
    return sum(xs) / len(xs)

# 중앙값의 구현, 홀수는 중앙 / 짝수는 중앙 2개의 평균.
# 데이터가 정렬되어있음을 가정해야 한다.!
def _median_odd(xs : List[float]) -> float:
    return sorted(xs)[len(xs) // 2]
def _median_even(xs: List[flaot]) -> float:
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs) // 2  # 둘 중 더 큰 값
    return (sorted_xs[hi_midpoint-1] + sorted_xs[hi_midpoint]) / 2
def median(v: List[float]) -> float:
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)

# 사분위수
def quantile(xs: List[float], p:float) -> float:
    p_index = int(p*len(xs))
    return sorted(xs)[p_index]

# 최빈값
def mode(x: List[float]) -> List[float]:
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
           if count == max_count]

```



## 산포도 : 분산과 표준편차

표본분산, 표본표준편차이므로, 자유도인 (n-1)로 나누어 주어야 한다는 사실은 까먹지 말자.

bias에 의해 추정값이 실제보다 작게 되는 것을 보정하기 위함이다.

어제 공부한 내용을 가져올거라 scratch 라는 구문을 사용.

```python
from scratch.linear_algebra import sum_of_squares

def de_mean(xs : List[float]) -> List[float]:
    x_bar = mean(xs)
    return [x-x_bar for x i xs]  # 편차치

def variance(xs : List[float]) -> float:
    assert len(xs) >= 2, "variance requires at least two elements"
    
    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations) / (n-1)  # 분산공식

def standard_deviation(xs: List[float]) -> float:
    return math.sqrt(variance(xs))
```





## 상관관계 : 공분산과 상관계수

먼저, 공분산의 개념부터 정리해보자.

###### 공분산

분산은 하나의 변수가 평균에서 얼마나 멀리 떨어져 있는지를 계산한다면, 공분산은 두 변수가 각각의 평균에서 얼마나 멀리 떨어져 있는지를 살펴본다.
$$
E(X)=a,\ E(Y)=b \\
Cov(X, Y) = E((X-a)(Y-b))
$$ {sigma}
이 공분산은 다음과 같은 특징들을 가지고 있다.  많은 성질이 있겠지만, 간단한 것은 다음과 같다.

- 두 확률변수가 독립이면, 공분산은 0이다.

- $$
  Cov(aX, bY) = ab\ Cov(X,Y)
  $$

  

###### 상관계수

공분산의 경우는, 단위가 입력 변수들의 단위를 곱해서 계산되기 때문에 이해하기가 쉽지 않다. 또한 한 변수만 변할 경우, 공분산 자체는 위의 성질에 의해 그 만큼 변하나 두 변수 간의 관계가 변했다고 보기는 어렵다. 즉, 공분산의 절대적인 값만으로 두 변수의 상관관계를 파악하기 어렵다.

따라서, 공분산을 각각의 표준편촤를 나눠 준 상관관계를 더 자주 살펴볼 수 밖에 없다.



이 상관관계는 단위가 없다! 그리고 항상 -1에서 1 사이의 값을 갖는다.

- -1 : 완벽한 음의 상관관계
- 0 : 상관관계가 없다.
- 1 : 완벽한 양의 상관관계



###### 코드

```python
from scratch.linear_algebra import dot

# 공분산의 구현, 정의대로 구현하면 된다.
def covariance(xs: List[float], ys: List[float]) -> float:
    assert len(xs) == len(ys), "xs and ys must have same number of elements"
    
    return dot(de_mean(xs), de_mean(ys)) / len((xs)-1)

# 상관계수의 구현
def correlation(xs: List[float], ys: List[float]) -> float:
    stdev_x = standard_deviations(xs)
    stdev_y = standard_deviations(ys)
    
    if stdex_x>0 ans stdev_y>0:
        return covariance(xs, ys) / (stdev_x * stdev_y)
    else:
        return 0  # 편차가 존재하지 않을 경우 상관관계는 0이다.
```

