harga_laptop = int(input("Masukkan harga laptop: "))
masa_pakai = int(input("Masukkan masa pakai barang (tahun): "))
masa_manfaat = int(input("Masukkan masa manfaat barang (tahun): "))
nilai_sisa = int(input("Masukkan nilai barang setelah masa manfaat habis: "))

susut_tahunan = (harga_laptop - nilai_sisa)/masa_manfaat
harga_susut = susut_tahunan*masa_pakai
nilai_aset_sisa = harga_laptop-harga_susut

print("Nilai sisa barang adalah ",nilai_aset_sisa)
