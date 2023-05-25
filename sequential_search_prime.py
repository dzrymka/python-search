def sequential_search_prime(n):
    if n < 2:
        return False
    for a in range(2, int(n ** 0.5) + 1):
        if n % a == 0:
            return False
    return True


daftar_angka = [7, 10, 13, 6, 17, 22, 19]
bilangan_prima = []

for bilangan in daftar_angka:
    if sequential_search_prime(bilangan):
        bilangan_prima.append(bilangan)

print("Bilangan prima yang terdapat pada daftar:", bilangan_prima)
