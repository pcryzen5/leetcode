class Solution:
    def countAndSay(self, n: int) -> str:

        string = "1"

        for i in range(n - 1):

            count = 1
            new_string = ""

            for j in range(len(string)):
                if j + 1 < len(string) and string[j] == string[j + 1]:
                    count += 1

                else:
                    new_string += str(count) + string[j]
                    count = 1


            string = new_string

        return string

