tax1=.095
prices_dict = {'Water':1.00, 'Milk': 1.50, 'Apple':.75}
def SaleTax (Tax): #function prototype
    return tax1 * Tax

print SaleTax(10)

def calculate_final_price (item_value):
    return  SaleTax(item_value) + item_value


def calculate_final (item_value):
    if user_input in prices_dict:
    final_price = prices_dict[item_value] * tax1 + prices_dict[item_value]

    else:
        print('No Item is found')

        final_price=-1

    return final_price




print calculate_final('Water')

print('Please insert item')
user_input=raw_input()
print calculate_final(user_input)
