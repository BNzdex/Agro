import pandas as pd

df = pd.read_excel("Recomendação de Adubação Bernardo.xls")

def get_recommendation(cultura, solo):
    resultado = df[(df['Cultura'] == cultura) & (df['Tipo de Solo'] == solo)]
    return resultado.to_dict(orient='records')