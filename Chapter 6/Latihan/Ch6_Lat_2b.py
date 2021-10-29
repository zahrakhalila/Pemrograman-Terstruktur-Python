def starFormation3(n):
    i = 1 
    while(i <= n/2):
        print('*' * i)
        i += 1   
    
    while(i > 0):
        print('*' * i)
        i -= 1

starFormation3(7)
