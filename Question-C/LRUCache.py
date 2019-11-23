from time import time, sleep
from collections import OrderedDict
'''
LRU cache based on Ordered Dictionary
'''
class LRUCache:
	'''
	cache: the LRU cache using OrderedDict (key, value)
	max_capacity: max_capacity of the cache
	access_time: an OrderedDict to track the access time of every item in the cache (key, time_in_secs)
	expiration: length of expiration time (in seconds)
	'''
	def __init__(self, max_capacity, expiration):
		self.cache = OrderedDict()
		self.max_capacity = max_capacity
		self.access_times = OrderedDict()
		self.expiration = expiration

	'''
	return the size of the cache
	'''
	def size(self):
		return len(self.cache)
		
	'''
	First, clear all the expired items in the cache before adding new item
	Then, add the key,value into cache and its access time into access_times
	By the property of OrderedDict, new item is inserted at the end of dictionary as the newest
	'''
	def set(self, key, value):
		if(self.size() >= self.max_capacity):
				self.clear_old()
		self.cache[key] = value
		self.access_times[key] = int(time())
	
	'''
	Update the access time of an item in get() operation
	Retrieve value of the key and pop it from the dictionary
	Update dictionary by inserting (key,value) at the end of the dictionary (as the newest) into the dictionary
	'''		
	def get(self, key):	
		self.access_times[key] = int(time())
		value = self.cache[key]
		self.cache.pop(key)
		self.cache.update({key: value})
		return value	
		
	'''
	Clear all expired items by check their expiration time with current time
	If the size of cache still exceeds the max capacity of the cache
		delete oldest items by using the property of FIFO from popitem(last=False)
	'''
	def clear_old(self):
		while(self.size() > self.max_capacity):
			for k in list(self.access_times.keys()):
				if self.access_times[k] + self.expiration < int(time()):
					self.access_times.pop(k)
					self.cache.pop(k)		
		while(self.size() >= self.max_capacity):
			self.cache.popitem(last=False)
			self.access_times.popitem(last=False)

