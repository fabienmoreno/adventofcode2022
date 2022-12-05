#Initial arrangement:
A=[["W","R","F"], \
["T","H","M", "C", "D", "V", "W", "P"], \
["P","M","Z","N","L"], \
["J","C","H", "R"], \
["C","P","G","H","Q","T","B"], \
["G","C","W","L","F","Z"], \
["W","V","L","Q","Z","J","G","C"], \
["P","N","R","F","W","T","V","C"], \
["J","W","H","G","R","S","V"]]

#Load sequence
f=open('05/moves.txt','r')
l=f.read().split("\n")
le=[list(map(int,i.replace('move ','').replace(" from "," ").replace(" to "," ").split(" "))) for i in l]
for s in le:
    qty=s[0]
    org=s[1]-1
    des=s[2]-1
    st=A[org][-qty:]
    A[org]=A[org][0:-qty]
    st.reverse()
    A[des].extend(st)
result = [c[-1] for c in A]
print(''.join(result))