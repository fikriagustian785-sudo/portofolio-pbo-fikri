class PenontonKonser:
    # Class Attributes
    nama = ""
    kota = ""
    band = ""

    # Methods
    def perkenalan(self):
        print(f"Halo, nama saya {self.nama}.")

    def menyapa(self, lawan_bicara):
        print(f"{self.nama}: Hai {lawan_bicara.nama}, seru banget ya konsernya!")

    def asal_kota(self, lawan_bicara):
        print(f"{self.nama}: Aku jauh-jauh datang dari {self.kota} nih. Kalau kamu {lawan_bicara.nama}?")
        print(f"{lawan_bicara.nama}: Wah keren! Kalau aku asli dari {lawan_bicara.kota}.")

    def membahas_band(self, lawan_bicara):
        print(f"{self.nama}: Ngomong-ngomong, band favoritku {self.band}. Kamu suka band apa?")
        print(f"{lawan_bicara.nama}: Kalau aku paling ngefans sama {lawan_bicara.band}!")


# Membuat object (orang1 dan orang2)
orang1 = PenontonKonser()
orang1.nama = "Fikri"
orang1.kota = "Bandung"
orang1.band = "Sheila on 7"

orang2 = PenontonKonser()
orang2.nama = "Lulu"
orang2.kota = "Jakarta"
orang2.band = "Dewa 19"

# Menjalankan program (Simulasi percakapan)
orang1.perkenalan()
orang2.perkenalan()
print("-" * 40)

orang1.menyapa(orang2)
orang1.asal_kota(orang2)
orang1.membahas_band(orang2)
