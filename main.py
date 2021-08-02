from geometri.bangunruang.krucut import luas_krucut, volume_krucut
from geometri.bangunruang.bola import luas_bola, volume_bola
from aritmatika.aritmatika import pengurangan, penjumlahan, perkalian
import geometri.bangundatar.persegi
import geometri.bangundatar.persegipanjang

import geometri.bangunruang.balok
import geometri.bangunruang.kubus

import geometri.bangundatar.belah_ketupat
import geometri.bangundatar.segitiga


from geometri.bangunruang import * 

satu = 1
dua = 2

print("penjumlahan",penjumlahan(satu,dua))
print("perkalian",perkalian(satu,dua))
print("pengurangan",pengurangan(satu,dua))


sisi = 10
panjang = 12
lebar = 10
print("luas persegi",geometri.bangundatar.persegi.luas_persegi(sisi))
print("keliling persegi",geometri.bangundatar.persegi.keliling_persegi(sisi))

print("luas persegi panjang",geometri.bangundatar.persegipanjang.luas_persegi_panjang(panjang,lebar))
print("keliling persegi panjang",geometri.bangundatar.persegipanjang.keliling_persegi_panjang(panjang,lebar))


print("luas belah ketupat : ", geometri.bangundatar.belah_ketupat.luas_belah_ketupat(d1=10))
print("keliling belah ketupat : ", geometri.bangundatar.belah_ketupat.keliling_belah_ketupat(sisi))


print("luas segitiga :", geometri.bangundatar.segitiga.luas_segitiga(alas=10, tinggi=20))
print("keliling segitiga :", geometri.bangundatar.segitiga.keliling_segitiga(sisi))


print("=========================================================")

print("luas balok", geometri.bangunruang.balok.luas_balok(panjang_balok=10,lebar_balok=12,tinggi_balok=22))
print("valoume balok",geometri.bangunruang.balok.volume_balok(panjang_balok=12,lebar_balok=44, tinggi_balok=12))


print("luas kubus",geometri.bangunruang.kubus.luas_kubus(sisi))
print("volume kubus", geometri.bangunruang.kubus.volume_kubus(sisi))


print("luas bola : ", luas_bola(jari_jari=10))
print("volume bola :", volume_bola(jari_jari=30))

print('Luas krucut :', luas_krucut(jari_jari_krucut=34, sisi_krucut=34))
print("volume krucut :", volume_krucut(jari_jari_krucut=23, tinggi_krucut=12))
