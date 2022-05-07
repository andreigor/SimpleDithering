class InputParameterError(Exception):
    "Raised when input parameter is not as expected"
    pass

class DitheringMask():
    def __init__(self, mask_strategy): 
        self.mask_strategy = mask_strategy
        self.weights, self.displacements = self.mask_strategy()


###################### FLOYD STEINBERG ###################

def _get_floyd_steinberg_weights():
    return [7/16, 3/16, 5/16, 1/16]

def _get_floyd_steinberg_displacements():
    return [[0,  1],[1, -1],[1,  0],[1,  1]]

def floyd_steinberg_strategy():
    weights = _get_floyd_steinberg_weights()
    displacements = _get_floyd_steinberg_displacements()
    return weights, displacements

##################### STEVENSON #########################

def _get_stevenson_weights():
    return [32/200, 12/200, 26/200, 30/200, 16/200, 12/200,
            26/200, 12/200, 5/200, 12/200, 12/200, 5/200]

def _get_stevenson_displacements():
    return [[0,  2],  [1, -3], [1,  -1], [1,  1],
            [1,  3],  [2, -2], [2,   0], [2,  2],
            [3,  -3], [3, -1], [3,   1], [3,  3]
            ]
            
def stevenson_strategy():
    weights = _get_stevenson_weights()
    displacements = _get_stevenson_displacements()
    return weights, displacements

##################### BURKES #########################

def _get_burkes_weights():
    return [8/32, 4/32, 2/32, 4/32, 8/32, 4/32, 2/32]

def _get_burkes_displacements():
    return [[0,  1], [0,  2], [1, -2], [1, -1],
            [1,  0], [1,  1], [1,  2]]

def burkes_strategy():      
    weights = _get_burkes_weights()
    displacements = _get_burkes_displacements()
    return weights, displacements

##################### SIERRA #########################

def _get_sierra_weights():
    return [5/32, 3/32, 2/32, 4/32, 5/32, 4/32, 2/32, 2/32, 3/32, 2/32]

def _get_sierra_displacements():
    return [[0,  1], [0,  2], [1, -2], [1, -1],
            [1,  0], [1,  1], [1,  2], [2, -1],
            [2,  0], [2,  1]]

def sierra_strategy():
    weights = _get_sierra_weights()
    displacements = _get_sierra_displacements()
    return weights, displacements

##################### STUCKI #########################

def _get_stucki_weights():
    return [8/42, 4/42, 2/42, 4/42, 8/42, 4/42, 2/42, 1/42, 2/42, 4/42, 2/42, 1/42]

def _get_stucki_displacements():
    return [[0,  1], [0,  2], [1, -2], [1, -1],
            [1,  0], [1,  1], [1,  2], [2, -2], 
            [2, -1], [2,  0], [2,  1], [2,  2]]

def stucki_strategy():
    weights = _get_stucki_weights()
    displacements = _get_stucki_displacements()
    return weights, displacements

##################### JARVIS JUDICE NINKE #########################

def _get_jarvis_judice_ninke_weights():
    return [7/48, 5/48, 3/48, 5/48, 7/48, 5/48, 3/48, 1/48, 3/48, 5/48, 3/48, 1/48]

def _get_jarvis_judice_ninke_displacements():
    return [[0,  1], [0,  2], [1, -2], [1, -1],
            [1,  0], [1,  1], [1,  2], [2, -2],
            [2, -1], [2,  0], [2,  1], [2,  2]]

def jarvis_judice_ninke_strategy():
    weights = _get_jarvis_judice_ninke_weights()
    displacements = _get_jarvis_judice_ninke_displacements()
    return weights, displacements
    
def get_chosen_mask(chosen_mask):
    masks = {key[:-9]: value for key,value in globals().items() if key.endswith('_strategy')}
    
    if chosen_mask in masks.keys():
        return DitheringMask(masks[chosen_mask])
    
    else:
        message = 'Error in masks.py - invalid input mask!\n'
        message += 'Available masks:\n floid_steinberg\n stevenson\n burkes\n sierra\n stucki\n jarvis_judice_ninke'
        raise NotImplementedError(message)






