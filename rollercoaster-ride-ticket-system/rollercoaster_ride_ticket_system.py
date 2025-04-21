print("Selamat datang di Wahana Rollercoaster!")
height = int(input("Berapa tinggi badanmu (dalam centimeter)? "))
bill = 0

if height >= 120:
    print("Selamat, kamu bisa masuk Wahana ini!")
    age = int(input("Berapa umurmu?"))
    if age <= 12:
        bill = 5
        print("Tiket anak-anak harganya $5")
    elif age <= 18:
        bill = 7
        print("Tiket remaja harganya $7")
    else:
        bill = 12
        print("Tiket dewasa harganya $12")

    wants_photo = input("Mau ambil foto sekalian? ketik y untuk iya, ketik n untuk tidak")
    if wants_photo == "y":
        confirmation = input("Ambil foto akan dikenai biaya tambahan sebesar $3, apakah anda setuju? ketik y untuk iya, ketik n untuk tidak.")
        if confirmation == "y":
            bill += 3
            print(f"Harga total yang harus dibayar adalah ${bill}")

else:
    print("Maaf, kamu harus lebih tinggi lagi untuk menaiki Wahana ini.")
