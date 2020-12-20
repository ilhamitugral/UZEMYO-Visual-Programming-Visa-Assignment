"""

Soru 3

Girilen bir string ifadede aranan bir ifade bulunduğunda bir önceki ve bir sonraki
karakteri ekrana getiren python kodunu yazınız.
• Girilen ifade : “Usak Universtesi”
• Aranan ifade : ver
• Sonuc : ivers

"""

# Gereken tanımlamayı yapalım.
text = "Usak Universitesi"

# Aranan ifadeyi belirtelim.
get = "ver"

# Aranan ifadenin nerede başladığını tespit edelim.
start = text.find(get)-1

# Aranan ifadenin nerede biteceğini belirtelim.
end = start + len(get)+2

# Son olarak bir önceki karakteri ve bir sonraki karakteri ekrana yazdıralım.
print(text[start:end])