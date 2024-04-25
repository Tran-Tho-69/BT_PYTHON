# =============================================================================
#2.1. Xét năm nhuần
# nam = int(input("nhap nam can xet :"))
# 
# if nam % 4 == 0 and nam % 100 != 0 :
#    
#     print(f"nam {nam} day la nam nhuan")
#     
# elif nam % 400 == 0 :
#    
#     print(f"nam {nam} day la nam nhuan")
# else:
#     
#     print(f"nam {nam} day k phai nam nhuan")
# =============================================================================
# =============================================================================
#2.2. Tính tiền thuê phòng resort
# phong = int(input("nhap ma phong 1 > 8 : "));
# so_dem = int(input("nhap so dem : "));
# 
# if so_dem == 2 or so_dem == 3 :
#     giam_gia = 0.75
# elif so_dem >= 4:
#     giam_gia = 0.70
# else:
#     giam_gia = 1;
#     
# if phong == 1 :
#    thanh_tien = (so_dem * 1260000) * giam_gia
#    print(f"thanh tien :{thanh_tien}")
# elif phong == 2 :
#    thanh_tien = (so_dem * 1550000) * giam_gia
#    print(f"thanh tien :{thanh_tien}")
# elif phong == 3 :
#    thanh_tien = (so_dem * 1830000) * giam_gia
#    print(f"thanh tien :{thanh_tien}")
# elif phong == 4 :
#    thanh_tien = (so_dem * 1830000) * giam_gia
#    print(f"thanh tien :{thanh_tien}")
# elif phong == 5 :
#    thanh_tien = (so_dem * 2120000) * giam_gia
#    print(f"thanh tien :{thanh_tien}")
# elif phong == 6 :
#    thanh_tien = (so_dem * 2120000) * giam_gia
#    print(f"thanh tien :{thanh_tien}")
# elif phong == 7 :
#    thanh_tien = (so_dem * 2540000) * giam_gia
#    print(f"thanh tien :{thanh_tien}")
# elif phong == 8 :
#    thanh_tien = (so_dem * 4800000) * giam_gia
#    print(f"thanh tien :{thanh_tien}")
# else:
#    print("moi ban nhap lai so phong") ;
# =============================================================================
# =============================================================================
# hoa_don = int(input("nhap so tien :"))
# if hoa_don < 500000:
#     print("ban khong dc giam gia ")
# elif 500000 < hoa_don < 1000000:
#     giam_gia = 0.95    
#     so_tien_tra = hoa_don * giam_gia
#     so_tien_gg = hoa_don - so_tien_tra
#     print(f"so tien hoa don : {hoa_don}")
#     print(f"so tien giam gia : {so_tien_gg}") 
#     print(f"so tien sau giam gia : {so_tien_tra}")
#       
# elif 1000000 < hoa_don < 2000000:
#     giam_gia = 0.9    
#     so_tien_tra = hoa_don * giam_gia
#     so_tien_gg = hoa_don - so_tien_tra
#     print(f"so tien hoa don : {hoa_don}")
#     print(f"so tien giam gia : {so_tien_gg}")
#     print(f"so tien sau giam gia : {so_tien_tra}")    
# else:
#     giam_gia = 0.85 
#     so_tien_tra = hoa_don * giam_gia
#     so_tien_gg = hoa_don - so_tien_tra
#     print(f"so tien hoa don : {hoa_don}")
#     print(f"so tien giam gia : {so_tien_gg}")
#     print(f"so tien sau giam gia : {so_tien_tra}")
# =============================================================================
# =============================================================================
#2.4. Xuất chuỗi
# input_st = ""
# char = ""
# while char != "0":
#         char = input("Nhập ký tự (ấn phím '0' để dừng): ")
#         if char == "0":
#             break
#         else:
#             input_st = input_st + char
# print(f"Các ký tự đã nhập: {input_st}")
# =============================================================================
# =============================================================================
# 2.5. Kiểm tra số nguyên tố
# n = int(input("Nhập vào một số tự nhiên: "))
# for i in range(2, n):
#     if n % i == 0:
#         print(f"Số {n} không phải số nguyên tố")
#         break
# else:
#     print(f"Số {n} là số nguyên tố")
# 
# =============================================================================



# =============================================================================
# def in_bang_cuu_chuong(n, m):
#     for i in range(n, m + 1):
#         print(f"Bảng cửu chương của {i}:")
#         for j in range(1, 11):
#             print(f"{i} x {j} = {i * j}")
#         print()
# n = int(input("Nhập số bắt đầu (n): "))
# m = int(input("Nhập số kết thúc (m): "))
# 
# in_bang_cuu_chuong(n, m)
# =============================================================================
# danh_sach_thuc_uong = ['Bạc Xỉu Đá', 'Freeze Trà Xanh',
# 'Trà Thạch Vải', 'Trà Thanh Đào',
# 'Cappuccino', 'Cà Phê Sữa Đá']




def tim_kiem_thuc_uong(danh_sach, tu_khoa):
    ket_qua = []
    for thuc_uong in danh_sach:
        if tu_khoa.lower() in thuc_uong.lower():
            ket_qua.append(thuc_uong)
    
    if ket_qua:
        print(f"Kết quả tìm kiếm cho từ khóa '{tu_khoa}':")
        for item in ket_qua:
            print(item)
    else:
        print(f"Không tìm thấy kết quả cho từ khóa '{tu_khoa}'.")

# Danh sách thức uống
danh_sach_thuc_uong = ['Bạc Xỉu Đá', 'Freeze Trà Xanh', 'Trà Thạch Vải', 'Trà Thanh Đào', 'Cappuccino', 'Cà Phê Sữa Đá']

# Nhập từ khóa từ người dùng
tu_khoa = input("Nhập từ khóa tìm kiếm: ")

# Tìm kiếm và hiển thị kết quả
tim_kiem_thuc_uong(danh_sach_thuc_uong, tu_khoa)























