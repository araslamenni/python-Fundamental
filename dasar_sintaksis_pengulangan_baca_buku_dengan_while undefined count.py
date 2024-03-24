"""
program pengulangan membaca dengan while sampai paham
"""
jumlah_buku = 10
print('ibu berkata, "baca semua bukumu"')

jumlah_buku_yang_sudah_dibaca_dan_dipahami= 0
print(f"Jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami}")
total_jumlah_baca = 0
while total_jumlah_baca < jumlah_buku * 2:
    total_jumlah_baca = total_jumlah_baca + 1
    if jumlah_buku_yang_sudah_dibaca_dan_dipahami == 9:
        print(f'Buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1} belum paham')
    else:
        jumlah_buku_yang_sudah_dibaca_dan_dipahami = jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1
        print(f'Buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami} sudah dibaca dan dipahami')

print(f'jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami}')

