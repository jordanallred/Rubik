from rubik.model.cube import Cube

def rotate(parms):
    """Return rotated cube""" 
    result = {}
    # cube must be alphanumeric of 54 characters with unique 6 unique colors and unique centers
    # stub code
    encodedCube = parms.get('cube')
    theCube = Cube(encodedCube)
    
    directions = parms.get('dir')
    theCube.rotate(directions)
    
    result['cube'] = theCube.get()
    
    # remember to check for errors before returning 200 status
    result['status'] = 'ok'
    return result