
class vec3: 
    def __init__ (self, x, y, z): 
        self.x = x 
        self.y = y 
        self.z = z 

    def matrix_mul(self, xvec, yvec, zvec): 
        inter_x = self.x * xvec.x + self.y * yvec.x + self.z * zvec.x 
        inter_y = self.x * xvec.y + self.y * yvec.y + self.z * zvec.y 
        inter_z = self.x * xvec.z + self.y * yvec.z + self.z * zvec.z 
        self.x = inter_x
        self.y = inter_y
        self.z = inter_z

    def print(self): 
        print(f"x: {self.x}\ny: {self.y}\nz: {self.z}\n") 

class canvas: 
    def __init__ (self, width, height): 
        self.width = width 
        self.height = height
        self.screenbuffer = [['.' for i in range(self.width + 1)]for t in range(self.height + 1)]
    
    def clear(self): 
        for i in range(len(self.screenbuffer)):
            for j in range(len(self.screenbuffer[i])):
                self.screenbuffer[i][j] = '.'

    def draw(self, vertices):
        for vertex in vertices:
            self.screenbuffer[int((vertex.y * 0.5 + 0.5) * self.height)][int((vertex.x * 0.5 + 0.5) * self.width)] = "%"

    def display(self): 
        for row in self.screenbuffer: 
            print(*row)
            
