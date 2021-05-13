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
print(products[0][0])
