
def get_weighted_average(x,p1,p2):
    (x1,y1) = p1
    (x2,y2) = p2
    if x1 == x2:
        return y1
    return y1 + (x - x1) / (x2 - x1) * (y2 - y1)

def min_by(f, xs):
    temp = xs[0]
    for x in xs:
        if f(x) < f(temp):
            temp = x
    return temp

def max_by(f, xs):
    temp = xs[0]
    for x in xs:
        if f(x) > f(temp):
            temp = x
    return temp

def get_x_value(p):
    (x,y) = p
    return x

class Interpolate:
    def __init__(self,dataset):
        self.dataset = dataset
        self.min_x_point = min_by(get_x_value, dataset)
        self.max_x_point = max_by(get_x_value, dataset)

    def get_value(self, x):
        if x <= self.min_x_point[0]:
            return self.min_x_point[1]
        elif x >= self.max_x_point[0]:
            return self.max_x_point[1]
        else:
            left_end_point = max_by(get_x_value, [
                    p for p in self.dataset
                    if p[0] <= x
                ])
            right_end_point = min_by(get_x_value, [
                    p for p in self.dataset
                    if p[0] >= x
                ])
            return get_weighted_average(x,left_end_point,right_end_point)


p1 = (1.0, 7.0)
p2 = (5.0, 3.0)

dataset = [(-4,4),(-2,0),(-1,6),(1,7),(5,3)]

inter_obj = Interpolate(dataset)

print(inter_obj.get_value(1))
print(inter_obj.get_value(2))
print(inter_obj.get_value(3))
print(inter_obj.get_value(4))
print(inter_obj.get_value(5))
