##################################################################################
# Variable definitions and such
name = 'Snorlaxative' # name of trainee :)
goal_EVs = [] # set for user input
cur_EVs = [] # EVs for defeating Pokemon
saved_EVs = [] # after implementing save
PokeDex = [] # will store array of pokemon (loaded depending no what user asks)


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

##################################################################################
# Main
reader('TestDex.txt')
#print(PokeDex)
print(bin_search(0, len(PokeDex), "Cranidos"))