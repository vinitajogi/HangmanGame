Z= [" o" , "/", "|", "\\", "/", "|", "\\"]
X = input('enter spell to be guess ')
x=list(X)
print(x)
i=len(x)
j=len(x)
T=''
for alpha in range(len(x)):
    Y = input('enter character of spelling, 1 character at a time')
    print(Y)
    c = 1
    for beta in range(len(x)):
        print(x[beta])
        if Y!= x[beta]:
            c+=1
            print("unmatch_count",c)
        if len(x)==c:
            T+=str(Z[alpha])
            if str(Z[alpha])==' o' or str(Z[alpha])=="\\":
                T+="\n"
        print(T)
