
import sys

#game tebak nama 
print ("cobalah tebak nama seseorang tersebut")
print (35*"=")

print("")
nama = ["Septi"," Bayu", "Budi", "Tono", "Dika", "Danu", "Anto", "Elga", "Safi", "Anto",]

print("masukkan nama :") 
jawab = str (input())


print("Daftar Nama  : 	")
for a in nama :
    print (a)
print("")
print(35*"=")

if jawab == nama[0]:
    jawaban = jawab
elif jawab == nama[1]:
    jawaban = jawab
elif jawab == nama[2]:
    jawaban = jawab
elif jawab == nama[3]:
    jawaban = jawab
elif jawab == nama[4]:
    jawaban = jawab
elif jawab == nama[5]:
    jawaban = jawab
elif jawab == nama[6]:
    jawaban = jawab
elif jawab == nama[7]:
    jawaban = jawab
elif jawab == nama[8]:
    jawaban = jawab
else :
    print ("tidak ada")
    sys.exit

print ("siapa ya namanya:")#nama yang akan ditebak
tebak = str (input())

if tebak == jawaban:
    print ("selamat anda benar")
else :
    print ("coba lagi")
    print ("kesempatan anda sisa 2")
    print ("siapa ya namanya:")#nama yang akan ditebak
    tebak = str (input())

    if  tebak == jawaban:
        print ("selamat anda benar")
    else :
        print ("coba lagi")
        print ("kesempatan anda sisa 2")
        print ("siapa ya namanya:")#nama yang akan ditebak
        tebak = str (input())

        if tebak == jawaban :
            print ("selamat anda benar")
        else :
            print ("kesempatan")

     

        



    



 



