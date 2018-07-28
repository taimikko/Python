line = input()
while line:
  vuosi=int(line)
  status='is not'
  if vuosi%4==0:
    status='is' #leap year
    if vuosi%100==0:
      status='is not' #not leap year
      if vuosi%400==0:
        status='is' #leap year
  print("The year", vuosi, status, "a leap year.")
  line = input()
# Here the input has ended. Also the program can end here.


