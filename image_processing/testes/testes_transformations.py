import numpy as np
from PIL import Image
from image_processing.processing.transformations import converter_para_cinza, normalizar_imagem, ajustar_histograma, redimensionar_imagem, calcular_similaridade
from skimage.data import camera
from skimage import data

# Teste para converter_para_cinza
def test_converter_para_cinza():
    imagem_colorida = data.astronaut() # Usando a imagem de exemplo do skimage
    imagem_cinza = converter_para_cinza(imagem_colorida)
    assert imagem_cinza.ndim == 2 
    #assert imagem_cinza.shape[2] == 1  # A imagem resultante deve ter um canal
    #assert imagem_cinza.dtype == np.float64  # O tipo de dado deve ser float

# Teste para normalizar_imagem
def test_normalizar_imagem():
    imagem = np.array([[0, 0, 0], [1, 1, 1]])  # Matriz simples
    imagem_normalizada = normalizar_imagem(imagem)
    
    assert np.all(imagem_normalizada >= 0)  # Verifica se todos os valores estão >= 0
    assert np.all(imagem_normalizada <= 1)  # Verifica se todos os valores estão <= 1

# Teste para ajustar_histograma
def test_ajustar_histograma():
    imagem_alvo = np.random.rand(100, 100, 3)  # Imagem alvo aleatória
    imagem_referencia = np.random.rand(100, 100, 3)  # Imagem referência aleatória
    imagem_ajustada = ajustar_histograma(imagem_alvo, imagem_referencia)

    assert imagem_ajustada.shape == imagem_alvo.shape  # As dimensões devem ser iguais

# Teste para calcular_similaridade


# Teste para redimensionar_imagem
def test_redimensionar_imagem():
    imagem = Image.new('RGB', (200, 100), color='red')
    imagem_redimensionada = redimensionar_imagem(imagem, 100, 50)

    assert imagem_redimensionada.size == (100, 50)  # Verifica se o tamanho é correto
