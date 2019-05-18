# price = 100
# discount = 5
# price_with_discount = price - price * discount / 100
# print(price_with_discount)
def get_summ(one, two, delimiter = '&'):
    a = f'{one} {delimiter} {two}'
    return a
b = get_summ("learn", "Python")
print(b.upper())

def format_price(price):
    price = int(price)
    return f"Цена: {price} руб"
a = format_price(56.24)
print(a)

def create_account(name, surname):
    a = f'{name} {surname}'
    return a
b = create_account("Vlad", "Bel")
print(b)
c = create_account("Kirill", "Darchev")
print(c)
