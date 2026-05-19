archivo=open("test.txt","a",encoding="utf-8")
for i in range(50000):
    archivo.write("a")
archivo.close