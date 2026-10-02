class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m = len(s)
        n = len(p)

        # dp[i][j] means:
        # Does s[:i] match p[:j]?
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Empty string matches empty pattern
        dp[0][0] = True

        # When s is empty, only '*' can match it
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 1]

        # Fill the table
        for i in range(1, m + 1):
            for j in range(1, n + 1):

                # Normal character or '?'
                if s[i - 1] == p[j - 1] or p[j - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]

                # '*'
                elif p[j - 1] == "*":
                    # '*' matches zero characters
                    # OR
                    # '*' matches one more character
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

                # Otherwise it stays False

        return dp[m][n]