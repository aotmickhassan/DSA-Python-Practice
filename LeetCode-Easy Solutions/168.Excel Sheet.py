# Input: columnNumber = 701
# Output: "ZY"

from math import remainder
from unittest import result


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""

        while columnNumber > 0:
            offset = (columnNumber - 1) % 26
            result += chr(ord("A") + offset)
            columnNumber = (columnNumber - 1) // 26

        return result[::-1]
