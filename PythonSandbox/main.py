#
# Zbiór modeli wygenerowany przez BlazorApp1
# Znacznik czasowy generacji: 24.11.2020 23:23:23
#
# Zażółć gęsią jaźń ZAŻÓŁĆ GĘSIĄ JAŹŃ

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from typing import List, Union

##
## Model: nazwa modelu
## Opis:  opis (Zażółć gęsią jaźń; ZAŻÓŁĆ GĘSIĄ JAŹŃ)
##
class Model_NazwaModelu(object):
    x_Wzrost = None # type: Union[List[float], np.ndarray] # Zmienna: wzrost
    x_Nazwa3 = None # type: Union[List[float], np.ndarray] # Zmienna: Nazwa 3
    x_Variable5e412271 = None # type: Union[List[float], np.ndarray] # Zmienna: Variable-5E412271

    def __init__(self):
        self.InitDomain()
        self.InitVariables()
#       self.ShowVariables()

    def InitDomain(self):
        self.x_Wzrost = np.arange(10.0000, 100.0000, 0.1000) # wzrost: Opis zmiennej Nazwa I
        self.x_Nazwa3 = np.arange(-40.0000, 40.0000, 0.1000) # Nazwa 3: Opis zmiennej Nazwa III
        self.x_Variable5e412271 = np.arange(0.0000, 100.0000, 0.1000) # Variable-5E412271: Description-5ED63C56

    def InitVariables(self):
        self.Wzrost_Malo = fuzz.trapmf(self.x_Wzrost, [0.0000, 0.0000, 25.0000, 40.0000])
        self.Wzrost_Srednio = fuzz.trapmf(self.x_Wzrost, [25.0000, 40.0000, 55.0000, 70.0000])
        self.Wzrost_Duzo = fuzz.trapmf(self.x_Wzrost, [55.0000, 70.0000, 110.0000, 110.0000])
        self.Wzrost_Value51736aad = fuzz.trapmf(self.x_Wzrost, [1.0000, 2.0000, 3.0000, 4.0000])
        self.Wzrost_Value28276813 = fuzz.trapmf(self.x_Wzrost, [1.0000, 2.0000, 3.0000, 4.0000])
        self.Nazwa3_Negatywny = fuzz.trapmf(self.x_Nazwa3, [-41.0000, -41.0000, -20.0000, 0.0000])
        self.Nazwa3_Zerowy = fuzz.trapmf(self.x_Nazwa3, [-20.0000, 0.0000, 0.0000, 20.0000])
        self.Nazwa3_Pozytywny = fuzz.trapmf(self.x_Nazwa3, [0.0000, 20.0000, 41.0000, 41.0000])
        self.Variable5e412271_Value441c506e = fuzz.trapmf(self.x_Variable5e412271, [10.0000, 20.0000, 30.0000, 40.0000])
        self.Variable5e412271_Value29974b38 = fuzz.trapmf(self.x_Variable5e412271, [25.0000, 35.0000, 45.0000, 55.0000])
        self.Variable5e412271_Value04836667 = fuzz.trapmf(self.x_Variable5e412271, [40.0000, 50.0000, 60.0000, 70.0000])

    def ShowVariables(self):
        fig, axes = plt.subplots(nrows=3, figsize=(8, 9))


        axes[0].plot(self.x_Wzrost, self.Wzrost_Malo, 'blue', linewidth=1.5, label='Mało')
        axes[0].plot(self.x_Wzrost, self.Wzrost_Srednio, 'red', linewidth=1.5, label='Średnio')
        axes[0].plot(self.x_Wzrost, self.Wzrost_Duzo, 'green', linewidth=1.5, label='Dużo')
        axes[0].plot(self.x_Wzrost, self.Wzrost_Value51736aad, 'black', linewidth=1.5, label='Value-51736AAD')
        axes[0].plot(self.x_Wzrost, self.Wzrost_Value28276813, 'magenta', linewidth=1.5, label='Value-28276813')
        axes[0].set_title('Opis zmiennej Nazwa I')
        axes[0].legend()

        axes[1].plot(self.x_Nazwa3, self.Nazwa3_Negatywny, 'blue', linewidth=1.5, label='Negatywny')
        axes[1].plot(self.x_Nazwa3, self.Nazwa3_Zerowy, 'red', linewidth=1.5, label='Zerowy')
        axes[1].plot(self.x_Nazwa3, self.Nazwa3_Pozytywny, 'green', linewidth=1.5, label='Pozytywny')
        axes[1].set_title('Opis zmiennej Nazwa III')
        axes[1].legend()

        axes[2].plot(self.x_Variable5e412271, self.Variable5e412271_Value441c506e, 'blue', linewidth=1.5, label='Value-441C506E')
        axes[2].plot(self.x_Variable5e412271, self.Variable5e412271_Value29974b38, 'red', linewidth=1.5, label='Value-29974B38')
        axes[2].plot(self.x_Variable5e412271, self.Variable5e412271_Value04836667, 'green', linewidth=1.5, label='Value-04836667')
        axes[2].set_title('Description-5ED63C56')
        axes[2].legend()

        # Turn off top/right axes
        for ax in axes:
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.get_xaxis().tick_bottom()
            ax.get_yaxis().tick_left()

        plt.tight_layout()
        plt.show()

##
## Model: nazwa modelu DRUGIEGO
## Opis:  opis DRUGIEGO!!
##
## Model nazwa modelu DRUGIEGO jest niedokończony.
##

if __name__ == "__main__":
    m0 = Model_NazwaModelu()
    m0.ShowVariables()

#    m1 = Model_NazwaModeluDrugiego()
#    m1.ShowVariables()

