"""

Soru 4

Üç basamaklı rakamları birbirinden farklı kaç tane sayı olduğunu bulan ve bu
sayıları ekrana yazdıran python kodunu yazınız.

"""

# Rakamları birbirinden farklı üç basamaklı en küçük sayıyı belirledik.
start = 102

# Rakamları farklı birbirinden farklı üç basamaklı en büyük sayıyı belirledik.
end = 987

for i in range(start, end+1):

    x = int(i/100)      # 216 sayısı için 2 değerini tutacak.
    y = int(i%100/10)   # 216 sayısı için 1 değerini tutacak.
    z = int(i%10)       # 216 sayısı için 6 değerini tutacak.

    # Tüm rakamları aralarında karşılaştırıyoruz. Hepsi birbirinden farklı ise,
    if x != y and x != z and y != z:

        # Bu değeri ekrana yazdırıyoruz.
        print(i)