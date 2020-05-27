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

    def __repr__(self):
        return f'(Upper left {self.upper_left}/lower right {self.lower_right})'


rectangles = [
    Rectangle(Points(0, 5), Points(5, 0)),
    Rectangle(Points(10, 15), Points(15, 10)),
    Rectangle(Points(2.5, 7), Points(7.5, 3)),
    Rectangle(Points(20, 5), Points(30, 15))
]


def main():
    '''
    Identify overlapping rectangles
    '''
    pass


if __name__ == '__main__':
    main()
