# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Admin(models.Model):
    rid = models.IntegerField(primary_key=True)
    nama = models.CharField(max_length=100)
    nik = models.CharField(max_length=45)
    prodi = models.CharField(max_length=4)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=100)
    level = models.IntegerField()
    sts = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'admin'


class AlumniMengisiDanWaktuTungguDapatKerja(models.Model):
    rid = models.IntegerField(blank=True, null=True)
    nim = models.CharField(max_length=10, blank=True, null=True)
    no_ika = models.CharField(max_length=100, blank=True, null=True)
    nama = models.CharField(max_length=100, blank=True, null=True)
    fid = models.CharField(max_length=4, blank=True, null=True)
    th_lulus = models.TextField(blank=True, null=True)  # This field type is a guess.
    tmp_lhr = models.CharField(max_length=50, blank=True, null=True)
    tgl_lhr = models.DateField(blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)
    no_hp = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    waktu_isi = models.DateTimeField(blank=True, null=True)
    waktu_tunggu_dapat_pekerjaan = models.IntegerField(db_column='Waktu tunggu dapat pekerjaan', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'alumni_mengisi_dan_waktu_tunggu_dapat_kerja'


class BidangPekerjaan(models.Model):
    rid = models.IntegerField()
    Pek_id = models.CharField(max_length=3)
    pilihan = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'bidang_pekerjaan'


class Fakultas(models.Model):
    rid = models.IntegerField()
    fak_id = models.CharField(max_length=1)
    nama = models.CharField(max_length=50)
    nama_singkat = models.CharField(max_length=30)
    publish = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fakultas'


class Feedback(models.Model):
    rid = models.IntegerField()
    nim = models.CharField(max_length=10)
    f20 = models.IntegerField()
    f211 = models.IntegerField()
    f212 = models.IntegerField()
    f213 = models.IntegerField()
    f214 = models.IntegerField()
    f221 = models.IntegerField()
    f222 = models.IntegerField()
    f223 = models.IntegerField()
    f224 = models.IntegerField()
    f225 = models.IntegerField()
    f231 = models.IntegerField()
    f232 = models.IntegerField()
    f233 = models.IntegerField()
    f234 = models.IntegerField()
    f235 = models.IntegerField()
    f24 = models.TextField()
    f25 = models.TextField()

    class Meta:
        managed = False
        db_table = 'feedback'


class Jurusan(models.Model):
    rid = models.IntegerField()
    kode_fak = models.CharField(max_length=1)
    kode_jur = models.CharField(max_length=4)
    nama_jur = models.CharField(max_length=50)
    publish = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jurusan'


class Jurusan3(models.Model):
    rid = models.IntegerField()
    kode_fak = models.CharField(max_length=1)
    kode_jur = models.CharField(max_length=4)
    nama_jur = models.CharField(max_length=50)
    publish = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jurusan3'


class KeaktifanDiOrganisasiMuhammadiyah(models.Model):
    rid = models.IntegerField(blank=True, null=True)
    nim = models.CharField(max_length=10, blank=True, null=True)
    f18 = models.IntegerField(blank=True, null=True)
    f191 = models.IntegerField(blank=True, null=True)
    f192 = models.IntegerField(blank=True, null=True)
    f193 = models.IntegerField(blank=True, null=True)
    f194 = models.IntegerField(blank=True, null=True)
    f195 = models.IntegerField(blank=True, null=True)
    f196 = models.IntegerField(blank=True, null=True)
    f197 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keaktifan di organisasi muhammadiyah'


class Kemuhammadiyahan(models.Model):
    rid = models.IntegerField()
    nim = models.CharField(max_length=10)
    f18 = models.IntegerField()
    f191 = models.IntegerField()
    f192 = models.IntegerField()
    f193 = models.IntegerField()
    f194 = models.IntegerField()
    f195 = models.IntegerField()
    f196 = models.IntegerField()
    f197 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'kemuhammadiyahan'


class Kompetensi(models.Model):
    rid = models.IntegerField()
    nim = models.CharField(max_length=10)
    f171 = models.IntegerField()
    f172 = models.IntegerField()
    f173 = models.IntegerField()
    f174 = models.IntegerField()
    f175 = models.IntegerField()
    f176 = models.IntegerField()
    f177 = models.IntegerField()
    f178 = models.IntegerField()
    f179 = models.IntegerField()
    f1710 = models.IntegerField()
    f1711 = models.IntegerField()
    f1712 = models.IntegerField()
    f1713 = models.IntegerField()
    f1714 = models.IntegerField()
    f1715 = models.IntegerField()
    f1716 = models.IntegerField()
    f1717 = models.IntegerField()
    f1718 = models.IntegerField()
    f1719 = models.IntegerField()
    f1720 = models.IntegerField()
    f1721 = models.IntegerField()
    f1722 = models.IntegerField()
    f1723 = models.IntegerField()
    f1724 = models.IntegerField()
    f1725 = models.IntegerField()
    f1726 = models.IntegerField()
    f1727 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'kompetensi'


class KondisiSaatIni1(models.Model):
    rid = models.IntegerField(blank=True, null=True)
    nim = models.CharField(max_length=10, blank=True, null=True)
    f8 = models.IntegerField(blank=True, null=True)
    f901 = models.IntegerField(blank=True, null=True)
    f902 = models.IntegerField(blank=True, null=True)
    f903 = models.IntegerField(blank=True, null=True)
    f904 = models.IntegerField(blank=True, null=True)
    f905 = models.IntegerField(blank=True, null=True)
    f906 = models.CharField(max_length=255, blank=True, null=True)
    f101 = models.IntegerField(blank=True, null=True)
    f102 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kondisi_saat_ini_1'


class KondisiSaatIniDanKesesuaianBidangPekerjaan(models.Model):
    rid = models.IntegerField(blank=True, null=True)
    nim = models.CharField(max_length=10, blank=True, null=True)
    f111 = models.IntegerField(blank=True, null=True)
    f112 = models.CharField(max_length=255, blank=True, null=True)
    f12 = models.IntegerField(blank=True, null=True)
    f13 = models.IntegerField(blank=True, null=True)
    f14 = models.IntegerField(blank=True, null=True)
    f15 = models.IntegerField(blank=True, null=True)
    f161 = models.IntegerField(blank=True, null=True)
    f162 = models.IntegerField(blank=True, null=True)
    f163 = models.IntegerField(blank=True, null=True)
    f164 = models.IntegerField(blank=True, null=True)
    f165 = models.IntegerField(blank=True, null=True)
    f166 = models.IntegerField(blank=True, null=True)
    f167 = models.IntegerField(blank=True, null=True)
    f168 = models.IntegerField(blank=True, null=True)
    f169 = models.IntegerField(blank=True, null=True)
    f1610 = models.IntegerField(blank=True, null=True)
    f1611 = models.IntegerField(blank=True, null=True)
    f1612 = models.IntegerField(blank=True, null=True)
    f1613 = models.IntegerField(blank=True, null=True)
    f1614 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kondisi_saat_ini_dan_kesesuaian_bidang_pekerjaan'


class KondisiSekarang1(models.Model):
    rid = models.IntegerField()
    nim = models.CharField(max_length=10)
    f8 = models.IntegerField()
    f901 = models.IntegerField()
    f902 = models.IntegerField()
    f903 = models.IntegerField()
    f904 = models.IntegerField()
    f905 = models.IntegerField()
    f906 = models.CharField(max_length=255)
    f101 = models.IntegerField()
    f102 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'kondisi_sekarang1'


class Kontribusi(models.Model):
    rid = models.IntegerField()
    nim = models.CharField(max_length=10)
    f171 = models.IntegerField()
    f172 = models.IntegerField()
    f173 = models.IntegerField()
    f174 = models.IntegerField()
    f175 = models.IntegerField()
    f176 = models.IntegerField()
    f177 = models.IntegerField()
    f178 = models.IntegerField()
    f179 = models.IntegerField()
    f1710 = models.IntegerField()
    f1711 = models.IntegerField()
    f1712 = models.IntegerField()
    f1713 = models.IntegerField()
    f1714 = models.IntegerField()
    f1715 = models.IntegerField()
    f1716 = models.IntegerField()
    f1717 = models.IntegerField()
    f1718 = models.IntegerField()
    f1719 = models.IntegerField()
    f1720 = models.IntegerField()
    f1721 = models.IntegerField()
    f1722 = models.IntegerField()
    f1723 = models.IntegerField()
    f1724 = models.IntegerField()
    f1725 = models.IntegerField()
    f1726 = models.IntegerField()
    f1727 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'kontribusi'


class KontribusiPerguruanTinggiDalamHalMeningkatkanKompetensi(models.Model):
    rid = models.IntegerField(blank=True, null=True)
    nim = models.CharField(max_length=10, blank=True, null=True)
    f171 = models.IntegerField(blank=True, null=True)
    f172 = models.IntegerField(blank=True, null=True)
    f173 = models.IntegerField(blank=True, null=True)
    f174 = models.IntegerField(blank=True, null=True)
    f175 = models.IntegerField(blank=True, null=True)
    f176 = models.IntegerField(blank=True, null=True)
    f177 = models.IntegerField(blank=True, null=True)
    f178 = models.IntegerField(blank=True, null=True)
    f179 = models.IntegerField(blank=True, null=True)
    f1710 = models.IntegerField(blank=True, null=True)
    f1711 = models.IntegerField(blank=True, null=True)
    f1712 = models.IntegerField(blank=True, null=True)
    f1713 = models.IntegerField(blank=True, null=True)
    f1714 = models.IntegerField(blank=True, null=True)
    f1715 = models.IntegerField(blank=True, null=True)
    f1716 = models.IntegerField(blank=True, null=True)
    f1717 = models.IntegerField(blank=True, null=True)
    f1718 = models.IntegerField(blank=True, null=True)
    f1719 = models.IntegerField(blank=True, null=True)
    f1720 = models.IntegerField(blank=True, null=True)
    f1721 = models.IntegerField(blank=True, null=True)
    f1722 = models.IntegerField(blank=True, null=True)
    f1723 = models.IntegerField(blank=True, null=True)
    f1724 = models.IntegerField(blank=True, null=True)
    f1725 = models.IntegerField(blank=True, null=True)
    f1726 = models.IntegerField(blank=True, null=True)
    f1727 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kontribusi perguruan tinggi dalam hal meningkatkan kompetensi'


class Kuisioner(models.Model):
    rid = models.IntegerField()
    kode_jur = models.CharField(max_length=4)
    thn_lulus = models.TextField()  # This field type is a guess.
    f1 = models.CharField(max_length=15)
    f2a = models.CharField(max_length=60)
    f2b = models.CharField(max_length=15, blank=True, null=True)
    f2c = models.CharField(max_length=50, blank=True, null=True)
    f301 = models.IntegerField(blank=True, null=True)
    f302 = models.IntegerField(blank=True, null=True)
    f303 = models.IntegerField(blank=True, null=True)
    f401 = models.IntegerField(blank=True, null=True)
    f402 = models.IntegerField(blank=True, null=True)
    f403 = models.IntegerField(blank=True, null=True)
    f404 = models.IntegerField(blank=True, null=True)
    f405 = models.IntegerField(blank=True, null=True)
    f406 = models.IntegerField(blank=True, null=True)
    f407 = models.IntegerField(blank=True, null=True)
    f408 = models.IntegerField(blank=True, null=True)
    f409 = models.IntegerField(blank=True, null=True)
    f410 = models.IntegerField(blank=True, null=True)
    f411 = models.IntegerField(blank=True, null=True)
    f412 = models.IntegerField(blank=True, null=True)
    f413 = models.IntegerField(blank=True, null=True)
    f414 = models.IntegerField(blank=True, null=True)
    f415 = models.IntegerField(blank=True, null=True)
    f416 = models.CharField(max_length=255, blank=True, null=True)
    f501 = models.IntegerField(blank=True, null=True)
    f502 = models.IntegerField(blank=True, null=True)
    f503 = models.IntegerField(blank=True, null=True)
    f6 = models.IntegerField(blank=True, null=True)
    f7 = models.IntegerField(blank=True, null=True)
    f8 = models.IntegerField(blank=True, null=True)
    f901 = models.IntegerField(blank=True, null=True)
    f902 = models.IntegerField(blank=True, null=True)
    f903 = models.IntegerField(blank=True, null=True)
    f904 = models.IntegerField(blank=True, null=True)
    f905 = models.IntegerField(blank=True, null=True)
    f906 = models.CharField(max_length=255, blank=True, null=True)
    f1001 = models.IntegerField(blank=True, null=True)
    f1002 = models.CharField(max_length=50, blank=True, null=True)
    f1101 = models.IntegerField(blank=True, null=True)
    f1102 = models.CharField(max_length=100, blank=True, null=True)
    f12 = models.IntegerField(blank=True, null=True)
    f1301 = models.IntegerField(blank=True, null=True)
    f1302 = models.IntegerField(blank=True, null=True)
    f1303 = models.IntegerField(blank=True, null=True)
    f14 = models.IntegerField(blank=True, null=True)
    f15 = models.IntegerField(blank=True, null=True)
    f1601 = models.IntegerField(blank=True, null=True)
    f1602 = models.IntegerField(blank=True, null=True)
    f1603 = models.IntegerField(blank=True, null=True)
    f1604 = models.IntegerField(blank=True, null=True)
    f1605 = models.IntegerField(blank=True, null=True)
    f1606 = models.IntegerField(blank=True, null=True)
    f1607 = models.IntegerField(blank=True, null=True)
    f1608 = models.IntegerField(blank=True, null=True)
    f1609 = models.IntegerField(blank=True, null=True)
    f1610 = models.IntegerField(blank=True, null=True)
    f1611 = models.IntegerField(blank=True, null=True)
    f1612 = models.IntegerField(blank=True, null=True)
    f1613 = models.IntegerField(blank=True, null=True)
    f1614 = models.CharField(max_length=100, blank=True, null=True)
    f1701 = models.IntegerField(blank=True, null=True)
    f1702 = models.IntegerField(blank=True, null=True)
    f1703 = models.IntegerField(blank=True, null=True)
    f1704 = models.IntegerField(blank=True, null=True)
    f1705 = models.IntegerField(blank=True, null=True)
    f1706 = models.IntegerField(blank=True, null=True)
    f1707 = models.IntegerField(blank=True, null=True)
    f1708 = models.IntegerField(blank=True, null=True)
    f1709 = models.IntegerField(blank=True, null=True)
    f1710 = models.IntegerField(blank=True, null=True)
    f1711 = models.IntegerField(blank=True, null=True)
    f1712 = models.IntegerField(blank=True, null=True)
    f1713 = models.IntegerField(blank=True, null=True)
    f1714 = models.IntegerField(blank=True, null=True)
    f1715 = models.IntegerField(blank=True, null=True)
    f1716 = models.IntegerField(blank=True, null=True)
    f1717 = models.IntegerField(blank=True, null=True)
    f1718 = models.IntegerField(blank=True, null=True)
    f1719 = models.IntegerField(blank=True, null=True)
    f1720 = models.IntegerField(blank=True, null=True)
    f1721 = models.IntegerField(blank=True, null=True)
    f1722 = models.IntegerField(blank=True, null=True)
    f1723 = models.IntegerField(blank=True, null=True)
    f1724 = models.IntegerField(blank=True, null=True)
    f1725 = models.IntegerField(blank=True, null=True)
    f1726 = models.IntegerField(blank=True, null=True)
    f1727 = models.IntegerField(blank=True, null=True)
    f1728 = models.IntegerField(blank=True, null=True)
    f1729 = models.IntegerField(blank=True, null=True)
    f1730 = models.IntegerField(blank=True, null=True)
    f1731 = models.IntegerField(blank=True, null=True)
    f1732 = models.IntegerField(blank=True, null=True)
    f1733 = models.IntegerField(blank=True, null=True)
    f1734 = models.IntegerField(blank=True, null=True)
    f1735 = models.IntegerField(blank=True, null=True)
    f1736 = models.IntegerField(blank=True, null=True)
    f1737 = models.IntegerField(blank=True, null=True)
    f1738 = models.IntegerField(blank=True, null=True)
    f1739 = models.IntegerField(blank=True, null=True)
    f1740 = models.IntegerField(blank=True, null=True)
    f1741 = models.IntegerField(blank=True, null=True)
    f1742 = models.IntegerField(blank=True, null=True)
    f1743 = models.IntegerField(blank=True, null=True)
    f1744 = models.IntegerField(blank=True, null=True)
    f1745 = models.IntegerField(blank=True, null=True)
    f1746 = models.IntegerField(blank=True, null=True)
    f1747 = models.IntegerField(blank=True, null=True)
    f1748 = models.IntegerField(blank=True, null=True)
    f1749 = models.IntegerField(blank=True, null=True)
    f1750 = models.IntegerField(blank=True, null=True)
    f1751 = models.IntegerField(blank=True, null=True)
    f1752 = models.IntegerField(blank=True, null=True)
    f1753 = models.IntegerField(blank=True, null=True)
    f1754 = models.IntegerField(blank=True, null=True)
    f18 = models.IntegerField(blank=True, null=True)
    f19 = models.IntegerField(blank=True, null=True)
    tgl = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'kuisioner'


class MasukanAtauSaranUntukProgramStudi(models.Model):
    rid = models.IntegerField(blank=True, null=True)
    nim = models.CharField(max_length=10, blank=True, null=True)
    f20 = models.IntegerField(blank=True, null=True)
    f211 = models.IntegerField(blank=True, null=True)
    f212 = models.IntegerField(blank=True, null=True)
    f213 = models.IntegerField(blank=True, null=True)
    f214 = models.IntegerField(blank=True, null=True)
    f221 = models.IntegerField(blank=True, null=True)
    f222 = models.IntegerField(blank=True, null=True)
    f223 = models.IntegerField(blank=True, null=True)
    f224 = models.IntegerField(blank=True, null=True)
    f225 = models.IntegerField(blank=True, null=True)
    f231 = models.IntegerField(blank=True, null=True)
    f232 = models.IntegerField(blank=True, null=True)
    f233 = models.IntegerField(blank=True, null=True)
    f234 = models.IntegerField(blank=True, null=True)
    f235 = models.IntegerField(blank=True, null=True)
    f24 = models.TextField(blank=True, null=True)
    f25 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'masukan atau saran untuk program studi'


class MencariPekerjaan(models.Model):
    rid = models.IntegerField()
    nim = models.CharField(max_length=10)
    f3 = models.IntegerField()
    f401 = models.IntegerField()
    f402 = models.IntegerField()
    f403 = models.IntegerField()
    f404 = models.IntegerField()
    f405 = models.IntegerField()
    f406 = models.IntegerField()
    f407 = models.IntegerField()
    f408 = models.IntegerField()
    f409 = models.IntegerField()
    f410 = models.IntegerField()
    f411 = models.IntegerField()
    f412 = models.IntegerField()
    f413 = models.IntegerField()
    f414 = models.IntegerField()
    f415 = models.IntegerField()
    f416 = models.CharField(max_length=255)
    f5 = models.IntegerField()
    f6 = models.IntegerField()
    f7 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mencari_pekerjaan'


class MencariPekerjaanDanMendapatkanPekerjaanPertama(models.Model):
    rid = models.IntegerField(blank=True, null=True)
    nim = models.CharField(max_length=10, blank=True, null=True)
    f3 = models.IntegerField(blank=True, null=True)
    f401 = models.IntegerField(blank=True, null=True)
    f402 = models.IntegerField(blank=True, null=True)
    f403 = models.IntegerField(blank=True, null=True)
    f404 = models.IntegerField(blank=True, null=True)
    f405 = models.IntegerField(blank=True, null=True)
    f406 = models.IntegerField(blank=True, null=True)
    f407 = models.IntegerField(blank=True, null=True)
    f408 = models.IntegerField(blank=True, null=True)
    f409 = models.IntegerField(blank=True, null=True)
    f410 = models.IntegerField(blank=True, null=True)
    f411 = models.IntegerField(blank=True, null=True)
    f412 = models.IntegerField(blank=True, null=True)
    f413 = models.IntegerField(blank=True, null=True)
    f414 = models.IntegerField(blank=True, null=True)
    f415 = models.IntegerField(blank=True, null=True)
    f416 = models.CharField(max_length=255, blank=True, null=True)
    f5 = models.IntegerField(blank=True, null=True)
    f6 = models.IntegerField(blank=True, null=True)
    f7 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mencari_pekerjaan_dan_mendapatkan_pekerjaan_pertama'


class PekerjaanSekarang(models.Model):
    rid = models.IntegerField()
    nim = models.CharField(max_length=10)
    f111 = models.IntegerField()
    f112 = models.CharField(max_length=255)
    f12 = models.IntegerField()
    f13 = models.IntegerField()
    f14 = models.IntegerField()
    f15 = models.IntegerField()
    f161 = models.IntegerField()
    f162 = models.IntegerField()
    f163 = models.IntegerField()
    f164 = models.IntegerField()
    f165 = models.IntegerField()
    f166 = models.IntegerField()
    f167 = models.IntegerField()
    f168 = models.IntegerField()
    f169 = models.IntegerField()
    f1610 = models.IntegerField()
    f1611 = models.IntegerField()
    f1612 = models.IntegerField()
    f1613 = models.IntegerField()
    f1614 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'pekerjaan_sekarang'


class Profil(models.Model):
    rid = models.IntegerField(primary_key=True)
    nim = models.CharField(max_length=10)
    no_ika = models.CharField(max_length=100)
    nama = models.CharField(max_length=100)
    fid = models.CharField(max_length=4)
    th_lulus = models.TextField()  # This field type is a guess.
    tmp_lhr = models.CharField(max_length=50)
    tgl_lhr = models.DateField()
    alamat = models.TextField()
    no_hp = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    waktu_isi = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'profil'


class ProfilDel1(models.Model):
    max_pekerjaan_sekarang_rid_field = models.IntegerField(db_column='Max(pekerjaan_sekarang.rid)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    nim = models.CharField(max_length=10, blank=True, null=True)
    jum = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profil del 1'
