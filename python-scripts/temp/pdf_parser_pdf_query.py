import pdfquery


# Michael Variola
def parse_data():

    filename = "../data/input/4_ini_3.pdf"

    pdf = pdfquery.PDFQuery(filename)

    pdf.load(1)

    print(pdf.pq('LTTextBoxHorizontal:contains("' + "Kalenderwoche:" + '")').text())