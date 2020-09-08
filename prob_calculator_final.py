import copy
import random
# Consider using the modules imported above.

class Hat:

    # Read input args; load balls (by: color, qty.) into list
    def __init__(self, **ball_args):
        self.contents = []
        for key, value in ball_args.items():
            for _ in range(value):
                self.contents.append(key)

    def draw(self, number):
        balls_drawn = []
        # Test if draw qty. > available ball qty.: return all the balls to the hat
        if number >= len(self.contents):
            return self.contents
        
        # Pick a ball at random and remove from the bag
        for _ in range(number):
            ball_picked = random.choice(self.contents)
            balls_drawn.append(ball_picked)
            self.contents.pop(self.contents.index(ball_picked))

        return balls_drawn

    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    match_count = 0
    for n in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        draw_sample = hat_copy.draw(num_balls_drawn)
#        print(draw_sample)        
        # compare drawn balls to expected balls
        match = True
        for key in expected_balls.keys():
            if draw_sample.count(key) < expected_balls[key]:
                match = False
                break
        if match:
            match_count += 1
  
    return match_count / num_experiments