def starFormation1(n):
    i = 1 
    while(i <= n):
        print('*' * i)
        i += 1
        
def starFormation2(n):
    i = 1
    while(i <= n):
        print('*' * n)
        n -= 1

starFormation1(4)
starFormation2(4)
