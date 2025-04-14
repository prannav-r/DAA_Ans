def karatsuba_multiply(num1_str: str, num2_str: str) -> str:
    """
    Multiplies two large integers (represented as strings) using the Karatsuba algorithm.
    
    Args:
        num1_str: The first large integer as a string.
        num2_str: The second large integer as a string.

    Returns:
        The product of the two integers as a string.
    """
    # Base case
    if len(num1_str) == 1 or len(num2_str) == 1:
        return str(int(num1_str) * int(num2_str))

    # Make lengths equal and even
    max_len = max(len(num1_str), len(num2_str))
    if max_len % 2 != 0:
        max_len += 1
    num1_str = num1_str.zfill(max_len)
    num2_str = num2_str.zfill(max_len)

    n = max_len
    m = n // 2

    # Split numbers into a, b and c, d
    a, b = num1_str[:-m], num1_str[-m:]
    c, d = num2_str[:-m], num2_str[-m:]

    # Recursive steps
    ac = karatsuba_multiply(a, c)
    bd = karatsuba_multiply(b, d)
    ad_plus_bc = karatsuba_multiply(str(int(a) + int(b)), str(int(c) + int(d)))

    # Karatsuba combination
    product = int(ac) * 10**(2 * m) + (int(ad_plus_bc) - int(ac) - int(bd)) * 10**m + int(bd)

    return str(product)

print(karatsuba_multiply("1234", "56"))
