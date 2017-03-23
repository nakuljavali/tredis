# Tredis

Tredis is a in-memory tree on top of redis. The goal is to build an effective relational database running on a cluster with a leaderless consensus algorithm.


## Test
To test run the following from the root of the project
`python -m tredis.test.basic`

## Usage
 - Make sure the redis server is running
 `tredis-usr$ redis-server`
 - Python code snippet as
 ```
 r = Tredis()
 obj = tObj({'founder': 'mediciBank'})
 r.create(obj, 'giovanniMedici')
 z = r.get('giovanniMedici')
 print z['founder']

 cosimoObj = tObj({'ruler' : 'florence'})
 r.create(cosimoObj, 'giovanniMedici', 'cosimo')
 y = r.get('giovanniMedici', 'cosimo')
 print y['ruler']
 ```
