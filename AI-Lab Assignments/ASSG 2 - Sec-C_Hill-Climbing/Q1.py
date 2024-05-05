import math

def Initialize():
    return [7, 1, 9, 0, 5, 8, 4, 2, 10, 0, 20]

def calculate_cost(state):
    sum = 0
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if state[j] < state[i]:
                sum+=1
            # print(state[i],'-->',sum)
    # print(state, ' -> ', sum) 
    return sum


def generate_neighbors(current_state):
    list_of_Current = current_state[:]

    neighbors = []
    for i in range(len(list_of_Current)):
        newList = current_state[:] 
        for j in range (i, len(list_of_Current)-1): 
            newList[j], newList[j+1] = newList[j+1], newList[j]  # swap
            # print(newList)
            neighbors.append(newList.copy())
            # neighbors.insert(len(neighbors)-1, newList)
            # print("tashin --> ", neighbors)

    return neighbors



def State_generation(current_state):

    while True:
        current_state_cost = calculate_cost(current_state)
        print(current_state, current_state_cost)

        # min_next_cost = float('inf') 
        min_next_cost = math.inf
        min_next_state = None

        for i in generate_neighbors(current_state):
            next_state = i
            next_state_cost = calculate_cost(next_state)

            if(next_state_cost < min_next_cost):
                min_next_cost = next_state_cost
                min_next_state = next_state
        
        if(min_next_cost < current_state_cost):
            current_state =min_next_state
        else:
            print("Final State:", current_state, current_state_cost )
            break


# main
state = Initialize()
State_generation(state)