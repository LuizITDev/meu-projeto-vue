import zipfile
import os


pasta_downloads = "downloads"


arquuivos = ["Anexo_I.pdf", "Anexo_II.pdf"]

caminho_zip = "output/anexos_ans_completos.zip"

with zipfile.ZipFile(caminho_zip, "w") as zipf:
   
    for arquivo in arquuivos:
        caminho_arquivo = os.path.join(pasta_downloads, arquivo)
        zipf.write(caminho_arquivo, arcname=arquivo)
        print(f"{arquivo} adicionado ao zip.")

        