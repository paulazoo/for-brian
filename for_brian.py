import PyPDF2

pdfFileObj = open('example_pdf.pdf','rb')     #'rb' for read binary mode
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(1)          #'9' is the page number
print(pageObj.extractText())

pdf_output = open("pdf_output.txt","w")
pdf_output.write(pageObj.extractText())
