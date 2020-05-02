# 200420_데이터베이스

정보처리기사 공부는 오늘도 계속됩니다.

4/25일(토) 시험 대비, 오늘은 3과목 파트 내용을 요약합니다.

3과목 양이 좀 많습니다....

- 코드 보다는 내용/개념 정리에 핵심을 뒀습니다.



## 데이터베이스의 설계와 데이터 모델

#### 데이터 베이스 설계의 개념

###### 데이터 베이스 설계의 순서

요구 조건 분석 -> 개념적 설계 -> 논리적 설계 -> 물리적 설계 -> 구현



###### 개념적 설계

- 현실 세계에 대한 인식을 추상적 개념으로 표현
  -> 개념 스키마 모델링, 트랜잭션 모델링 병행 수행
- E-R 다이어그램 작성

###### 논리적 설계(데이터 모델링)

+ 현실 세계에서 발생하는 자료를 컴퓨터가 이해하고 처리할 수 있는 물리적 저장장치에 저장할 수 있도록 변환하기 위해 특정 DBMS가 지원하는 논리적 자료 구조로 변환하는 과정
+ 트랜잭션의 인터페이스 설계
+ 관계형 데이터베이스의 경우 테이블을 설계

###### 물리적 설계 (데이터 구조화)

- 데이터베이스 파일의 저장 구조, 액세스 경로 설정
- 데이터가 컴퓨터에 저장되는 방법 묘사



#### 데이터 모델의 구성 요소

###### 데이터 모델의 개념

현실 세계의 정보들을 컴퓨터로 표현하기 위하여 단순화, 추상화하여 체계적으로 표현한 개념적 모형

구성요소 : 개체, 속성, 관계

모델종류 : 개념적 데이터모델, 논리적 데이터 모델, 물리적 데이터 모델



###### 개체(Entity)

데이터베이스에 표현하려는 것, 파일 시스템의 레코드에 대응

**개체의 구성요소**

- 속성 : 개체가 가지고 있는 특성

- 개체타입 : 속송으로만 기술된 개체의 정의

- 개체 인스턴스 : 개체를 구성하는 각 속성들의 값을 가짐 -> 하나의 개체를 나타냄

- 개체 세트 : 개체 인스턴스의 집합



###### 속성(Attribute)

**데이터베이스를 구성하는 가장 작은 논리적 단위**로 개체의 특성을 기술한다.

속성의 수를 Degree, 차수라고 한다.



###### 관계(Relationship)

개체와 개체 사이의 논리적인 연결을 의미

**관계의 형태** : 1:1, 1:N, N:M

**관계의 종류**

- 종속 관계 
- 중복 관계
- 재귀 관계
- 배타 관계



## 식별자(Identifier)

식별자는 하나의 개체 내에서 각각의 인스턴스를 유일하게 구분할 수 있는 구분자



###### 주 식별자 vs 보조 식별자

**주 식별자** : 개체를 대표하는 유일한 식별자, 한 개만 존재

**보조 식별자** : 주 식별자를 대신하여 개체를 식별할 수 있는 속성, 한 개 이상 존재



###### 내부 식별자 vs 외부 식별자

**내부 식별자** : 개체 내에서 스스로 만들어지는 식별자

**외부 식별자** : 다른 개체와의 관계에 의해 외부 개체 식별자를 가져와 사용



###### 단일 식별자 vs 복합 식별자

**단일 식별자** : 주 식별자가 한 가지 속성으로만

**복합 식별자** : 주 식별자가 두개 이상의 속성



###### 후보 식별자

후보 식별자는 개체에서 각 인스턴스를 유일하게 식별할 수 있는 속성 또는 속성 집합을 의미

**후보 식별자의 조건**

- 각 인스턴스를 유일하게 식별할 수 있어야 한다
- 속성들을 직접 식별할 수 있어야 한다
- 널 값이 될 수 없다
- 후보 식별자의 데이터는 자주 변경되지 않아야 한다.
- 속성 집합은 후보 식별자로 지정한 경우 개념적으로 유일해야 한다



## E-R (개체-관계) 모델

#### 개요

개체와 개체간의 관계를 기본 요소로 이용하여 표현, 데이터를 개체 / 관계 / 속성으로 묘사



###### 피터 첸 표기법

사각형 : 개체 타입

마름모 : 관계 타입

타원 : 속성

이중타원 : 다중값 속성

밑줄 타원 : 기본키 속성

복수 타원 : 복합 속성

관계 : 1:1, 1:N, N:M 대응 수를 위에 기록

선, 링크 : 개체타입, 속성 연결





## 관계형 데이터베이스

관계형 데이터베이스는 가장 널리 사용되는 데이터 모델로, 2차원적인 표를 사용하여 데이터 상호관계를 정의.

- 테이블들을 하나의 DB로 묶어서 속성간의 관계나 테이블 간의 관계 설정
- 기본키와 이를 참조하는 외래키로 데이터 관계를 표현
- SQL



#### 관계형 데이터베이스의 구조

###### 튜플

- 튜플은 릴레이션을 구성하는 각 행을 의미
- 속성의 모임으로 구성
- 파일 구조에서 레코드와 같은 의미
- 튜플의 수를 카디널리티라고 한다.

###### 속성

- 데이터베이스를 구성하는 가장 작은 논리적 단위
- 개체의 특성을 기술
- 파일 구조상의 데이터 항목 / 필드
- 속성의 수를 디그리 또는 차수 라고 한다.

###### 도메인

- 하나의 속성이 취할 수 있는 같은 타입의 원자 값
  ex) 성별 : 남 / 녀



#### 관계형 데이터베이스의 제약 조건(키, 무결성)

##### 키(Key)

###### 후보키, 기본키, 대체키 : 위와 동일

###### 슈퍼키

한 릴레이션에 내에 있는 속성들의 집합으로 구성된 키

###### 외래키

다른 릴레이션의 기본키를 참조하는 속성 / 속성들의 집합



##### 무결성(Integrity)

무결성이란 **데이터베이스에 저장된 데이터 값과 그것이 표현하는 현실 세계의 값이 일치하는 정확성 의미**

###### 개체 무결성(Entity Integrity)

기본 테이블의 기본키를 구성하는 어떤 속성도 Null값이나 중복값을 가질 수 없다.

###### 도메인 무결성(Domain Integrity)

주어진 속성 값이 정의된 도메인에 속한 값이어야 한다.

###### 참조 무결성(Referential Integrity)

외래키 값은 Null이거나 참조 릴레이션의 기본키 값과 동일해야 한다.



## 정규화(Normalization)

정규화란, 함수의 종속성 등의 종속성 이론을 이용하여 잘못 설계된 관계형 스키마를 더 작은 속성의 세트로 쪼개어 바람직한 스키마로 만들어 가는 과정

-> 정규화된 데이터 모델은 일관성, 정확성, 단순성, 비중복성, 안정성 보장



#### 이상(Anormaly)의 개념 및 종류

정규화를 거치지 않으면 데이터베이스 내에 데이터들이 불필요하게 중복되어 릴레이션 조작 시 예기치 못한 곤란한 현상이 발생.

삽입 이상 : 의도와 상관없이 원하지 않는 값도 같이 삽입

삭제 이상 : 의도와 상관없는 값들도 함께 삭제되는 연쇄가 일어남

갱신 이상 : 속성값 갱신할 때 일부 튜플의 정보만 갱신, 정보에 모순



#### 정규화의 과정

|                       비정규 릴레이션                        |
| :----------------------------------------------------------: |
|          도메인이 원자값,  즉 모든 속성값 = 원자값           |
|                           **1NF**                            |
| 부분적 함수 종속 제거, 즉 모든 속성이 기본키에 대하여 완전 함수적 종속 |
|                           **2NF**                            |
|                    이행적 함수 종속 제거                     |
|                           **3NF**                            |
|              결정자이면서 후보키가 아닌 것 제거              |
|                           **BCNF**                           |
|                        다치 종속 만족                        |
|                           **4NF**                            |
|                       조인 종속성 만족                       |
|                           **5NF**                            |





## 물리 데이터 베이스 설계 - 트랜잭션, 인덱스, 뷰

#### 트랜잭션

###### 트랜잭션이란?

트랜잭션은 데이터 베이스의 상태를 변환시키는 하나의 논리적 기능을 수행하기 위한 작업의 단위 또는 한꺼번에 모두 수행되어야 할 일련의 연산들을 의미



###### 트랜잭션의 특성

원자성(Atomicity) : 트랜잭션의 연산은 데이터에 모두 반영되도록 하거나, 전혀 반영되지 않도록

일관성(Consistency) : 트랜잭션이 그 실행을 성공적으로 완료하면 언제나 일관성 있는 데이터베이스 상태로 변환

독립성(Isolation) : 둘 이상의 트랜잭션이 동시 병행 실행 시 어느 하나의 트랜잭션 실행 중에 다른 트랜잭션의 연산이 끼어들 수 없다.

지속성(Durability) : 성공적으로 완료된 트랜잭션의 결과는 시스템이 고장나더라도 영구적으로 반영



###### CRUD 분석

C(Create), R(Read), U(Update), D(Delete)

CRUD 매트릭스를 통해 분석. (C>D>U>R 우선순위로)



#### 인덱스

인덱스는 데이터 레코드를 빠르게 접근하기 위해 <키 값, 포인터>의 쌍으로 구성



#### 뷰

사용자에게 접근이 허용된 자료만들 제한적으로 보여주기 위해, 하나 이상의 기본 테이블로부터 유도된, 이름을 가지는 **가상 테이블**

- 가상 테이블이기에 물리적으로 구현되어 있지 않다
- 논리적 독립성 제공, 사용자의 데이터 관리를 간단하게 해줌
- 독립적인 인덱스를 가질 수 없으며, 뷰의 정의를 바꿀수는 없다.