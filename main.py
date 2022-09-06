from PIL import Image
import pytesseract as pt
import os
from pdf2image import convert_from_path
import csv
import glob
import pandas as pd
import argparse

# Part 1 - Pdf to Image

def convert_pdf(path):
    """
    This convert the pdf file to images which page by page, it will take path for pdf file 
    and return the page with count and its respective file path.

    :param path: string, file location or pdf location
    :return: page_count, path
    """
    pages = convert_from_path(path)
    page_count = 1

    # check whether the folder is present or not
    # if not present create with the file name
    if not os.path.isdir(path.split(".")[0]):
        os.mkdir(path.split(".")[0])
    
    for page in pages:
        file_name = path.split(".")[0] + "_" + str(page_count) + ".png"
        file_path = os.path.join(path.split(".")[0], file_name)
        # print("1", file_name)
        page.save(file_path, 'PNG')
        page_count += 1
    return page_count, path

# Part 2 - Image to Text

def image_to_text(page_count, path):
    """
    :param page_count: int, page count
    :param path: string, path of pdf
    :return: image_data
    """
    # path = "/home/deepak/Documents/pdf2image/f1/f1_image"
    # tempPath = "/home/deepak/Documents/pdf2image/f1/f1_text/"
    # for imageName in os.listdir(path):
    #     inputpath = os.path.join(path, imageName)
    #     text = pt.image_to_string(Image.open(inputpath))
    #     imageName = imageName[0:-4]
    #     fulltemppath = os.path.join(tempPath, 'page_'+imageName+".txt")
    #     # print(text)
    #     file1 = open(fulltemppath, "w")
    #     file1.write(text)
    #     file1.close()
    
    image_data = {}
    for i in range(1, page_count):
        file_name = path.split(".")[0] + "_" + str(i) + ".png"
        # print("2", file_name)
        # print("3", path.split(".")[0] + "/" + file_name)
        text = str(pt.image_to_string(path.split(".")[0] + "/" + file_name))
        image_data[i] = text
    return image_data

# Part 3 - Text to CSV

def text_to_csv(image_data, path):
    """
    Thie will take the dictonary and convert it to dataframe and ultimately convert to csv.
    :param image_data: dict, dictonary from the image
    :param path: string, pdf location
    :return: file_path


    """

    # files = sorted(
    #     glob.glob('/home/deepak/Documents/pdf2image/f1/f1_text/*.txt'))
    # dfs = []

    # for file in files:
    #     df = pd.read_csv(file, sep='\t', lineterminator='\r')
    #     dfs.append(df)
    # df = pd.concat(dfs, axis=1)
    # df.to_csv('/home/deepak/Documents/pdf2image/f1/output.csv')

    df = pd.Series(image_data).to_frame()
    df.to_csv(path.split(".")[0] + ".csv")
    file_path = path.split(".")[0] + ".csv"
    return file_path

def process(pdf_file):
    """
    First process will return page count and pdf file with calling convert pdf function.
    :param pdf_file: string, pdf file location
    
    """
    page_count, pdf_file = convert_pdf(pdf_file)

    image_data = image_to_text(page_count, pdf_file)

    file_path = text_to_csv(image_data, pdf_file)
    print(file_path)