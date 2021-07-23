
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
    "Middot": 3,
    "Kinnim": 4,
    "Tamid": 8,
    "Niddah": 71
}
first_cycle, cur = date(1923,9,23), date.today()
days_since = cur-first_cycle
days_since = days_since.days
total_dapim = sum(mesekhtot.values())
dapim_in_current_cycle = days_since%total_dapim+63
# print(dapim_in_current_cycle)
for mesekhta,pages in mesekhtot.items():
    if dapim_in_current_cycle < pages:
        print("Today's Daf is " + mesekhta,dapim_in_current_cycle+1)
        break
    dapim_in_current_cycle = dapim_in_current_cycle-pages

# print(sum(mesekhtot.values()))