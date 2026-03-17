from pypdf import PdfWriter

merger = PdfWriter()

pdf_Lists = ["AI for Everyone Certificate Coursera(DeepLearning.AI).pdf" , "Bits and Bytes Certificate Cousera(Google).pdf" , "Foundations Data, Data, Everywhere Certificate Coursera(Google).pdf",
              "GenAI Certificate Coursera(IBM).pdf" , "Java Certificate Coursera(IBM).pdf" , "Java Certificate Coursera(IBM).pdf"]

for pdf in pdf_Lists:
     merger.append(pdf)

merger.write("All Merged.pdf")

merger.close()

# After running this code you will see the file is being created named (All Merged.pdf) that will contain the content of the all pdfs combined 
# note this i added my coursera certificates as an pdf becouse i dont had any sample pdf. so this can be also done with the text pdfs