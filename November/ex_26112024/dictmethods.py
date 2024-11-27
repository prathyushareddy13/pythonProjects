
user_details = {
    "Name": "Rakesh",
    "Age" : 40,
    "Education": "M.tech",
    "Address" : {
        "Home" : "KA",
        "Office" : "Hyd"
    }
}
print(user_details["Address"])
print(user_details["Address"]["Home"])

#another way to create dict
stud_info = dict(name = "Prathyusha", age = 10, grade = "fourth")
print(stud_info)
print(stud_info["name"])
print(user_details.get("Education"))
