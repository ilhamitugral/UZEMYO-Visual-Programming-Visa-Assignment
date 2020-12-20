"""

Soru 5

Girilen ifade aşağıdakilerden biri olabilir
• receive-23-1-0\n
• send-181-3-0-1\nreceive-170-3-0\n
• receive-150-0-1\n0-4-5-6-\n
Kurallar :
• Her ifade receive ya da send ile ba¸slamalıdır.
• Her ifade \n karakteri ile sonlanmalıdır.
•
˙Ifadeler arka arkaya gelebilir b¨oyle bir durumda \nreceive ya da \nsend
durumları g¨ozlenebilir ve ge¸cerli durumlardır.
• receive ile başlayan ifadede 3 parametre yoksa geçersizdir.
• send ile başlayan ifadede 4 parametre yoksa geçersizdir.
• receive ya da send kelimesinden sonra gelen parametreler bulunduğu bölümdeki
parametre aralığını içermiyorsa, ifade geçersizdir.
Ornek : İkinci bölümde 1,2,3,4 değerlerinin karşılığı var. 5 değeri girilirse
ifade geçersizdir. Geçersiz ifade receive-23-5-0\n

"""

# Programın sona ermesi için durum ekliyoruz.
appStatus = True

# İstenilen cevapları list halinde belirtiyoruz.
code = ["Giden", "Gelen"]
devices = ["Televizyon", "Çamaşır Makinesi", "Buzdolabı", "Fırın"]
status = ["Off", "On"]
response = ["Cevap istenmiyor", "Cevap isteniyor"]

# Girilen parametre sonucunda sinyal durumunu str tipinde veren fonksiyon.
def signalPower(value):
    """
    • 0 - 50    : Çok Zayıf Sinyal
    • 51 - 100  : Zayıf Sinyal
    • 101 - 150 : Orta Sinyal
    • 151 - 200 : Güçlü Sinyal
    • 201 - 255 : Çok Güçlü Sinyal
    """
    # Girilen parametreyi int tipine çevirerek karşılaştırma yapıyoruz.
    value = int(value)

    # Eğer sinyal değeri 0 - 50 arasında ise;
    if 0 <= value < 50:

        # Çok zayıf sinyal bilgisini geri dönüyoruz.
        return "Çok Zayıf Sinyal"

    # Eğer sinyal değeri 50 - 100 arasında ise;
    elif 50 < value <= 100:

        # Zayıf sinyal bilgisini geri dönüyoruz.
        return "Zayıf Sinyal"

    # Eğer sinyal değeri 100 - 150 arsaında ise;
    elif 100 < value <= 150:

        # Orta sinyal bilgisini geri dönüyoruz.
        return "Orta Sinyal"

    # Eğer sinyal değeri 150 - 200 arasında bir değer ise;
    elif 150 < value <= 200:

        # Güçlü sinyal mesajı dönüyoruz.
        return "Güçlü Sinyal"

    # Eğer sinyal değeri 200 - 255 arasında bir değer ise;
    elif 200 < value <= 255:

        # Çok güçlü sinyal mesajını geri döndürüyoruz.
        return "Çok Güçlü Sinyal"

    # Eğer bu değer 0 - 255 aralığında değil ise;
    else:

        # Geriye False mesajı döndürüyoruz.
        return False

# List tipinde girilen parametreleri ayrıştırıp, gerekli mesajı yazdıran fonksiyon.
def displayMessage(arg):

    # Sinyal değerini alıyoruz.
    signalValue = arg[1]

    # Cihaz tipini alıyoruz.
    deviceType = int(arg[2])

    # Cihaz durumunu tespit ediyoruz.
    deviceStatus = int(arg[3])

    # Eğer girilen parametre "send" ise;
    if arg[0] == "send":

        # Varolan codeType değerini 0 olarak güncelliyoruz.
        codeType = 0

    # Eğer girilen parametre "receive" ise;
    elif arg[1] == "receive":

        # codeType değerini 1 olarak ifade ediyoruz.
        codeType = 1

    # "send" veya "receive" değil ise;
    else:

        # codeType değerini -1 olarak belirtiyoruz.
        codeType = -1


    # Eğer sinyal değeri False ise;
    if not signalPower(arg[1]):

        # Ekrana hata mesajını yazıyoruz.
        print("Error : birinci bölüm hatalı")

    # Eğer girilen parametre cihaz sayısından büyük ve cihaz değeri 0 ise,
    # ikinci koşulu int veri tipinde çeviriyoruz. Aksi halde; "0" == 0 mı diye kontrol sağlıyor.
    elif int(arg[2]) > len(devices) or int(arg[2]) == 0:

        # Hata mesajı yazıyoruz.
        print("Error : ikinci bölüm hatalı")

    # Eğer verilen değer, olası durum sayılarından büyük ise,
    elif int(arg[3]) > len(status):

        # Üçüncü bölüm hatalı mesajı yazdırıyoruz.
        print("Error : üçüncü bölüm hatalı")

    # Eğer girilen parametre "send" ve verilen değer response'de yer alan eleman sayısından fazla ise,
    elif arg[0] == "send" and int(arg[4]) > len(response):

        # Hata mesajını ekrana basıyoruz.
        print("Error : dördüncü bölüm hatalı")

    # Eğer hiç hata ile karşılaşmadıysak;
    else:

        # Tüm değerleri formatlayarak ekrana basıyoruz.
        print("Kod Tipi: {} - {}".format(arg[0], code[codeType]))
        print("Sinyal Gücü: {} - {}".format(arg[1], signalPower(signalValue)))
        print("Cihaz: {} - {}".format(str(deviceType), devices[deviceType - 1]))
        print("Durumu: {} - {}".format(str(deviceStatus), status[deviceStatus]))

        # Eğer "send" komutu gönderildiyse;
        if arg[0] == "send":

            # info isminde değişken oluşturup, gerekli 4. parametreyi ekliyoruz.
            info = arg[4]

            # Ardından formatlayarak ekrana gereken bilgileri yazdırıyoruz.
            print("Cevap: {} - {}".format(info, response[int(info)]))

##################################### UYGULAMA ALANI #####################################

# Programı döngüye sokarak sürekli input almasını sağlıyoruz.
while appStatus:

    # Bir input hazırlıyoruz. Ardından alınan değeri query değişkenine aktarıyoruz.
    query = input(r"Değer Giriniz: ")

    # Eğer girilen değer "exit" ise;
    if query == "exit":

        # Döngünün sonlanmasını sağlıyoruz.
        appStatus = False

    # Girilen değer "exit" değil ise, kullanıcı parametre gönderecek demek.
    # Eğer girilen parametre sonunda \n değeri yok ise, hata veriyoruz. Çünkü her parametre sonunda \n olmalı.
    elif not query.endswith(r"\n"):

        # Hata mesajını ekrana basıyoruz.
        print(r"Error: Son kısımda \n bulunamadı.")

    # Gerekli kontroller sonucunda parametrenin düzgün girildiğini tespit ettik ve bu alandan ilerliyoruz.
    else:

        # Birden fazla girilen komutları \n ile ayıklıyoruz.
        # Son parametre boş değer alacağı için bu değeri liste dahil etmiyoruz.
        commands = query.split(r"\n")[:-1]

        # Olası bir hatanın önüne geçmek için arg değişkenini önceden tanımlıyoruz.
        # arg değişkeni list veri tipinde olacak.
        arg = []

        # Tüm komutları teker teker geziyoruz.
        for i in range(len(commands)):

            # Her komut parametrelerini arg değişkenine sırayla atıyoruz.
            # Her parametre arasında "-" işareti olduğu için ayıklıyoruz.
            arg = commands[i].split("-")

            # Eğer girilen parametre "send" veya "receive" ise işlemlere başlıyoruz.
            # Aksi halde bu işlemlere devam edemeyiz.
            if arg[0] == "send" or arg[0] == "receive":

                # Eğer "send" verisi isteniyorsa ve bu parametre sayısı 5 değil ise hata veriyoruz.
                # Aynı şekilde eğer "receive" verisi isteniyorsa ve bu parametre sayısı 4 değil ise hata veriyoruz.
                if arg[0] == "send" and len(arg) != 5 or arg[0] == "receive" and len(arg) != 4:

                    # Hata mesajını ekrana basıyoruz.
                    print("Error: parametre hatalı")

                # Eğer hata yok ise;
                else:

                    # Ekrana veri yazdırıyoruz.
                    displayMessage(arg)

            # Eğer girilen parametreler "send" veya "receive" değil ise;
            else:

                # Hata mesajını ekrana basıyoruz.
                print("Error: send ya da receive içermiyor")

            # Ayraç için ayrı bir işlem yapıyoruz.
            # Eğer ayraç değeri sondaki komutun indis değerine sahip değil ise;
            if not i == len(commands)-1:

                # Ayraç ekliyoruz ve ekrana basıyoruz.
                print("------")

##########################################################################################