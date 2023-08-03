# locale para internacionalização (tradução)
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps
import calendar
import locale

locale.setlocale(locale.LC_ALL, '')
print(calendar.calendar(2023))
print(70*'-')
print(f'{"Imprimindo o local atual identificado pelo Python":.^70}')
print(locale.getlocale())
print(70*'-')
