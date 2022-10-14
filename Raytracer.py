from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *


width = 512
height = 512

# Materiales

brick = Material(diffuse = (0.8, 0.3, 0.3), spec = 16)
stone = Material(diffuse = (0.4, 0.4, 0.4), spec = 8)
grass = Material(diffuse = (0.3, 1.0, 0.3), spec = 64)
earth = Material(texture=Texture('earthDay.bmp'))


marble = Material(spec = 64, texture = Texture("descarga.bmp"), matType= REFLECTIVE)

mirror = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, matType = REFLECTIVE)
glass = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, ior = 1.5, matType = TRANSPARENT)
blueMirror = Material(diffuse = (0.2, 0.2, 0.9), spec = 64, matType = REFLECTIVE)
yellowMirror = Material(diffuse = (0.9, 0.9, 0.2), spec = 64, matType = REFLECTIVE)

rtx = Raytracer(width, height)

rtx.envMap = Texture("parkingLot.bmp")

rtx.lights.append( AmbientLight(intensity = 0.1 ))
#rtx.lights.append( DirectionalLight(direction = (0,0,-1), intensity = 0.5 ))
rtx.lights.append( PointLight(point = (-1,-1,0) ))


rtx.scene.append( Plane(position = (0,-10,0), normal = (0,1,0), material = brick ))
rtx.scene.append( Plane(position = (0,10,0), normal = (0,-1,0), material = earth ))
rtx.scene.append( Plane(position = (-10,0,0), normal = (1,0,0), material = stone ))
rtx.scene.append( Plane(position = (10,0,0), normal = (-1,0,0), material = yellowMirror ))
rtx.scene.append( Plane(position = (0,0,-40), normal = (0,0,1), material = stone ))

rtx.scene.append( Disk(position = (0,-3,-7), radius = 2, normal = (0,1,0), material = mirror ))



rtx.glRender()

rtx.glFinish("output.bmp")