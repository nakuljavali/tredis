import json, sys, logging
import redis, ast

def tObj(mo):
    mo['children'] = {}
    objJson = json.dumps(mo)
    return objJson

class Tredis:
    'Main Tree-Redis implementation'

    def __init__(self, host='localhost', port=6379):
        self.handle = redis.StrictRedis(host=host, port=port, db=0)
        self.handle.set('__id__', 0)

    def _getId(self):
        self.handle.incr('__id__')
        return self.handle.get('__id__')

    def _addChild(self, mo):
        id = self._getId()
        self.handle.set(id, mo)
        return id

    def _getParentId(self, args):
        startObj = self.handle.get(1)
        if len(args)==2:
            return 1

        count = len(args)-1
        i = 1
        parentId = 1
        while count > i:
            objJson = json.loads(startObj)
            children = objJson['children']
            parentObj = args[i]
            parentId = children[args[i]]
            startObj = self.handle.get(parentId)
            i = i + 1
            #print json.loads(self.handle.get(parentId))
        #print 'Parent Object: ' + parentObj + ' Parent Id: ' + parentId
        return parentId

    def create(self, mo, *args):
        #print 'Request to create object: ' + str(args)
        parent = 0
        if len(args) == 1:
            self._addChild(mo)
        else:
            id = self._addChild(mo)
            loc = args[-1]
            #print 'Location: ' + loc
            parentId = self._getParentId(args)
            parentObj = self.handle.get(parentId)
            obj = json.loads(parentObj)
            #print ' Obj: ' + str(obj)
            #print obj['children']
            #print type(obj['children'])
            d = obj['children']
            d[loc] = id
            obj['children'] = d
            objJson = json.dumps(obj)
            #print objJson + "\n"
            self.handle.set(parentId, objJson)
            parentId = id

    def get(self, *args):
        if len(args) == 1:
            rt = self.handle.get(1)
            return json.loads(rt)
        else:
            parentId = self._getParentId(args)
            rt = self.handle.get(parentId)
            obj = json.loads(rt)
            children = obj['children']
            childId = children[args[-1]]
            object = self.handle.get(childId)
            return json.loads(object)
