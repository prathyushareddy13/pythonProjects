Student_info = {
    "name" : "Amit",
    "age"  : 18,
    "Grade" : "Inter",
    "Place" : {
        "home": "Bangalore",
        "office" : "Hyderabad"
    }
}

Student_info2 = {
    "name" : "Akshay",
    "age"  : 19,
    "Grade" : "Inter",
    "Place" : "Bangalore"

}


#combining multiple dictionaries into a list
comb_dict = [Student_info,Student_info2]

print(comb_dict[0]["name"])
print(comb_dict[0]["Place"]["home"]) # 0 to refer which list
print(comb_dict[1]["Grade"])

print(Student_info["Place"]["home"])  #to access directly