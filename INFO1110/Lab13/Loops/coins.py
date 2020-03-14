def coins(dollar):
    dollar = int(dollar)
    if not isinstance(dollar, int):
        raise TypeError
    total = 0
    hundred = 0
    fifty = 0
    twenty = 0
    ten = 0
    five = 0
    two = 0
    one = 0
    while total <= dollar:
        difference = dollar - total
        if difference >= 100:
            total += 100
            hundred += 1
        elif difference < 100 and difference >= 50:
            total += 50
            fifty += 1
        elif difference < 50 and difference >= 20:
            total += 20
            twenty += 1
        elif difference < 20 and difference >= 10:
            total += 10
            ten += 1
        elif difference < 10 and difference >= 5:
            total += 5
            five += 1
        elif difference < 5 and difference >= 2:
            total += 2
            two += 1
        elif difference < 2 and difference >= 1:
            total += 1
            one += 1
        elif difference == 0:
            break
    if hundred > 0:
        print('{} x $100'.format(hundred))
    if fifty > 0:
        print('{} x $50'.format(fifty))
    if twenty > 0:
        print('{} x $20'.format(twenty))
    if ten > 0:
        print('{} x $10'.format(ten))
    if five > 0:
        print('{} x $5'.format(five))
    if two > 0:
        print('{} x $2'.format(two))
    if one > 0:
        print('{} x $1'.format(one))
    return

amount = int(input('Enter a dollar amount: '))
dollar = coins(amount)
