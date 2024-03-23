"""
Semua sintaksis dasar bahasa pemograman terdiri dari:
1.Sekuensial: langkah terurut
2.Percabangan: langkah melompat jika kondisi terpenuhi
3.Perulangan: mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

#Sekuensial
print ('Ibu berkata, "pergi ke toko"')
print('Budi menjawab, "Baik, apa yang harus saya lakukan di toko?"')
print('Ibu menjawab, "Beli satu botol susu, dan jika ada telor beli 6')
print('Maka Budi berangkat ke toko')
print('Dan mulai berbelanja')

#Percabangan
jumlah_botol_susu= 173
jumlah_telur = 1587
print(f"jumlah botol susu {jumlah_botol_susu} btl")
print(f"jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print("Budi mengecek harganya, dan ternyta uangnya cukup")
    print("Budi membeli sebotol susu")
    if jumlah_telur == 0:
        print("Budi membeli sebotol susu")
        print("Budi membeli telur")
else:
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi pulang ke rumah")
print("Menyerahkan hasil belanjaan kepada ibu")



