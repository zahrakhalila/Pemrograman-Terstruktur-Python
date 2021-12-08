from datetime import *

def diffDate(x):
    now = datetime.date(datetime.now())
    x = datetime.strptime(x, '%Y-%m-%d').date()
    return abs((x - now).days)

print('Selisih harinya adalah {0} hari'.format(diffDate('2022-01-01')))
