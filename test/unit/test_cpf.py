import pytest
from src.domain.entity.cpf import Cpf


def test_cpf_valid():
    valid_cpf = "847.903.332-05"
    cpf = Cpf(valid_cpf)
    assert cpf.value == valid_cpf


def test_valid_cpf():
    invalid_cpf = "111.111.111-11"
    with pytest.raises(ValueError):
        Cpf(invalid_cpf)
