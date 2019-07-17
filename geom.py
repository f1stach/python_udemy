import math

# tworzymy moduł do obliczen na ciągach geometrycznych -przyjmuje 3 parametry a1 - o domyślnej wartości  2,
# która oznacza pierwszy element ciągu, factor - o domyślnej wartości 2, która oznacza współczynnik ciągu
# geometrycznego, index o domyślnej wartości 2, która oznacza  który element ciągu ma być wyliczony


def give_geom_seq_element(a1=2, factor=2, index=2):
    a_n = a1*pow(factor, index-1)

    return a_n


def give_factor_for_geom_seq(term, nextterm):
    # return the value of a factor

    return nextterm/term


def give_sum_of_n_elements_geom_seq(a1=2, factor=2, n=2):
    if factor == 1:
        s_n = a1*n
    else:
        s_n = a1*(1-pow(factor, n))/(1-factor)

    return s_n
