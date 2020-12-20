"""

Soru 1

Girilen bir string ifadenin email adresi olup olmadığını doğrulayan python kodunu string metodları kullanmadan yazınız.
• Örnek Email : ali.erbey@usak.edu.tr

"""


# Kendimize uygun String parçalama fonksiyonu yazalım.
def explodeString(value, cut):
    # Parçalanan öğeleri hafızada tutması için bir list oluşturuyoruz.
    cuts = []

    # Hafızada tutması için string oluşturuyoruz.
    temp = ""

    # String içindeki karakterlere teker teker bakıyoruz.
    for x in value:
        # Eğer girilen karakter cut değişkenine eşit ise, parçalama işlemi yapıyoruz.
        if x == cut:

            # Geçici string değerini array içine atıyoruz. Böylece parçalamış oluyoruz.
            cuts.append(temp)

            # Hafızada tutulan string değerini sıfırlıyoruz.
            temp = ""

            # Bu karakteri es geçmesini sağlıyoruz.
            continue

        # String karaktere ekleme yapıyoruz.
        temp += x
    # For döngüsünde işi bittikten sonra,
    else:
        # En son hafızada tutulan değeri de listeye ekliyoruz.
        cuts.append(temp)

        # Hataların önüne geçebilmek için hafızada tutulan geçici string değeri sıfırlıyoruz.
        temp = ""

        # Son olarak parçalanan değerleri geri döndürüyoruz.
        return cuts

# E-posta doğrulama işlemi yapıyoruz.
def confirmEmail(email):
    # @ ile parçalıyoruz.
    # explodeString('admin@example.com', '@') => ['admin', 'example.com']
    cuts = explodeString(email, '@')

    # Eğer listedeki eleman sayısı birden fazla ise,
    if len(cuts) > 1:
        # Bu sefer sağ taraftaki adresi noktalardan arındırıyoruz.
        # explodeString('example.com', '.') => ['example', 'com']
        extension = explodeString(cuts[1], '.')

        # Eğer parçalama sonrasında eleman sayısı birden fazla ise
        if len(extension) > 1:
            # E-posta adresi olduğunu doğrulayalım.
            return True
        # Eğer birden fazla değil ise, içinde nokta yok demektir.
        else:
            # E-posta adresi geçersiz olduğunu tespit edip, False yanıtı dönelim.
            return False
    # Eleman sayısı birden fazla değilse, @ işareti yok demektir.
    else:
        # Bu durumda False yanıtı dönmemiz gerekir.
        return False

##################################### UYGULAMA ALANI #####################################

print(confirmEmail("ilhamitugral@gmail.com"))           # Geçerli
print(confirmEmail("ilhamitugral[at]gmail.com"))        # Geçersiz, @ işareti yok.
print(confirmEmail("ilhamitugral@gmail"))               # Geçersiz, Uzantı geçersiz.

##########################################################################################