from unittest import TestCase, main

class _node:
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head, self.tail = _node(), _node()
        self.head.next, self.tail.prev = self.tail, self.head
        self.cache = {}

    def _addnode(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def _removenode(self, node):
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev
    
    def _popitem(self):
        item = self.tail.prev
        self._removenode(item)
        return item

    def _movetohead(self, node):
        self._removenode(node)
        self._addnode(node)

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._movetohead(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._movetohead(node)
        else:
            node = _node()
            node.key = key
            node.value = value
            self.cache[key] = node
            self._addnode(node)
            if len(self.cache) > self.capacity:
                item = self._popitem()
                del self.cache[item.key]

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