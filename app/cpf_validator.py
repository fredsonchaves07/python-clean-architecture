black_list = [
    "00000000000",
    "11111111111",
    "22222222222",
    "33333333333",
    "44444444444",
    "55555555555",
    "66666666666",
    "77777777777",
    "88888888888",
    "99999999999",
]


def is_valid(cpf: str) -> bool:
    return len(cpf) >= 11 or len(cpf) <= 14


def format_cpf(cpf: str) -> str:
    # TODO -> Regex
    return cpf.replace(".", "").replace(".", "").replace("-", "").replace(" ", "")


def is_first_digit_valid(cpf: str) -> bool:
    first_digit = cpf[-2]
    check_digit = calculate_first_digit(cpf)
    if check_digit != first_digit:
        return False
    return True


def is_second_digit_valid(cpf: str) -> bool:
    second_digit = cpf[-1]
    check_digit = calculate_second_digit(cpf)
    if check_digit != second_digit:
        return False
    return True


def calculate_first_digit(cpf: str) -> str:
    sum_digit = 0
    for digit, index in enumerate(range(10, 1, -1)):
        sum_digit += int(cpf[digit]) * index
    if (sum_digit % 11) < 2:
        first_digit = 0
    else:
        first_digit = 11 - (sum_digit % 11)
    return str(first_digit)


def calculate_second_digit(cpf: str) -> str:
    sum_digit = 0
    for digit, index in enumerate(range(11, 1, -1)):
        sum_digit += int(cpf[digit]) * index
    if (sum_digit % 11) < 2:
        second_digit = 0
    else:
        second_digit = 11 - (sum_digit % 11)
    return str(second_digit)


def validate(cpf: str) -> str:
    if not cpf:
        return False
    if not is_valid(cpf):
        return False
    formatted_cpf = format_cpf(cpf)
    if formatted_cpf in black_list:
        return False
    if not is_first_digit_valid(formatted_cpf):
        return False
    if not is_second_digit_valid(formatted_cpf):
        return False
    return True


print(validate("111.111.111-11"))
print(validate("123.456.789-99"))
print(validate("935.411.347-80"))
