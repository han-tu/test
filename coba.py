pas=str(input("masukkan password: "))
while len(pas) != 8 or pas.isupper() or pas.islower():
    if len(pas) != 8 or pas.isupper() or pas.islower():
        print("password tidak valid \nulangi lagi!!")
    else:
        print("\npassword valid,\nsilakan login")
    pas=str(input("masukkan password: "))   
else:
    print("\npassword valid \nsilakan login")
print("")

passwordlogin=str(input("masukkan password unntuk login: "))
while pas!=passwordlogin:
    if pas!=passwordlogin:
        print("password slah ulangi lagi")
    else:
        print("selamaat anda berhasil login")
    passwordlogin=str(input("masukkan password unntuk login: "))
else:
    print("selamaat anda berhasil login")
    
