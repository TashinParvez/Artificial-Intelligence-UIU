# A* Search Assignment

## Part 1

> ### Graph Data Structure
> Keep a dictionary of the adjacent list as, **adjacency_list**:
> 
> Nodename as key, value as list of tuples
> 
> Keep another dictionary as **H**:
> 	Nodename as key, heuristic value as value

## Part 2

> ### Node Class
> Write a python class named **Node** with the following attributes:
> nodename : **String**
> 
> - **parent** : **Node**
> 
> - **g** : **float**
> 
> - **h** : **float**
> 
> - **f** : **float**
> 
> Add a constructor that takes four parameters(**nodename**, **parent**, **g**, **h**) to initialize the attributes

## Part 3

> ### A* Search & Solution Finding
> Create an empty list name priority_queue
> 
> Create a Node object, NOb of the “S” node with (**nodename**: ‘S’, parent: **None**, g: 0, h: **H**[‘S’]) and
> Insert the node in priority_queue
> 
> Now inside a while loop:

```
 while priority_queue is not empty:
 
 	Find out the Node object in priority_queue with the minimum value of f
 
 	Extract it from the priority_queue and store it in NOb
 
 	If NOb.nodename == ‘G’:
           break

 	For every neighbor of NOb.nodename from adjacency_list
 		Insert a new node in priority_queue with (nodename: neighbor_name, parent: NOb, g: NOb.g + edge_cost, h: H[NOb.nodename])
 	Set NOb = None
```

## Part 4

> ### Path Generation
> path = []
> 
> cost = NOb.g
> 
> **while** NOb.parent is not None:
> 
>> 	path.insert(**NOb**.**nodename**)
>> 
>> 	**NOb** = **NOb**.**parent**
> 
> **Reverse** the path list
> 
> Print the path and cost
>

# Given code:
```python

adjacency_list = {
    'S': [('A', 1), ('B', 4)],
    'A': [('B', 2), ('C', 5), ('G', 12)],
    'B': [('C', 2)],
    'C': [('D', 2), ('G', 3)],
    'D': [('G', 2), ('A', 2)],
    'G': [('C', 4)]
}

H = {
    'S': 7,
    'A': 6,
    'B': 2,
    'C': 1,
    'D': 1,
    'G': 0
}

```

# Solution : [LINK](https://github.com/TashinParvez/Artificial-Intelligence-UIU/blob/master/AI-Lab%20Assignments/ASSG%201%20-%20Sec-C__Spring24/011221437.py)
