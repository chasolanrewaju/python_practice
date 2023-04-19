text_file= open("text.txt",'w') 
text_file.write ("Hello people")
text_file.close()

text_file= open("text.txt",'a')
text_file.write("How has been our day in Nigeria,Toge and Guinea")
text_file.close()

print (len('text_file.read().split()'))