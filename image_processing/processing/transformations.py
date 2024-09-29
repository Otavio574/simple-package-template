from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity
import numpy as np

def converter_para_cinza(imagem):
    return rgb2gray(imagem)


def normalizar_imagem(imagem):
    return (imagem - np.min(imagem)) / (np.max(imagem) - np.min(imagem))


def ajustar_histograma(imagem_alvo, imagem_referencia):
    return match_histograms(imagem_alvo, imagem_referencia)


def redimensionar_imagem(imagem, nova_largura, nova_altura):
    return imagem.resize((nova_largura, nova_altura))
