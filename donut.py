from lin_algebra import * 
from math import pi, sin, cos
import os

def gen_donut(rings_in_donut, vertices_per_ring, radius, thickness): 
    ring = []
    donut = []
    angle_per_vertex = (2*pi)/vertices_per_ring
    for i in range(vertices_per_ring):
        ring.append(vec3((thickness/2) * sin(i * angle_per_vertex) + radius - (thickness / 2), 0, (thickness/2) * cos(i * angle_per_vertex)))
    angle_per_ring = (2*pi)/rings_in_donut
    for i in range(rings_in_donut):
        for vertex in ring: 
            donut.append(vec3(vertex.x, vertex.y, vertex.z))
            vertex.matrix_mul(vec3(cos(angle_per_ring), sin(angle_per_ring), 0), vec3(-sin(angle_per_ring), cos(angle_per_ring), 0), vec3(0,0,1))
    return donut

def rotate(donut, rotations): 
    angle = (2*pi) / rotations
    i = vec3(0.5 * (1 + cos(angle)), 0.5 * (sin(angle)), 0)
    j = vec3(0.5 * (-sin(angle)), cos(angle), 0.5 * sin(angle))
    k = vec3(0, 0.5 * -sin(angle), 0.5* (1 + cos(angle))) 
    for vertex in donut: 
        vertex.matrix_mul(i, j, k)


donut = gen_donut(200, 100, 0.9, 0.5)
screen = canvas(80, 80)

while True:
    
    screen.clear()
    rotate(donut, 100)
    screen.draw(donut)
    os.system('clear')
    screen.display()
