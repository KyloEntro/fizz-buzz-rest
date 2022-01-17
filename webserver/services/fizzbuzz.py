from typing import List


def generate_fizz_buzz_string(int1: int, str1: str, int2: int, str2: str, limit: str) -> List[str]:
    """ Generate a list of strings with numbers from 1 to limit, where: 
    all multiples of int1 are replaced by str1, all multiples of int2 are replaced by str2, 
    all multiples of int1 and int2 are replaced by str1str2
    """
    result = []

    for index in range(1, limit + 1):
        resultStr = ""
        if index % int1 == 0:
            resultStr += str1
        if index % int2 == 0:
            resultStr += str2

        if len(resultStr) == 0:
            resultStr = str(index)

        result.append(resultStr)

    return result
