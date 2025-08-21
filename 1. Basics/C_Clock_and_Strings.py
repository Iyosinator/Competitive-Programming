import math

def hour_to_angle(hour):
    return math.radians((12 - hour) * 30)

def hour_to_point(hour):
    theta = hour_to_angle(hour)
    return (math.cos(theta), math.sin(theta))

def line_from_points(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (y2 - y1, x1 - x2, (y2 - y1) * x1 + (x1 - x2) * y1)

def intersection(line1, line2):
    A1, B1, C1 = line1
    A2, B2, C2 = line2
    det = A1 * B2 - A2 * B1
    if abs(det) < 1e-9:
        return None
    x = (C1 * B2 - C2 * B1) / det
    y = (A1 * C2 - A2 * C1) / det
    return (x, y)

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)

t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    
    A = hour_to_point(a)
    B = hour_to_point(b)
    C = hour_to_point(c)
    D = hour_to_point(d)

    line_AB = line_from_points(A, B)
    line_CD = line_from_points(C, D)

    E = intersection(line_AB, line_CD)

    if E is None:
        print("NO")
    else:
        AE = distance(A, E)
        EB = distance(E, B)
        CE = distance(C, E)
        ED = distance(E, D)

        print(f"{AE*EB:.3f} {CE*ED:.3f}")
        
        if abs(AE*EB - CE*ED) < 1e-6:
            print("YES")
        else:
            print("NO")

A = hour_to_point(a)
B = hour_to_point(b)
C = hour_to_point(c)
D = hour_to_point(d)

line_AB = line_from_points(A, B)
line_CD = line_from_points(C, D)

E = intersection(line_AB, line_CD)

if E is None:
    print("The chords do not intersect")
else:
    AE = distance(A, E)
    EB = distance(E, B)
    CE = distance(C, E)
    ED = distance(E, D)

    print(f"{AE*EB:.3f} {CE*ED:.3f}")
