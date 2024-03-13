#  # 3-misol
# def almashtirish(gap):
#     yigindi = len(gap)
#     markaz = yigindi // 2

#     bir = gap[:markaz]
#     ikki = gap[markaz:]

#     new_sen = ikki + bir
#     return new_sen

# def takrorlanmas(sozlar):
#     takrorlanmas_sozlar = []
#     for soz in sozlar:
#         takrorlanmas_soz = ""
#         for harf in soz:
#             if soz.count(harf) == 1:
#                 takrorlanmas_soz += harf
#         takrorlanmas_sozlar.append(takrorlanmas_soz)
#     return takrorlanmas_sozlar

# if __name__ == "__main__":
#     gaplar = input("matn kiriting: ").split()
#     takrorlanmas_sozlar = takrorlanmas(gaplar)
#     for soz in takrorlanmas_sozlar:
#         print(almashtirish(soz))



# # 1-misol
# soz = input("Ma'lumotni kiriting: ")
# uzun = len(soz)
# markaz = uzun // 2
# bir = soz[:markaz]
# ikki = soz[markaz:]

# if uzun % 2 != 0: 
#     ikk = soz[markaz + 1:]
# new = ikki + bir
# print(new)

