# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 21:58:25 2026

@author: santo
"""
"In matrix element form"
# import numpy as np

# omega= np.exp(2j*np.pi/3)

# def E(s1, s2, s3, phi):
#     a= (np.exp(1j*phi))* (omega**(s2-s1)) 
#     b= np.conj(a)
#     c= (np.exp(1j*phi))* (omega**(s3-s2)) 
#     d= np.conj(c)
#     return (a+b+c+d)

# def g1(s1, s2, s3, phi):
#     return (1/(E(s1, s2, s3, phi) - E(s1+1, s2, s3, phi)))

# def g2(s1, s2, s3, phi):
#     return (1/(E(s1, s2, s3, phi) - E(s1+1, s2+1, s3, phi)))

# def g3(s1, s2, s3, phi):
#     return (1/(E(s1, s2, s3, phi) - E(s1+1, s2-1, s3, phi)))

# def g4(s1, s2, s3, phi):
#     return (1/(E(s1, s2, s3, phi) - E(s1, s2+1, s3, phi)))


# def f11(s1, s2, s3, phi):
#     nr = -omega**(s1+1) + omega**(s1) 
#     return (nr*g1(s1, s2, s3, phi))


# def f12(s1, s2, s3, phi):
#     nr = f11(s1-1, s2, s3, phi) - f11(s1+1, s2, s3, phi)
#     return (nr*g1(s1, s2, s3, phi))

# def f22(s1, s2, s3, phi):
#     nr = f11(s1, s2, s3, phi) - f11(s1, s2+1, s3, phi)
#     return (nr*g2(s1, s2, s3, phi))

# def f32(s1, s2, s3, phi):
#     nr = f11(s1, s2, s3, phi) - f11(s1, s2-1, s3, phi)
#     return (nr*g3(s1, s2, s3, phi))


# def f13(s1, s2, s3, phi):
#     nr = f12(s1-1, s2, s3, phi) + f22(s1, s2, s3, phi) +  f32(s1, s2, s3, phi)- f12(s1+1, s2, s3, phi) - f22(s1, s2-1, s3, phi) - f32(s1, s2+1, s3, phi)
#     return (nr*g1(s1, s2, s3, phi))

# def f23(s1, s2, s3, phi):
#     nr = f12(s1, s2, s3, phi) + f32(s1-1, s2+1, s3, phi) + f32(s1, s2, s3, phi)- f12(s1, s2+1, s3, phi) - f32(s1+1, s2+1, s3, phi) - f32(s1, s2-1, s3, phi)
#     return (nr*g2(s1, s2, s3, phi))

# def f33(s1, s2, s3, phi):
#     nr = f12(s1, s2, s3, phi) + f22(s1, s2, s3, phi) + f22(s1-1, s2-1, s3, phi)- f12(s1, s2-1, s3, phi) - f22(s1, s2+1, s3, phi) - f12(s1+1, s2-1, s3, phi)
#     return (nr*g3(s1, s2, s3, phi))

# def f43(s1, s2, s3, phi):
#     nr = f22(s1, s2, s3, phi) + f32(s1-1, s2+1, s3, phi) - f22(s1-1, s2, s3, phi) - f32(s1, s2+1, s3, phi)
#     return (nr*g4(s1, s2, s3, phi))

# def che(s1, s2, s3, phi):
#     nr = f22(s1, s2, s3, phi) + f32(s1-1, s2+1, s3, phi) - f22(s1-1, s2, s3, phi) - f32(s1, s2+1, s3, phi)
#     return (nr)


# # def tf(h, s1, s2, phi):
# #     x= f(s1, s2, phi)
# #     y= h*g(s1, s2, phi)*(-1)*f(s1+1, s2, phi)
# #     z= h*g(s1, s2, phi)*(+1)*f(s1-1, s2, phi)
# #     return ((x+y+z)*h)

# # ============================================================
# # Parameters
# # ============================================================

# q=3
# omega = np.exp(2j * np.pi / 3)

# phi = np.pi *(0.2)
# h = 1


# # ============================================================
# # Basis
# # ============================================================

# basis = [(s1, s2, s3) for s1 in range(3) for s2 in range(3) for s3 in range(3)]
# dim = len(basis)

# index = {state: i for i, state in enumerate(basis)}


# # ============================================================
# # Single-site operators
# # ============================================================

# U = np.diag([omega**s for s in range(3)]).astype(complex)

# V = np.zeros((3, 3), dtype=complex)

# for s in range(3):
#     V[(s - 1) % 3, s] = 1

# Vdag = V.conj().T
# Udag = U.conj().T

# I = np.eye(3, dtype=complex)


# # ============================================================
# # Two-site operators
# # ============================================================

# U1 = np.kron(np.kron(U, I), I)
# U1dag = U1.conj().T
# U2 = np.kron(np.kron(I, U), I)
# U2dag = U2.conj().T
# U3 = np.kron(np.kron(I, I), U)
# U3dag = U3.conj().T

# V1 = np.kron(np.kron(V, I), I)
# V1dag = V1.conj().T
# V2 = np.kron(np.kron(I, V), I)
# V2dag = V2.conj().T
# V3 = np.kron(np.kron(I, I), V)
# V3dag = V3.conj().T


# # ============================================================
# # Hamiltonian
# # ============================================================

# H0 = (
#     np.exp(1j * phi) * ((U1dag @ U2) + (U2dag @ U3)) 
#     + np.exp(-1j * phi) *((U2dag @ U1) + (U3dag @ U2)) 
# )

# H1 = V1 + V1dag + V2 + V2dag

# H = H0 + h * H1


# # ============================================================
# # YOUR O_1 AND O_2
# #
# # Define their diagonal matrix elements as functions
# # of (s1,s2).
# #
# # Replace these two functions with your expressions.
# # ============================================================

# # def o1(h, s1, s2, phi):
# #     # YOUR EXPRESSION FOR O1(s1,s2)
# #     return (tf(h, s1, s2, phi))


# # def o2(h, s1, s2, phi):
# #     # YOUR EXPRESSION FOR O2(s1,s2)
# #     return (tf(h, s1-1, s2, phi))


# # ============================================================
# # Construct diagonal O1 and O2
# # ============================================================

# O11 = np.zeros((dim, dim), dtype=complex)
# O11d = np.zeros((dim, dim), dtype=complex)

# for i, (s1, s2, s3) in enumerate(basis):
#     O11[i, i] = f11(s1, s2, s3, phi)
#     O11d[i, i] = f11(s1-1, s2, s3, phi)
    
    
# O12 = np.zeros((dim, dim), dtype=complex)
# O12d = np.zeros((dim, dim), dtype=complex)
# O22 = np.zeros((dim, dim), dtype=complex)
# O22d = np.zeros((dim, dim), dtype=complex)
# O32 = np.zeros((dim, dim), dtype=complex)
# O32d = np.zeros((dim, dim), dtype=complex)

# for i, (s1, s2, s3) in enumerate(basis):
#     O12[i, i] = f12(s1, s2, s3, phi)
#     O12d[i, i] = f12(s1-1, s2, s3, phi)
#     O22[i, i] = f22(s1, s2, s3, phi)
#     O22d[i, i] = f22(s1-1, s2-1, s3, phi)
#     O32[i, i] = f32(s1, s2, s3, phi)
#     O32d[i, i] = f32(s1-1, s2+1, s3, phi)
    
    
# O13 = np.zeros((dim, dim), dtype=complex)
# O13d = np.zeros((dim, dim), dtype=complex)
# O23 = np.zeros((dim, dim), dtype=complex)
# O23d = np.zeros((dim, dim), dtype=complex)
# O33 = np.zeros((dim, dim), dtype=complex)
# O33d = np.zeros((dim, dim), dtype=complex)
# O43 = np.zeros((dim, dim), dtype=complex)
# O43d = np.zeros((dim, dim), dtype=complex)

# for i, (s1, s2, s3) in enumerate(basis):
#     O13[i, i] = f13(s1, s2, s3, phi)
#     O13d[i, i] = f13(s1-1, s2, s3, phi)
#     O23[i, i] = f23(s1, s2, s3, phi)
#     O23d[i, i] = f23(s1-1, s2-1, s3, phi)
#     O33[i, i] = f33(s1, s2, s3, phi)
#     O33d[i, i] = f33(s1-1, s2+1, s3, phi)
#     O43[i, i] = f43(s1, s2, s3, phi)
#     O43d[i, i] = f43(s1, s2-1, s3, phi)
# # ============================================================
# # Calculate alpha^(i)_{x,y}
# #
# # alpha^(i)_{x,y} =
# # (1/9) sum_{s1,s2} omega^(-x*s1-y*s2)
# # <s1,s2| O_i |s1,s2>
# #
# # x,y = 0,1,2
# # ============================================================

# # def alpha(O, x, y):
# #     total = 0.0 + 0.0j

# #     for s1 in range(3):
# #         for s2 in range(3):

# #             # Matrix index corresponding to |s1,s2>
# #             idx = index[(s1, s2)]

# #             # Diagonal matrix element
# #             O_diag = O[idx, idx]

# #             total += (
# #                 omega**(-x*s1 - y*s2)
# #                 * O_diag
# #             )

# #     return total / 9


# # ============================================================
# # Calculate all alpha^(1)_{x,y} and alpha^(2)_{x,y}
# # ============================================================

# # alpha1 = np.zeros((3, 3), dtype=complex)
# # alpha2 = np.zeros((3, 3), dtype=complex)

# # for x in range(3):
# #     for y in range(3):
# #         alpha1[x, y] = alpha(O1, x, y)
# #         alpha2[x, y] = alpha(O2, x, y)


# # ============================================================
# # Print results
# # ============================================================

# # np.set_printoptions(precision=10, suppress=True)

# # print("\nalpha^(1)_{x,y} =")
# # print(alpha1)

# # print("\nalpha^(2)_{x,y} =")
# # print(alpha2)

# Gamma0 = U1
# Gamma1 = O11 @ V1 + O11d @ V1dag
# Gamma2 = (O12 @ V1) + (O12d @ V1dag) + (O22 @ V1 @ V2) + (O22d @ V1dag @ V2dag) + (O32 @ V1 @ V2dag) + (O32d @ V1dag @ V2)
# Gamma3 = (O13 @ V1) + (O13d @ V1dag) + (O23 @ V1 @ V2) + (O23d @ V1dag @ V2dag) + (O33 @ V1 @ V2dag) + (O33d @ V1dag @ V2) + (O43 @ V2) + (O43d @ V2dag)

# # ============================================================
# # Commutator
# # ============================================================

# commutator1 = H0 @ Gamma1 - Gamma1 @ H0 + H1 @ Gamma0 - Gamma0 @ H1 
# commutator2 = H0 @ Gamma2 - Gamma2 @ H0 + H1 @ Gamma1 - Gamma1 @ H1 


# # ============================================================
# # Print everything
# # ============================================================

# np.set_printoptions(precision=8, suppress=True)

# print("Basis:")
# print(basis)


# print("\nMaximum absolute matrix element:")
# print(np.max(np.abs(commutator1)))
# print(np.max(np.abs(commutator2)))

# print("\nIs this order satisfied?")
# print(np.allclose(commutator1, 0, atol=1e-10))
# print(np.allclose(commutator2, 0, atol=1e-10))

# print("\nMaximum absolute matrix element of Gammas:")
# print(np.max(np.abs(Gamma1)))
# print(np.max(np.abs(Gamma2)))

"The operator form"

import numpy as np

# ============================================================
# Parameters: four-site Z_3 chiral clock model
# ============================================================
L = 4
q = 3
dim = q**L

phi = 0.4 * np.pi       # Change as needed
z = np.exp(1j * phi)
zb = np.conj(z)

om = np.exp(2j * np.pi / q)
omb = np.conj(om)

eye = np.eye(dim, dtype=complex)
tol = 1e-8

# ============================================================
# Single-site clock operators
# U|s> = omega^s |s>
# V|s> = |s-1>, so VU = omega UV
# ============================================================
U = np.diag([om**s for s in range(q)])
V = np.roll(np.eye(q, dtype=complex), -1, axis=0)
I3 = np.eye(q, dtype=complex)

def site_operator(op, j):
    """Put a single-site operator on site j (zero-based)."""
    ops = [I3.copy() for _ in range(L)]
    ops[j] = op
    result = ops[0]
    for opj in ops[1:]:
        result = np.kron(result, opj)
    return result

Us = [site_operator(U, j) for j in range(L)]
Vs = [site_operator(V, j) for j in range(L)]

Uds = [x.conj().T for x in Us]
Vds = [x.conj().T for x in Vs]

# ============================================================
# Hamiltonian H = H0 + H1
# H0 = sum_j [z U_j^dag U_{j+1} + h.c.]
# H1 = sum_j [V_j + V_j^dag]
# Open boundary conditions
# ============================================================
H0 = np.zeros((dim, dim), dtype=complex)
H1 = np.zeros((dim, dim), dtype=complex)

for j in range(L - 1):
    H0 += (
        z * Uds[j] @ Us[j+1]
        + zb * Us[j] @ Uds[j+1]
    )

for j in range(L):
    H1 += Vs[j] + Vds[j]

# ============================================================
# Gamma_0 = U_1
# Gamma_1 from your equation
# ============================================================
Gamma0 = Us[0]

C1 = (
    zb**2 * Us[1]
    + omb * Us[0]
    + om * z**2 * Uds[0] @ Uds[1]
)

C2 = (
    zb**2 * Us[1]
    + om * Us[0]
    + omb * z**2 * Uds[0] @ Uds[1]
)

denom = zb**3 - z**3

Gamma1 = (C1 @ Vs[0] + C2 @ Vds[0]) / denom

# ============================================================
# Auxiliary operator A and its adjoint
# A = U_1^dag U_2 + U_2^dag U_3
# ============================================================
A = Uds[0] @ Us[1] + Uds[1] @ Us[2]
Ad = A.conj().T
AA = A @ Ad

# ============================================================
# Gamma_2 coefficients O_1,...,O_6
# Prefactor for O_1,...,O_4: 1/denom^2
# Prefactor for O_5,O_6: 1/(8 denom^2)
# ============================================================
d2 = denom**2

O1 = (
    (zb**2 * Uds[0] @ Us[1]
     + om * z**2 * Us[0] @ Uds[1]
     + omb * eye)
    @ (-Us[0] + omb * z**2 * Uds[0] @ Uds[1])
) / d2

O2 = (
    (z**2 * Us[0] @ Uds[1]
     + om * zb**2 * Uds[0] @ Us[1]
     + omb * eye)
    @ (-omb * Us[0] + z**2 * Uds[0] @ Uds[1])
) / d2

O3 = (
    (zb**2 * Uds[1] @ Us[2]
     + om * z**2 * Us[1] @ Uds[2]
     + omb * eye)
    @ (zb**2 * Us[1] - z**2 * Uds[0] @ Uds[1])
) / d2

O4 = (
    (zb**2 * Uds[1] @ Us[2]
     + omb * z**2 * Us[1] @ Uds[2]
     + om * eye)
    @ (zb**2 * Us[1] - z**2 * Uds[0] @ Uds[1])
) / d2

P5 = (
    om * zb**2 * (Ad@Ad)
    + z**2 * (A@A)
    + omb * AA
)

Q5 = (
    omb * zb**2 * Us[1]
    - om * z**2 * Uds[0] @ Uds[1]
)

O5 = P5 @ Q5 @ (3*AA - 11*eye) / (8*d2)

P6 = (
    zb**2 * (Ad @ Ad)
    + om * z**2 * (A @ A)
    + omb * (A @ Ad)
)

Q6 = (
    zb**2 * Us[1]
    - om * z**2 * Uds[0] @ Uds[1]
)

O6 = P6 @ Q6 @ (3 * A @ Ad - 11 * eye) / (8 * d2)

# ============================================================
# Gamma_2
# Gamma_2 = O1 V1 + O2 V1^dag
#          + O3 V1 V2 + O4 V1^dag V2^dag
#          + O5 V1 V2^dag + O6 V1^dag V2
# ============================================================
Gamma2 = (
    O1 @ Vs[0]
    + O2 @ Vds[0]
    + O3 @ Vs[0] @ Vs[1]
    + O4 @ Vds[0] @ Vds[1]
    + O5 @ Vs[0] @ Vds[1]
    + O6 @ Vds[0] @ Vs[1]
)

# ============================================================
# Verify clock algebra and perturbative equations
# ============================================================
d=1/denom
def comm(X, Y):
    return X @ Y - Y @ X

R1 = comm(H0, Gamma1) + comm(H1, Gamma0)

R21 = comm(H0, O1@Vs[0]) + d*comm(Vds[0], C2@Vds[0])
R22 = comm(H0, O2@Vds[0]) + d*comm(Vs[0], C1@Vs[0])
R23 = comm(H0, O3@Vs[0]@Vs[1]) + d*comm(Vs[1], C1@Vs[0])
R24 = comm(H0, O4@Vds[0]@Vds[1]) + d*comm(Vds[1], C2@Vds[0])
R25 = comm(H0, O5@Vs[0]@Vds[1]) + d*comm(Vds[1], C1@Vs[0])
R26 = comm(H0, O6@Vds[0]@Vs[1]) + d*comm(Vs[1], C2@Vds[0])

Gamma2 = O1@Vs[0] + O2@Vds[0] + O3@Vs[0]@Vs[1] + O4@Vds[0]@Vds[1] + O5@Vs[0]@Vds[1] + O6@Vds[0]@Vs[1]

R2 = comm(H0, Gamma2) + comm(H1, Gamma1)


solvability = comm(Vs[0], C2@Vds[0])+comm(Vds[0], C1@Vs[0])

RVd= comm(Vs[0], O4@Vds[0]@Vds[1]) + comm(Vds[0], O5@Vs[0]@Vds[1])
RV = comm(Vs[0], O3@Vs[0]@Vs[1]) + comm(Vds[0], O6@Vds[0]@Vs[1])

print("\nPerturbative zero-mode checks:")
print("[H0,Gamma1] + [H1,U1] = 0:",
      np.allclose(R1, 0, atol=tol, rtol=0))
print("Maximum residual 1:", np.max(np.abs(R1)))

print("[H0,Gamma2] + [H1,Gamma1] = 0:",
      np.allclose(R2, 0, atol=tol, rtol=0))
print("Maximum residual 1:", np.max(np.abs(R2)))

print("coefficient of V2dagger :",
      np.allclose(RVd, 0, atol=tol, rtol=0))
print("Maximum residual V2dagger:", np.max(np.abs(RVd)))

print("coefficient of V2 :",
      np.allclose(RV, 0, atol=tol, rtol=0))
print("Maximum residual V2:", np.max(np.abs(RV)))


# print("V1 = 0:",
#       np.allclose(R21, 0, atol=tol, rtol=0))
# print("Maximum residual V1:", np.max(np.abs(R21)))

# print("V1d = 0:",
#       np.allclose(R22, 0, atol=tol, rtol=0))
# print("Maximum residual V1d:", np.max(np.abs(R22)))

# print("V1V2 = 0:",
#       np.allclose(R23, 0, atol=tol, rtol=0))
# print("Maximum residual V1V2:", np.max(np.abs(R23)))

# print("V1dV2d = 0:",
#       np.allclose(R24, 0, atol=tol, rtol=0))
# print("Maximum residual V1dV2d:", np.max(np.abs(R24)))


# print("V1V2d = 0:",
#       np.allclose(R25, 0, atol=tol, rtol=0))
# print("Maximum residual V1V2d:", np.max(np.abs(R25)))

# print("V1dV2 = 0:",
#       np.allclose(R26, 0, atol=tol, rtol=0))
# print("Maximum residual V1dV2:", np.max(np.abs(R26)))
# print("\n[H0,Gamma2] + [H1,Gamma1] = 0:",
#       np.allclose(R2, 0, atol=tol, rtol=0))
# print("Maximum residual 2:", np.max(np.abs(R2)))

# print("solvability = 0:",
#       np.allclose(solvability, 0, atol=tol, rtol=0))
# print("Maximum residual sol:", np.max(np.abs(solvability)))




