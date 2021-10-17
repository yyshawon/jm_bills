print("Welcome To JibonMukhi Bill Splitter!\n")
bill = input("Bill koto?\n৳: ")
person = input("Koyjon khaite aisis?\n: ")
cokeman = input("Coke khawabe kida?\n: ")

res = (int(bill) / int(person))

cokewala = res + 50
r_c = round(cokewala)
final = round(res)

print(f"{final} Taka Kore de shob.")
print(f"{cokeman} de {r_c} Taka.")
