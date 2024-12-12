# Kiểm tra nếu tất cả các chữ số trong một số đều là số chẵn
def tat_ca_la_so_chan(num):
    return all(int(chu_so) % 2 == 0 for chu_so in str(num))

# Tìm các số có tất cả chữ số là số chẵn trong khoảng từ 1000 đến 3000
so_chan = [str(num) for num in range(1000, 3001) if tat_ca_la_so_chan(num)]

# In ra các số cách nhau bởi dấu phẩy
print(",".join(so_chan))
print('Tran Quang Anh, 235752021610095')
