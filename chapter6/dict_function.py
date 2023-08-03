dictionary = {
    "name": "grace",
    "age": 21,
    "height": 5.3,
    "true": "value"

}
dictionary["hobbies"] = ["singing", "zara", "code"]

print(dictionary.get("hobbies"))

print(dictionary)

register = [{"name": "grace",
             "age": 21,
             "height": 5.3,
             "hobbies": "driving"

             },

            {"name": "milo",
             "age": 21,
             "height": 5.3,
             "hobbies": ("sleeping","writing")

             }

            ]
register [0]["name"] = "chiamaka"
print(register[0])