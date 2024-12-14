from setuptools import setup, find_packages

setup(
    name='data_profiler',
    version='0.1.0',    
    description='Um pacote Python para criação de perfil de dados',
    url='https://github.com/seu_usuario/data_profiler', #opcional - se for publicar no GitHub
    author='Seu Nome',
    author_email='seu_email@example.com',
    license='MIT', #ou outra licença
    packages=find_packages(),
    install_requires=['pandas','numpy'], #adicione outras dependências aqui
    classifiers=[ #opcional - para classificar o pacote
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
