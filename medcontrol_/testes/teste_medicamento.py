import pytest
from src.medicamento import Medicamento

def test_criar_medicamento():
    med = Medicamento("Dipirona", "08:00")
    assert med.nome == "Dipirona"

def test_nome_vazio():
    with pytest.raises(ValueError):
        Medicamento("", "08:00")

def test_to_dict():
    med = Medicamento("Paracetamol", "10:00")
    assert med.to_dict() == {"nome": "Paracetamol", "horario": "10:00"}