#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Shapelets.io
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

########################################################################################################################
# IMPORT
########################################################################################################################
import ctypes
from khiva.library import KhivaLibrary
from khiva.array import Array


########################################################################################################################

def k_means(tss, k, tolerance=1e-10, max_iterations=100):
    """ Calculates the K-Means algorithm.

    :param tss: Expects an input array whose dimension zero is the length of the time series (all the same) and
    dimension one indicates the number of time series.
    :param k:                   The number of means to be computed.
    :param tolerance:           The error tolerance to stop the computation of the centroids.
    :param max_iterations:      The maximum number of iterations allowed.
    """
    centroids = ctypes.c_void_p(0)
    labels = ctypes.c_void_p(0)

    KhivaLibrary().c_khiva_library.k_means(ctypes.pointer(tss.arr_reference),
                                           ctypes.pointer(ctypes.c_int(k)),
                                           ctypes.pointer(centroids),
                                           ctypes.pointer(labels),
                                           ctypes.pointer(ctypes.c_float(tolerance)),
                                           ctypes.pointer(ctypes.c_int(max_iterations))
                                           )
    return Array(array_reference=centroids), Array(array_reference=labels)


def k_shape(tss, k, tolerance=1e-10, max_iterations=100):
    """ Calculates the K-Shape algorithm.

    :param tss: Expects an input array whose dimension zero is the length of the time series (all the same) and
    dimension one indicates the number of time series.
    :param k:                   The number of means to be computed.
    :param tolerance:           The error tolerance to stop the computation of the centroids.
    :param max_iterations:      The maximum number of iterations allowed.
    """
    centroids = ctypes.c_void_p(0)
    labels = ctypes.c_void_p(0)

    KhivaLibrary().c_khiva_library.k_shape(ctypes.pointer(tss.arr_reference),
                                                          ctypes.pointer(ctypes.c_int(k)),
                                                          ctypes.pointer(centroids),
                                                          ctypes.pointer(labels),
                                                          ctypes.pointer(ctypes.c_float(tolerance)),
                                                          ctypes.pointer(ctypes.c_int(max_iterations))
                                                          )
    return Array(array_reference=centroids), Array(array_reference=labels)


