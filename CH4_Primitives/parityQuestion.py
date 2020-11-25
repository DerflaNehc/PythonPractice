# Write a program to find the node at which the intersection of two singly linked lists begins.

def paritybitBrute(integer_64: int) -> int:
    parity_count = 0
    while integer_64:
        parity_count ^= integer_64 & 1
        integer_64 >>= 1
    return parity_count


def paritybit2(integer_64: int) -> int:
    dict_16Bit = {}
    parity_count = 0
    while integer_64:
        lowest_16 = integer_64 & 0xffff
        integer_64 >>= 16
        if lowest_16 in dict_16Bit:
            parity_count ^= dict_16Bit[lowest_16]
        else:
            low_parity = 0
            while lowest_16:
                low_parity ^= 1
                lowest_16 &= lowest_16 - 1
            dict_16Bit[lowest_16] = low_parity
            parity_count ^=low_parity
    return parity_count

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for number in range(10**5):
        deq_res = paritybit2(number)
        trivial_res = paritybitBrute(number)
        assert deq_res == trivial_res, \
            'deque = {}, trivial = {}, number = {}'.format(
                deq_res,
                trivial_res,
                number
            )
