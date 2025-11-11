
#Creating priority queue 
'''
Method 1:  Using a LIST
A very simple and straightforward way is to use the normal list but sort it every time an item is added. Here’s an example:
'''
customers = []
customers.append((2, "Harry")) #no sort needed here because 1 item. 
customers.append((3, "Charles"))
customers.sort(reverse=True) 
#Need to sort to maintain order
customers.append((1, "Riya"))
customers.sort(reverse=True) 
#Need to sort to maintain order
customers.append((4, "Stacy"))
customers.sort(reverse=True)
while customers:
     print(customers.pop(0))
#Will print names in the order: Stacy, Charles, Harry, Riya. 
print("\n\n\n")



'''
Method 2:  Using HEAPQ
We can also use the heapq module in Python to implement our priority queue. This implementation has O(log n) time for insertion and extraction of the smallest element. Note that heapq only has a min heap implementation, but there are other ways to use a max heap that we won’t cover in this article.
'''
import heapq
customers = []
heapq.heappush(customers, (2, "Harry"))
heapq.heappush(customers, (3, "Charles"))
heapq.heappush(customers, (1, "Riya"))
heapq.heappush(customers, (4, "Stacy"))
while customers:
     print(heapq.heappop(customers))
#Will print names in the order: Riya, Harry, Charles, Stacy.
print("\n\n\n")




'''
MAX HEAP
By default Min Heap is implemented by heapq. But we multiply each value by -1 so that we can use it as MaxHeap. 
'''
import heapq
customers = []
heapq.heappush(customers, (-1 * 2, "Harry"))
heapq.heappush(customers, (-1 * 3, "Charles"))
heapq.heappush(customers, (-1 * 1, "Riya"))
heapq.heappush(customers, (-1 * 4, "Stacy"))
while customers:
     print(heapq.heappop(customers))


'''
MAX HEAP 
using undocumented functionality of heapq
By default Min Heap is implemented by heapq. But we multiply each value by -1 so that we can use it as MaxHeap. 
'''
import heapq
customers = []
heapq.heappush(customers, (2, "Harry"))
heapq.heappush(customers, (3, "Charles"))
heapq.heappush(customers, (1, "Riya"))
heapq.heappush(customers, (4, "Stacy"))
print("----------")
print(customers)
heapq._heapify_max(customers)
print(customers)
# for pop use _heapop_max() instead of heappop()
print(heapq._heappop_max(customers))


# find n largest and n smallest elements from the heap using nlargest() and nsmallest()
import heapq
customers = []
customers.append((5, "Abhi5"))
customers.append((0, "Abhi0"))
heapq.heapify(customers)
heapq.heappush(customers, (2, "Harry"))
heapq.heappush(customers, (3, "Charles"))
heapq.heappush(customers, (1, "Riya"))
heapq.heappush(customers, (4, "Stacy"))

print("nsmallest")
print(heapq.nsmallest(2, customers))  # Output: [0,1]

print("nlargest")
print(heapq.nlargest(2, customers))  # Output: [4, 5]

