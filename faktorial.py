def faktorial (n) :
    if n <= 1:
        return 1 
    return n*faktorial(n-1)


n = int(input('Masukkan angka: '))

print('Faktorial: ',faktorial(n))
