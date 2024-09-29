import matplotlib.pyplot as plt

def plotar_imagem(imagem, titulo='Imagem'):
    plt.figure(figsize=(12, 4))
    plt.imshow(imagem, cmap='gray')
    plt.title(titulo)
    plt.axis('off')
    plt.show()

def plotar_imagens(*imagens):
    
    numero_imagens = len(imagens)
    fig, eixos = plt.subplots(nrows=1, ncols=numero_imagens, figsize=(12, 4))
    for ax, imagem in zip(eixos, imagens):
        ax.imshow(imagem, cmap='gray')
        ax.axis('off')
    plt.show()

def plotar_histograma(imagem):
    fig, eixos = plt.subplots(nrows=1, ncols=3, figsize=(12, 4), sharex=True, sharey=True)
    cores = ['red', 'green', 'blue']
    for i, cor in enumerate(cores):
        eixos[i].hist(imagem[:, :, i].ravel(), bins=256, color=cor, alpha=0.8)
        eixos[i].set_title(f'Histograma da Cor {cor.title()}')
    plt.tight_layout()
    plt.show()

def plotar_diferenca(imagem1, imagem2, diferenca):
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1)
    plt.imshow(imagem1, cmap='gray')
    plt.title('Imagem 1')
    plt.axis('off')
    
    plt.subplot(1, 3, 2)
    plt.imshow(imagem2, cmap='gray')
    plt.title('Imagem 2')
    plt.axis('off')
    
    plt.subplot(1, 3, 3)
    plt.imshow(diferenca, cmap='gray')
    plt.title('Diferença')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()

def plotar_resultados(imagem1, imagem2, resultado, titulo1='Imagem 1', titulo2='Imagem 2', titulo_resultado='Resultado'):
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1)
    plt.imshow(imagem1, cmap='gray')
    plt.title(titulo1)
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(imagem2, cmap='gray')
    plt.title(titulo2)
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(resultado, cmap='gray')
    plt.title(titulo_resultado)
    plt.axis('off')

    plt.tight_layout()
    plt.show()

