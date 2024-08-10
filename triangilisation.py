import math as m
import matplotlib.pyplot as plt
import sympy.geometry as sm
def cercle_of_triangle(T):
     circle = sm.Circle(sm.Point(T[0][0],T[0][1]),sm.Point(T[1][0],T[1][1]),sm.Point(T[2][0],T[2][1]))
     return circle.radius.evalf(),(circle.center.evalf()[0],circle.center.evalf()[1])

def test_in_cercle(r,o,p):
     d_op = m.sqrt((p[0] - o[0])**2 + (p[1] - o[1])**2)
     if d_op < r :
          return True
     else :
          return False
def creat_super_trinagle(L):
     global sup_tr
     a = sorted(L)
     xmin,xmax = a[0][0],a[-1][0]
     b= sorted([(y,x) for x,y in L])
     ymin,ymax = b[0][0],b[-1][0]
     plt,prt,prb,plb = (xmin -1,ymax+1),(xmax +1,ymax+1),(xmax +1,ymin-1),(xmin -1,ymin - 1)
     a1 = -(prt[0]-plb[0])/(prt[1]-plb[1])
     a2 = -(plt[0]-prb[0])/(plt[1]-prb[1])
     print(plt,plb,prt,prb)

     b1 = prt[1]- a1*prt[0]
     b2 = plt[1]- a2*plt[0]
     p1 = (b2-b1)/(a2-a1),(a1*(b2-b1)/(a2-a1) + b1)
     p2 = (plb[1]-b2)/a2,plb[1]
     p3 = (prb[1]-b1)/a1,prb[1]
     return p1,p2,p3


     

def equals(tr1,tr2):
    for p in tr1 :
         if not p in tr2:
              return False
    return True
def In(trinagles , tr):
    for t in trinagles :
        if equals(t,tr):
            return True
    return False
def denely_trinagilisation(triangles,P):
    if triangles == []:
        return []
    for point in triangles[0]:
        if not point in P :
            return denely_trinagilisation(triangles[1:], P)
    return [triangles[0]] + denely_trinagilisation(triangles[1:], P)
points = [(1, 2), (4, 8), (7, 3), (2, 6), (5, 11), (9, 4), (6, 7), (10, 1), (3, 9), (8, 5), (12, 2), (14, 7), (11, 10), (13, 3), (15, 8),(4.94906,2.72425),(3.81318,1.54468),(5.82282,1.08595),(3.52921,2.72425),(3.44183,4.42807),(3.68212,0.58354),(2.67729,1.58836)]
sup_tr = []

def  triangilisation(P):
     sup_triangle = creat_super_trinagle(P)
     triangles = [sup_triangle]
     new_triangles = []
     triagle_to_be_removed = []
     for p in P :
          for tr in  triangles:
               r,o = cercle_of_triangle(tr)

               if test_in_cercle(r,o,p):
                triagle_to_be_removed+= [tr]
                for i in range(3):
                     for j in range(i+1,3):
                          temp_tr = [p,tr[i],tr[j]]
                          if In(new_triangles,temp_tr):
                           new_triangles.remove(temp_tr)
                          else :
                           new_triangles.append(temp_tr)
          for tr in triagle_to_be_removed :
              triangles.remove(tr)
          for tr in new_triangles :
              triangles.append(tr)
          triagle_to_be_removed = []
          new_triangles = []
     return denely_trinagilisation(triangles,P)
# print(triangilisation(points))
# plt.scatter([point[0] for point in points],[point[1] for point in points])
# plt.show()
# print(cercle_of_triangle([(1,2),(4,6),(5,1)]))
# import matplotlib.pyplot as plt
# import matplotlib.tri as tri
# import numpy as np

# # Exemple de coordonnées des sommets du triangle
# triangles = triangilisation(points)
# for tr in triangles:
#  x = np.array([tr[0][0], tr[1][0], tr[2][0]])
#  y = np.array([tr[0][1], tr[1][1], tr[2][1]])

#  # Créer une triangulation
#  triangulation = tri.Triangulation(x, y)

#  # Tracer la triangulation
#  plt.triplot(triangulation, '', label='')
#  plt.scatter([x for x,y in points],[y for x,y in points])
# plt.scatter([x for x,y in sup_tr],[y for x,y in sup_tr],c='red')


# plt.show()






