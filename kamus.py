import sys

kata =  ["kaji,sia,maneng,mangan,tunung"]
print("masukkan kata: ",end= '')
kata = str(input())

if kata ==  "kamu":
    print ("kaji")
elif kata ==  "saya":
    print("sia")
elif kata == "mandi" :
    print("maneng")
elif kata == "mangan" :
    print("makan")
elif kata == "tidur" :
    print("tunung")
else:
    print("tidak terdeteksi")
    sys.exit()

print()

