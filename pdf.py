import PyPDF2 as p
file=open("C:/Users/Dell/Downloads/mgt_f1_4.pdf","rb")
pd=p.PdfFileReader(file)
x=pd.getPage(0)
y=pd.getPage(2)
#print(x.extracttext())
print(y.extractText())
