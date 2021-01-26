while 1:
    try:
        a,b,c,d=map(int,input().split())
        if d/c==c/b==b/a:
            x=int(d/c)
            print(a,b,c,d,d*x)
        elif d-c==c-b==b-a:
            y=int(d-c)
            print(a,b,c,d,d+y)
        else:
            break
    except:
        continue