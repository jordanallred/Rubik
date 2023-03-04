from rubik.model.cube import Cube

def rotate(parms):
    result = {}
    
    try:
        if 'dir' not in parms:
            parms['dir'] = ''
                
        if 'cube' not in parms:
            raise ValueError("Request does not contain parameter 'cube'")

        encodedCube = parms.get('cube')
        theCube = Cube(encodedCube)
        directions = parms.get('dir')
        theCube.rotate(directions)
        result['cube'] = theCube.get()
        result['status'] = 'ok'
    
    except Exception as e:
        result['status'] = 'error: ' + str(e).lower()
    
    return result