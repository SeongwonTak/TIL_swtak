# heap 구현 코드
# https://www.fun-coding.org/Chapter11-heap.html
# 주석을 달면서 이해해보았다. 그래도 너무 어렵다.
class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)  # 인덱스 번호는 1번부터
        self.heap_array.append(data)  # 최초의 루트 노드 설정

    def move_down(self, popped_idx):
        left_child_popped_idx = popped_idx * 2
        right_child_popped_idx = popped_idx * 2 + 1
        if left_child_popped_idx >= len(self.heap_array):
            return False
        elif right_child_popped_idx >= len(self.heap_array):
            if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                return True
            else:
                return False
        else:
            if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
                    return True
                else:
                    return False

    def pop(self):
        if len(self.heap_array) <= 1:  # 더 뺄게 없음
            return None

        returned_data = self.heap_array[1]  # 루트를 제외하고
        self.heap_array[1] = self.heap_array[-1]  # 가장 마지막게 올라옴
        del self.heap_array[-1]
        popped_idx = 1

        while self.move_down(popped_idx):
            left_child_popped_idx = popped_idx * 2
            right_child_popped_idx = popped_idx * 2 + 1
            if right_child_popped_idx >= len(self.heap_array):
                self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[
                                                                                          left_child_popped_idx], \
                                                                                      self.heap_array[popped_idx]
                poppoed_idx = left_child_popped_idx
            else:
                if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                    self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[
                                                                                              left_child_popped_idx], \
                                                                                          self.heap_array[popped_idx]
                    poppoed_idx = left_child_popped_idx
                else:
                    self.heap_array[popped_idx], self.heap_array[right_child_popped_idx] = self.heap_array[
                                                                                               right_child_popped_idx], \
                                                                                           self.heap_array[popped_idx]
                    poppoed_idx = right_child_popped_idx

        return returned_data

    def move_up(self, inserted_idx):
        if inserted_idx <= 1:
            return False
        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

    def insert(self, data):
        if len(self.heap_array) == 1:
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)
        inserted_idx = len(self.heap_array) - 1

        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[
                inserted_idx]
            inserted_idx = parent_idx
        return True