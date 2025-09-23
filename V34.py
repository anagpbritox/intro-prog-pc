# @cikey b8c2f0e997296c4047aa90efbb14a388
# @sid 20251174010038
# @aid V3.4


#begin_inputs

# programa sem entrada (input)

#end_inputs

for a in range(2017, 2021):
    for m in range(1, 13):
        for d in range(1, 31):
            if a == 2020 and m == 12 and d == 31:
                break
            print(f"{d}/{m}/{a}")