import PyPDF2
import sys

input_file = sys.argv[1:]
merge_file = PyPDF2.PdfFileMerger()
for file_name in input_file:
    merge_file.append(file_name)

merge_file.write('merged.pdf')
