with open("draft.txt") as f:
    data = list(f)

idx = 0 #Mốc bắt đầu
txt_len = len(data) #Mốc kết thúc
new_content = '' #Content mới sau khi chỉnh sửa

while idx < txt_len:  #List index lúc nào cũng phải bé hơn độ dài của của đoạn/ câu
    # Tách một dòng thành list      
    line_list = data[idx].split()
    idline = 0
    len_line = len(line_list)
    while idline < len_line:
        #Thay thế chữ trước Kteam thành How
        if line_list[idline] == "Kteam":
            line_list[idline-1] = "How"
        idline += 1
    # nối lại thành một dòng chuỗi
    new_content += ' '.join(line_list) + '\n'
    idx += 1

with open('kteam.txt', 'w') as new_f:
    # ghi nội dung mới vào file kteam.txt
    new_f.write(new_content)
