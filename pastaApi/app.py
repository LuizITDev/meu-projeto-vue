from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import os


csv_path = '/Applications/web_scraping_ans/dados_ans/operadoras_ativas.csv'

if not os.path.exists(csv_path):
    raise FileNotFoundError(f"O arquivo {csv_path} não foi encontrado.")


operadoras_df = pd.read_csv(csv_path, delimiter=';')


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.get("/buscar-operadora")
async def buscar_operadora(termo: str):
    try:
        
        resultado = operadoras_df[operadoras_df['Nome_Fantasia'].str.contains(termo, case=False, na=False)]

        
        if not resultado.empty:
            
            operadoras = resultado[['Nome_Fantasia', 'CNPJ', 'Registro_ANS', 'Telefone', 'Cidade', 'UF']].to_dict(orient='records')
            return {"message": "Operadoras encontradas", "data": operadoras}
        else:
            return {"message": "Nenhuma operadora encontrada", "data": []}
    except Exception as e:
        return {"message": f"Erro ao buscar operadora. Tente novamente mais tarde. {str(e)}", "data": []}
