##################################################################################
# Variable definitions and such
name = 'Snorlaxative' # name of trainee :)
goal_EVs = [] # set for user input
cur_EVs = [] # EVs for defeating Pokemon
saved_EVs = [] # after implementing save
PokeDex = [] # will store array of pokemon (loaded depending on what user asks)
has_goal = False
has_cur = False


##################################################################################
# Function definitions and such
def reader(dex):
    with open(dex) as f:
        for line in f: # read rest of lines
            PokeDex.append([x for x in line.split()])

def bin_search(low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if PokeDex[mid][0] == x:
            return PokeDex[mid]
        elif PokeDex[mid][0] > x:
            return bin_search(low, mid - 1, x)
        else:
            return bin_search(mid + 1, high, x)
    else:
        return -1

def welcome():
    # initialization of information (name, goals/current EVs, which dex to use, etc)
    name = input("Enter trainee's name: ")
    print("Welcome, %s" %name)

    while not has_goal:
        goal_line = input("Enter 6 GOAL EVs (separated by spaces)\nRefer to README for details")
        goal_EVs.append(x for x in goal_line.split())
        if len(goal_EVs) == 6:
            has_goal = True
        else:
            goal_EVs = []
    
    
    while not has_cur:
        cur_line = input("Enter 6 current EVs (separated by spaces), -1 if untrained\nRefer to README for details")
        if cur_line == -1:
            has_cur = True

        else:
            cur_EVs.append(x for x in cur_line.split())
            if len(cur_EVs) == 6:
                has_cur = True
            else:
                cur_EVs = []


##################################################################################
# Main
reader('TestDex.txt')
#print(PokeDex)
print(bin_search(0, len(PokeDex), "Cranidos"))