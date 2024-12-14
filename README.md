# Pacote Python Para Cria o de Perfil de Dados

# data_profiler

Um pacote Python para gerar perfis de dados.

# Estrutura do Projeto:

```bash
 data_profiler/
 ├── __init__.py
 ├── profiler.py
 ├── tests/
 │   ├── __init__.py
 │   └── test_profiler.py
 ├── setup.py
 └── README.md
```

## Instalação

```bash
pip install .  # Instala a partir do código fonte
# ou, se publicado no pypi:
# pip install data_profiler
```
## Uso

```bash
import pandas as pd
from data_profiler import profile_data, gerar_relatorio

df = pd.read_csv("seu_arquivo.csv")
profile = profile_data(df)

gerar_relatorio(profile) #gera saída no console

#acessando elementos específicos do perfil:
#print(profile['nome_da_coluna']['media'])
```
## Executando os testes

python -m unittest discover data_profiler/tests


**Como usar:**

1.  **Instalar:**  `pip install .` (dentro do diretório `data_profiler/`) ou, se publicado no PyPI:  `pip install data_profiler`
2.  **Importar:** `from data_profiler import profile_data, gerar_relatorio`
3.  **Usar:**  `profile = profile_data(seu_dataframe)`


**Próximos passos:**

* Adicionar mais estatísticas e detecção de anomalias.
* Criar um relatório mais completo (HTML, PDF, etc.).
* Publicar o pacote no PyPI.
* Implementar logging.
