import math

from utilities.DBFS import DBFS


class Converter:
    def __init__(self):
        pass

    def linear_to_dbfs_bits(self,value,bit_depth):
        valueDBFS = 20 * math.log10(abs(value)/bit_depth)
        sign = 1
        if valueDBFS < 0:
            sign = -1

        return DBFS(valueDBFS, sign)

    def linear_to_dbfs(self,value):
        return self.linear_to_dbfs_bits(value,1)
