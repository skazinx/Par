from src.matematica import eh_par

def test_numeros_pares():
    assert eh_par(2) == True
    assert eh_par(4) == True
    assert eh_par(100) == True

def test_numeros_impares():
    assert eh_par(1) == False
    assert eh_par(3) == False
    assert eh_par(99) == False
