for i in range(1,101,1):
    for div in range(i-1,0,-1):
        modul=i%div
        if modul==0 and div>1:
            break
        elif div==1:
            print(i)