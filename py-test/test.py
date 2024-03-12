"""
@author David Antilles
@description 
@timeSnapshot 2024/2/1-21:57:39
"""


# res = [
#     'KeyValueData',
#     'UserTags',
#     'Users',
#     'UserPhysical',
#     'UserMedicineHistory',
#     'HospitalTags',
#     'Hospital',
#     'HospitalDoctorProficiencyTags',
#     'HospitalDoctors',
#     'StaticRecommendedNutritionInTake',
#     'UserUploadedInTake'
# ]
#
# for name in res:
#     print(f"PydanticModel{name}: Type[PydanticModel] = pydantic_model_creator({name})")
#     print(f"PydanticQuerySet{name}: Type[PydanticListModel] = pydantic_queryset_creator({name})")


def read():
    ret = {}
    with open("ratings.dat", "r") as file:
        for line in file:
            split = line.split("::")
            if ret.get(split[0]) is None:
                ret[split[0]] = []
            else:
                ret[split[0]].append(split[1])
        return ret


def calc(data: dict):
    ret = {}
    keys = data.keys()
    for i in keys:
        for j in keys:
            if i != j:
                u1 = set(data[i])
                u2 = set(data[j])
                try:
                    len(ret.get(i))
                    ret[i].append({
                        j: len(u1 & u2)
                    })
                except:
                    ret[i] = []

    return ret


if __name__ == '__main__':
    print(calc(read()))
