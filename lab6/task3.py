def palndr(txt):
  txt = txt.lower()
  return  txt == txt[:: -1]
         
stringg = input()                
if  palndr(stringg):
  print("YES")
else :
  print("NO")  
                        
