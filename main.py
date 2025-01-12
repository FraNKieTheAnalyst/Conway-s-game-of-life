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

# calcul du nombre de cellules voisines
def compute_number_neighbors(paded_frame, index_line, index_column):
    
    neighbors = [
            (-1, -1), (-1, 0), (-1, 1),  
            (0, -1),         (0, 1),     
            (1, -1), (1, 0), (1, 1)]
        
    count_neighbors = 0

    for coordinate in neighbors:
        new_index_line, new_index_column = index_line + coordinate[0], index_column + coordinate[1]
        if padded_frame[new_index_line, new_index_column] == 1:  # Si la cellule voisine est vivante (1)
            count_neighbors += 1
        
    return count_neighbors 

for index_line in range(1, padded_frame.shape[0] - 1):
    for index_column in range(1, padded_frame.shape[1] - 1):
        count_neighbors = compute_number_neighbors(padded_frame, index_line, index_column)
        print(f"Cellule ({index_line-1}, {index_column-1}) a {count_neighbors} voisins vivants.")
        