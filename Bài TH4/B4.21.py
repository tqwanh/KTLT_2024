# Nhập chuỗi các số nhị phân
chuoi_nhi_phan = input("Nhập chuỗi các số nhị phân 4 chữ số, cách nhau bởi dấu phẩy: ")

# Tách chuỗi thành danh sách các số nhị phân
danh_sach_nhi_phan = chuoi_nhi_phan.split(',')

# Kiểm tra và in ra các số chia hết cho 5
ket_qua = [nhi_phan for nhi_phan in danh_sach_nhi_phan if int(nhi_phan, 2) % 5 == 0]

# In kết quả
print(",".join(ket_qua))
5
print('Tran Quang Anh, 235752021610095')
