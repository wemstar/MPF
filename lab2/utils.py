__author__ = 'wemstar'
import numpy as np
import matplotlib.pyplot as plt

temperatura=0.0

def iteracja(tablica, k=401.0, dt=1.0, cw=380.0, ro=8920.0, dx=0.005, dy=0.005):
    tablica[1:-1, 1:-1] = tablica[1:-1, 1:-1] + (k * dt) / (cw * ro * (dx )) * (
        tablica[2:, 1:-1] - 2.0 * tablica[1:-1, 1:-1] + tablica[:-2, 1:-1]) + (k * dt) / (cw * ro * (dy )) * (
        tablica[1:-1, 2:] - 2.0 * tablica[1:-1, 1:-1] + tablica[1:-1, :-2])
    return tablica


def warunekPoczatkowy(blaszka):
    blaszka[0, :] = 10.0;
    blaszka[-1, :] = 10.0;
    blaszka[:, 0] = 10.0;
    blaszka[:, -1] = 10.0;
    blaszka[90:110, 90:110] = 80.0


def warunekDwa(blaszka, dt=1.0, cw=380.0, ro=8920.0):
        global temperatura
        temp = (50.0 * dt) / (cw * ro * 0.05 * 2.0 * 2.0);
        blaszka[90:110, 90:110]=blaszka[90:110, 90:110]+temp
        temperatura+=temp


def iteruj(data, warunek, n=50000):
    for x in range(n):
        data = iteracja(data, dt=1.0)
        if x < 11:
            warunek(data)

    return data
