from Bank import *

def register():
  print "Register"
  print "Complete all boxes!\n"
  user = raw_input("User: ")
  password = raw_input("Password: ")
  money = raw_input("How much do you want to deposit? ")
  income = raw_input("What is your income? ")
  cash = raw_input("How much cash do you have? ")
  if user and password and money and income and cash: #check if any box is empty
    if user not in database.users.keys():
      f = open('Account.py', 'a')
      f.write('/n')
      f.write(user + '=Account('+user+','+password+',"","waiting"')
      f.write(user+'.money='+money)
      f.write(user+'.income='+income)
      f.write(user+'.proprieties["cash"]='+cash)
      f.close()
      
      f = open('db.py', 'a')
      f.write('\n')
      f.write('database.addUser('+username+')')
      f.close()

def login():
  pass
	
	
def main():
  pass
	
if __name__ == '__main__': main()
