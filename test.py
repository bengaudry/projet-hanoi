
def test(output, expected, testIndex: str | int = ""):
    if output == expected:
        print(f"TEST {testIndex} : PASSED")
    else:
        print(f"TEST {testIndex} : FAILED")
        print(f"Expected output : {expected}")
        print(f"Your output : {output}")