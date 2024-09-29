from setuptools import setup, find_packages

setup(
    name='image_processor',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow',  # Dependência para manipulação de imagens
    ],
    author='Otávio Augusto',
    author_email='otavioscr42@gmail.com',
    description='Um pacote para processamento básico de imagens',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Otavio574/simple-package-template',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
