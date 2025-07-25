from tabulate import tabulate as td

mydata = [
    ["Sujal", "Himachal"],
    ["GAgan", "Punjab"],
    ["Hema", "west bengal"]
]
head = ["Name", "city"]

print(td(mydata, headers = head, tablefmt = "fancy_grid"))