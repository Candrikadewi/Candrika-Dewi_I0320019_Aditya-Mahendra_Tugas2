nama_mahasiswa = "Candrika Dewi"
nama_panggilan = "Candrika"
program_studi = "Teknik Industri UNS"
pendidikan = "SMA N 1 Purworejo"

tlahir = 18
blahir = 6
ylahir = 2002
lahir = tlahir + (blahir * 30) + (ylahir * 365)
tsekarang = 12
bsekarang = 3
ysekarang = 2021
sekarang = tsekarang + (bsekarang * 30) + (ysekarang * 365)
tahun = int ((sekarang - lahir) / 365)
bulan = int (((sekarang - lahir)%365) / 30)
hari = int (((sekarang - lahir)%365) % 30)
bulann = (tahun*12) + bulan

Alamat = "RT 02 / RW 03, Bagung, Prembun. Kabupaten Kebumen, Jawa Tengah"
Tinggi_badan = float(158)
Berat_badan = float(50)
Ukuran_sepatu = int(38)
Anak_ke = int(2)
Hobi = "membaca buku, menulis, menonton film, dan mendengarkan musik"

Cold_button = "makanan enak, me time, dan apresiasi"
Current_interest = "Saham, Entrepreneruship, dan Design"
Current_activity = "mengerjakan tugas praktikum program komputer"
Motivational_quotes = "Just be kind and be courage"

print("Dia bernama", nama_mahasiswa)
print("Biasa dipanggil",nama_panggilan)
print("Saat ini ia berusia", bulann,"bulan", hari, "hari")
print("Ia lulus dari",pendidikan,"pada tahun 2020")
print("Candrika saat ini menempuh pendidikan di",program_studi)
print("Alamat rumah Candrika adalah",Alamat)
print("Dia merupakan anak ke",Anak_ke,"dari dua bersaudara")
print("Tinggi badannya",Tinggi_badan,"sentimeter")
print("Berat badannya", Berat_badan,"kilogram")
print("Ukuran sepatunya adalah",Ukuran_sepatu)
print("Candrika memiliki hobi yaitu",Hobi)
print("Hal-hal yang dapat membuatnya bahagia adalah", Cold_button)
print("Saat ini Candrika tertarik dengan", Current_interest)
print("Dan saat ini Candrika sedang", Current_activity)
print("Motto hidupnya adalah", Motivational_quotes)


