#
# Zbiór modeli wygenerowany przez BlazorApp1
# Znacznik czasowy generacji: 27.11.2020 11:52:59
#
# Zażółć gęsią jaźń ZAŻÓŁĆ GĘSIĄ JAŹŃ

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from typing import List, Union
from typing import Callable


class FuzzyOperation(object):
    or_connective = None # type: Callable[[float, float], float]
    and_connective = None # type: Callable[[float, float], float]
    negation = None # type: Callable[[float], float]

    def __init__(self, or_connective = None, and_connective = None, negation = None):
        self.or_connective = or_connective or (lambda x, y: x if x > y else y)
        self.and_connective = and_connective or (lambda x, y: x if x < y else y)
        self.negation = negation or (lambda x: 1 - x)


    def And(self, *memberships: float):
        if len(memberships) < 2:
            raise ValueError("*memberships")
        elif len(memberships) == 2:
            return self.and_connective(memberships[0], memberships[1])
        v = memberships[0]
        for i in range(1, len(memberships)):
            v = self.and_connective(v, memberships[i])
        return v

    def Or(self, *memberships: float):
        if len(memberships) < 2:
            raise ValueError("*memberships")
        elif len(memberships) == 2:
            return self.or_connective(memberships[0], memberships[1])
        v = memberships[0]
        for i in range(1, len(memberships)):
            v = self.or_connective(v, memberships[i])
        return v

    def Not(self, membership: float) -> float:
        return self.negation(membership)

    def Inference(self, activation: float, fuzzyValue: np.ndarray) -> np.ndarray:
        output = np.fmin(activation, fuzzyValue)
        return output

    def NeutralUnion(self, domain: np.ndarray) -> np.ndarray:
        if not isinstance(domain, np.ndarray):
            raise TypeError("domain")

        if len(domain) == 0:
            raise ValueError("domain")

        output = np.zeros(domain.shape)
        return output

    def Union(self, fuzzyValue1: np.ndarray, fuzzyValue2: np.ndarray) -> np.ndarray:
        if not isinstance(fuzzyValue1, np.ndarray):
            raise TypeError("fuzzyValue1")
        if not isinstance(fuzzyValue2, np.ndarray):
            raise TypeError("fuzzyValue1")

        if len(fuzzyValue1) != len(fuzzyValue2):
            raise ValueError("len(fuzzyValue1) != len(fuzzyValue2)")

        output = np.fmax(fuzzyValue1, fuzzyValue2)
        return output

    def NeutralAggregate(self, domain: np.ndarray) -> np.ndarray:
        if not isinstance(domain, np.ndarray):
            raise TypeError("domain")

        if len(domain) == 0:
            raise ValueError("domain")

        output = np.zeros(domain.shape)
        return output

    def Aggregation(self, fuzzyValue1: np.ndarray, fuzzyValue2: np.ndarray) -> np.ndarray:
        if not isinstance(fuzzyValue1, np.ndarray):
            raise TypeError("fuzzyValue1")
        if not isinstance(fuzzyValue2, np.ndarray):
            raise TypeError("fuzzyValue1")

        if len(fuzzyValue1) != len(fuzzyValue2):
            raise ValueError("len(fuzzyValue1) != len(fuzzyValue2)")

        output = np.fmax(fuzzyValue1, fuzzyValue2)
        return output

    def Centroid(self, domain: np.ndarray, aggregatedVariable: np.ndarray) -> float:
        if not isinstance(domain, np.ndarray):
            raise TypeError("domain")
        if not isinstance(aggregatedVariable, np.ndarray):
            raise TypeError("aggregatedVariable")

        if len(domain) != len(aggregatedVariable):
            raise ValueError("len(domain) != len(aggregatedVariable)")

        output = fuzz.defuzz(domain, aggregatedVariable, 'centroid')
        return output

## -------------------------------------------------------------------------

##
## Model: 'nazwa modelu'
## Opis:  opis (Zażółć gęsią jaźń; ZAŻÓŁĆ GĘSIĄ JAŹŃ)
##
class Model_NazwaModelu(object):
    foper = None #type: FuzzyOperation

    # Wartości ostre dla zmiennych wejściowych
    input_Wzrost = None # type: float # Zmienna: wzrost
    input_Nazwa3 = None # type: float # Zmienna: Nazwa 3

    # Wartości ostre dla zmiennych wyjściowych
    output_Variable5e412271 = None # type: float # Zmienna: Variable-5E412271

    # Dziedziny zmiennych rozmytych
    x_Wzrost = None # type: Union[List[float], np.ndarray]
    x_Nazwa3 = None # type: Union[List[float], np.ndarray]
    x_Variable5e412271 = None # type: Union[List[float], np.ndarray]

    # Wartości przynależności
    memb_Wzrost_Malo = None # type: Union[List[float], np.ndarray]
    memb_Wzrost_Srednio = None # type: Union[List[float], np.ndarray]
    memb_Wzrost_Duzo = None # type: Union[List[float], np.ndarray]
    memb_Wzrost_Value51736aad = None # type: Union[List[float], np.ndarray]
    memb_Wzrost_Value28276813 = None # type: Union[List[float], np.ndarray]
    memb_Nazwa3_Negatywny = None # type: Union[List[float], np.ndarray]
    memb_Nazwa3_Zerowy = None # type: Union[List[float], np.ndarray]
    memb_Nazwa3_Pozytywny = None # type: Union[List[float], np.ndarray]
    memb_Variable5e412271_Value441c506e = None # type: Union[List[float], np.ndarray]
    memb_Variable5e412271_Value29974b38 = None # type: Union[List[float], np.ndarray]
    memb_Variable5e412271_Value04836667 = None # type: Union[List[float], np.ndarray]

    def __init__(self):
        self.foper = FuzzyOperation()

        self.InitDomain()
        self.InitVariables()
#       self.ShowVariables()

    def InitDomain(self):
        x_step = 0.01
        self.x_Wzrost = np.arange(10.0000, 100.0000, x_step) # wzrost: Opis zmiennej Nazwa I
        self.x_Nazwa3 = np.arange(-40.0000, 40.0000, x_step) # Nazwa 3: Opis zmiennej Nazwa III
        self.x_Variable5e412271 = np.arange(0.0000, 100.0000, x_step) # Variable-5E412271: Description-5ED63C56

    def InitVariables(self):

        # Wejście: wzrost
        self.memb_Wzrost_Malo = fuzz.trapmf(self.x_Wzrost, [0.0000, 0.0000, 25.0000, 40.0000])
        self.memb_Wzrost_Srednio = fuzz.trapmf(self.x_Wzrost, [25.0000, 40.0000, 55.0000, 70.0000])
        self.memb_Wzrost_Duzo = fuzz.trapmf(self.x_Wzrost, [55.0000, 70.0000, 110.0000, 110.0000])
        self.memb_Wzrost_Value51736aad = fuzz.trapmf(self.x_Wzrost, [1.0000, 2.0000, 3.0000, 4.0000])
        self.memb_Wzrost_Value28276813 = fuzz.trapmf(self.x_Wzrost, [1.0000, 2.0000, 3.0000, 4.0000])

        # Wejście: Nazwa 3
        self.memb_Nazwa3_Negatywny = fuzz.trapmf(self.x_Nazwa3, [-41.0000, -41.0000, -20.0000, 0.0000])
        self.memb_Nazwa3_Zerowy = fuzz.trapmf(self.x_Nazwa3, [-20.0000, 0.0000, 0.0000, 20.0000])
        self.memb_Nazwa3_Pozytywny = fuzz.trapmf(self.x_Nazwa3, [0.0000, 20.0000, 41.0000, 41.0000])

        # Wyjście: Variable-5E412271
        self.memb_Variable5e412271_Value441c506e = fuzz.trapmf(self.x_Variable5e412271, [10.0000, 20.0000, 30.0000, 40.0000])
        self.memb_Variable5e412271_Value29974b38 = fuzz.trapmf(self.x_Variable5e412271, [25.0000, 35.0000, 45.0000, 55.0000])
        self.memb_Variable5e412271_Value04836667 = fuzz.trapmf(self.x_Variable5e412271, [40.0000, 50.0000, 60.0000, 70.0000])

    def Execute(self, input_Wzrost: float, input_Nazwa3: float):
        self.input_Wzrost = input_Wzrost
        self.input_Nazwa3 = input_Nazwa3

        # Wyznacz poziomy przynależności
        level_Wzrost_Malo = fuzz.interp_membership(self.x_Wzrost, self.memb_Wzrost_Malo, self.input_Wzrost)
        level_Wzrost_Srednio = fuzz.interp_membership(self.x_Wzrost, self.memb_Wzrost_Srednio, self.input_Wzrost)
        level_Wzrost_Duzo = fuzz.interp_membership(self.x_Wzrost, self.memb_Wzrost_Duzo, self.input_Wzrost)
        level_Wzrost_Value51736aad = fuzz.interp_membership(self.x_Wzrost, self.memb_Wzrost_Value51736aad, self.input_Wzrost)
        level_Wzrost_Value28276813 = fuzz.interp_membership(self.x_Wzrost, self.memb_Wzrost_Value28276813, self.input_Wzrost)
        level_Nazwa3_Negatywny = fuzz.interp_membership(self.x_Nazwa3, self.memb_Nazwa3_Negatywny, self.input_Nazwa3)
        level_Nazwa3_Zerowy = fuzz.interp_membership(self.x_Nazwa3, self.memb_Nazwa3_Zerowy, self.input_Nazwa3)
        level_Nazwa3_Pozytywny = fuzz.interp_membership(self.x_Nazwa3, self.memb_Nazwa3_Pozytywny, self.input_Nazwa3)

        #
        # Tutaj wnioskowanie ....

        #
        # Reguła IF [wzrost IS Ma&#322;o] And [wzrost IS &#346;rednio] Or [Nazwa 3 IS Pozytywny] THEN [Variable-5E412271 IS Value-441C506E]
        temp1 = self.foper.And(level_Wzrost_Malo, level_Wzrost_Srednio)
        temp2 = self.foper.And(level_Wzrost_Malo, level_Wzrost_Srednio)
        temp3 = self.foper.And(level_Nazwa3_Pozytywny, level_Wzrost_Malo)
        temp4 = self.foper.And(temp3, level_Wzrost_Srednio)

        temp5 = self.foper.Or(temp1, level_Nazwa3_Pozytywny)
        temp6 = self.foper.Or(temp5, temp2)
        temp7 = self.foper.Or(temp6, temp4)
        temp8 = self.foper.Or(temp7, level_Nazwa3_Pozytywny)
        rule1_activation = temp8
        rule1_Variable5e412271_Value441c506e = self.foper.Inference(rule1_activation, self.memb_Variable5e412271_Value441c506e)

        #
        # Reguła IF [wzrost IS Du&#380;o] And [Nazwa 3 IS Negatywny] THEN [Variable-5E412271 IS Value-29974B38] And [Variable-5E412271 IS Value-441C506E]
        temp9 = self.foper.And(level_Wzrost_Duzo, level_Nazwa3_Negatywny)
        temp10 = self.foper.And(level_Wzrost_Duzo, level_Nazwa3_Negatywny)
        temp11 = self.foper.And(temp10, level_Wzrost_Duzo)
        temp12 = self.foper.And(temp11, level_Nazwa3_Negatywny)

        temp13 = self.foper.Or(temp9, temp12)
        rule2_activation = temp13
        rule2_Variable5e412271_Value29974b38 = self.foper.Inference(rule2_activation, self.memb_Variable5e412271_Value29974b38)
        rule2_Variable5e412271_Value441c506e = self.foper.Inference(rule2_activation, self.memb_Variable5e412271_Value441c506e)

        #
        # Reguła IF [wzrost IS &#346;rednio] Or [Nazwa 3 IS Zerowy] THEN [Variable-5E412271 IS Value-04836667] And [Variable-5E412271 IS Value-441C506E] And [Variable-5E412271 IS Value-29974B38]
        temp14 = self.foper.And(level_Nazwa3_Zerowy, level_Wzrost_Srednio)

        temp15 = self.foper.Or(level_Wzrost_Srednio, level_Nazwa3_Zerowy)
        temp16 = self.foper.Or(temp15, level_Wzrost_Srednio)
        temp17 = self.foper.Or(temp16, temp14)
        temp18 = self.foper.Or(temp17, level_Nazwa3_Zerowy)
        rule3_activation = temp18
        rule3_Variable5e412271_Value04836667 = self.foper.Inference(rule3_activation, self.memb_Variable5e412271_Value04836667)
        rule3_Variable5e412271_Value441c506e = self.foper.Inference(rule3_activation, self.memb_Variable5e412271_Value441c506e)
        rule3_Variable5e412271_Value29974b38 = self.foper.Inference(rule3_activation, self.memb_Variable5e412271_Value29974b38)

        #
        # Agregacja wyników wnioskowania w ramach tych samych wartości lingwistycznych zmiennych wyjściowych
        conclusion = self.foper.NeutralUnion(self.x_Variable5e412271)
        conclusion = self.foper.Union(conclusion, rule1_Variable5e412271_Value441c506e)
        conclusion = self.foper.Union(conclusion, rule2_Variable5e412271_Value441c506e)
        conclusion = self.foper.Union(conclusion, rule3_Variable5e412271_Value441c506e)
        self.conclusion_Variable5e412271_Value441c506e = conclusion
        conclusion = self.foper.NeutralUnion(self.x_Variable5e412271)
        conclusion = self.foper.Union(conclusion, rule2_Variable5e412271_Value29974b38)
        conclusion = self.foper.Union(conclusion, rule3_Variable5e412271_Value29974b38)
        self.conclusion_Variable5e412271_Value29974b38 = conclusion
        conclusion = self.foper.NeutralUnion(self.x_Variable5e412271)
        conclusion = self.foper.Union(conclusion, rule3_Variable5e412271_Value04836667)
        self.conclusion_Variable5e412271_Value04836667 = conclusion

        #
        # Wyostrzanie zmiennych wyjściowych
        aggregate = self.foper.NeutralAggregate(self.x_Variable5e412271)
        aggregate = self.foper.Aggregation(aggregate, self.conclusion_Variable5e412271_Value441c506e)
        aggregate = self.foper.Aggregation(aggregate, self.conclusion_Variable5e412271_Value29974b38)
        aggregate = self.foper.Aggregation(aggregate, self.conclusion_Variable5e412271_Value04836667)
        self.__aggregated_Variable5e412271 = aggregate
        self.output_Variable5e412271 = self.foper.Centroid(self.x_Variable5e412271, aggregate)

        #
        # przygotowanie słownika wyników
        result = dict(Variable5e412271 = self.output_Variable5e412271)
        return result


    def ShowAllVariables(self):
        fig, axes = plt.subplots(nrows=2 + 1, figsize=(8, 3 * (2 + 1)))
        if not hasattr(axes, "__len__"):
            axes = [axes]

        axes[0].plot(self.x_Wzrost, self.memb_Wzrost_Malo, 'blue', linewidth=1.5, label='Mało')
        axes[0].plot(self.x_Wzrost, self.memb_Wzrost_Srednio, 'red', linewidth=1.5, label='Średnio')
        axes[0].plot(self.x_Wzrost, self.memb_Wzrost_Duzo, 'green', linewidth=1.5, label='Dużo')
        axes[0].plot(self.x_Wzrost, self.memb_Wzrost_Value51736aad, 'black', linewidth=1.5, label='Value-51736AAD')
        axes[0].plot(self.x_Wzrost, self.memb_Wzrost_Value28276813, 'magenta', linewidth=1.5, label='Value-28276813')
        axes[0].set_title('WE: Opis zmiennej Nazwa I')
        axes[0].legend()

        axes[1].plot(self.x_Nazwa3, self.memb_Nazwa3_Negatywny, 'blue', linewidth=1.5, label='Negatywny')
        axes[1].plot(self.x_Nazwa3, self.memb_Nazwa3_Zerowy, 'red', linewidth=1.5, label='Zerowy')
        axes[1].plot(self.x_Nazwa3, self.memb_Nazwa3_Pozytywny, 'green', linewidth=1.5, label='Pozytywny')
        axes[1].set_title('WE: Opis zmiennej Nazwa III')
        axes[1].legend()

        axes[2+0].plot(self.x_Variable5e412271, self.memb_Variable5e412271_Value441c506e, 'blue', linewidth=1.5, label='Value-441C506E')
        axes[2+0].plot(self.x_Variable5e412271, self.memb_Variable5e412271_Value29974b38, 'red', linewidth=1.5, label='Value-29974B38')
        axes[2+0].plot(self.x_Variable5e412271, self.memb_Variable5e412271_Value04836667, 'green', linewidth=1.5, label='Value-04836667')
        axes[2+0].set_title('WY: Description-5ED63C56')
        axes[2+0].legend()

        for ax in axes:
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.get_xaxis().tick_bottom()
            ax.get_yaxis().tick_left()

        plt.tight_layout()
        plt.show()


    def ShowActivations(self):
        fig, axes = plt.subplots(nrows=1, figsize=(8, 3 * 1))
        if not hasattr(axes, "__len__"):
            axes = [axes]

        axes[0].fill_between(self.x_Variable5e412271, np.zeros_like(self.x_Variable5e412271), self.conclusion_Variable5e412271_Value441c506e, facecolor='blue', alpha=0.5)
        axes[0].plot(self.x_Variable5e412271, self.memb_Variable5e412271_Value441c506e, 'blue', linewidth=0.5, linestyle='--', )
        axes[0].fill_between(self.x_Variable5e412271, np.zeros_like(self.x_Variable5e412271), self.conclusion_Variable5e412271_Value29974b38, facecolor='red', alpha=0.5)
        axes[0].plot(self.x_Variable5e412271, self.memb_Variable5e412271_Value29974b38, 'red', linewidth=0.5, linestyle='--', )
        axes[0].fill_between(self.x_Variable5e412271, np.zeros_like(self.x_Variable5e412271), self.conclusion_Variable5e412271_Value04836667, facecolor='green', alpha=0.5)
        axes[0].plot(self.x_Variable5e412271, self.memb_Variable5e412271_Value04836667, 'green', linewidth=0.5, linestyle='--', )

        memb = fuzz.interp_membership(self.x_Variable5e412271, self.__aggregated_Variable5e412271, self.output_Variable5e412271)
        axes[0].plot([self.output_Variable5e412271]*2, [0, memb], 'k', linewidth=3, alpha=0.9)
        axes[0].set_title('Description-5ED63C56')

        for ax in axes:
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.get_xaxis().tick_bottom()
            ax.get_yaxis().tick_left()

        plt.tight_layout()
        plt.show()


##
## Model: 'nazwa modelu DRUGIEGO'
## Opis:  opis DRUGIEGO!!
##
## Model 'nazwa modelu DRUGIEGO' jest niedokończony.
##

if __name__ == "__main__":

    m0 = Model_NazwaModelu()
    m0.ShowAllVariables()
    m0_result = m0.Execute(np.random.choice(m0.x_Wzrost), np.random.choice(m0.x_Nazwa3))
    m0.ShowActivations()
    print(f"NazwaModelu: { m0_result }")

"""
    m1 = Model_NazwaModeluDrugiego()
    m1.ShowAllVariables()
    m1_result = m1.Execute()
    m1.ShowActivations()
    print(f"NazwaModeluDrugiego: { m1_result }")
"""
