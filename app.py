import argparse

from main import process, convert_pdf

# parser = argparse.ArgumentParser(description='Coversion of Pdf to csv file')
# parser.add_argument('-f', '--pdf_file', type=str, metavar='', required=True, help='Enter the pdf')
# parser.add_argument('-d', '--folder_name', type=str, metavar='', required=True, help='specify the folder name')
# args = parser.parse_args()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Coversion of Pdf to csv file')
    parser.add_argument('-f', '--pdf_file', type=str, metavar='', 
    required=True, help='Enter the pdf path')
    args = parser.parse_args()

    process(args.pdf_file)
    
