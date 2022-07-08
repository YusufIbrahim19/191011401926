def down(x, xmin, xmax):
    return (xmax - x) / (xmax - xmin)


def up(x, xmin, xmax):
    return (x - xmin) / (xmax - xmin)


class TinggiBadan():
    sangatpendek = 130
    pendek = 150
    tinggi = 170
    sangattinggi = 190

    def SangatPendek(self, x):
        if x >= self.pendek:
            return 0
        elif x <= self.sangatpendek:
            return 1
        else:
            return down(x, self.sangatpendek, self.pendek)

    def SangatTinggi(self, x):
        if x >= self.sangattinggi:
            return 1
        elif x <= self.tinggi:
            return 0
        else:
            return up(x, self.tinggi, self.sangattinggi)

    def Pendek(self, x):
        if x >= self.sangattinggi or x <= self.sangatpendek:
            return 0
        elif self.sangatpendek < x < self.pendek:
            return up(x, self.sangatpendek, self.pendek)
        elif self.pendek < x < self.tinggi:
            return down(x, self.pendek, self.tinggi)
        elif self.tinggi < x < self.sangattinggi:
            return down(x, self.tinggi, self.sangattinggi)
        else:
            return 1

    def Tingi(self, x):
        if x >= self.sangattinggi or x <= self.sangatpendek:
            return 0
        elif self.sangatpendek < x < self.pendek:
            return up(x, self.sangatpendek, self.pendek)
        elif self.pendek < x < self.tinggi:
            return up(x, self.pendek, self.tinggi)
        elif self.tinggi < x < self.sangattinggi:
            return down(x, self.tinggi, self.sangattinggi)
        else:
            return 1


class BeratBadan():
    ringan = 40
    sedang = 60
    berat = 80

    def Ringan(self, x):
        if x >= self.sedang:
            return 0
        elif x <= self.ringan:
            return 1
        else:
            return down(x, self.ringan, self.sedang)

    def Berat(self, x):
        if x >= self.berat:
            return 1
        elif x <= self.sedang:
            return 0
        else:
            return up(x, self.sedang, self.berat)

    def Sedang(self, x):
        if x >= self.berat or x <= self.ringan:
            return 0
        elif self.ringan < x < self.sedang:
            return up(x, self.ringan, self.sedang)
        elif self.sedang < x < self.berat:
            return down(x, self.sedang, self.berat)
        else:
            return 1


class Postur():
    palingbesar = 82
    sedang = 54
    palingkecil = 35
    tinggibadan = 176
    beratbadan = 63

    def _kecil(self, a):
        return self.sedang - a*(self.sedang - self.palingkecil)

    def kecil_sedang(self, a):
        return a*(self.sedang - self.palingkecil) + self.palingkecil

    def sedang_besar(self, a):
        return self.palingbesar - a*(self.palingbesar - self.sedang)

    def _besar(self, a):
        return a*(self.palingbesar - self.sedang) + self.sedang

    def _inferensi(self, tb=TinggiBadan(), bb=BeratBadan()):
        Hasil = []

        # [R1] JIKA Tinggi Badan SANGAT PENDEK, dan Berat Badan BERAT, MAKA
        # Postur Badan Harusnya Lebih KECIL.
        a1 = min(tb.SangatPendek(self.tinggibadan), bb.Berat(self.beratbadan))
        z1 = self._kecil(a1)
        Hasil.append((a1, z1))
        # [R2] JIKA Tinggi Badan SANGAT PENDEK, dan Berat Badan SEDANG, MAKA
        # Postur Badan Harusnya Lebih KECIL.
        a2 = min(tb.SangatPendek(self.tinggibadan), bb.Sedang(self.beratbadan))
        z2 = self._kecil(a2)
        Hasil.append((a2, z2))
        # [R3] JIKA Tinggi Badan SANGAT PENDEK, dan Berat Badan Ringan, MAKA
        # Postur Badan Harusnya Lebih KECIL.
        a3 = min(tb.SangatPendek(self.tinggibadan), bb.Ringan(self.beratbadan))
        z3 = self._kecil(a3)
        Hasil.append((a3, z3))
        # [R4] JIKA Tinggi Badan PENDEK, dan Berat Badan BERAT, MAKA
        # Postur Badan Harusnya Lebih KECIL.
        a4 = min(tb.Pendek(self.tinggibadan), bb.Berat(self.beratbadan))
        z4 = self.kecil_sedang(a4)
        Hasil.append((a4, z4))
        # [R5] JIKA Tinggi Badan PENDEK, dan Berat Badan SEDANG, MAKA
        # Postur Badan Harusnya Lebih KECIL.
        a5 = min(tb.Pendek(self.tinggibadan), bb.Sedang(self.beratbadan))
        z5 = self.kecil_sedang(a5)
        Hasil.append((a5, z5))
        # [R6] JIKA Tinggi Badan PENDEK, dan Berat Badan RINGAN, MAKA
        # Postur Badan Harusnya Lebih BESAR.
        a6 = min(tb.Pendek(self.tinggibadan), bb.Ringan(self.beratbadan))
        z6 = self.kecil_sedang(a6)
        Hasil.append((a6, z6))
        # [R7] JIKA Tinggi Badan TINGGI, dan Berat Badan BERAT, MAKA
        # Postur Badan Harusnya Lebih KECIL.
        a7 = min(tb.Tingi(self.tinggibadan), bb.Berat(self.beratbadan))
        z7 = self.sedang_besar(a7)
        Hasil.append((a7, z7))
        # [R8] JIKA Tinggi Badan TINGGI, dan Berat Badan SEDANG, MAKA
        # Postur Badan Harusnya Lebih BESAR.
        a8 = min(tb.Tingi(self.tinggibadan), bb.Sedang(self.beratbadan))
        z8 = self.sedang_besar(a8)
        Hasil.append((a8, z8))
        # [R9] JIKA Tinggi Badan TINGGI, dan Berat Badan RINGAN, MAKA
        # Postur Badan Harusnya Lebih BESAR.
        a9 = min(tb.Tingi(self.tinggibadan), bb.Ringan(self.beratbadan))
        z9 = self.sedang_besar(a9)
        Hasil.append((a9, z9))
        # [R10] JIKA Tinggi Badan SANGAT TINGGI, dan Berat Badan BERAT, MAKA
        # Postur Badan Harusnya Lebih BESAR.
        a10 = min(tb.SangatTinggi(self.tinggibadan),
                  bb.Berat(self.beratbadan))
        z10 = self._besar(a10)
        Hasil.append((a10, z10))
        # [R11] JIKA Tinggi Badan SANGAT TINGGI, dan Berat Badan SEDANG, MAKA
        # Postur Badan Harusnya Lebih BESAR.
        a11 = min(tb.SangatTinggi(self.tinggibadan),
                  bb.Sedang(self.beratbadan))
        z11 = self._besar(a11)
        Hasil.append((a11, z11))
        # [R12] JIKA Tinggi Badan SANGAT TINGGI, dan Berat Badan RINGAN, MAKA
        # Postur Badan Harusnya Lebih BESAR.
        a12 = min(tb.SangatTinggi(self.tinggibadan),
                  bb.Ringan(self.beratbadan))
        z12 = self._besar(a12)
        Hasil.append((a12, z12))
        return Hasil

    def defuzifikasi(self, data_inferensi=[]):
        # (α1∗z1+α2∗z2+α3∗z3+α4∗z4) / (α1+α2+α3+α4)
        data_inferensi = data_inferensi if data_inferensi else self._inferensi()
        res_a_z = 0
        res_a = 0
        for data in data_inferensi:
            # data[0] = a
            # data[1] = z
            res_a_z += data[0] * data[1]
            res_a += data[0]
        return [res_a_z/res_a, res_a_z, res_a]
