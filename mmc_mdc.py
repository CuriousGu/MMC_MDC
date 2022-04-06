from typing import List


def factorization(value: int) -> List[int]:
    initial = 2
    factors = []

    while value != 1:
        if value % initial == 0:
            value = value / initial
            factors.append(initial)

        else:
            initial += 1

    return factors


def finding_equals(values: List[int]) -> List[int]:
    a, b = values
    fat_a, fat_b = factorization(a), factorization(b)
    common_factors = []

    for i in fat_a:
        if i in fat_b:
            common_factors.append(i)

    return common_factors


def mdc(values: List[int]) -> int:
    answer = 1
    common_values = finding_equals(values)
    for i in common_values:
        answer *= i

    return answer


def mmc(values: List[int]) -> int:
    a, b = values
    return int((a*b)/mdc(values))
