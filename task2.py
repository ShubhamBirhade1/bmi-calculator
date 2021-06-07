from patients_data import bmi_data, health_data


def get_bmi(WeightKg, HeightCm):
    height_in_meter = float(HeightCm/100)
    print("height_in_meter:", height_in_meter)
    bmi = WeightKg/(height_in_meter**2)
    print("calculated_bmi:", round(bmi, 2))
    return bmi


for data in health_data:
    WeightKg = int(data['WeightKg'])
    HeightCm = int(data['HeightCm'])
    bmi = get_bmi(WeightKg, HeightCm)
    for i in bmi_data:
        if int(bmi)*10 in list(i):
            print(bmi_data[i])


def get_overweight_people():
    overweight = []
    for person in bmi*10:
        if person >= 250:
            overweight.append(person)
        else:
            overweight.append('not overweight')


get_overweight_people()
