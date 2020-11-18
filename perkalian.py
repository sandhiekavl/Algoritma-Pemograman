def perkalian (n) :
    hasil = 1 
    for x in n :
        hasil = hasil * x
    return hasil

a = list(map(int, input('angka? ').split()))
print (a)
print (perkalian(a))