# Test inputs

# wire1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
# wire2 = ['U62','R66','U55','R34','D71','R55','D58','R83']

# wire1 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
# wire2 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']
#
# wire1 = ['R8', 'U5', 'L5', 'D3']
# wire2 = ['U7', 'R6', 'D4', 'L4']

# Read input from file
file = open('puzzle_input.txt', 'r')
lines = file.readlines()
ll = []

for line in lines:
    ll.append(line.split(','))

wire1 = ll[0]
wire2 = ll[1]


def get_wire_path_coordinates(wire_path):
    origin = [0, 0]
    path = []
    all_points = []

    for direction in wire_path:
        if direction[0] == 'R':
            for c in range(origin[0]+1, origin[0] + int(direction[1:]) + 1):
                all_points.append((c, origin[1]))
            origin[0] += int(direction[1:])
            coordinate = (origin[0], origin[1])
            path.append(coordinate)

        if direction[0] == 'L':
            for c in range(origin[0]-1, origin[0]-int(direction[1:]) - 1, -1):
                all_points.append((c, origin[1]))
            origin[0] -= int(direction[1:])
            coordinate = (origin[0], origin[1])
            path.append(coordinate)

        if direction[0] == 'U':
            for c in range(origin[1]+1, origin[1] + int(direction[1:]) + 1):
                all_points.append((origin[0], c))
            origin[1] += int(direction[1:])
            coordinate = (origin[0], origin[1])
            path.append(coordinate)

        if direction[0] == 'D':
            for c in range(origin[1]-1, origin[1]-int(direction[1:]) - 1, -1):
                all_points.append((origin[0], c))
            origin[1] -= int(direction[1:])
            coordinate = (origin[0], origin[1])
            path.append(coordinate)

    return all_points


points1 = get_wire_path_coordinates(wire1)
points2 = get_wire_path_coordinates(wire2)


wc1 = list(dict.fromkeys(get_wire_path_coordinates(wire1)))
wc2 = list(dict.fromkeys(get_wire_path_coordinates(wire2)))

intersections = set(wc1).intersection(set(wc2))

min_steps = 9999999999999
for i in intersections:
    min_steps1 = points1.index(i) + 1
    min_steps2 = points2.index(i) + 1
    total_steps = min_steps1 + min_steps2
    if total_steps < min_steps:
        min_steps = total_steps

# Alternate method to avoid holding all coordinates of the wire, needs tweaking

# def line_segment_intersection(point1, point2, point3, point4):
#
#     x1, y1 = point1
#     x2, y2 = point2
#     x3, y3 = point3
#     x4, y4 = point4
#
#     a = x1-x3
#     b = y3-y4
#     c = y1-y3
#     d = x3-x4
#     e = x1-x2
#     f = y1-y2
#
#     if (e*b)-(f*d) == 0:
#         return None
#     else:
#         t = ((x1 - x3)*(y3 - y4) - (y1 - y3)*(x3 - x4)) / ((x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4))
#
#         u = -((x1 - x2)*(y1 - y3) - (y1 - y2)*(x1 - x3)) / ((x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4))
#
#         if 0 <= t <= 1 and 0 <= u <= 1:
#             intersection = (x1+t*(x2-x1), y1+t*(y2-y1))
#             return intersection
#         else:
#             return None


# def list_intersection_points():
#
#     intersection_points = []
#     wire1_coords = get_wire_path_coordinates(wire1)
#     wire2_coords = get_wire_path_coordinates(wire2)
#
#
#     for i in range(0, len(wire1_coords)-1):
#         for j in range(0, len(wire2_coords)-1):
#             intersection = line_segment_intersection(
#                             wire1_coords[i], wire1_coords[i+1],
#                             wire2_coords[j], wire2_coords[j+1]
#                             )
#
#             if intersection:
#                 intersection_points.append(intersection)
#
#     return intersection_points


def closest_intersection_point(list_points):
    closest_coords = min(list_points, key=lambda x: abs(x[0]) + abs(x[1]))
    return abs(closest_coords[0]) + abs(closest_coords[1])
