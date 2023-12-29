#Vending machine
#Create a dictionary with the menu items with their codes and prices
items_A={
'A1':{'item':'Chilli chips','price':2},
'A2':{'item':'Salty chips','price':2},
'A3':{'item':'Sour and cream chips','price':3},
'A4':{'item':'Salt and vineger chips','price':4}}
items_B={
'B1':{'item':'Water','price':1},
'B2':{'item':'Coca cola','price':2},
'B3':{'item':'Orange juice','price':2},
'B4':{'item':'Mixed fruit juice','price':2}}
items_C={
'C1':{'item':'Iced tea','price':2},
'C2':{'item':'Mocha drink','price':2},
'C3':{'item':'Iced coffee','price':3},
'C4':{'item':'Cappuccino','price':4}}
items_D={
'D1':{'item':'Sour punk','price':3},
'D2':{'item':'Snickers chocolate','price':4},
'D3':{'item':'Galaxy chocolate','price':4},
'D4':{'item':'Gummies','price':3}}

#Print a welcome message and the menu
print('''
░█──░█ █▀▀ █── █▀▀ █▀▀█ █▀▄▀█ █▀▀ 　 ▀▀█▀▀ █▀▀█ 　 █▀▄▀█ █──█ 
░█░█░█ █▀▀ █── █── █──█ █─▀─█ █▀▀ 　 ──█── █──█ 　 █─▀─█ █▄▄█ 
░█▄▀▄█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀───▀ ▀▀▀ 　 ──▀── ▀▀▀▀ 　 ▀───▀ ▄▄▄█ 

░█──░█ █▀▀ █▀▀▄ █▀▀▄ ─▀─ █▀▀▄ █▀▀▀ 　 ░█▀▄▀█ █▀▀█ █▀▀ █──█ ─▀─ █▀▀▄ █▀▀ █ 
─░█░█─ █▀▀ █──█ █──█ ▀█▀ █──█ █─▀█ 　 ░█░█░█ █▄▄█ █── █▀▀█ ▀█▀ █──█ █▀▀ ▀ 
──▀▄▀─ ▀▀▀ ▀──▀ ▀▀▀─ ▀▀▀ ▀──▀ ▀▀▀▀ 　 ░█──░█ ▀──▀ ▀▀▀ ▀──▀ ▀▀▀ ▀──▀ ▀▀▀ ▄
                        Select an item from below'''+'\n')

print('''█▀▀ █░█ █ █▀█ █▀
█▄▄ █▀█ █ █▀▀ ▄█
Code | Price  |  Item
---------------------------------------''')
def display_A():
    for key, product in items_A.items():
        print(f" {key}  | AED {product['price']}  |  {product['item']}")

display_A()
print('''
█▀▄ █▀█ █ █▄░█ █▄▀ █▀
█▄▀ █▀▄ █ █░▀█ █░█ ▄█
Code | Price  |  Item
---------------------------------------''')
def display_B():
    for key, product in items_B.items():
        print(f" {key}  | AED {product['price']}  |  {product['item']}")

display_B()
print('''
█▀▀ █▀█ █░░ █▀▄   █▄▄ █▀▀ █░█ █▀▀ █▀█ ▄▀█ █▀▀ █▀▀ █▀
█▄▄ █▄█ █▄▄ █▄▀   █▄█ ██▄ ▀▄▀ ██▄ █▀▄ █▀█ █▄█ ██▄ ▄█
Code | Price  |  Item
---------------------------------------''')
def display_C():
    for key, product in items_C.items():
        print(f" {key}  | AED {product['price']}  |  {product['item']}")

display_C()
print('''
█▀ █▄░█ ▄▀█ █▀▀ █▄▀ █▀
▄█ █░▀█ █▀█ █▄▄ █░█ ▄█
Code | Price  |  Item
---------------------------------------''')
def display_D():
    for key, product in items_D.items():
        print(f" {key}  | AED {product['price']}  |  {product['item']}")

display_D()

#ask user to enter their amount
user_amount=int(input('\n'+'Please enter your amount AED '))
#ask user to enter the code of the item they want
user_input=input('\n'+'Enter the code for the item you would like to buy: ')
#using if to print the item the user has selected
if user_input in items_A:
    item_selected=items_A[user_input]
    print (f"You have selected {item_selected['item']}")
elif user_input in items_B:
    item_selected=items_B[user_input]
    print (f"You have selected {item_selected['item']}")
elif user_input in items_C:
    item_selected=items_C[user_input]
    print (f"You have selected {item_selected['item']}")
elif user_input in items_D:
    item_selected=items_D[user_input]
    print (f"You have selected {item_selected['item']}")
    
print('''
      
      ⋘  𝑃𝑙𝑒𝑎𝑠𝑒 𝑤𝑎𝑖𝑡...⋙

      ''')
#print that the user's item has been dispensed
print (f"Your {item_selected['item']} has been dispensed!")
#use if and elif to calculate and print the user's change
if user_input in items_A:
    user_change=items_A[user_input]
    change = user_amount-user_change['price']
    print ('Your change is AED', change)
elif user_input in items_B:
    user_change=items_B[user_input]
    change = user_amount-user_change['price']
    print ('Your change is AED', change)
elif user_input in items_C:
    user_change=items_C[user_input]
    change = user_amount-user_change['price']
    print ('Your change is AED', change)
elif user_input in items_D:
    user_change=items_D[user_input]
    change = user_amount-user_change['price']
    print ('Your change is AED', change)
#suggestion for a few items using if and elif
if user_input == 'A1':
    input_A1=(input('Would you like Orange juice with your Chilli chips? Yes/No: '))
    if input_A1 == 'Yes':
        print ('''
        ⋘  𝑃𝑙𝑒𝑎𝑠𝑒 𝑤𝑎𝑖𝑡...⋙
               
Your Orange juice has been dispensed!
Your change is now AED''',(change-2),'''
Thank you for vending! see you next time''')
    elif input_A1 == 'No':
        print('Thank you for vending! see you next time')

elif user_input == 'C2':
    input_C2=(input('Would you like a Snickers chocolate with your Mocha drink? Yes/No: '))
    if input_C2 == 'Yes':
        print ('''
        ⋘  𝑃𝑙𝑒𝑎𝑠𝑒 𝑤𝑎𝑖𝑡...⋙

Your Snickers chocolate has been dispensed
Your change is now AED''',(change-4),'''
Thank you for vending! see you next time''')
    elif input_C2 == 'No':
        print('Thank you for vending! see you next time')
elif user_input == 'D1':
    input_D1=(input('Would you like Gummies with your Sour punk? Yes/No: '))
    if input_D1 == 'Yes':
        print ('''
        ⋘  𝑃𝑙𝑒𝑎𝑠𝑒 𝑤𝑎𝑖𝑡...⋙

Your Gummies have been dispensed
Your change is now AED''',(change-3),'''
Thank you for vending! see you next time''')
    elif input_D1 == 'No':
        print('Thank you for vending! see you next time')
elif user_input == 'A4':
    input_A4=(input('Would you like a Coca cola with your Salt and vineger chips? Yes/No: '))
    if input_A4 == 'Yes':
        print ('''
        ⋘  𝑃𝑙𝑒𝑎𝑠𝑒 𝑤𝑎𝑖𝑡...⋙
               
Your Coca cola has been dispensed
Your change is now AED''',(change-2),'''
Thank you for vending! see you next time''')
    elif input_A4 == 'No':
        print('Thank you for vending! see you next time')

elif user_input == 'B1':
    input_B1=(input('Would you like a Galaxy chocolate with your Water? Yes/No: '))
    if input_B1 == 'Yes':
        print ('''
        ⋘  𝑃𝑙𝑒𝑎𝑠𝑒 𝑤𝑎𝑖𝑡...⋙
               
Your Galaxy chocolate has been dispensed
Your change is now AED''',(change-4),'''
Thank you for vending! see you next time''')
    elif input_B1 == 'No':
        print('Thank you for vending! see you next time')
else:   #if the user chose none of the 5 code suggestions then print thank you message
    print('Thank you for vending! see you next time')