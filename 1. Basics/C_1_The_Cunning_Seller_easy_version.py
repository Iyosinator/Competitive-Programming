t = int(input())

for _ in range(t):
    n = int(input())
    coins = 0      
    deal_size = 1   
    deal_num = 0    

    while n > 0:
        r = n % 3
        n //= 3

        cost = 3 * deal_size + (deal_num * (deal_size // 3) if deal_num > 0 else 0)
        
        coins += r * cost

        deal_size *= 3
        deal_num += 1

    print(coins)
