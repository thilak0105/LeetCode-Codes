class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxx = ""
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                if num[i:i+3] > maxx:
                    maxx = num[i:i+3]
        return maxx