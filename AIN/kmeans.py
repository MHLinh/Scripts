import sys
import math
from tabulate import tabulate
import numpy as np

# Point class
# with coordinates x, y, z
class Point:
  def __init__(self, x, y, z = 0):
    self.x = x
    self.y = y
    self.z = z
  
  def __str__(self):
    return(f"({self.x}, {self.y}, {self.z})")

# A function for computing the Euclidean distance of two points.
# Parameters:
#   a, b - Points
def euclidean(a, b):
  x1 = a.x
  x2 = b.x
  y1 = a.y
  y2 = b.y
  z1 = a.z
  z2 = b.z
  return math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)

# A function for computing the Manhattan distance of two points.
# Parameters:
#   a, b - Points
def manhattan(a, b):
  x1 = a.x
  x2 = b.x
  y1 = a.y
  y2 = b.y
  z1 = a.z
  z2 = b.z
  return abs(x1-x2) + abs(y1-y2) + abs(z1-z2)

# A function for computing and assigning points to clusters.
# Parameters:
#   points - list of points
#   centers - list of centers
#   dist_func - method for calculating distance (Euclidean or Manhattan)
def calculate_clusters(points, centers, dist_func):
  data = []
  clusters = []
  for center in centers:
    clusters.append([])

  for point in points:
    distances = []
    for center in centers:
      distances.append(dist_func(point, center))
    cluster = min(distances)
    min_index = distances.index(cluster)
    clusters[min_index] += [point]
    row = [str(point)] + distances + [str(centers[min_index])] + [min_index+1]
    data.append(row)

  return data, clusters

# A helper function for printing a table of results for given iteration.
# Parameters:
#   data - list data about Points, its coordinates, center assigned to, and index of the center.
#   centers - list of centers
def print_table(data, centers):
  headers = ["Points"]
  for center in centers:
      headers.append(str(center))
  headers.append("Center")
  headers.append("Index")
  print()
  print(tabulate(data, headers))
  print()

# A function for computing the new center for a cluster.
# Parameters:
#   clusters - list of points belonging to a cluster
def calculate_centers(clusters):
  centers = []
  for cluster in clusters:
    total_x = 0
    total_y = 0
    total_z = 0
    num_points = len(cluster)
    for point in cluster:
      total_x += point.x
      total_y += point.y
      total_z += point.z
    if num_points > 0:
      average_x = total_x / num_points
      average_y = total_y / num_points
      average_z = total_z / num_points
      centers.append(Point(average_x, average_y, average_z))
  return centers

# A function for computing the clustering.
# Parameters:
#   points - list of points
#   initial_centers - list of initial centers
#   dist_func - method for calculating distance (Euclidean or Manhattan)
#   iterations - number of iterations to compute for
def clustering_iterations(points, initial_centers, dist_func, iterations):
  centers = initial_centers
  for i in range(iterations):
    print()
    print(f"Iteration: {i+1}")
    # print("Iteration: " + str(i+1))
    data, clusters = calculate_clusters(points, centers, dist_func)
    new_centers = calculate_centers(clusters)
    print_table(data, centers)
    print("New centers")
    for center in new_centers:
      print(center)
    centers = new_centers

# A function for computing the clustering using k means ++.
# Parameters:
#   points - list of points
#   initial_center - the initial centers
#   k - the k number
#   dist_func - method for calculating distance (Euclidean or Manhattan)
#   iterations - number of iterations to compute for
def k_means_pp(points, initial_center, dist_func, k, iterations):
  centers = [initial_center]
  for j in range(k-1):
    djs = []
    for each in points:
        distance = [dist_func(each, center) for center in centers]
        min_d = min(distance)
        djs.append(min_d*min_d)
    probs = []
    dl = sum(djs)
    for i, each in enumerate(djs):
        probs.append(djs[i]/dl)
    new_center = points[np.array(probs).argmax()]
    centers.append(new_center)
    print(f"Iteration {j}, probabilities {probs}, new center {new_center}")
  
  print("All centers")
  for each in centers:
    print(each)
    
  clustering_iterations(arr, centers, euclidean, iterations)

# p1 = Point(2,1)
# p2 = Point(1,2)
# print(euclidean(p1, p2))
# print(manhattan(p1, p2))

# arr = [
#   Point(2.1,4.2),
#   Point(3.2,5.1),
#   Point(4.7,5.5),
#   Point(2.6,2.9),
#   Point(5.4,4.6),
#   Point(3.5,2.9),
#   Point(1.3,1.7),
#   Point(1.2,1.9),
# ]

arr = [
  Point(5,8),
  Point(6,7),
  Point(6,4),
  Point(5,7),
  Point(5,5),
  Point(6,5),
  Point(1,7),
  Point(7,5),
  Point(6,5),
  Point(6,7)
]

initial_centers = [
  Point(7,5),
  Point(9,7),
  Point(9,1)
]

print("Manhattan K-Median")
clustering_iterations(arr, initial_centers, manhattan, 3)

# print("Euclidean K-Means")
# clustering_iterations(arr, initial_centers, euclidean, 3)

# print("K-Means++")
# k_means_pp(initial_centers[0], arr, euclidean, 2, 3)