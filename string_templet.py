from string import Template

mytemplet = Template("my name is $name, my location is $location.i am ${location}y")

print(mytemplet.substitute(name = "sandeep",location = "Hyderabad"))

students = [("sandeep","amp"),("rani","nsp"),("shanvith","hyd")]

for element in students:
    print(mytemplet.substitute(name = element[0], location = element[1]))

