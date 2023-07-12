from pdf2image import convert_from_path

images = convert_from_path(r'C:\Users\wagta\Documents\その他\pdf-to-image-app\gamma.pdf',poppler_path = r"C:\Users\wagta\Documents\その他\pdf-to-image-app\poppler\Library\bin") 
for i in range(len(images)):
          images[i].save('img'+str(i)+'.jpg', 'JPEG')