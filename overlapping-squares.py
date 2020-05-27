class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'X: {self.x}, Y: {self.y}'


class Rectangle:
    def __init__(self, upper_left, lower_right):
        self.upper_left = upper_left
        self.lower_right = lower_right

    @property
    def x_min(self):
        return min(self.upper_left.x, self.lower_right.x)

    @property
    def x_max(self):
        return max(self.upper_left.x, self.lower_right.x)

    @property
    def y_min(self):
        return min(self.upper_left.y, self.lower_right.y)

    @property
    def y_max(self):
        return max(self.upper_left.y, self.lower_right.y)

    def __repr__(self):
        return f'(Upper left {self.upper_left}, lower right {self.lower_right})'


rectangles = [
    Rectangle(Points(0, 5), Points(5, 0)),
    Rectangle(Points(10, 15), Points(15, 10)),
    Rectangle(Points(2.5, 7), Points(7.5, 3))
]


def create_mapping():
    mapping = {}
    for rect1 in rectangles:
        not_self = []
        for rect2 in rectangles:
            if rect1 != rect2:
                not_self.append(rect2)
        mapping.update({rect1: not_self})
    return mapping


def compare_rectangles(rect1, rect2):
    '''
    1. Break compenents down: X, Y
    2. For each component, if max or min of rect1 is between max and min of rect2, then there is overlap
    '''
    x_between = False
    y_between = False
    cond1 = (rect2.x_min <= rect1.x_max <= rect2.x_max)
    cond2 = (rect2.x_min <= rect1.x_min <= rect2.x_max)
    if cond1 or cond2:
        x_between = True
    cond1 = (rect2.y_min <= rect1.y_max <= rect2.y_max)
    cond2 = (rect2.y_min <= rect1.y_min <= rect2.y_max)
    if cond1 or cond2:
        y_between = True

    if x_between or y_between:
        print('Overlap!')
        return True


def main():
    '''
    Identify overlapping rectangles
    1. Create dictionary with key as rectangle and value as list of other rectangles
    2. Compare key with all rectangles in value
    3. Keep only rectangles that overlap
    '''
    keep_list = []
    mapping = create_mapping()
    for key, value in mapping.items():
        for item in value:
            print('Comparing')
            print(key)
            print(item)
            overlap = compare_rectangles(key, item)
            if overlap:
                keep_list.append(key)
            print('\n')
    overlapping_rectangles = set(keep_list)
    print(overlapping_rectangles)


if __name__ == '__main__':
    main()
