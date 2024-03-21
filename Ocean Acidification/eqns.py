# Zackary Cleveland PHYS3000
import numpy as np
from math import sqrt


def f_CO(t) :
    exp1 = 2.0 * np.exp(-((t - 1988) / 21) ** 2)
    exp2 = 10.5 * np.exp(-((t - 2100) / 96) ** 2)
    exp3 = 2.7 * np.exp(-((t - 2265) / 57) ** 2)
    return exp1 + exp2 + exp3


# function to set initial conditions and create output space
def init_array(yf , yi , p = 1.00 , os = 2.01 , od = 2.23 , alpha_s = 2.26 , ad = 2.26) :
    output_space = np.zeros((8,yf - yi))

    output_space[0 , 0] = p
    output_space[1 , 0] = os
    output_space[2 , 0] = od
    output_space[3 , 0] = alpha_s
    output_space[4 , 0] = ad
    output_space[5 , 0] = hs_func(os,alpha_s)
    output_space[6 , 0] = cs_func(os,alpha_s)
    output_space[7 , 0] = ps_func(os,alpha_s)

    return output_space


# array to contain k1-4
def k_array(k1 = 2.19e-4 , k2 = 6.12e-5 , k3 = .997148 , k4 = 6.79e-2) :
    return np.array([k1 , k2 , k3 , k4])


# array to contain u1,2
def u_array(u1 = 4.95e2, u2=4.95e-2) :
    return np.array([u1 , u2])


# helper for ps-p/d
def p_diff_comp(p , os , alpha_s , d = 8.64) :
    return (ps_func(os , alpha_s) - p) / d


# helper for w(od-os)
def wo_diff_comp(od , os , w = 0.001) :
    return w * (od - os)


# helper for w(ad-as)
def wa_diff_comp(ad , alpha_s , w = 0.001) :
    return w * (ad - alpha_s)


# helper for 1/vs
def vs_comp(vs = 0.12) :
    return 1 / vs


# helper for 1/vd
def vd_comp(vd = 1.23) :
    return 1 / vd


# equation for od
def od_dt(od , os) :
    return vd_comp() * (k_array()[0] - wo_diff_comp(od , os))


# equation for os
def os_dt(od , os , p , alpha_s) :
    return vs_comp() * (wo_diff_comp(od , os) - k_array()[0] - (u_array()[1] * p_diff_comp(p ,os, alpha_s)))


# equation for ad
def ad_dt(ad , alpha_s) :
    return vd_comp() * (k_array()[1] - wa_diff_comp(ad , alpha_s))


# equation for as
def as_dt(ad , alpha_s) :
    return vs_comp() * (wa_diff_comp(ad , alpha_s) - k_array()[1])


# equation for hs
def hs_func(os , alpha_s) :
    diff = (2*os) - alpha_s
    k3 = k_array()[2]
    diff_coeff = diff * alpha_s * k3
    os2 = os * os

    return (os-sqrt(os2-diff_coeff))/k3


# equation for cs
def cs_func(os , alpha_s) :
    return (alpha_s - hs_func(os , alpha_s)) / 2


# equation for ps
def ps_func(os , alpha_s) :
    return k_array()[3] * (((hs_func(os , alpha_s))**2) / cs_func(os , alpha_s))


# equation for dp/dt
def dp_dt(alpha_s , os , p , t) :
    return p_diff_comp(alpha_s , os , p) + (f_CO(t) / u_array()[0])


# function to take all necessary input parameters to solve each derivative value each timestep
def runge_katta_iterator(current_row,current_time) :
    output_space = np.zeros((8))
    p = current_row[0]
    os = current_row[1]
    od = current_row[2]
    alpha_s = current_row[3]
    ad = current_row[4]

    output_space[0] = dp_dt(alpha_s,os,p,current_time)
    output_space[1] = os_dt(od,os,p,alpha_s)
    output_space[2] = od_dt(od,os)
    output_space[3] = as_dt(ad,alpha_s)
    output_space[4] = ad_dt(ad,alpha_s)
    #output_space[5] = hs_func(os,alpha_s)
    #output_space[6] = cs_func(os,alpha_s)
    #output_space[7] = ps_func(os,alpha_s)

    return output_space
