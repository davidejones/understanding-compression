from collections import Counter


def generate_code(table, code='0'):
    match = False
    for k, v in table.items():
        if v.startswith(code):
            # prefix matched already we need a new code
            match = True
    if match:
        code = '{:b}'.format(1 + int(code, 2))
        return generate_code(table, code)
    else:
        return code


def encode(data):
    # Calculate probability for all symbols
    probabilities = Counter(data)
    # Assign codewords to symbols based upon their probability, more frequent symbols are assigned smaller codewords
    codeword_table = {}
    for char, _ in probabilities.items():
        # after we select a code no other code can start with that pattern or it falls apart
        code = generate_code(codeword_table)
        codeword_table[char] = code
    # Walk through the data set when you encode a symbol output tits codeword to the compressed bit stream
    print(codeword_table)


def decode():
    pass
