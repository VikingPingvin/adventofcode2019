from Day3.parse_source_into_lines import parse_source as ps


def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return 0

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

def is_intersect_result_tuple(result):
    return True if isinstance(result, tuple) else False

class line:
    def __init__(self, startPoints, endPoints):
        (x0, y0) = startPoints
        (x1, y1) = endPoints


if __name__ == '__main__':
    A = (1, 2)
    print(is_intersect_result_tuple(A))
    wires_parsed = ps("source")
    print(wires_parsed)