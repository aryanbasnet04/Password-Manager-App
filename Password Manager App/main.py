from tkinter import *
from tkinter import  messagebox
import json

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
passwordList=[]
finalPassword=""

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatePassword():

  global letters,numbers,symbols,passwordList,finalPassword
  for n in range(0,5):
    passwordList+=random.choice(letters)

  for n in range(0,4):
    passwordList+=random.choice(numbers)

  for n in range(0,3):
    passwordList+=random.choice(symbols)

  random.shuffle(passwordList)
  print(passwordList)

  for pw in passwordList:
    finalPassword+=pw
  print(finalPassword)

  passwordEntry.insert(END,finalPassword)



#----------------------------SEARCH Website--------------------------------#
def searchWebsite():
  global websiteEntry
  webSearch=websiteEntry.get()
  try:
    with open("data.json") as dataFile:
        data=json.load(dataFile)
      
  except FileNotFoundError:
      messagebox.showinfo(title="Error",message="No data file founde")
  
  else:
      if webSearch in data:
        email=data[webSearch]["email"]
        password=data[webSearch]["password"]
        messagebox.showinfo(message=f"Email: {email} \n password: {password} ")
      else:
        messagebox.askretrycancel(message=f"Website: {webSearch} not found.")

 
  
     
      
      
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

  webName=websiteEntry.get()
  webEmail=UnameEntry.get()
  webPassword=passwordEntry.get()
  newData={
    webName: {
             "email":webEmail,
              "password":webPassword
           }}

  
  if webEmail!="" and webPassword!="" and webName!="":

   
      messageBox=messagebox.askyesno(message=f"These are your details entered: \nWebsite:{webName} \n Email:{webEmail} \n Password:{webPassword} \n")
      if messageBox:

          websiteEntry.delete(0,END)
          UnameEntry.delete(0,END)
          passwordEntry.delete(0,END)

          try:
            with open("data.json","r") as dataFile:
              
  
          # Reading the old data
              data=json.load(dataFile)

      

          except FileNotFoundError:
            with open("data.json","w") as dataFile:  
              data=json.dump(newData,dataFile,indent=4) 

          else:
            # Updating the new data
            data.update(newData)
            with open("data.json","w") as dataFile:
          # Writing the new data 
              json.dump(data,dataFile,indent=4)        
  else:
    messagebox.askretrycancel(message="Information hasn't been completed.")


# ---------------------------- UI SETUP ------------------------------- 
window=Tk()
window.title("Password Manager")
window.minsize(width=600,height=600)
window.config(padx=200,pady=50)

canvas=Canvas(width=200,height=200,highlightthickness=0)
passwordImage=PhotoImage(file="logo.png")
canvas.create_image(100,112,image=passwordImage)
canvas.grid(row=2,column=2)

websiteName=Label(text="Website:")
websiteName.grid(row=3,column=1)
websiteName.config(padx=20,pady=20)

websiteEntry=Entry(width=40)
websiteEntry.grid(column=2,row=3)
websiteEntry.focus()

search=Button(text="Search",command=searchWebsite)
search.grid(row=3,column=3)

UnameLabel=Label(text="Email/Username: ")
UnameLabel.grid(row=4,column=1)
UnameLabel.config(padx=20,pady=20)

UnameEntry=Entry(width=40)
UnameEntry.grid(row=4,column=2)

Password=Label(text="Password: ")
Password.grid(row=5,column=1)
Password.config(width=20,pady=20)

passwordEntry=Entry(width=40)
passwordEntry.grid(row=5,column=2)


generatePasswordBtn=Button(text="Generate Password",command=generatePassword)
generatePasswordBtn.grid(row=5,column=3)

AddButton=Button(text="Add",command=save)
AddButton.grid(row=6,column=2)
window.mainloop()
