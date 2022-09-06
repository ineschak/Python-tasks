
def atbash(txt):

    a=["A","B","C" ,"D","E","F","G","H","I","J","K","L",
    "M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    b=["Z","Y","X","W","V","U","T","S","R","Q","P","O","N","M",
    "L","K","J","I","H","G","F","E","D","C","B","A"]
    s=''
    txt=txt.upper()

    for i in txt:
        if i in a:

            s+=(b[a.index(i)])
    print(s)


atbash("Hello world!")