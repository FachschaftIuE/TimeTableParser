from pdfquery import *


def count_pdf_pages(filepath):

    """
     Summary
     -------
     This function returns number of pages in pdf-file

     Parameter
     ---------
     filepath : string     # String with filepath

     Returns
     -------

     pages : int           # returns int of pages
     """

    file = filepath
    pdf = pdfquery.PDFQuery(file)
    pages = pdf.doc.catalog['Pages'].resolve()['Count']
    
    return pages
