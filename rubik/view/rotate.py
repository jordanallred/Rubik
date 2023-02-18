from rubik.model.cube import Cube

def rotate(parms):
    result = {}
    
    try:
        encodedCube = parms.get('cube')
        theCube = Cube(encodedCube)
        directions = parms.get('dir')
        theCube.rotate(directions)
        result['cube'] = theCube.get()
        result['status'] = 'ok'
    
    except Exception as e:
        result['status'] = 'error: ' + str(e).lower()
    
    return result