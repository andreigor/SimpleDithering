class InputParameterError(Exception):
    "Raised when input parameter is not as expected"
    pass

class FloydSteinbergMask():
    def __init__(self, direction = 'right'):
        self.displacements = self.get_displacements(direction)
        self.weights = self.get_weights()
    
    def get_displacements(self, direction):
        
        direction = 1 if direction == 'right' else -1
        displacements = [[0, direction *  1],
                         [1, direction * -1],
                         [1, direction *  0],
                         [1, direction *  1]]
        return displacements
    def get_weights(self):
        weights = [7/16, 3/16, 5/16, 1/16]
        return weights

class StevensonMask():
    def __init__(self, direction = 'right'):
        self.displacements = self.get_displacements(direction)
        self.weights = self.get_weights()
    
    def get_displacements(self, direction):
        direction = 1 if direction == 'right' else -1
        displacements = [[0, direction *  2],  [1, direction * -3], [1, direction *  -1], [1, direction *  1],
                         [1, direction *  3],  [2, direction * -2], [2, direction *   0], [2, direction *  2],
                         [3, direction *  -3], [3, direction * -1], [3, direction *   1], [3, direction *  3]
                         ]
        return displacements
    def get_weights(self):
        weights = [32/200, 12/200, 26/200, 30/200, 16/200, 12/200,
                   26/200, 12/200, 5/200, 12/200, 12/200, 5/200]
        return weights

class BurkesMask():
    def __init__(self, direction = 'right'):
        self.displacements = self.get_displacements(direction)
        self.weights = self.get_weights()
    
    def get_displacements(self, direction):
        direction = 1 if direction == 'right' else -1
        displacements = [[0, direction *   1],
                         [0, direction *   2],
                         [1, direction *  -2],
                         [1, direction *  -1],
                         [1, direction *   0],
                         [1, direction *   1],
                         [1, direction *   2]
                         ]
        return displacements
    def get_weights(self):
        weights = [8/32, 4/32, 2/32, 4/32, 8/32, 4/32, 2/32]
        return weights

class SierraMask():
    def __init__(self, direction = 'right'):
        self.displacements = self.get_displacements(direction)
        self.weights = self.get_weights()
    
    def get_displacements(self, direction):
        direction = 1 if direction == 'right' else -1
        displacements = [[0, direction *   1],
                         [0, direction *   2],
                         [1, direction *  -2],
                         [1, direction *  -1],
                         [1, direction *   0],
                         [1, direction *   1],
                         [1, direction *   2],
                         [2, direction *  -1],
                         [2, direction *   0],
                         [2, direction *   1]
                         ]
        return displacements
    def get_weights(self):
        weights = [5/32, 3/32, 2/32, 4/32, 5/32, 4/32, 2/32, 2/32, 3/32, 2/32]
        return weights
    
class StuckiMask():
    def __init__(self, direction = 'right'):
        self.displacements = self.get_displacements(direction)
        self.weights = self.get_weights()
    
    def get_displacements(self, direction):
        direction = 1 if direction == 'right' else -1
        displacements = [[0, direction *   1],
                         [0, direction *   2],
                         [1, direction *  -2],
                         [1, direction *  -1],
                         [1, direction *   0],
                         [1, direction *   1],
                         [1, direction *   2],
                         [2, direction *  -2],
                         [2, direction *  -1],
                         [2, direction *   0],
                         [2, direction *   1],
                         [2, direction *   2]
                         ]
        return displacements
    def get_weights(self):
        weights = [8/42, 4/42, 2/42, 4/42, 8/42, 4/42, 2/42, 1/42, 2/42, 4/42, 2/42, 1/42]
        return weights

class JarvisJudiceNinkeMask():
    def __init__(self, direction = 'right'):
        self.displacements = self.get_displacements(direction)
        self.weights = self.get_weights()
    
    def get_displacements(self, direction):
        direction = 1 if direction == 'right' else -1
        displacements = [[0, direction *   1],
                         [0, direction *   2],
                         [1, direction *  -2],
                         [1, direction *  -1],
                         [1, direction *   0],
                         [1, direction *   1],
                         [1, direction *   2],
                         [2, direction *  -2],
                         [2, direction *  -1],
                         [2, direction *   0],
                         [2, direction *   1],
                         [2, direction *   2]
                         ]
        return displacements
    def get_weights(self):
        weights = [7/48, 5/48, 3/48, 5/48, 7/48, 5/48, 3/48, 1/48, 3/48, 5/48, 3/48, 1/48]
        return weights

def get_chosen_mask(mask_choice, direction):
    if mask_choice == 'floyd_steinberg':
        return FloydSteinbergMask(direction)
    elif mask_choice == 'stevenson':
        return StevensonMask(direction)
    elif mask_choice == 'burkes':
        return BurkesMask(direction)
    elif mask_choice == 'sierra':
        return SierraMask(direction)
    elif mask_choice == 'stucki':
        return StuckiMask(direction)
    elif mask_choice == 'jarvis_jucide_ninke':
        return JarvisJudiceNinkeMask(direction)
    else:
        message = 'Error in masks.py - invalid input mask!\n'
        message += 'Available masks:\n floid_steinberg\n stevenson\n burkes\n sierra\n stucki\n jarvis_judice_ninke'
        raise NotImplementedError(message)