import pytest
import numpy as np
from PIL import Image
from image_processing.utils.plot import plotar_diferenca, plotar_imagem, plotar_imagens, plotar_histograma, plotar_resultados

def test_plotar_imagem():
    imagem = np.random.rand(100, 100)  # Criando uma imagem aleatória
    try:
        plotar_imagem(imagem, titulo='Teste')
    except Exception as e:
        pytest.fail(f"plotar_imagem falhou com erro: {e}")

# Teste para plotar_imagens
def test_plotar_imagens():
    imagem1 = np.random.rand(100, 100)  # Criando uma imagem aleatória
    imagem2 = np.random.rand(100, 100)  # Outra imagem aleatória
    try:
        plotar_imagens(imagem1, imagem2)
    except Exception as e:
        pytest.fail(f"plotar_imagens falhou com erro: {e}")

# Teste para plotar_histograma
def test_plotar_histograma():
    imagem = np.random.rand(100, 100, 3)  # Criando uma imagem colorida aleatória
    try:
        plotar_histograma(imagem)
    except Exception as e:
        pytest.fail(f"plotar_histograma falhou com erro: {e}")

# Teste para plotar_diferenca
def test_plotar_diferenca():
    imagem1 = np.random.rand(100, 100)  # Criando uma imagem aleatória
    imagem2 = np.random.rand(100, 100)  # Outra imagem aleatória
    diferenca = np.abs(imagem1 - imagem2)  # Diferença simples
    try:
        plotar_diferenca(imagem1, imagem2, diferenca)
    except Exception as e:
        pytest.fail(f"plotar_diferenca falhou com erro: {e}")

# Teste para plotar_resultados
def test_plotar_resultados():
    imagem1 = np.random.rand(100, 100)  # Criando uma imagem aleatória
    imagem2 = np.random.rand(100, 100)  # Outra imagem aleatória
    resultado = (imagem1 + imagem2) / 2  # Resultado simples
    try:
        plotar_resultados(imagem1, imagem2, resultado)
    except Exception as e:
        pytest.fail(f"plotar_resultados falhou com erro: {e}")