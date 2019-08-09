"""
geometry_analysis.def ():
This module contains geometry analysis.
"""

import numpy
import os
import sys


def open_xyz(input_filename):
    '''
    #read the file and process and xyz file
    #function name open_xyz
    #input filename
    #two outputs: symbol and coordinates
    '''
    xyz_file = numpy.genfromtxt(fname=input_filename, skip_header=2, dtype='unicode')
    symbols = xyz_file[:,0]
    coordinates = (xyz_file[:,1:])
    coordinates = coordinates.astype(numpy.float)
    #symbol = symbol.astype(numpy.str)
    return symbols, coordinates


def bond_check(distance, minimum_length=0, maximum_length=1.5):
    '''
    bond check function - check and see the distance is between specified minimum (0) nd maximum length (1.5) and return TRUE or FALSE
    '''
    if distance < 0:
        raise ValueError(F"distance cannot be negative. {distance}")

    if distance > minimum_length and distance < maximum_length:
        return True
    else:
        return False


def calculate_distance(atom1_coord, atom2_coord):
    x_distance = atom1_coord[0] - atom2_coord[0]
    y_distance = atom1_coord[1] - atom2_coord[1]
    z_distance = atom1_coord[2] - atom2_coord[2]
    bond_length_12 = numpy.sqrt(x_distance**2+y_distance**2+z_distance**2)
    return bond_length_12



#file_location =os.path.join('data', 'water.xyz')


if __name__ == "__main__":
    print(F"Running {sys.argv[0]} ...")
    if len(sys.argv) < 2:
        raise NameError("Incorrect input! Please specify a xyz file.")

    #bond_check(-5)

    file_location = sys.argv[1]
    symbols, coord = open_xyz(file_location)
    num_atoms = len(symbols)
    for num1 in range(0, num_atoms):
        for num2 in range(0, num_atoms):
            if num1 < num2:
                bond_length_12 = calculate_distance(coord[num1], coord[num2])
                if bond_check(bond_length_12) is True:
                    print(F'{symbols[num1]} to {symbols[num2]} : {bond_length_12:.3f}')
