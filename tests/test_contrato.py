import pytest
from pydantic import ValidationError
from datetime import datetime
from src.contrato import Vendas


def test_vendas_com_dados_validos():
      
    dados_validos = {
        "email": "comprador@exemplo.com",
        "data": datetime.now(),
        "valor": 100.50,
        "produto": "Produto X",
        "quantidade": 3,
        "categoria": "categoria3",
    }
    venda = Vendas(**dados_validos)

    assert venda.email == dados_validos["email"]
    assert venda.data == dados_validos["data"]
    assert venda.valor == dados_validos["valor"]
    assert venda.produto == dados_validos["produto"]
    assert venda.quantidade == dados_validos["quantidade"]
    assert venda.categoria == dados_validos["categoria"]

def testes_vendas_com_dados_invalidos():
    dados_invalidos = {
        "email": "comprador",
        "data": "nao e uma data",
        "valor": -100,
        "produto": "",
        "quantidade": -1,
        "categoria": "categoria3"
    }

    with pytest.raises(ValidationError):
        Vendas(**dados_invalidos)
    
#Teste de validação de categoria
def test_validacao_categoria():
    dados_categoria = {
        "email": "comprador",
        "data": "nao e uma data",
        "valor": -100,
        "produto": "",
        "quantidade": -1,
        "categoria": "categoria3"
    }
    
    with pytest.raises(ValidationError):
        Vendas(**dados_categoria)