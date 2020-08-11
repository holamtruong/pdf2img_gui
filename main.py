from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

# pages = convert_from_path('input/file_a.pdf', output_folder='output', poppler_path='poppler/bin')

"""
images = convert_from_path('input/file_a.pdf', poppler_path='poppler/bin')
for image in images:
    image.save('output/sample1.png', 'PNG')
"""

images = convert_from_path('input/file_multi.pdf', dpi=700,  poppler_path='poppler/bin')
i = 1
for image in images:
    image.save('output/' + 'multi_' + str(i) + '.tiff', 'TIFF')
    i = i + 1

print("Done! Your results in 'output' folder.")
