from itertools import combinations_with_replacement, product
from tqdm import tqdm

from src.base_class import riddle



class action():
    def __init__(self, action: str):
        self.action = list(map(int, action[1:-1].split(",")))
        
    def __repr__(self):
        return f"action({self.action})"
    

class Light():
    def __init__(self, vals: list[int], goal = ""):
        self.value = vals
        self.original_goal = goal
        self.has_goal = len(goal) > 0
        if self.has_goal:
            self.goal = goal

    
    def __repr__(self):
        return f"Light({self.value}, {self.goal})"  
    
    def add(self, other:action):
        for i in other.action:
            self.value[i] += 1
            if not self.has_goal:
                self.value[i] %= 2
            
    def is_zero(self):
        if self.has_goal:
            return all( v == g for v, g in zip(self.value, self.goal) )
        return all(v == 0 for v in self.value)

   
      
class day(riddle):
    def __init__(self, day, mode):
        super().__init__(day, mode)

    def a(self):
        fewest_clicks = [] 
        with open("day10/full.txt") as f:
            for line in tqdm(f.read().splitlines()):

                line = line.split(" ")
                l = Light(list(map(int, line[0][1:-1].replace("#", "1").replace(".", "0"))))
                possible_actions = [action(x) for x in line[1:-1]]

                my_repeat = 1 
                found_solution = False 
                
                while not found_solution:
                    
                    for my_actions in product(possible_actions, repeat=my_repeat):
                        test_light = Light(l.value.copy())

                        for a in my_actions:
                            test_light.add(a)
                        if test_light.is_zero():
                            # print(f"Found solution: {my_actions}")
                            found_solution = True
                            fewest_clicks.append(len(my_actions))
                            break
                        
                    my_repeat += 1
        print(sum(fewest_clicks))

    def b(self):
        fewest_clicks = [] 
        with open("day10/test.txt") as f:
            for line in tqdm(f.read().splitlines()):
                line = line.split(" ")

                possible_actions = [action(x) for x in line[1:-1]]
                goal =line[-1]

                l = Light(list(map(int, line[0][1:-1].replace("#", "1").replace(".", "0"))), goal=list(map(int,goal[1:-1].split(","))))

                my_repeat = 1 
                found_solution = False 
                
                while not found_solution:

                    for my_actions in product(possible_actions, repeat=my_repeat):
                        test_light = Light(l.value.copy(), l.original_goal.copy())

                        for a in my_actions:
                            test_light.add(a)
                        if test_light.is_zero():
                            # print(f"Found solution: {my_actions}")
                            found_solution = True
                            fewest_clicks.append(len(my_actions))
                            break
                        
                    my_repeat += 1
        print(sum(fewest_clicks))


if __name__ == "__main__":
    x = day(day=8, mode="full")
    x.a()
    x.b()