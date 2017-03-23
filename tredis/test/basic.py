import redis
import json
from ..tredis import Tredis
from ..tredis import tObj

obj = tObj({'founder': 'mediciBank'})
cosimoObj = tObj({'ruler' : 'florence'})
pieroObj = tObj({'ruler' : 'florence'})
lucreziaObj = tObj({'famous' : 'writer'})
lorenzoObj = tObj({'famous' : 'italian renaissance'})

r = Tredis()

r.create(obj, 'giovanniMedici')
r.create(cosimoObj, 'giovanniMedici', 'cosimo')
r.create(pieroObj, 'giovanniMedici', 'cosimo', 'piero')
r.create(lucreziaObj, 'giovanniMedici', 'cosimo', 'lucrezia')
r.create(lorenzoObj, 'giovanniMedici', 'cosimo', 'lucrezia', 'lorenzo')

z = r.get('giovanniMedici')
print z['founder']

y = r.get('giovanniMedici', 'cosimo')
print y['ruler']

z = r.get('giovanniMedici', 'cosimo', 'piero')
print z['ruler']

z1 = r.get('giovanniMedici', 'cosimo', 'lucrezia')
print z1['famous']

z2 = r.get('giovanniMedici', 'cosimo', 'lucrezia', 'lorenzo')
print z2['famous']
