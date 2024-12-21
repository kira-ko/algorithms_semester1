import unittest
from lab6.task4.src.main import ThreadedMap

class TestThreadedMap(unittest.TestCase):

    def test_put_and_get(self):
        tm = ThreadedMap()
        tm.put("a", "1")
        tm.put("b", "2")
        self.assertEqual(tm.get("a"), "1")
        self.assertEqual(tm.get("b"), "2")
        self.assertEqual(tm.get("c"), "<none>")

    def test_update_put(self):
        tm = ThreadedMap()
        tm.put("a", "1")
        tm.put("a", "2")
        self.assertEqual(tm.get("a"), "2")

    def test_delete(self):
        tm = ThreadedMap()
        tm.put("a", "1")
        tm.put("b", "2")
        tm.delete("a")
        self.assertEqual(tm.get("a"), "<none>")
        self.assertEqual(tm.get("b"), "2")

    def test_prev(self):
        tm = ThreadedMap()
        tm.put("a", "1")
        tm.put("b", "2")
        tm.put("c", "3")
        self.assertEqual(tm.prev("b"), "1")
        self.assertEqual(tm.prev("a"), "<none>")

    def test_next(self):
        tm = ThreadedMap()
        tm.put("a", "1")
        tm.put("b", "2")
        tm.put("c", "3")
        self.assertEqual(tm.next("b"), "3")
        self.assertEqual(tm.next("c"), "<none>")

    def test_delete_and_order(self):
        tm = ThreadedMap()
        tm.put("a", "1")
        tm.put("b", "2")
        tm.put("c", "3")
        tm.delete("b")
        self.assertEqual(tm.prev("c"), "1")
        self.assertEqual(tm.next("a"), "3")

if __name__ == "__main__":
    unittest.main()
