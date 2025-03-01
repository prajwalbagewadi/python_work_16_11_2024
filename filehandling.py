from os import write


"""
x -> create new file
w -> write into file
r -> read from file
a ->
"""
file=open("file.txt","x")
file.close()


file=open("file.txt","w")
file.write("helloworld")
file.close()

file=open("file.txt","r")
view=file.read()
file.close()

print(f"view={view}")

file=open("file.txt","a")
file.write("\n hellopython")
file.close()
