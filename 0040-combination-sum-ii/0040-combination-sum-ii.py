class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        result = []
        current = []

        def backtrack(start, remaining):

            if remaining == 0:
                result.append(current.copy())
                return

            if remaining < 0:
                return

            for i in range(start, len(candidates)):

                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                current.append(candidates[i])

                backtrack(i+1, remaining - candidates[i])

                current.pop()

        backtrack(0, target)

        return result