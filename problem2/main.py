def maximum_buy_product(money, product_price):
    price_list=[]
    n= len(product_price)

    # generate semua list price yang berurutan
    for i in range(n):
        for j in range(n-i):
            price_list.append(product_price[j:i+j+1])
    
    # get maximum sum per elemen l
    max_product=0
    max_sum=0
    for p in price_list:
        sumlist=sum(p)
        if max_product < len(p):
            if sumlist <= money:
                max_product= len(p)
    return max_product

if __name__ == "__main__":
    print(maximum_buy_product(50000, [25000, 25000, 10000, 14000]))      # 3
    print(maximum_buy_product(30000, [15000, 10000, 12000, 5000, 3000])) # 4
    print(maximum_buy_product(10000, [2000, 3000, 1000, 2000, 10000]))   # 4
    print(maximum_buy_product(4000, [7500, 3000, 2500, 2000]))           # 1
    print(maximum_buy_product(0, [10000, 30000]))                        # 0