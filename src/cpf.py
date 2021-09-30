import re


class Cpf:
    _CPF_VALID_LENGTH: int = 11
    _FACTOR_FIST_VERIFY_DIGIT: int = 10
    _FACTOR_SECOND_VERIFY_DIGIT: int = 11

    def __init__(self, value: str) -> None:
        if not self._validate(value):
            raise ValueError("Invalid CPF")
        self.value = value

    def _validate(self, cpf: str) -> bool:
        if not cpf:
            return False
        formatted_cpf = self._format_cpf(cpf)
        if len(formatted_cpf) != self._CPF_VALID_LENGTH:
            return False
        if self._all_digit_equal(formatted_cpf):
            return False
        if not self._is_first_digit_valid(
            formatted_cpf, self._FACTOR_FIST_VERIFY_DIGIT
        ):
            return False
        if not self._is_second_digit_valid(
            formatted_cpf, self._FACTOR_SECOND_VERIFY_DIGIT
        ):
            return False
        return True

    def _format_cpf(self, cpf: str) -> str:
        return re.sub(r"[^0-9]", "", cpf)

    def _all_digit_equal(self, cpf: str) -> bool:
        return len(set(cpf)) == 1

    def _is_first_digit_valid(self, cpf: str, factor_digit: int) -> bool:
        first_digit = cpf[-2]
        check_digit = self._calculate_digit(cpf, factor_digit)
        if check_digit != first_digit:
            return False
        return True

    def _is_second_digit_valid(self, cpf: str, factor_digit: int) -> bool:
        second_digit = cpf[-1]
        check_digit = self._calculate_digit(cpf, factor_digit)
        if check_digit != second_digit:
            return False
        return True

    def _calculate_digit(self, cpf: str, factor_digit: int) -> str:
        sum_digit = 0
        for digit, index in enumerate(range(factor_digit, 1, -1)):
            sum_digit += int(cpf[digit]) * index
        if (sum_digit % 11) < 2:
            first_digit = 0
        else:
            first_digit = 11 - (sum_digit % 11)
        return str(first_digit)
