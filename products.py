import os  # operation system 作業系統


products = []  # 先建立大清單

if os.path.isfile('products.csv'):  # 檢查檔案在不在
    print('Yeah! 找到檔案了!')
    # 讀取檔案
    with open('products.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue  # 還在迴圈之中，但直接跳到下一迴，不執行後面的指令

            '''
            s = line.strip().split(',')  # 先處理掉每一行資料尾巴的換行字碼\n，再用逗號','分隔開-->s變成清單格式
            name = s[0]
            price = s[1]        
            '''
            name, price = line.strip().split(',')  # 比上面的程式碼簡潔的方式，直接將分割開的值存入兩個變數
            products.append([name, price])  # 把小清單加入大清單中
    print(products)
else:
    print('找不到檔案.....')



# 讓使用者輸入
while True:
    name = input('請輸入商品名稱： ')
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

# 印出所有購買紀錄
for p in products:
    print(p[0], '的價格是', p[1])

# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:  # 打開檔案或開新檔案
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + "," + str(p[1]) + '\n')  # 四個字串合併在一起，並寫入檔案；注意將整數的price轉成字串才能連結在起
