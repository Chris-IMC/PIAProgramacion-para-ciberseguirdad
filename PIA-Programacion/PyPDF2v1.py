import PyPDF2

pdf = open("Textos y actividades del Manual de la Cultura de la Legalidad.pdf", "rb")

reader = PyPDF2.PdfReader(pdf)

while True:
    try:
        pagenumber = int(input("Ingresa un numero:"))
        page = reader.getPage(pagenumber)
        metad =reader.metadata
        print("Extrayendo texto del pdf..")
        print(page.extractText())
        print("Extrayendo metadata del pdf ")
        print(metad)
        break
    except ValueError:
        print("Vuelva a intentar")
