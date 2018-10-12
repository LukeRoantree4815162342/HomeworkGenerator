# The purpose of this module is to provide a function for converting markdown files to pdfs
import markdown2
from xhtml2pdf import pisa


def convert(markdown_filename: str, output_filename: str) -> bool:
    # First convert markdown to HTML
    html = markdown2.markdown_path(markdown_filename)

    # open output file for writing (truncated binary)
    resultFile = open(output_filename, "w+b")

    # convert HTML to PDF
    pisaStatus = pisa.CreatePDF(
            html,                # the HTML to convert
            dest=resultFile)           # file handle to recieve result

    # close output file
    resultFile.close()                 # close output file

    # return True on success and False on errors
    return pisaStatus.err
