# 200520 통계기초(2)

오늘도 보던 내용을 이어간다.



## 정규분포와 표준정규분포

정규분포는 평균과, 표준편차의 두 파라미터로 정의. 평균은 중심점, 표준편차는 종 모양 그래프의 폭 표현.

그 중 표준정규분포는 평균이 0, 표준편차가 1인 정규분포를 의미. 표준화 공식 등은 잊지 말자.

```python
import math
SQRT_TWO_PI = math.sqrt(2 * math.pi)

# 정규분포, 정규분포의 밀도 함수를 그대로 표현
def normal_pdf(x: float, mu: float - 0, sigma: float = 1) -> float:
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (SQRT_TWO_PI * sigma))
# 표준 정규 분포는 값을 그대로 넣으면 그만이므로..
```



## 이항분포

성공률이 p인 사건을 n번 시행할 때 성공률에 대한 분포는 이항분포  B(n, p)로 표기한다.

B(n,p)에서 n이 커지면 정규분포가 되는것을 **중심극한정리**라고 한다.

베르누이 분포를 그래프로 표현하고, 근사된 정규분포 또한 그림으로 그리는 코드를 확인하자.

```python
def bernoulli_trial(p: float) -> int:
    return 1 if random.random() < p else 0

def binomial(n: int, p: float) -> int:
    return sum(bernoulli_trial(p) for _ in range(n))

#히스토그램 표현시간
from collections import Counter
def binomial_histogram(p: float, n: int, num_points: int) -> None:
    data = [binomial(n, p) for _ in range(num_points)]
    
    #이항분포 표본 그리기
    histogram = Counter(data)
    plt.bar([x-0.4 for x in histogram.keys()],
           [v / num_points for v in histogram.values()],
           0.8,
           color='0.75')
    
    mu = p*n
    sigma = math.sqrt(n*p*(1-p))
    
    # 근사된 정규분포 라인으로 그리기
    xs = range(min(data), max(data)+1)
    ys = [normal_cdf(i+0.5, mu, sigma)-normal_cdf(i-0.5, mu, sigma)
         for i in xs]
    plt.plot(xs, ys)
    plt.title("Binomial Distribution vs Normal Approximation")
    plt.show()
```

