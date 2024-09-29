from PIL import Image
import os
import numpy as np

def salvar_imagem(imagem, caminho):
    imagem.save(caminho)


def carregar_imagem(caminho):
    imagem = Image.open(caminho)
    imagem.close()
    return imagem


def listar_imagens(diretorio):
    return [f for f in os.listdir(diretorio) if f.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]


def imagem_para_array(imagem):
    return np.array(imagem)


def array_para_imagem(array):
    return Image.fromarray(array)
