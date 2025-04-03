import pdfplumber
import pandas as pd

caminho_pdf = "downloads/Anexo_I.pdf"

with pdfplumber.open(caminho_pdf) as pdf:
    
    pagina = pdf.pages[0]

    
    tabelas = pagina.extract_tables()


    if tabelas:
        for i, tabela in enumerate(tabelas):
            print(f"Tabela {i + 1}:")
            for linha in tabela:
                print(linha)
            print("-" * 40)
    else:
        print("Nenhuma tabela encontrada na página 1.")