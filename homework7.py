print("Работа со словарями:")
my_dict = {"Санкт-Петербург": [78, 98, 178, 198], "Калининградская область": [39, 91], "Алтайский край": [22, 122]}
print("Dict:", my_dict)
print("Existing value:", my_dict.get("Санкт-Петербург"))
print("Not existing value:", my_dict.get("Москва", "Ключ 'Москва' отсутствует"))
my_dict.update({"Ленинградская область": [47, 147],
                "Камчатский край": 41})
print("Deleted value:", my_dict.pop("Калининградская область"))
print("Modified dictionary:", my_dict, "\n")

print("Работа с множествами:")
my_set = {"Timur", 29.5, (11, 12), 1994, True, False, 0, 1994, True, "Tima", (11, 12)}
print(my_set)
my_set.add("Dzhafarov")
my_set.add("December")
my_set.remove(29.5)
print(my_set)
