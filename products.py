products = [] # 先建立大清單
while True:
    name = input('請輸竹商品名稱： ')
    if name == 'q':
        break
    price = input('請輸入商品價格： ')
    price = int(price)
    '''
    p = [] # 大清單products中的小清單元素
    p.append(name)
    p.append(price)
    '''
    # p = [name, price] # 比上一段簡潔的程式碼
    products.append([name, price]) # 更簡潔的程式碼-->直接創造小清單然後加入大清單中
print(products)


with open('products_utf8.csv', 'w', encoding='utf-8') as f:  # 打開檔案或開新檔案
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + "," + str(p[1]) + '\n')  # 四個字串合併在一起，並寫入檔案；注意將整數的price轉成字串才能連結在起
