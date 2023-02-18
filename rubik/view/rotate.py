from rubik.model.cube import Cube

def rotate(parms):
    result = {}
    
    if len(parms) != 2:
        raise ValueError("Request has too many parameters - should only have 'dir' and 'cube'")

    if 'dir' not in parms:
        raise ValueError("Request does not contain parameter 'dir'")
    
    if 'cube' not in parms:
        raise ValueError("Request does not contain parameter 'cube'")

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