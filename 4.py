sting = "23:41"
out = "23:43"
req = "90"

xsignIn = sting.split(":")
signIn = int(xsignIn[0]) * 60 + int(xsignIn[1])

xOut = out.split(":")
signOut = int(xOut[0]) * 60 + int(xOut[1])

xreq = int(req)*60

print("reqired duty:",xreq)
print("Sign In :" , signIn)
print("Sign Out :" , signOut)
print("render time: ",signOut-signIn)
rem = xreq-(signOut-signIn)
formulation=str(rem/60)
formulation_lista = formulation.split(".")
print(formulation_lista)

converttomin = "0."+str(formulation_lista[1])
mins = float(converttomin)*60
print("rem hours:",formulation_lista[0]+"h"+":",mins.__round__())

