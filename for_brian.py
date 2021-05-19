'''
1) pip install pypdf2
2) move the relevant pdf file into this folder
3) open either the vs code terminal or the anaconda prompt whichever is easier
4) in the terminal type "python for_brian.py" to run

'''


import PyPDF2

pdf_file_name = input("Enter PDF file name: ")

pdfFileObj = open(pdf_file_name+'.pdf','rb')     #'rb' for read binary mode
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(1)          #'9' is the page number
print(pageObj.extractText())

pdf_file_name = input("Enter output txt file name: ")
pdf_output = open(pdf_output_file+".txt","w")
pdf_output.write(pageObj.extractText())
