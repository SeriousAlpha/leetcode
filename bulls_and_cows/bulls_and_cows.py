class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        s = []
        g = []
        l = len(secret)
        a = 0
        b = 0
        for i in range(l):
            if guess[i] == secret[i]:
                a += 1
            else:
                s.append(secret[i])
                g.append(guess[i])

        for j in range(len(g)):
            if g[j] in s:
                b += 1
                s.remove(g[j])

        a = str(a)
        b = str(b)
        hint = a + 'A' + b + 'B'
        return hint

c = Solution()
h = c.getHint('1807', '7810')
print h