import math

from utilities.DBFS import DBFS


class Converter:
    def __init__(self):
        pass

    @staticmethod
    def linear_to_dbfs_bits(value,bit_depth):
        valueDBFS = 20 * math.log10(abs(value)/bit_depth)
        sign = 1
        if value < 0:
            sign = -1

        return DBFS(valueDBFS, sign)

    @staticmethod
    def linear_to_dbfs(value):
        return Converter.linear_to_dbfs_bits(value,1)
