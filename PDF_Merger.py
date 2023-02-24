from PyPDF2 import PdfMerger
import os

source_folder = r'C:\Users\levi.silva\Desktop\TesteRenomeador\Pokemons' + '\\'
target_folder = r'C:\Users\levi.silva\Desktop\TesteRenomeador\Output' + '\\'
merger = PdfMerger()
pdfs = []

def read_files (sourceFolder):
    try:
        for path, dir, files in os.walk(sourceFolder):
            if files:
                for file in files:
                    pdfs.append(path + '\\' + file)
        print('All files are append')
    except Exception as e:
        print(e)

def merge_pdfs (pdf_files):
    for file in pdf_files:
        if file.endswith('.pdf'):
            try:
                print("Merging file %s" % file)
                merger.append(file)
            except FileNotFoundError:
                    print("Skipping file %s" % file)
    print("Writing result file")
    merger.write(target_folder + "Merged.pdf")
    merger.close()

read_files(source_folder)
merge_pdfs(pdfs)