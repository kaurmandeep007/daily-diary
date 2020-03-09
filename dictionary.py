dict={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
print(dict)

#acess items:
x=dict["model"]
x=dict.get("model")
print(x)

#change values:
dict["year"]=2014
print(dict)

#loop through a dictionary:
for x in dict:
    print(x)

#if key exists:
if "brand" in dict:
    print("yes,'brand' is one of the keys in dict dictionary")

#dictionary length:
print(len(dict))

#add items:
dict["color"]="red"
print(dict)

#remove items:
dict.pop("year")
print(dict)

#copy a dictionary:
mydict=dict.copy()
print(mydict)

#nested dictionaries:
myfamily={
    "child1":{
        "name":"emil",
        "year":"2004"
    },
    "child2":{
        "name":"tobias",
        "year":"2001"
    },
    "child3":{
        "name":"limra",
        "year":"1998"
    }
}
print(myfamily)
for x in myfamily:
    print(x)