from typing import Tuple
import numpy as np
def get_index_from_direction(image: np.ndarray, x: int, y: int, direction: str) -> (int, int):
    """
    Gets the image index from the direction.
    If sweeping the image from left to right, the index are the same as x and y. If sweeping
    the image from right to left, the j index is inverted

    Parameters:
    image: input image
    x,y: original row,col coordinate
    direction: dithering direction

    Returns:
    i,j: new image pixel coordinates
    """
    n_cols = image.shape[1] - 1
    return x, (n_cols - y if direction == 'left' else y)
   

def calculate_new_image_value(image: np.ndarray, i: int, j: int) -> int:
    """
    Applies a threshold in the output image in the given image pixel coordinate
    Parameters:
    image: input image
    i,j: image pixel coordinates

    
    """
    return 0 if image[i,j] < 128 else 1
    

def calculate_error(f: np.ndarray, output_image: np.ndarray, i: int, j: int) -> int:
    """
    Calculates the error between output (g) and input (image) in the given image pixel coordinate:
    error = f[x,y] - g[x,y] * 255

    Parameters:
    f: input image
    output_image: output image g
    i,j: image pixel coordinates


    Return:
    calculated error
    """
    return int(f[i,j]) - int(output_image[i,j] * 255)


def difuse_error(f: np.ndarray, error: int, mask, direction: str, i: int, j: int) -> None:
    """
    Applies the calculated error in the f image accordingly to the given mask.

    Parameters:
    f: input image that will receive the difused error
    error: calculated error (f[x,y] - g[x,y])
    mask: chosen dithering mask
    i,j: image pixel coordinates


    Returns:
    void: doesn't return anything, just modifies the f image
    """
    direction = 1 if direction == 'right' else -1
    for displacement, weight in zip(mask.displacements, mask.weights):
        try:
            f[i + displacement[0], j +  direction * displacement[1]] += weight * error
        except IndexError:
            pass

def get_dithering_direction(row: int, pattern: str) -> str:
    """
    Gets the dithering direction from the matrix row and from chosen pattern.
    There are 2 patterns types: zigzag and uniform. The uniform always sweeps the columns
    from left to right, while the zigzag alternates between left to right and right to left.

    Parameters:
    row: current image row
    pattern (str): uniform or zigzag. 

    Returns:
    string: dithering direction 
    """
    if pattern == 'zigzag':
        return 'right' if (row % 2) == 0 else 'left'
    elif pattern == 'uniform':
        return 'right'
    else:
        message = 'Error in utils.py - invalid dithering direction pattern!\n'
        message += 'Available patterns:\nuniform (always left to right)\nzigzag (alternated pattern)'
        raise NotImplementedError(message)