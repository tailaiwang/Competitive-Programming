#Design HashMap
#https://leetcode.com/problems/design-hashmap/
#Easy (Data Structures II), 18/04/2022
#Tailai Wang

class MyHashMap(object):
    myMap = {}
    def __init__(self):
        self.myMap = {}

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.myMap[key] = value
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.myMap:
            return self.myMap[key]
        else:
            return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.myMap:
            del self.myMap[key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)