import pytest
import os
import numpy as np
from PIL import Image
from image_processing.utils.io import salvar_imagem, carregar_imagem, listar_imagens, imagem_para_array, array_para_imagem

def test_salvar_imagem():
    img = Image.new('RGB', (100, 100), color='black')
    output_path = 'teste_imagem.png'
    salvar_imagem(img, output_path)
    assert os.path.exists(output_path), "A imagem não foi salva."
    if os.path.exists(output_path):
        os.remove(output_path)

# Teste para carregar_imagem
def test_carregar_imagem():
    img = Image.new('RGB', (100, 100), color='black')
    output_path = 'teste_carregar.png'
    salvar_imagem(img, output_path)
    imagem_carregada = carregar_imagem(output_path)
    assert imagem_carregada.size == img.size, "As dimensões da imagem carregada estão incorretas."
    os.remove(output_path)

# Teste para listar_imagens
def test_listar_imagens(tmpdir):
    # Criar diretório temporário e arquivos de imagem
    temp_dir = tmpdir.mkdir("imagens")
    img1_path = temp_dir.join("imagem1.png")
    img2_path = temp_dir.join("imagem2.jpg")
    img1 = Image.new('RGB', (100, 100), color='black')
    img2 = Image.new('RGB', (100, 100), color='white')
    img1.save(img1_path)
    img2.save(img2_path)

    imagens = listar_imagens(str(temp_dir))
    assert len(imagens) == 2, "Nem todas as imagens foram listadas."

# Teste para imagem_para_array
def test_imagem_para_array():
    img = Image.new('RGB', (100, 100), color='black')
    array = imagem_para_array(img)
    assert isinstance(array, np.ndarray), "A função não retornou um array numpy."
    assert array.shape == (100, 100, 3), "A dimensão do array está incorreta."

# Teste para array_para_imagem
def test_array_para_imagem():
    array = np.zeros((100, 100, 3), dtype=np.uint8)
    img = array_para_imagem(array)
    assert isinstance(img, Image.Image), "A função não retornou uma imagem PIL."
    assert img.size == (100, 100), "As dimensões da imagem convertida estão incorretas."