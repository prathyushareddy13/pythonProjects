class ApiRestfulBooker:
    name = "List of API's"
    api_names = ["Amazon", "Myntra", "Babli"]
    list_api = {"https://www.amazon.in/", "https://www.myntra.com/", "https://babli.in/"}
    def __init__(self):
       pass

api1 = ApiRestfulBooker()
print(api1.name)
print(api1.api_names[0])
print(api1.list_api)