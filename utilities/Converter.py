import math

from utilities.DBFS import DBFS


class Converter:
    def __init__(self):
        pass

    @staticmethod
    def linear_to_dbfs_bits(value,bit_depth):
        valueDBFS = 20 * math.log10(abs(value)/pow(2,bit_depth-1))
        sign = 1
        if value < 0:
            sign = -1

        return DBFS(valueDBFS, sign)

    @staticmethod
    def linear_to_dbfs(value):
        return Converter.linear_to_dbfs_bits(value,1)

    @staticmethod
    def dbfs_to_linear(dbfs):
        return Converter.dbfs_to_linear_bits(dbfs, 1)

    @staticmethod
    def dbfs_to_linear_bits(dbfs, bit_depth):
        linear_value = pow(10, dbfs.DBFS/20)*pow(2,bit_depth-1)
        linear_value *= dbfs.sign
        return linear_value

    @staticmethod
    def samples_to_seconds(samples,sample_rate):
        return samples/sample_rate

    @staticmethod
    def seconds_to_samples(seconds,sample_rate):
        return seconds*sample_rate
