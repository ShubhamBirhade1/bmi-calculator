from patients_data import bmi_data

WeightKg = int(input("enter weight:"))
HeightCm = int(input("enter height:"))


def get_bmi(WeightKg, HeightCm):
    height_in_meter = float(HeightCm/100)
    #print("height_in_meter:", height_in_meter)
    bmi = WeightKg/(height_in_meter**2)
    print("calculated_bmi:", round(bmi, 2))
    return bmi


bmi = get_bmi(WeightKg, HeightCm)
for i in bmi_data:
    if int(bmi)*10 in list(i):
        print(bmi_data[i])