import numpy as np
import numpy.linalg as npl


def normalize_vector(vector) :
    """
        Normalize a single vector.

        Parameters:
        - vector: NumPy array representing the vector to be normalized.

        Returns:
        - normalized_vector: Normalized version of the input vector.
    """

    normalized_vector = vector  # Placeholder for output w/shape of input vector
    magnitude = npl.norm(vector)  # Stores the magnitude of the input vector

    return normalized_vector * (1 / magnitude)


# Normalizes an array of vectors
def normalize_vectors(vectors) :
    """
        Normalize an array of vectors.

        Parameters:
        - vectors: NumPy array containing multiple vectors as rows.

        Returns:
        - normalized_vectors: NumPy array with each vector normalized.
    """

    normalized_vectors = vectors  # Placeholder for output
    num_rows , num_columns = vectors.shape  # Unpack and store input array size

    for i in range(num_rows) :
        vectors[i , :] = normalize_vector(vectors[i , :])  # Calls the vector normalization function row by row

    return normalized_vectors


def magnitude_over_t(V , n_dimn = 2) :
    """
        Compute the magnitudes of vectors over time.

        Parameters:
        - V: NumPy array containing vectors as columns.
        - n_dimn: Dimensionality of each vector (default is 2).

        Returns:
        - out: NumPy array containing magnitudes of vectors over time.
    """
    len = int(V.size / n_dimn)  # Stores the length of the row space
    out = np.zeros(len)  # Creates a placeholder for the output with the correct size
    for j in range(len) :
        out[j] = npl.norm(
            V[: , j])  # Stores the magnitude in the output array corresponding to each t in len of the array
    return out
