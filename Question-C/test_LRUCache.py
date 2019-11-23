from LRUCache import *

def testLRUCache():		
	# create a cache which has maxcapacity = 3, expiration time = 4 seconds
	lru = LRUCache(3, 4)
	
	# add k,v pair and sleep for 5 seconds for the purpose of testing expiration
	lru.set("a", 1)
	sleep(5)
	print("set(\"a\", 1)")
	print("access_times:", lru.access_times)
	print("cache:",lru.cache, "\n")
	
	# add k,v pair and sleep for 2 seconds
	lru.set("b", 2)
	sleep(2)
	print("set(\"b\", 2)")
	print("access_times:", lru.access_times)
	print("cache:",lru.cache, "\n")	
	
	# add k,v pair and sleep for 3 seconds
	lru.set("c", 3)
	sleep(1)
	print("set(\"c\", 3)")
	print("access_times:", lru.access_times)
	print("cache:",lru.cache, "\n")
	
	# get b from the cache, b then should be at the end of cache
	lru.get("b")
	print("get(\"b\")")
	print("access_times:", lru.access_times)
	print("cache:",lru.cache, "\n")	
	
	# add fourth k,v pair, at this time, a should be removed since it is expired
	lru.set("d", 4)
	print("set(\"d\", 4)")
	print("access_times:", lru.access_times)
	print("cache:",lru.cache, "\n")
	
	# add another k,v pair, at this time c should be removed since it is the oldest (not because it is expired)
	lru.set("e", 5)
	print("set(\"e\", 5)")
	print("access_times:", lru.access_times)
	print("cache:",lru.cache, "\n")
	
if __name__ == '__main__':
	print("Start testing:\n")
	testLRUCache()
