# pdf çevirici

from pdf2docx import Converter

my_pdf = "mypdf.pdf"
my_docx = "mydocx.docx"

cv = Converter(pdf_file= my_pdf)
cv.convert(docx_filename=my_docx)
cv.close()
