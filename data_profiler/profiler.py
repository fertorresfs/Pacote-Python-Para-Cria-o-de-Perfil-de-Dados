import pandas as pd
import numpy as np

def profile_data(df):
    """
    Gera um perfil de um DataFrame Pandas.

    Args:
        df: O DataFrame Pandas a ser analisado.

    Returns:
        Um dicionário contendo estatísticas descritivas e informações sobre anomalias.
    """

    profile = {}

    for col in df.columns:
        profile[col] = {
            'tipo': df[col].dtype.name,
            'nao_nulos': df[col].count(),
            'nulos': df[col].isnull().sum(),
            'unicos': df[col].nunique(),

        }

        if pd.api.types.is_numeric_dtype(df[col]):
            profile[col].update({
                'media': df[col].mean(),
                'mediana': df[col].median(),
                'desvio_padrao': df[col].std(),
                'minimo': df[col].min(),
                'maximo': df[col].max(),
                'percentil_25': df[col].quantile(0.25),
                'percentil_75': df[col].quantile(0.75),

            })

            #Detecção simples de anomalias (exemplo com z-score) -  apenas exemplo, pode ser expandido
            z = np.abs((df[col] - df[col].mean()) / df[col].std())
            outliers = df[z > 3]
            profile[col]['outliers'] = len(outliers)

    return profile



def gerar_relatorio(profile):
    # Gera um relatório formatado a partir do dicionário profile
    # Pode ser em texto, HTML, etc. - adicione sua lógica aqui

    for col, stats in profile.items():
        print(f"Coluna: {col}")
        for stat, value in stats.items():
          print(f"  {stat}: {value}")


#Exemplo básico de uso (dentro do profiler.py ou em um script separado)
#df = pd.read_csv("seu_arquivo.csv")
#profile = profile_data(df)
#gerar_relatorio(profile)
