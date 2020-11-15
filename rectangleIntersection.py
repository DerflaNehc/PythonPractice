from typing import List

#Given two rectangles, return the intersected rectangle if it exists
def rectangleIntersection(rec1:List[List[int]],rec2:List[List[int]])->List[List[int]]:
    #Sort the inputs in respect to the x values
    rec1.sort()
    rec2.sort()
    #obtain x values from smallest to largest
    x1 = [rec1[0][0],rec1[2][0]]
    x2 = [rec2[0][0],rec2[2][0]]

    #Sort the inputs in respect to the y values
    rec1.sort(key=lambda e:e[1])
    rec2.sort(key=lambda e:e[1])
    #obtain y values from smallest to largest
    y1 = [rec1[0][1],rec1[2][1]]
    y2 = [rec2[0][1],rec2[2][1]]

    #Return nothing if rectangles do not intersect
    if x1[0]>x2[1] or x1[1]<x2[0] or y1[0]>y2[1] or y1[1]<y2[0]:
        return 0

    #Coordinates for new rectangle
    xn1 = max(x1[0],x2[0])
    xn2 = min(x1[1],x2[1])
    yn1 = max(y1[0],y2[0])
    yn2 = min(y1[1],y2[1])

    return [[xn1,yn1],[xn1,yn2],[xn2,yn1], [xn2,yn2]]

if __name__ == '__main__':
    a = [[1,0],[-1,5],[-1,0],[1,5]]
    b = [[0,0],[-1,3],[-1,0],[0,3]]
    print(rectangleIntersection(a,b))