shopping_cart = [{'name': 'apple', 'price_per_item': 0.21, 'number': 4}, {'name': 'banana', 'price_per_item': 0.12, 'number': 5}]

apples = shopping_cart[0]
bananas =shopping_cart[1]

price_of_apples = apples['price_per_item'] * apples['number']
price_of_bananas = bananas['price_per_item'] * bananas['number']
total_before_any = price_of_apples+price_of_bananas
total_apple_after_disc = price_of_apples*.5 
total_after_disc =total_apple_after_disc+price_of_bananas
total_tax=total_after_disc*.15
final_total=total_tax+total_after_disc


print(f"Cost of basket before sales and tax £" ,total_before_any )
print(f"Cost of basket after sales, before tax:" ,total_after_disc )
print(f"Cost of basket after sales and tax: £ {final_total:.2f}" )




