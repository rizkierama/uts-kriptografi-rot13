def rot13(teks):
    hasil = ""
    
    teks = teks.upper()

    for huruf in teks:
        if huruf == " ":
            hasil += " "
        elif huruf.isalpha():
            pos = ord(huruf) - ord('A')
            pos = (pos + 13) % 26
            hasil += chr(pos + ord('A'))
    return hasil

# Program utama
if __name__ == "__main__":
    print("=== PROGRAM ROT13 ===")
    print("Ketik exit untuk berhenti.\n")

    riwayat = []

    while True:
        teks = input("Masukkan teks (exit untuk selesai): ").upper()

        if teks == "EXIT":
            print("\n=== RIWAYAT ENKRIPSI & DEKRIPSI ===")
            for i, r in enumerate(riwayat, 1):
                print(f"{i}. {r['input']} -> {r['encrypt']} -> {r['decrypt']}")
            print("\nProgram selesai. Terima kasih!")
            break

        if not all(c.isalpha() or c == " " for c in teks):
            print("Masukkan Inputan huruf!\n")
            continue

        hasil_encrypt = rot13(teks)
        hasil_decrypt = rot13(hasil_encrypt)

        print("Hasil Enkripsi :", hasil_encrypt)
        print("Hasil Dekripsi :", hasil_decrypt, "\n")

        riwayat.append({
            "input": teks,
            "encrypt": hasil_encrypt,
            "decrypt": hasil_decrypt
        })

