import pytest
from process import process


@pytest.mark.statement
@pytest.mark.parametrize("valores, esperado", [
    ([2], ["positivo", "par"]),
])
def test_statement_coverage(valores, esperado):
    assert process(valores) == esperado

# ramas
@pytest.mark.branch
@pytest.mark.parametrize("valores, esperado", [
    ([2], ["positivo", "par"]),
    ([-1], []),
    ([], []),
])
def test_branch_coverage(valores, esperado):
    assert process(valores) == esperado
