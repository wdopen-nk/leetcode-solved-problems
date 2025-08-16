class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = [[1]]
        for i in range(2, numRows + 1):
            triangle.append([1] + [triangle[-1][j] + triangle[-1][j + 1] for j in range(i - 2)] + [1])
        return triangle

# print(generate(5))