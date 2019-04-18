chleb_szt = 1.99
mleko_l = 2.50
cukierki_kg = 12.99

x_chleb = float(input("Ile sztuk chleba chcesz: "))
x_mleko = float(input("Ile litrow mleka chcesz: "))
x_cukierki = float(input("ile kg cukierkow chcesz: "))

suma = round((chleb_szt*x_chleb + mleko_l*x_mleko + cukierki_kg*x_cukierki), 2)

print("Calosc kosztuje: " + str(suma) + " zlotych.")
