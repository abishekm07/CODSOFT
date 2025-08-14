                    continue

      def xor(a, b):
    # Perform XOR operation on two strings
    result = []
    for i in range(1, len(b)):
        result.append('0' if a[i] == b[i] else '1')
    return ''.join(result)

def mod2div(dividend, divisor):
    # Perform Modulo-2 division
    pick = len(divisor)
    tmp = dividend[0:pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0' * pick, tmp) + dividend[pick]
        pick += 1

    # Last bit of the division
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)
    return tmp

def encode_data(data, key):
    # Append zeros equivalent to the key's length - 1
    l_key = len(key)
    appended_data = data + '0' * (l_key - 1)
    remainder = mod2div(appended_data, key)
    # Append remainder to the original data (codeword)
    codeword = data + remainder
    return codeword

def decode_data(data, key):
    remainder = mod2div(data, key)
    return remainder

# Example usage
if __name__ == "__main__":
    # Example data to be transmitted
    data = "1011001"  # Binary data to transmit
    key = "1101"      # Divisor (CRC key)

    # Sender side: encoding the data with CRC
    print("Original Data: ", data)
    codeword = encode_data(data, key)
    print("Encoded Data (Codeword): ", codeword)

    # Receiver side: decoding the received codeword
    received_data = codeword  # In a real scenario, this would be the received codeword
    remainder = decode_data(received_data, key)

    # Check if there is an error
    if '1' in remainder:
        print("Error detected in received data.")
    else:
        print("No error detected in received data.")
