#Dictionary 

info ={
    "name" : "Kuheli",
    "subjects" : ["python" , "C++" , "Java"],#stores list
    "topics" : ("dict" , "set"),#stores tuple
    "age" : 20 ,
    "isAdult" : True ,
    12.99 : 56
}
print(info)
print(type(info))
print(info["subjects"])
print(info[12.99])

info["name"] = "Koyel"#changing value of key "name"
print(info)