# Vertices
VERTICES = [
    # A (adj. B, S)
    [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
    # B (adj. A, C, T)
    [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
    # C (adj. B, D, U)
    [0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    # D (adj. C, E)
    [0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    # E (adj. D, F)
    [0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    # F (adj. E, G)
    [0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    # G (adj. F, H, R)
    [0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0],
    # H (adj. G, I)
    [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    # I (adj. H, J)
    [0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
    # J (adj. I, K, R)
    [0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0],
    # K (adj. J, L)
    [0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0],
    # L (adj. K, M)
    [0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0],
    # M (adj. L, N, R)
    [0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0],
    # N (adj. M, O)
    [0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],
    # O (adj. N, P, S)
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0],
    # P (adj. O, Q)
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0],
    # Q (adj. P, R)
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0],
    # R (adj. G, J, M, Q)
    [0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,0,0],
    # S (adj. A, O, T)
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0],
    # T (adj. B, S, U)
    [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
    # U (adj. C, T)
    [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
]

EDGES = [
    # A (adj. B, S)
    [0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
    # B (adj. A, C, T)
    [3,0,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15,0],
    # C (adj. B, D, U)
    [0,2.5,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,16],
    # D (adj. C, E)
    [0,0,1,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    # E (adj. D, F)
    [0,0,0,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    # F (adj. E, G)
    [0,0,0,0,2,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    # G (adj. F, H, R)
    [0,0,0,0,0,3,0,1,0,0,0,0,0,0,0,0,0,7,0,0,0],
    # H (adj. G, I)
    [0,0,0,0,0,0,1,0,0.5,0,0,0,0,0,0,0,0,0,0,0,0],
    # I (adj. H, J)
    [0,0,0,0,0,0,0,0.5,0,0.5,0,0,0,0,0,0,0,0,0,0,0],
    # J (adj. I, K, R)
    [0,0,0,0,0,0,0,0,0.5,0,0.5,0,0,0,0,0,0,1,0,0,0],
    # K (adj. J, L)
    [0,0,0,0,0,0,0,0,0,0.5,0,5,0,0,0,0,0,0,0,0,0],
    # L (adj. K, M)
    [0,0,0,0,0,0,0,0,0,0,5,0,4,0,0,0,0,0,0,0,0],
    # M (adj. L, N, R)
    [0,0,0,0,0,0,0,0,0,0,0,4,0,1,0,0,0,10,0,0,0],
    # N (adj. M, O)
    [0,0,0,0,0,0,0,0,0,0,0,0,1,0,15,0,0,0,0,0,0],
    # O (adj. N, P, S)
    [0,0,0,0,0,0,0,0,0,0,0,0,0,15,0,5,0,0,5,0,0],
    # P (adj. O, Q)
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,2,0,0,0,0],
    # Q (adj. P, R)
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,2,0,0,0],
    # R (adj. G, J, M, Q)
    [0,0,0,0,0,0,7,0,0,1,0,0,10,0,0,0,2,0,0,0,0],
    # S (adj. A, O, T)
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,10,0],
    # T (adj. B, S, U)
    [0,15,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,0,2],
    # U (adj. C, T)
    [0,0,16,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0]
]