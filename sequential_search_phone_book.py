def find_phone_number(name, phone_book):
    for contact_name, phone_number in phone_list.items():
        if contact_name == name:
            return phone_number
    return None


# Daftar Nomor Telepon
phone_list = {
    "John Doe": "081234567890",
    "Jane Smith": "089876543210",
    "Micheal Jhonson": "087811223344",
    "Emily Davis": "082122232425"
}

# Nama yang ingin dicari nomor teleponnya
name = "Jane Smith"

# Menemukan nomor telepon Marck
phone_list = find_phone_number(name, phone_list)

# Menampilkan nomor telepon Jane
if phone_list:
    print("Nomor telepon", name, "adalah", phone_list)
else:
    print("Nomor telepon", name, "tidak ditemukan.")
