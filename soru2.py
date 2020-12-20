"""

Soru 2

Girilen bir string ifadenin url olup olmadığını doğrulayan python kodunu string
metodları kullanmadan yazınız.
• Örnek URL : www.alierbey.com

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

# URL doğrulama işlemi yapıyoruz.
def confirmUrl(url):

    # HTTP veya HTTPS portu olup olmadığını tespit edelim.
    if url[:7] == "http://" or url[:8] == "https://":
        # Var ise, True sonucunu dönsün.
        return True
    # Eğer HTTP veya HTTPS doğrulaması yapamadıysa, diğer sorgulama yöntemine geçelim.
    else:
        # URL'i noktalar ile parçalayalım.
        # explodeString('example.com', '.') => ['example', 'com']
        cuts = explodeString(url, '.')

        # Eğer list eleman sayısı birden büyük ise,
        if len(cuts) > 1:
            # True dönsün.
            return True
        # Eğer eleman sayısı bir ise False dönsün.
        else:
            # False dönsün.
            return False

##################################### UYGULAMA ALANI #####################################

print(confirmUrl("ilhamitugral.com"))               # .com uzantısından ötürü URL'dir.
print(confirmUrl("https://ilhamitugral"))           # http portunu gördüğü için URL'dir.
print(confirmUrl("ilhamitugral"))                   # URL değildir. Uzantısı ve portu belirtilmemiş.
print(confirmUrl("www.ilhamitugral"))               # www yi alan adı olarak görüp, ilhamitugral'ı da uzantı olarak görecek.

##########################################################################################