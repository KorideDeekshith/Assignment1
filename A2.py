#Creating an empty dictionary
dog = {}
print(type(dog))

#Adding elements
dog.update({"name" : "pammi", "color": "red", "breed " : "pamarian", "legs" : 4, "age" : 6})
print(dog)

#creating a student dictionary and adding elements
student ={
    "first_name": "Erica",
    "last_name" : "Brooks",
    "Gender" : "Female",
    "Age" : 26,
    "Marital Status" : "Not married",
    "Skills" : ["Python", "Java", ".Net"],
    "Country" : "Brazil",
    "City" : "Oak park",
    "Address" : "5601 west 133rd terrace"
}

#To get the length 
print(len(student))

#Value of skills
print(student["Skills"])

#To check the data tyoe of skills
print(type(student["Skills"]))

#Modifying the skill values
student["Skills"].append("C++")
student["Skills"].append("Golang")

#Value of skills
print(student["Skills"])

#To get the dictionary keys and values as a list
print(list(student.keys()))
print(list(student.values()))