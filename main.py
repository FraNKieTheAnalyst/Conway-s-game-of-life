import numpy
frame = numpy.array([[0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 1, 1, 1, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0]])

# Ajouter une ligne en haut et en bas (avec des zéros)
padded_frame = numpy.pad(frame, ((1, 1), (0, 0)), mode='constant', constant_values=0)
                   
# Ajouter une colonne à gauche et à droite (avec des zéros)
padded_frame = numpy.pad(padded_frame, ((0, 0), (1, 1)), mode='constant', constant_values=0)

#(padded_frame = np.pad(frame, 1, mode="constant", constant_values=0)) est une autre manière de faire
print(padded_frame) 