
print ("kalkulator versi saya")
print (30*"=")

operator = input ("operator (+,-,*,/,exit):")
satu = float (input("masukan angka1 ="))
dua = float (input("masukkan angka2 ="))

if operator =="+":
    hasil = satu + dua
    print(f"hasilnya adalah{hasil}")
elif operator =="-":
    hasil =  satu - dua
    print(f"hasilnya adalah{hasil}")
elif operator =="*":
    hasil = satu * dua
    print(f"hasilnya adalah{hasil}")
elif operator =="/":
    hasil = satu / dua
    print(f"hasilnya adalah{hasil}")

elif operator =="exit":
    print("selesai")
else :
    print ("perintah tidak dikenali")