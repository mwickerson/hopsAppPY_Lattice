"""Hops flask middleware example"""
from flask import Flask
import ghhops_server as hs
import rhino3dm

# register hops app as middleware
app = Flask(__name__)
hops: hs.HopsFlask = hs.Hops(app)

# flask app can be used for other stuff drectly
@app.route("/help")
def help():
    return "Welcome to Grashopper Hops for CPython!"

"""
██╗      █████╗ ████████╗████████╗██╗ ██████╗███████╗
██║     ██╔══██╗╚══██╔══╝╚══██╔══╝██║██╔════╝██╔════╝
██║     ███████║   ██║      ██║   ██║██║     █████╗  
██║     ██╔══██║   ██║      ██║   ██║██║     ██╔══╝  
███████╗██║  ██║   ██║      ██║   ██║╚██████╗███████╗
╚══════╝╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝ ╚═════╝╚══════╝
"""            
#write a @hops component for a simple lattice structure
@hops.component(
    "/lattice_01",
    name="Lattice",
    description="Create a simple lattice structure",
    inputs = [
        hs.HopsInteger("Size", 10),
        hs.HopsInteger("Spacing", 10)
    ],
    outputs = [
        hs.HopsPoint("Points", "P", "Generated points")
    ]
)
def lattice_01(size, spacing):
    points = []
    for i in range(size):
        for j in range(size):
            points.append(rhino3dm.Point3d(i*spacing, j*spacing, 0))
    return points

#write a @hops component for a simple lattice structure and generate curves
@hops.component(
    "/lattice_lines_01",
    name="Lattice Lines",
    description="Create a simple lattice structure and generate lines",
    inputs = [
        hs.HopsInteger("Size", 10),
        hs.HopsInteger("Spacing", 10)
    ],
    outputs = [
        hs.HopsCurve("Lines", "L", "Generated lines")
    ]
)
def lattice_lines_01(size, spacing):
    import rhino3dm
    import math
    #create the list of points
    points = []
    for i in range(size):
        for j in range(size):
            points.append(rhino3dm.Point3d(i*spacing, j*spacing, 0))
    #create the list of lines
    lines = []
    for i in range(size-1):
        for j in range(size-1):
            lines.append(rhino3dm.LineCurve(points[i*size+j], points[i*size+j+1]))
            lines.append(rhino3dm.LineCurve(points[i*size+j], points[(i+1)*size+j]))
    return lines

#write a @hops component for a simple lattice structure with 3D trigonometric points
@hops.component(
    "/lattice_trig_02",
    name="Lattice Trig",
    description="Create a simple lattice structure with 3D trigonometric points",
    inputs = [
        hs.HopsInteger("Size", 10, access=hs.HopsParamAccess.ITEM),
        hs.HopsInteger("Spacing", 10, access=hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Amplitude", "A", "Amplitude of the trigonometric function", access=hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Frequency", "F", "Frequency of the trigonometric function", access=hs.HopsParamAccess.ITEM)
    ],
    outputs = [
        hs.HopsPoint("Points", "P", "Generated points", access=hs.HopsParamAccess.LIST)
    ],
)
def lattice_trig_02(size, spacing, amplitude, frequency):
    import math
    points = []
    for i in range(size):
        for j in range(size):
            points.append(rhino3dm.Point3d(i * spacing, j * spacing, amplitude * math.sin(frequency * i)))
    return points

#write a @hops component for a simple lattice structure with 3D trigonometric points into curves
@hops.component(
    "/lattice_trig_curves_01",
    name="Lattice Trig Curves", 
    description="Create a simple lattice structure with 3D trigonometric points into curves",
    inputs = [
        hs.HopsInteger("Size", 10, access=hs.HopsParamAccess.ITEM),
        hs.HopsInteger("Spacing", 10, access=hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Amplitude", "A", "Amplitude of the trigonometric function", access=hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Frequency", "F", "Frequency of the trigonometric function", access=hs.HopsParamAccess.ITEM)
    ],
    outputs = [
        hs.HopsCurve("Curves", "C", "Generated curves", access=hs.HopsParamAccess.LIST)
    ],
)
def lattice_trig_curves_01(size, spacing, amplitude, frequency):
    import math
    #create the list of points
    points = []
    for i in range(size):
        for j in range(size):
            points.append(rhino3dm.Point3d(i * spacing, j * spacing, amplitude * math.sin(frequency * i)))
    
    #create the list of lines
    curves = []
    for i in range(size-1):
        for j in range(size-1):
            curves.append(rhino3dm.LineCurve(points[i*size+j], points[i*size+j+1]))
            curves.append(rhino3dm.LineCurve(points[i*size+j], points[(i+1)*size+j]))
    return curves

#write a @hops component for a simple lattice structure with 3D trigonometric points into curves
#with rotations and stepping up in the z direction 
@hops.component(
    "/lattice_trig_rotation_01",
    name="Lattice Trig Rotation",
    description="Create a simple lattice structure with 3D trigonometric points into curves with rotations and stepping up in the z direction",
    inputs = [
        hs.HopsInteger("Size", 10, access=hs.HopsParamAccess.ITEM),
        hs.HopsInteger("Spacing", 10, access=hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Amplitude", "A", "Amplitude of the trigonometric function", access=hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Frequency", "F", "Frequency of the trigonometric function", access=hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Rotation", "R", "Rotation of the curves", access=hs.HopsParamAccess.ITEM)
        #hs.HopsNumber("Step", "S", "Step in the z direction", access=hs.HopsParamAccess.ITEM)
    ],
    outputs = [
        hs.HopsCurve("Curves", "C", "Generated curves", access=hs.HopsParamAccess.LIST)
    ],
)
def lattice_trig_rotation_01(size, spacing, amplitude, frequency, rotation):
    import math
    #create the list of points
    points = []
    for i in range(size):
        for j in range(size):
            points.append(rhino3dm.Point3d(i * spacing, j * spacing, amplitude * math.sin(frequency * i)))
    
    #create the list of lines
    curves = []
    for i in range(size-1):
        for j in range(size-1):
            curves.append(rhino3dm.LineCurve(points[i*size+j], points[i*size+j+1]))
            curves.append(rhino3dm.LineCurve(points[i*size+j], points[(i+1)*size+j]))
    
    #rotate the curves
    for i in range(len(curves)):
        curves[i].Rotate(rotation, rhino3dm.Vector3d(0,0,1), rhino3dm.Point3d(0,0,0))
    return curves

#write a @hops component for a simple lattice structure with 3D trigonometric points into curves
#with rotations and stepping up in the z direction 
@hops.component(
    "/lattice_trig_rotation_02",
    name="Lattice Trig Rotation",
    description="Create a simple lattice structure with 3D trigonometric points into curves with rotations and stepping up in the z direction",
    inputs = [
        hs.HopsInteger("Size", 10, access=hs.HopsParamAccess.ITEM),
        hs.HopsInteger("Spacing", 10, access=hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Amplitude", "A", "Amplitude of the trigonometric function", access=hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Frequency", "F", "Frequency of the trigonometric function", access=hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Rotation", "R", "Rotation of the curves", access=hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Step", "S", "Step in the z direction", access=hs.HopsParamAccess.ITEM)
    ],
    outputs = [
        hs.HopsCurve("Curves", "C", "Generated curves", access=hs.HopsParamAccess.LIST)
    ],
)
def lattice_trig_rotation_02(size, spacing, amplitude, frequency, rotation, step):
    import math
    #create the list of points
    points = []
    for i in range(size):
        for j in range(size):
            points.append(rhino3dm.Point3d(i * spacing, j * spacing, amplitude * math.sin(frequency * i)))

    #create the list of lines
    curves = []
    for i in range(size-1):
        for j in range(size-1):
            curves.append(rhino3dm.LineCurve(points[i*size+j], points[i*size+j+1]))
            curves.append(rhino3dm.LineCurve(points[i*size+j], points[(i+1)*size+j]))

    #rotate the curves
    for i in range(len(curves)):
        curves[i].Rotate(rotation, rhino3dm.Vector3d(0,0,1), rhino3dm.Point3d(0,0,0))

    #step up the curves
    for i in range(len(curves)):
        curves[i].Translate(rhino3dm.Vector3d(0,0,step))
    return curves

    















if __name__ == "__main__":
    app.run(debug=True)