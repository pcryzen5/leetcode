class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):

                product = int(num1[i]) * int(num2[j])

                position = i + j + 1

                result[position] += product

                result[position - 1] += result[position] // 10
                result[position] %= 10

        # Remove leading zeros
        while len(result) > 1 and result[0] == 0:
            result.pop(0)

        return ''.join(map(str, result))