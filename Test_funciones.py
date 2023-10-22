import pytest
from funciones import sum_digit,choiced_word

# parametrizacion para probar distintos casos de la suma de digitos
@pytest.mark.parametrize("number,result", [
    (32, 5),
    (-5-5, -10),
    (352, 10),
    (59438, 29),
])

def test_sum_digit(number, result):
    assert sum_digit(number) == result

# parametrizacion para encontrar la frase oculta
@pytest.mark.parametrize("word,phrase,res", [
    ("pedro","apghehjktrdo", "pedro"),
    ("casa", "pTeCyfahJstuA", "casa"),
    ("murcielago", "AeiOu", "_u__ie_a_o")
])

def test_choice_word(word,phrase,res):
    assert choiced_word(word,phrase) == res