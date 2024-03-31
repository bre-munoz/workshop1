import pandas as pd
from contrato import Vendas

def process_excel(uploaded_file):
    try:
        df = pd.read_excel(uploaded_file)

        # Verificar se há colunas extras no DataFrame
        extra_cols = set(df.columns) - set(Vendas.model_fields.keys())
        if extra_cols:
            return False, f"Colunas extras detectadas no Excel: {', '.join(extra_cols)}" 
        
        # Validar cada linha com o schema escolhido
        for index, row in df.iterrows():
            try:
               _ = Vendas(**row.to_dict()) #Testar cada linha para o dicionário
            except Exception as e:
                raise ValueError(f"Erro na linha{index + 2}: {e}") 
        # Retorna tanto o resultado da validação, os erros, quanto o DataFrame
        return True, None
    
    except ValueError as ve:
        return False, str(ve)    
    except Exception as e:
        # Se houver exceção, retorna o erro e um DataFrame vazio
        return pd.DataFrame(), f"Erro inesperado: {str(e)}"