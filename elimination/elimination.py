import math


def encode(data):
    """
    Takes a list of integers and encodes by index
    :param data: list of integers to encode
    :return: the encoded result as bit string
    """
    if type(data) != list:
        raise TypeError('Lists of integers only accepted')
    # create empty result
    result = ''
    # Create an array of data length with empty slots
    slots = [x for x in range(len(data))]
    for num in data:
        # calculate its free slot index. Find the index of the slot with the value of our number.
        # so if the value is 5 its index is at 5 (on first pass)
        free_slot_index = slots.index(num)
        # determine how many bits you need to encode the free slot index, because there are 8 slots LOG2(8) = 3.
        # So we encode the number 5 using only 3 bits which is 101
        bits_required = math.ceil(math.log2(len(slots)))
        # now remove the slot
        result += "{0:0{1}b} ".format(free_slot_index, bits_required)
        del slots[free_slot_index]
    return result.strip()


def decode(indata):
    """
    Takes a string of binary index data and decodes to the original values
    :param indata: string of binary
    :return:
    """
    result = []
    # Create empty slots
    slots = [x for x in range(len(indata.split(' ')))]
    num_free_slots = len(indata.split(' ')) - len(result)
    data = str(indata).replace(' ', '')
    bit_start = 0
    while num_free_slots > 0:
        bits_required = math.ceil(math.log2(num_free_slots))
        if bits_required:
            bits = data[bit_start:bit_start+bits_required]
            bit_start += bits_required
        else:
            bits = '0'
        index = int(bits, 2)
        result.append(slots[index])
        del slots[index]
        num_free_slots = len(indata.split(' ')) - len(result)
    return result