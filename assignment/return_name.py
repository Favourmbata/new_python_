# def new_name(input):
#     name_with_s = {name: input.count(name) for name in input if name.capitalize().startswith("S")or  name.capitalize().startswith("s")}
#     return name_with_s
#
#
# names = ["joe","Daniel","seyi","Kelvin","Muhammad","Hakimi","Segun","Seyi","solo"]
# s = new_name(names)
# print(s)


def student_names(name_with_s):
    name_dict = {}
    for name in name_with_s:
        if name.startswith("S") or name.startswith("s"):
            capitalised_name = name.capitalize()
            if capitalised_name in name_dict:
                name_dict[capitalised_name] += 1
            else:
                name_dict[capitalised_name] = 1
    return name_dict


name_with_s = ["joe", "Daniel", "seyi", "Kelvin", "Muhammad", "Hakimi", "Segun", "Seyi", "solo"]
result = student_names(name_with_s)
print(result)
