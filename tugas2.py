bilangan_max = 0

while True:
    bilangan = int(input("Masukan bilangan: "))
    if bilangan == 0:
        break
    if bilangan > bilangan_max:
        bilangan_max = bilangan
print(f"Bilangan paling gede: {bilangan_max}")        