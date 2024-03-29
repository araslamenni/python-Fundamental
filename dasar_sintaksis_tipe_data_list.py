daftar_buku = ['lord of the rings', "kisah sang kancil", "hiduplah sepenuhnya", 'sesuatu yang hilang darimu']
print('Tampilkan semua isi dari daftar_buku')
print(daftar_buku)

print('\nproses semua dengan for in')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampilkan dengan for in range')
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku =[1, 'kenji volume 1', -313, 3.14]
print('\nTampilkan dengan for in range, dimana tipe data tiap element berbeda2')
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nkembalikan nilai awal daftar_buku')
daftar_buku = ['lord of the rings', "kisah sang kancil", "hiduplah sepenuhnya", 'sesuatu yang hilang darimu']
print('\ntambahkan 1 buku baru')
daftar_buku.append('tunggu hujan berhenti dulu')
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])


print('\nClear list')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print('\nGanti elemen pertama')
daftar_buku = ['lord of the rings', "kisah sang kancil", "hiduplah sepenuhnya", 'sesuatu yang hilang darimu']
daftar_buku[0] = 'lord of the kings'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print('\nAmbil elemen ke-2')
buku = daftar_buku.pop(1)
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nBuku yang diambli tadi')
print(buku)


print('\nPop')
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print('\nPop -1')
daftar_buku = ['lord of the rings', "kisah sang kancil", "hiduplah sepenuhnya", 'sesuatu yang hilang darimu']
daftar_buku.pop(-1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print('\nPerintah del')
daftar_buku = ['lord of the rings', "kisah sang kancil", "hiduplah sepenuhnya", 'sesuatu yang hilang darimu']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension')
daftar_buku = ['lord of the rings', "kisah sang kancil", "hiduplah sepenuhnya", 'sesuatu yang hilang darimu']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension start')
daftar_buku = ['lord of the rings', "kisah sang kancil", "hiduplah sepenuhnya", 'sesuatu yang hilang darimu']
del daftar_buku[0:-2]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension start2')
daftar_buku = ['lord of the rings', "kisah sang kancil", "hiduplah sepenuhnya", 'sesuatu yang hilang darimu']
del daftar_buku[0::2]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])













