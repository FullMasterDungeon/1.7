from datetime import date
group = {
    "members" : {"Van" : {'role': 'artist', "bday": date(1983, 10, 9)},
                "Billy" : {'role': 'Boss', "bday": date(1987, 1, 2)},
                "Mark": {'role': 'Master', "bday": date(1979, 12, 11)}},
    "performance" : {"Moscow" : {"date" : date(2021, 3, 12 ),"profit" : 12000, "expenses" : [1000, 300, 100]},
                    "Berlin" : {"date" : date(2021, 5, 12 ),"profit" : 15000, "expenses" : [2200, 320, 520]},
                    "Paris" : {"date" : date(2021, 7, 12 ),"profit" : 14000, "expenses" : [1500, 700, 50]},
                    "London" : {"date" : date(2021, 9, 12 ),"profit" : 17000, "expenses" : [5500, 900, 1000]},
                    "Amsterdam" : {"date" : date(2021, 10, 12 ),"profit" : 10000, "expenses" : [1000, 300, 110]}
}}
#print(group)

def kick(a):
    del group["members"][a]
    return(group)
kick("Van")
print(group["members"])

def invite(**kwargs):
    group["members"].update(kwargs)
    return(group)
invite(**{"Brad" : {'role': 'Boss', "bday": date(1987, 1, 2)}})
print(group["members"])

def add_performance(**kwargs):
    group["performance"].update(kwargs)
    return(group)
add_performance(**{"Bishkek" : {"date" : date(2021, 10, 12 ),"profit" : 10000, "expenses" : [1000, 300, 110]}})
print(group["performance"])

def expenses():
    ex = 0
    for i in group["performance"]:
        for b in group["performance"][i]["expenses"]:
            ex += b
    return(ex)
print(expenses())

def earnings():
    prof = 0
    for i in group["performance"]:
        prof += group["performance"][i]["profit"]
    total = prof - expenses()
    return(total)
print(earnings())