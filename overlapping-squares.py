class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        print(f'X: {self.x}, Y: {self.y}')


class Rectangle:
    def __init__(self, upper_left, lower_right):
        self.upper_left = upper_left
        self.lower_right = lower_right

    def __repr__(self):
        print(f'''Rectangle bounds has upper left: {self.upper_left}
            and lower right {self.lower_right}''')


rectangles = [
    Rectangle(Points(0, 5), Points(5, 0)),
    Rectangle(Points(10, 15), Points(5, 10)),
    Rectangle(Points(2.5, 7.5), Points(7.5, 2.5))
]


def main():
    '''
    Identify overlapping rectangles
    '''
    pass


if __name__ == '__main__':
    main()
