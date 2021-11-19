discounts = {'apple': 0.5} # {item:discount, ...}

def shopping_cart(shopping_list):
    tot=0.0
    disco=0.0
    
    for i in shopping_list:
        item_name=i['name']
        number_of_items=i['number']
        price_per=i['price_per_item']
        discount=discounts.get(item_name, 1.0)
       # print(item_name, "discount=", 1.0 - discount)
        tot += price_per*number_of_items
        disco += price_per*number_of_items*discount
 
  
    print(f"the total value of items is: £{tot}")
    print(f"the total value of items is with discount is: £{disco}")
  
      

shopping_cart([{'name': 'apple', 'price_per_item': 0.21, 'number': 4}, {'name': 'banana', 'price_per_item': 0.12, 'number': 5}
,{'name': 'oranges', 'price_per_item': 0.5, 'number': 1}
])


