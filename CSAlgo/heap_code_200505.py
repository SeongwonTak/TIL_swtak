# heap 구현 코드
# https://www.fun-coding.org/Chapter11-heap.html
# 우선, 코드를 긁어왔고, 주석을 달면서 이해해보려고 한다.
# 아직 이 코드를 이해할 수가 없다...
class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)  # 인덱스 번호는 1번부터
        self.heap_array.append(data)  # 최초의 루트 노드 설정

    def move_down(self, popped_idx):
        left_child_popped_idx = popped_idx * 2
        right_child_popped_idx = popped_idx * 2 + 1
        if left_child_popped_idx >= len(self.heap_array):  # 이 코드의 목적을 모르겠음 왜 len을 사용했어?
            return False
        elif right_child_popped_idx >= len(self.heap_array):  # 이 코드도 왜 이렇게 분기가 되어있나. 왜 또 len이야?
            if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                return True
            else:
                return False
        else:
            if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:  # 더 큰게
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:  # 추출된거보다 크면 바꿀꺼
                    return True
                else:
                    return False
            else:
                if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:  # 반대방향
                    return True
                else:
                    return False

    def pop(self):
        if len(self.heap_array) <= 1:  # 더 뺄게 없음
            return None

        returned_data = self.heap_array[1]  # 루트를 제외하고
        self.heap_array[1] = self.heap_array[-1]  # 가장 마지막게 올라옴
        del self.heap_array[-1] # 가장 마지막 칸을 지운다.
        popped_idx = 1 # 인덱스를 설정해야 한다...

        while self.move_down(popped_idx):  # 삭제과정에서 마지막을 루트로 끌고 자리 잡는 과정임
            left_child_popped_idx = popped_idx * 2
            right_child_popped_idx = popped_idx * 2 + 1
            if right_child_popped_idx >= len(self.heap_array):  # 여기도 왜, 대체 len을 쓰는거지..??? 글고 왜 left?
                self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[
                                                                                          left_child_popped_idx], \
                                                                                      self.heap_array[popped_idx]
                popped_idx = left_child_popped_idx
            else:  # 위 조건이 안될때 위 처럼 더 큰애가 밑에 있으면 바꿔주려는 코드
                if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                    self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[
                                                                                              left_child_popped_idx], \
                                                                                          self.heap_array[popped_idx]
                    popped_idx = left_child_popped_idx
                else:
                    self.heap_array[popped_idx], self.heap_array[right_child_popped_idx] = self.heap_array[
                                                                                               right_child_popped_idx], \
                                                                                           self.heap_array[popped_idx]
                    popped_idx = right_child_popped_idx

        return returned_data

    def move_up(self, inserted_idx):  # 이건 삽입을 위해서 위로 가는 코드
        if inserted_idx <= 1:  # 최초는 뭐....
            return False
        parent_idx = inserted_idx // 2  # 부모노드는 절반에 가우스니까
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:  # 부모가 더 작으면 바꿔치기해야함
            return True
        else:
            return False

    def insert(self, data):  # 삽입
        if len(self.heap_array) == 1:   # 최초면 걍 루트에 넣어야함. (0번칸에만 있다는거)
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)
        inserted_idx = len(self.heap_array) - 1  # 가장 마지막에 넣어서

        while self.move_up(inserted_idx):  # 바꿔야 할때 부모랑 바꿔주는 코드, 인덱스도 바꿔준다.
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[
                inserted_idx]
            inserted_idx = parent_idx
        return True
