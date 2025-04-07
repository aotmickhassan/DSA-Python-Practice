class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.arr[self.size]

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_array = [0] * self.capacity

        for i in range(self.size):
            new_array[i] = self.arr[i]
        self.arr = new_array

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity


# # Dynamic Array implementation
# # Note: Python lists are dynamic arrays by default,
# # but this is an example of what's going on under the hood.
# class DynamicArray:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.length = 0
#         self.arr = [0] * self.capacity

#     # Get value at i-th index
#     def get(self, i: int) -> int:
#         return self.arr[i]

#     # Set n at i-th index
#     def set(self, i: int, n: int) -> None:
#         self.arr[i] = n

#     # Insert n in the last position of the array
#     def pushback(self, n: int) -> None:
#         if self.length == self.capacity:
#             self.resize()

#         # insert at next empty position
#         self.arr[self.length] = n
#         self.length += 1

#     # Remove the last element in the array
#     def popback(self) -> int:
#         if self.length > 0:
#             # soft delete the last element
#             self.length -= 1
#         # return the popped element
#         return self.arr[self.length]

#     def resize(self) -> None:
#         # Create new array of double capacity
#         self.capacity = 2 * self.capacity
#         new_arr = [0] * self.capacity

#         # Copy elements to new_arr
#         for i in range(self.length):
#             new_arr[i] = self.arr[i]
#         self.arr = new_arr

#     def getSize(self) -> int:
#         return self.length

#     def getCapacity(self) -> int:
#         return self.capacity
