
from datetime import date


mesekhtot = {
    "Berakhot": 63,
    "Shabbat": 156,
    "Eruvin": 104,
    "Pesahim": 120,
    "Shekalim": 21,
    "Yoma": 87,
    "Sukkah": 55,
    "Beitzah": 39,
    "Rosh Hashana": 34,
    "Taanit": 30,
    "Megilah": 31,
    "Moed Katan": 28,
    "Hagigah": 26,
    "Yevamot": 121,
    "Ketuvot": 111,
    "Nedarim": 90,
    "Nazir": 65,
    "Sotah": 48,
    "Gittin": 89,
    "Kiddushin": 81,
    "Bava Kamma": 118,
    "Bava Metzia": 118,
    "Bava Batra": 175,
    "Sanhedrin": 112,
    "Makkot": 23,
    "Shevuot": 48,
    "Avoda Zara": 75,
    "Horiyot": 13,
    "Zevachim":119,
    "Menahot": 109,
    "Hulin": 141,
    "Bekhorot": 60,
    "Arakhin": 33,
    "Temurah": 33,
    "Keratot": 27,
    "Meilah": 21,
    "Tamid": 8,
    "Niddah": 71
}
new_cycle, cur = date(2020,1,4), date.today()
days_since = cur-new_cycle
days_since = days_since.days
# print(days_since)
for mesekhta,pages in mesekhtot.items():
    if days_since < pages:
        print("Today's Daf is " + mesekhta,days_since+1)
        break
    days_since = days_since-pages

# print(sum(mesekhtot.values()))