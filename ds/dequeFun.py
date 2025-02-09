import collections

#######################   Stack   #######################
print("\n\n  #######################   Stack   #######################")

s = collections.deque()
s.append(1);  # 1
s.append(2);  # 1,2
s.append(3);  # 1,2,3
print(s)
s.pop();      # 1,2
print(s)
s.pop();      # 1
print(s)


#######################   QUEUE   #######################
print("\n\n  #######################   QUEUE   #######################")
q = collections.deque()
q.append(1);  # 1
q.append(2);  # 1,2
q.append(3);  # 1,2,3
print(q)
q.popleft();  # 2,3
print(q)
q.popleft();  # 3
print(q)



#######################   LINKEDLIST   #######################
print("\n\n  #######################   LINKEDLIST   #######################")
ll = collections.deque()
ll.append(1);     # 1
ll.append(2);     # 1,2
print(ll)
ll.appendleft(0); # 0,1,2
print(ll)
ll.pop();         # 0,1
print(ll)
ll.popleft();     # 1
print(ll)
