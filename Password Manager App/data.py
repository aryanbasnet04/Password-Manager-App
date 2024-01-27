import json
webName=input("Enter the webName: ")
emailName=input("Enter your email: ")
passwordName=input("Enter your Password: ")
newData={
webName:{
  "email":emailName,
  "password":passwordName
}
}

with open("jsonfile.json","w") as jsonFile:
  json.dump(newData,jsonFile,indent=4)






