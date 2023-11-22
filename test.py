
def test(output, expected, test_index: int = None):
    if output == expected:
        print(f"TEST {test_index if test_index is not None else ''} : PASSED")
    else:
        print(f"TEST {test_index} : FAILED")
        print(f"Expected output : {expected}")
        print(f"Your output : {output}")
    return output == expected
