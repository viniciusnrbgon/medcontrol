import pytest
from unittest.mock import patch
from src.services.medicamento_api import MedicamentoService

@patch('requests.get')
def test_buscar_medicamento_sucesso(mock_get):
    
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "results": [{
            "openfda": {
                "brand_name": ["Amoxicilina"],
                "manufacturer_name": ["Laboratório Neo Química"]
            },
            "active_ingredient": ["Amoxicilina tri-hidratada"],
            "purpose": ["Antibiótico"]
        }]
    }

    resultado = MedicamentoService.buscar_medicamento_por_nome("Amoxicilina")

    assert resultado["nome"] == "Amoxicilina"
    assert resultado["fabricante"] == "Laboratório Neo Química"
    assert resultado["substancia_ativa"] == "Amoxicilina tri-hidratada"


@patch('requests.get')
def test_buscar_medicamento_nao_encontrado(mock_get):

    mock_get.return_value.status_code = 404

    with pytest.raises(Exception) as contexto:
        MedicamentoService.buscar_medicamento_por_nome("MedicamentoInexistente")
    
    assert "Medicamento não encontrado" in str(contexto.value)
