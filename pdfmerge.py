import os
from PyPDF2 import PdfFileReader, PdfFileWriter


def merge_pdf(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        path = os.path.abspath(path)
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)