import easyocr # ---- Module for detecting the text from the image
import cv2 as cv #----- Module for image analysis
import matplotlib.pyplot as plt#--- Module for graphical analysis of information
import numpy as np # ------Module for arrays or matrix manipulations
from fpdf import FPDF
import os

'''
Program for detecting and identifying text from image format jpg,png
1. Python program to identify and extract words from these selected images.
2. Python program for enhancing the report with visuals (e.g., bar chart, line chart).
3. The count statistics of each word identified by the OCR.
4. Python program for generating a single-page report document.
'''

class BonusTask:
    def __init__(self, result, user_input, wordcount, word_found):
        self.result = result
        self.user_input = user_input
        self.wordcount = wordcount
        self.word_found = word_found
        self.total_words = self.get_total_words()
        self.user_input_percentage = (self.wordcount / sum(self.total_words.values())) * 100 if sum(self.total_words.values()) > 0 else 0

    def get_total_words(self):
        total_words=dict()
        for i in range(len(result)):
            length=len(result[i][1].split())
            to_split=result[i][1].split()
            for j in range(length):
                total_words[to_split[j].lower()]=0
        if word_found==True:
            total_words[self.user_input]=wordcount
        return total_words

    def bar_graph(self):
        plt.figure(figsize=(10, 5))
        plt.bar(self.total_words.keys(), self.total_words.values(), color='black')
        plt.xlabel('Words')
        plt.ylabel('Counts')
        plt.title('Occurrences of Words in Image')
        plt.xticks(rotation=45)
        bargraph_path = os.path.join("C:\\Users\\CHARAN\\OneDrive\\Desktop\\Assignment_Taks", "bargraph.png")
        plt.savefig(bargraph_path)
        plt.close()
        return bargraph_path

    def line_graph(self):
        plt.figure(figsize=(10, 5))
        plt.plot(list(self.total_words.keys()), list(self.total_words.values()), color='black', marker='o', linestyle='-')
        plt.xlabel('Words')
        plt.ylabel('Counts')
        plt.title('Occurrences of Words in Image')
        plt.xticks(rotation=45)
        linegraph_path = os.path.join("C:\\Users\\CHARAN\\OneDrive\\Desktop\\Assignment_Taks", "linegraph.png")
        plt.savefig(linegraph_path)
        plt.close()
        return linegraph_path

    def generate_pdf(self, bargraph_path, linegraph_path):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="OCR Word Count Report", ln=True, align='C')
        pdf.cell(200, 10, txt=f"User Input Word: {self.user_input}", ln=True)
        pdf.cell(200, 10, txt=f"Word Count: {self.wordcount}", ln=True)
        pdf.cell(200, 10, txt=f"Total Words in Image: {sum(self.total_words.values())}", ln=True)
        pdf.cell(200, 10, txt=f"Percentage of User Input Word: {self.user_input_percentage:.2f}%", ln=True)
        
        for i, (word, count) in enumerate(self.total_words.items(), start=1):
            pdf.cell(200, 10, txt=f"{i}. {word}: {count}", ln=True)

        pdf.cell(200, 10, txt=f"Total Words count in Image: {len(self.total_words)}", ln=True)

        # Add the bar chart and line chart images to the PDF
        pdf.image(bargraph_path, x=10, y=100, w=180)
        pdf.add_page()  # Adding a new page for the line graph
        pdf.image(linegraph_path, x=10, y=10, w=180)

        output_file = os.path.join("C:\\Users\\CHARAN\\OneDrive\\Desktop\\Assignment_Taks", "OCR_Report.pdf")
        pdf.output(output_file)
        print(f"PDF report has been saved to: {output_file}")

# Path of the image file
img_path = "C:\\Users\\CHARAN\\OneDrive\\Desktop\\example_images\\images.png"

reader = easyocr.Reader(['en'], gpu=False)
result = reader.readtext(img_path)

# User input and defining the word count that is the number of occurrences of the word found in the image file
word_found = False
wordcount = 0
user_input = input("Enter the word you want from the image: ").lower()

for detection in result:
    text = detection[1].lower()
    if user_input in text.split():
        wordcount += 1
        word_found = True

if not word_found:
    print(f"The word {user_input} does not exist in the image")
else:
    print(f"The word {user_input} is found in the selected image and the count of the word is {wordcount}")

# Create an instance of the class
report = BonusTask(result, user_input, wordcount, word_found)

# Generate the bar chart and line chart and get the file paths
bargraph_path = report.bar_graph()
linegraph_path = report.line_graph()

# Generate the PDF report
report.generate_pdf(bargraph_path, linegraph_path)
