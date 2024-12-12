import pandas as pd

# Baca data dari Excel
df_excel = pd.read_excel('data.xlsx', sheet_name='data')

# 1. Buat DataFrame dari open data jabar
dframe = pd.DataFrame(df_excel)
print(dframe)

# 2. Hitung total seluruh produksi sampah di tahun tertentu
tahun_tertentu = int(input("\nMasukkan tahun yang di pilih : "))
total_tahun_tertentu = 0

for index, row in dframe.iterrows():
    if row['tahun'] == tahun_tertentu:
        total_tahun_tertentu += row['jumlah_produksi_sampah']

print(f"\nTotal produksi sampah di seluruh Kabupaten/Kota pada tahun {tahun_tertentu} = {total_tahun_tertentu:.2f} ton/hari")

# 3. Jumlahkan data per tahun
total_per_tahun = {}

for index, row in dframe.iterrows():
    tahun = row['tahun']
    if tahun not in total_per_tahun:
        total_per_tahun[tahun] = 0
    total_per_tahun[tahun] += row['jumlah_produksi_sampah']

print("\nTotal produksi sampah di seluruh Kabupaten/Kota per tahun:")
for tahun, total in total_per_tahun.items():
    print(f"Tahun {tahun} = {total:.2f} ton/hari")

# 4. Jumlahkan data per Kota/Kabupaten per tahun
total_per_kota_tahun = {}

for index, row in dframe.iterrows():
    kota = row['nama_kabupaten_kota']
    tahun = row['tahun']
    key = (kota, tahun)
    if key not in total_per_kota_tahun:
        total_per_kota_tahun[key] = 0
    total_per_kota_tahun[key] += row['jumlah_produksi_sampah']

print("\nTotal produksi sampah per Kota/Kabupaten per tahun:")
for (kota, tahun), total in total_per_kota_tahun.items():
    print(f"{kota}, Tahun {tahun} = {total:.2f} ton/hari")

# Export ke CSV
x = dframe.to_csv("produksi_sampah_hasil.csv", index=False)
print("\nData berhasil diexport ke CSV", x)

# Export ke Excel
y = dframe.to_excel("produksi_sampah_hasil.xlsx", index=False)
print("\nData berhasil diexport ke Excel", y)
