
integer_var = 20
print("age:", integer_var)


float_var = 89.5
print("marks of student:", float_var)

string_var = "YO,my man!"
print("Message:", string_var)

boolean_var = False
print("Boolean:", boolean_var)

list_var = ['football','cricket','kho-kho','swimming']
list_var.append('shooting')
print("List:", list_var)

# tuple_var = (abc,abd)          //unmutable
# print("Tuple:", tuple_var)

tuple_var = (1,2,3)
print("Tuple:", tuple_var)


dict_var = {"name": "Omkar", "age": 25, "city": "Kolhapur"}
print("Dictionary:", dict_var)


set_var = {'India','France','Japan','Brazil'}
print("Set:", set_var)


complex_var = 2 + 7j
print("Complex:", complex_var)


none_var = None
print("NoneType:", none_var)

stuent_admission=2_899_750
print(f"admission at DYPCET (int):{stuent_admission}")

cricket_team=range(1,12)                                  #range
print(f"Cricket team (range): {list(cricket_team)}")

#frozenset
car_company=frozenset({"Porsche","BMW","Buggatti","Lamborgini","Ferrari"})
print(f"Car company (frozenset): {car_company}")

x=5
y=2
print(x//y)
print(x/y)
print(x%y)
print(x**y)

x=5
y="5"
print(x + int(y))
print(str, x + (y))

a=10
b=20
a,b=b,a
print("a={a},b ={b}")