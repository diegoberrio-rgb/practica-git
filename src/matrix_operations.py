import numpy as np


def crear_vector():
    """Sección 1.2 de la guía: un vector = una observación con 3 características."""
    x = np.array([35, 72000, 4])  # edad, ingreso, compras
    print("Vector:", x)
    print("Shape:", x.shape)   # (3,)
    print("Ndim:", x.ndim)     # 1
    return x


def crear_matriz():
    """Sección 2: una matriz X = varias observaciones (filas) x características (columnas)."""
    X = np.array([
        [35, 72000, 4],
        [28, 52000, 2],
        [42, 91000, 7],
        [31, 63000, 3]
    ])
    print("Matriz X:\n", X)
    print("Shape:", X.shape)   # (4, 3)
    return X


def transponer(X):
    """Sección 4: la transpuesta intercambia filas y columnas."""
    X_t = X.T
    print("Transpuesta:\n", X_t)
    print("Shape original:", X.shape, "-> Shape transpuesta:", X_t.shape)
    return X_t


def reordenar(x):
    """Sección 4: reshape reorganiza un array sin cambiar sus valores."""
    A = x.reshape(2, 3)
    print("Reshape a (2,3):\n", A)
    return A