from unittest import TestCase, main
from collections import OrderedDict
class LRUCache(OrderedDict):
    def __init__(self, capacity: int):
        self.size = capacity

    def get(self, key: int) -> int:
        item = -1
        if key in self:
            item = self[key]
            self.move_to_end(key)
        return item

    def put(self, key: int, value: int) -> None:
        self[key] = value
        self.move_to_end(key)
        if len(self) > self.size:
            self.popitem(last=False)

class testLRUCache(TestCase):
    def test_get(self):
        lrucache = LRUCache(3)
        self.assertEqual(lrucache.get('one'),-1)
        lrucache.put('one', 1)
        self.assertEqual(lrucache.get('one'),1)
        lrucache.put('two', 2)
        self.assertEqual(lrucache.get('two'),2)
        
    def test_put(self):
        lrucache = LRUCache(3)
        lrucache.put('one', 1)
        self.assertEqual(lrucache.get('one'),1)
        lrucache.put('one', '1')
        self.assertEqual(lrucache.get('one'),'1')
        lrucache.put('two', 2)
        self.assertEqual(lrucache.get('two'),2)
        lrucache.put('three', 3)
        lrucache.put('four', 4)
        self.assertEqual(lrucache.get('one'),-1)
        lrucache.get('two')
        lrucache.put('five', 5)
        self.assertEqual(lrucache.get('three'),-1)

if __name__ == "__main__":
    main()