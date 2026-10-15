import pytest
from process import process


@pytest.mark.statement
@pytest.mark.parametrize("valores, esperado", [
    ([2], ["positivo", "par"]),
])
def test_statement_coverage(valores, esperado):
    assert process(valores) == esperado
