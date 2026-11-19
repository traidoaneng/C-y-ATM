so_du = 99999
while True:
    print("===== MÁY ATM =====")
    print("0. Thoát chương trình")
    print("1. Xem số dư hiện tại")
    print("2. Nạp tiền")
    print("3. Rút tiền")
    print("===================")

    lua_chon = int(input("Nhập lựa chọn của bạn: "))

    if lua_chon == 0:
        print("Cảm ơn quý khách đã sử dụng dịch vụ!")
        break

    elif lua_chon == 1:
        print(f"Số dư hiện tại: {so_du} VND")

    elif lua_chon == 2:
        tien_nap = float(input("Nhập số tiền bạn muốn nạp: "))
        if tien_nap > 0:
            so_du += tien_nap
            print(f"Nạp tiền thành công. Số dư mới: {so_du} VND")
        else:
            print("Số tiền nạp phải lớn hơn 0!")

    elif lua_chon == 3:
        tien_rut = float(input("Nhập số tiền bạn muốn rút: "))
        if 0 < tien_rut <= so_du:
            so_du -= tien_rut
            print(f"Rút tiền thành công. Số dư hiện tại: {so_du} VND")
        else:
            print("Số tiền rút không hợp lệ hoặc số dư hiện tại của bạn không đủ!")

    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại từ 0 đến 3!")