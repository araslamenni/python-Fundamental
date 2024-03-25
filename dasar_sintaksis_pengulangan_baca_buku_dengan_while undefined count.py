"""
program pengulangan membaca dengan while sampai paham
"""
jumlah_buku = 10
print('ibu berkata, "baca semua bukumu"')

jumlah_dipahami= 0
print(f"Jumlah buku yang sudah dibaca dan dipahami {jumlah_dipahami}")
jumlah_baca = 0
while jumlah_baca < jumlah_buku * 2:
    jumlah_baca = jumlah_baca + 1
    if jumlah_dipahami == 9:
        print(f'Buku ke {jumlah_dipahami + 1} belum paham')
    else:
        jumlah_dipahami = jumlah_dipahami + 1
        print(f'Buku ke {jumlah_dipahami} sudah dibaca dan dipahami')

print(f'jumlah buku yang sudah dibaca dan dipahami {jumlah_dipahami}')
if jumlah_dipahami == jumlah_buku:
    print('budi berkata, "bu, semua buku sudah dibaca dan dipahami"')
else:
    print(f'Budi berkata, "Bu, tidak semua buku bisa dipahami, '
          f'Budi hanya bisa memahami {jumlah_dipahami} buku saja.')

