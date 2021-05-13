products = [] # 先建立大清單
while True:
    name = input('請輸竹商品名稱： ')
    if name == 'q':
        break
    price = input('請輸入商品價格： ')
    '''
    p = [] # 大清單products中的小清單元素
    p.append(name)
    p.append(price)
    '''
    # p = [name, price] # 比上一段簡潔的程式碼
    products.append([name, price]) # 更簡潔的程式碼-->直接創造小清單然後加入大清單中
print(products)

for p in products:
    print(p)
    print(p[0])
    print(p[0], '的價格是：', p[1])

with open('products.txt', 'w') as f:  # 打開檔案或開新檔案
    for p in products:
        f.write(p[0] + "," + p[1] + '\n')  # 四個字串合併在一起，並寫入檔案
