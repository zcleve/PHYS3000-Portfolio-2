# Zackary Cleveland PHYS3000
def V_potential(phi , alpha = 2.0 , beta = 0.5 , eta = 1.0) :
    return alpha * (phi ** 2 - eta ** 2) ** 2 - beta * phi

# first derivative of the V_potential with repsect to phi, done analytically
def dV_dPhi(phi , alpha = 2.0 , beta = 0.5 , eta = 1.0) :
    return 4 * alpha * (phi ** 3 - phi * eta ** 2) - beta

# second derivative of the V_potential with repsect to phi, done analytically
def d2V_dPhi(phi , alpha = 2.0 , beta = 0.5 , eta = 1.0) :
    return 12 * alpha * phi ** 2 - 4 * alpha * eta ** 2

# second derivative of phi with respect to r, change of variables from r: (1,inf) to u: (0,1)
def phi_2dot(u , phi , phidot) :
    r = 1 / (1 - u)
    # print(r)
    return dV_dPhi(phi) - ((3 / r) * phidot)
