import pdfplumber

caminho_pdf = "downloads/Anexo_I.pdf"

with pdfplumber.open(caminho_pdf) as pdf:
    pagina = pdf.pages[0]  
    texto = pagina.extract_text()

    if texto:
        print("Texto da página 1:\n")
        print(texto)
    else:
        print("Nenhum texto detectado na página 1.")
        