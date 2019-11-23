# Question C
**Description:** 

- At Ormuco, we want to optimize every bits of software we write. Your goal is to write a new library that can be integrated to the Ormuco stack. Dealing with network issues everyday, latency is our biggest problem. Thus, your challenge is to write a new Geo Distributed LRU (Least Recently Used) cache with time expiration. This library will be used extensively by many of our services so it needs to meet the following criteria:
 
    1. Simplicity. Integration needs to be dead simple.
    2. Resilient to network failures or crashes.
    3. Near real time replication of data across Geolocation. Writes need to be in real time. 
    4. Data consistency across regions 
    5. Locality of reference, data should almost always be available from the closest region
    6. Flexible Schema
    7. Cache can expire

**Solutions:**

- In **LRUCache.py**, a LRU cache based on Ordered Dictionary is implemented as the class `LRUCache` with the following attributes:
  - `cache`: the LRU cache using OrderedDict (key, value)
  - `max_capacity`: max_capacity of the cache
  -	`access_time`: an OrderedDict to track the access time of every item in the cache (key, time_in_secs)
  -	`expiration`: length of expiration time (in seconds)

- test script is written in **test_LRUCache.py**