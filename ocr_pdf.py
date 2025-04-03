import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import pandas as pd
import zipfile

pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"


caminho_pdf = "downloads/Anexo_I.pdf"

imagens = convert_from_path(caminho_pdf)

linhas_gerais = []


for i, imagem in enumerate(imagens):
    print(f"Processando página {i+1}")
    texto = pytesseract.image_to_string(imagem, lang="por")  
    linhas = texto.split('\n')  

    for linha in linhas:
        if linha.strip():  
            linhas_gerais.append([linha.strip()]) 


df = pd.DataFrame(linhas_gerais, columns=["Conteudo"])


df["Conteudo"] = df["Conteudo"].str.replace(" OD", " Odontologia")
df["Conteudo"] = df["Conteudo"].str.replace(" AMB", " Ambulatorial")


caminho_csv = "output/anexo_I_extraido.csv"
df.to_csv(caminho_csv, index=False)
print("CSV salvo com sucesso!")


caminho_zip = "output/Teste_Luiz.zip"  
with zipfile.ZipFile(caminho_zip, "w") as zipf:
    zipf.write(caminho_csv, arcname="anexo_I_extraido.csv")

print("ZIP criado com sucesso em:", caminho_zip)