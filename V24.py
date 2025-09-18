# @cikey b8c2f0e997296c4047aa90efbb14a388
# @sid 20251174010038
# @aid V2.4


#begin_inputs

valor_compra = int(input("Digite o valor da compra: "))

#end_inputs

à_vista = valor_compra * 0.09

parcelado_5 = valor_compra / 5

total_juros = valor_compra * 1.17
parcelado_10 = total_juros / 10

print("{}".format(valor_compra - à_vista))
print("{}".format(parcelado_5))
print("{}".format(round(parcelado_10, 2)))