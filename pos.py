import matrix
import quaternion

# transformation matrices

class Position:

    def __init__(self, x, y, z):
        self.vec = [
            [x],
            [y],
            [z],
            [1]
        ]

    # world coords transformations
    def rotateX(self, theta):
        r = quaternion.rotate([self.vec[0][0], self.vec[1][0], self.vec[2][0]],
            [1,0,0], theta)
        return Position(r[0],r[1],r[2])
    
    def rotateY(self, theta):
        r = quaternion.rotate([self.vec[0][0], self.vec[1][0], self.vec[2][0]],
            [0,1,0], theta)
        return Position(r[0],r[1],r[2])
                
    def rotateZ(self, theta):
        r = quaternion.rotate([self.vec[0][0], self.vec[1][0], self.vec[2][0]],
            [0,0,1], theta)
        return Position(r[0],r[1],r[2])

    def rotate(self, rot_about, theta):
        """rot_about = unit vector to rotate about
        theta = radians"""
        r = quaternion.rotate([self.vec[0][0], self.vec[1][0], self.vec[2][0]],
            [rot_about[0], rot_about[1], rot_about[2]], theta)
        return Position(r[0],r[1],r[2])

    def scale(self, factor = 1, **kwargs):
        """vec = column vector of homogeneous coords
        factor = uniform scaling factor
        x = scaling factor of x
        y = scaling factor of y
        z = scaling factor of z"""
        S = [
            [factor*kwargs["x"], 0, 0, 0],
            [0, factor*kwargs["y"], 0, 0],
            [0, 0, factor*kwargs["z"], 0],
            [0, 0, 0, 1]
        ]
        vec = matrix.multiply(S, self.vec)
        return Position(vec[0][0],vec[1][0],vec[2][0])

    def translate(self, x, y, z):
        T = [
            [1, 0, 0, x],
            [0, 1, 0, y],
            [0, 0, 1, z],
            [0, 0, 0, 1]
        ]
        vec = matrix.multiply(T, self.vec)
        return Position(vec[0][0],vec[1][0],vec[2][0])

    # transform world space coords into eye space coords (view matrix)
    # it's inverse of the camera's transformation matrix in world-space
    def cam_transform(self, cam_pos, cam_upvec = [[0],[1],[0]]):
        """cam_pos = column vec3 representing camera's position
        cam_upvec = column vec3 representing camera's upright direction
        returns Position object representing the camera's view"""

        t = self.translate(-cam_pos[0][0], -cam_pos[1][0], -cam_pos[2][0])

        # ***maybe try quaternions here instead?
        # 3 perpendicular unit vecs with Z pointing towards the camera
        Z = matrix.normalize(matrix.subtract(t.vec[0:3], cam_pos))
        X = matrix.normalize(matrix.crossprod(cam_upvec, Z))
        Y = matrix.crossprod(Z, X)
        C = [
            [X[0][0], X[1][0], X[2][0], 0], # [Xaxis.x, Xaxis.y, Xaxis.z, 0]
            [Y[0][0], Y[1][0], Y[2][0], 0], # [Yaxis.x, Yaxis.y, Yaxis.z, 0]
            [Z[0][0], Z[1][0], Z[2][0], 0], # [Zaxis.x, Zaxis.y, Zaxis.z, 0]
            [0, 0, 0, 1]
        ]
        vec = matrix.multiply(C, t.vec)
        return Position(vec[0][0],vec[1][0],vec[2][0])

    # projects to normalized device coords (NDC)
    def project(self, **frustum):
        """parameter frustum takes in a frustum defined by:
        l = left of projection plane
        r = right of projection plane
        t = top of projection plane
        b = bottom of projection plane
        n = near (focal pt to proj plane in abs dist)
        f = far (abs dist)
        returns vec3 representing NDC"""
        r4 = [0, 0, -1, 0] # copy -z to w to convert clip to NDC

        l = frustum['l']
        r = frustum['r']
        t = frustum['t']
        b = frustum['b']
        n = frustum['n']
        f = frustum['f']
        r1 = [2*n/(r-l), 0, (r+l)/(r-l), 0] # converts x from eye to clip coords
                                            # (linear relationship between x proj and x ndc)

        r2 = [0, 2*n/(t-b), (t+b)/(t-b), 0] # converts y from eye to clip coords, as x
        
        r3 = [0, 0, -(f+n)/(f-n), -2*f*n/(f-n)] # converts z from eye to clip coords
                                                # although z always projects to -n, 
                                                # each z in eye space has to have
                                                # a unique value in clip space to
                                                # know what's nearer and what's further
        
        P = [r1, r2, r3, r4]
        vec = matrix.multiply(P, self.vec) # transform from eye space to clip space

        w = vec[3][0]
        vec = [
            [vec[0][0]/w], 
            [vec[1][0]/w], 
            [vec[2][0]/w]
        ] # convert from clip space (homogeneous coords) to NDC (cartesian)
        return vec

    @staticmethod
    def to_screen(vec, x_offset, y_offset, width, height):
        """converts NDC to screen coordinates using a linear mapping
        vec = vec3
        x_offset = x value screen offset
        y_offset = y value screen offset
        width = screen width
        height = screen height
        returns [x, y] representing screen coordinates"""
        # ***work on adding Z mapping
        return [(width/2)*vec[0][0] + x_offset + width/2,
            (height/2)*vec[1][0] + y_offset + height/2]
    
if __name__ == "__main__":
    # v = Position(1,1,1)
    # # top 4 vertex
    # v1 = Position(1,1,1)
    # v2 = Position(-1,1,1)
    # v3 = Position(-1,1,-1)
    # v4 = Position(1,1,-1)
    # # bottom 4 vertex
    # v5 = Position(1,-1,1)
    # v6 = Position(-1,-1,1)
    # v7 = Position(-1,-1,-1)
    # v8 = Position(1,-1,-1)
    # vertex = [v1,v2,v3,v4,v5,v6,v7,v8]

    # for v in range(len(vertex)):
    #     vertex[v].project(l=-2,r=2,t=2,b=-2,n=2,f=8)
    
    # print("\n\n")
    # for v in range(len(vertex)):
    #     print(vertex[v].vec)
    pass