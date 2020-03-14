while True:
    command = str(input())
    if not (command == "sell" or command == "bye" or command == "next" or command == "info"):
        print("Invalid commmand")
    if command == "bye":
        print("You made ${:.2f} in sales!".format(sales))
        break
    if command == "sell":
        sales = sales + starting_price
        stock = stock - 1
        sold_today = sold_today + 1
        sold = sold + 1
        print("Sold 1 item.")
        if stock == 0:
            print("No more stock!")
            break
    if command == "info":
        print("Day ", day_number + 1)
        print("Current price: ${:.2f}".format(current_price))
        print("Current sales: ${:.2f}".format(sales))
        print("Stock left: {:.0f}".format(stock))
        print(sold_yesterday, "item(s) sold yesterday")
        print(sold_today, "item(s) sold today")
    if command == "next":
        day_number = day_number + 1
        sold_today = sold_today
        sold_yesterday = sold_yesterday + (sold - sold_today) # 
        print("Summary of day {:.0f}: {} item(s) sold".format(day_number, sold_today))
        sold_today = 0
        if sold_today < sold_yesterday:
            current_price = current_price - 0.10
        elif current_price == minimum_price:
            current_price >= minimum_price #fix this for price reaching the minimum price
