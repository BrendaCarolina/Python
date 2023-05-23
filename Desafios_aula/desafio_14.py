# Converta a temperatura em Cº se ela for digitada em Fº e vice e versa

c = float(input('Qual a temperatura em Celsius? '))
print(f' {c}ºC equivale a {(c * 1.8) + 32}ºF e {c + 273.15:.3f}ºK')

f = float(input('Qual a temperatura em Fahrenheit? '))
print(f'{f}ºF equivale a {(f - 32) * (5 / 9):.3f}ºC e {(f - 32) * (5 / 9) + 273.15:.3f}ºK')

k = float(input('Qual a temperatura em Kelvin? '))
print(f'{k}ºK equivale a {k - 273.15:.3f}ºC e {(k - 273.15) * 1.8 + 32:.3f}ºF')
