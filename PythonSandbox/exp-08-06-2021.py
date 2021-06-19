#
# Zbiór modeli wygenerowany przez WebFuzzyEditor
# Znacznik czasowy generacji: 08.06.2021 20:52:17
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
## Model: 'przekaz_tresc'
## Opis:  Description-76876E73
##
class Model_Przekaz_tresc(object):
    foper = None #type: FuzzyOperation

    # Wartości ostre dla zmiennych wejściowych
    input_Censydiam1 = None # type: float # Zmienna: censydiam1
    input_Censydiam2 = None # type: float # Zmienna: censydiam2
    input_Censydiam3 = None # type: float # Zmienna: censydiam3
    input_Censydiam4 = None # type: float # Zmienna: censydiam4

    # Wartości ostre dla zmiennych wyjściowych
    output_Tresc_przekazu = None # type: float # Zmienna: tresc_przekazu

    # Dziedziny zmiennych rozmytych
    x_Censydiam1 = None # type: Union[List[float], np.ndarray]
    x_Censydiam2 = None # type: Union[List[float], np.ndarray]
    x_Censydiam3 = None # type: Union[List[float], np.ndarray]
    x_Censydiam4 = None # type: Union[List[float], np.ndarray]
    x_Tresc_przekazu = None # type: Union[List[float], np.ndarray]

    # Wartości przynależności
    memb_Censydiam1_Zabawa = None # type: Union[List[float], np.ndarray]
    memb_Censydiam1_Kontrola = None # type: Union[List[float], np.ndarray]
    memb_Censydiam2_Witalnosc = None # type: Union[List[float], np.ndarray]
    memb_Censydiam2_Wyciszenie = None # type: Union[List[float], np.ndarray]
    memb_Censydiam3_Status = None # type: Union[List[float], np.ndarray]
    memb_Censydiam3_Przynaleznosc = None # type: Union[List[float], np.ndarray]
    memb_Censydiam4_Dzielenie = None # type: Union[List[float], np.ndarray]
    memb_Censydiam4_Wyroznianie = None # type: Union[List[float], np.ndarray]
    memb_Tresc_przekazu_Kontrola = None # type: Union[List[float], np.ndarray]
    memb_Tresc_przekazu_Zabawa = None # type: Union[List[float], np.ndarray]

    def __init__(self):
        self.foper = FuzzyOperation()

        self.InitDomain()
        self.InitVariables()
#       self.ShowVariables()

    def InitDomain(self):
        x_step = 0.01
        self.x_Censydiam1 = np.arange(0.0000, 10.0000, x_step) # censydiam1: Description-1EAE9877??
        self.x_Censydiam2 = np.arange(0.0000, 10.0000, x_step) # censydiam2: Description-6DD9A966
        self.x_Censydiam3 = np.arange(0.0000, 10.0000, x_step) # censydiam3: Description-6DD9A966
        self.x_Censydiam4 = np.arange(0.0000, 10.0000, x_step) # censydiam4: Description-6DD9A966
        self.x_Tresc_przekazu = np.arange(0.0000, 10.0000, x_step) # tresc_przekazu: Description-6DD9A966

    def InitVariables(self):

        # Wejście: censydiam1
        self.memb_Censydiam1_Zabawa = fuzz.trapmf(self.x_Censydiam1, [0.0000, 0.0000, 1.0000, 9.0000])
        self.memb_Censydiam1_Kontrola = fuzz.trapmf(self.x_Censydiam1, [1.0000, 9.0000, 10.0000, 10.0000])

        # Wejście: censydiam2
        self.memb_Censydiam2_Witalnosc = fuzz.trapmf(self.x_Censydiam2, [0.0000, 0.0000, 1.0000, 9.0000])
        self.memb_Censydiam2_Wyciszenie = fuzz.trapmf(self.x_Censydiam2, [1.0000, 9.0000, 10.0000, 10.0000])

        # Wejście: censydiam3
        self.memb_Censydiam3_Status = fuzz.trapmf(self.x_Censydiam3, [0.0000, 0.0000, 1.0000, 9.0000])
        self.memb_Censydiam3_Przynaleznosc = fuzz.trapmf(self.x_Censydiam3, [1.0000, 9.0000, 10.0000, 10.0000])

        # Wejście: censydiam4
        self.memb_Censydiam4_Dzielenie = fuzz.trapmf(self.x_Censydiam4, [0.0000, 0.0000, 1.0000, 9.0000])
        self.memb_Censydiam4_Wyroznianie = fuzz.trapmf(self.x_Censydiam4, [1.0000, 9.0000, 10.0000, 10.0000])

        # Wyjście: tresc_przekazu
        self.memb_Tresc_przekazu_Kontrola = fuzz.trapmf(self.x_Tresc_przekazu, [0.0000, 0.0000, 1.0000, 9.0000])
        self.memb_Tresc_przekazu_Zabawa = fuzz.trapmf(self.x_Tresc_przekazu, [1.0000, 9.0000, 10.0000, 10.0000])

    def Execute(self, input_Censydiam1: float, input_Censydiam2: float, input_Censydiam3: float, input_Censydiam4: float):
        self.input_Censydiam1 = input_Censydiam1
        self.input_Censydiam2 = input_Censydiam2
        self.input_Censydiam3 = input_Censydiam3
        self.input_Censydiam4 = input_Censydiam4

        # Wyznacz poziomy przynależności
        level_Censydiam1_Zabawa = fuzz.interp_membership(self.x_Censydiam1, self.memb_Censydiam1_Zabawa, self.input_Censydiam1)
        level_Censydiam1_Kontrola = fuzz.interp_membership(self.x_Censydiam1, self.memb_Censydiam1_Kontrola, self.input_Censydiam1)
        level_Censydiam2_Witalnosc = fuzz.interp_membership(self.x_Censydiam2, self.memb_Censydiam2_Witalnosc, self.input_Censydiam2)
        level_Censydiam2_Wyciszenie = fuzz.interp_membership(self.x_Censydiam2, self.memb_Censydiam2_Wyciszenie, self.input_Censydiam2)
        level_Censydiam3_Status = fuzz.interp_membership(self.x_Censydiam3, self.memb_Censydiam3_Status, self.input_Censydiam3)
        level_Censydiam3_Przynaleznosc = fuzz.interp_membership(self.x_Censydiam3, self.memb_Censydiam3_Przynaleznosc, self.input_Censydiam3)
        level_Censydiam4_Dzielenie = fuzz.interp_membership(self.x_Censydiam4, self.memb_Censydiam4_Dzielenie, self.input_Censydiam4)
        level_Censydiam4_Wyroznianie = fuzz.interp_membership(self.x_Censydiam4, self.memb_Censydiam4_Wyroznianie, self.input_Censydiam4)

        #
        # Tutaj wnioskowanie ....

        #
        # Reguła IF [censydiam1 IS zabawa] Or [censydiam2 IS witalnosc] Or [censydiam3 IS status] Or [censydiam4 IS wyroznianie] THEN [tresc_przekazu IS zabawa]
        temp1 = self.foper.And(level_Censydiam4_Wyroznianie, level_Censydiam1_Zabawa)

        temp2 = self.foper.Or(level_Censydiam1_Zabawa, level_Censydiam2_Witalnosc)
        temp3 = self.foper.Or(temp2, level_Censydiam3_Status)
        temp4 = self.foper.Or(temp3, level_Censydiam4_Wyroznianie)
        temp5 = self.foper.Or(temp4, level_Censydiam1_Zabawa)
        temp6 = self.foper.Or(temp5, level_Censydiam2_Witalnosc)
        temp7 = self.foper.Or(temp6, level_Censydiam3_Status)
        temp8 = self.foper.Or(temp7, temp1)
        temp9 = self.foper.Or(temp8, level_Censydiam2_Witalnosc)
        temp10 = self.foper.Or(temp9, level_Censydiam3_Status)
        temp11 = self.foper.Or(temp10, level_Censydiam4_Wyroznianie)
        rule1_activation = temp11
        rule1_Tresc_przekazu_Zabawa = self.foper.Inference(rule1_activation, self.memb_Tresc_przekazu_Zabawa)

        #
        # Reguła IF [censydiam1 IS kontrola] Or [censydiam2 IS wyciszenie] Or [censydiam3 IS przynaleznosc] Or [censydiam4 IS dzielenie] THEN [tresc_przekazu IS kontrola]
        temp12 = self.foper.And(level_Censydiam4_Dzielenie, level_Censydiam1_Kontrola)

        temp13 = self.foper.Or(level_Censydiam1_Kontrola, level_Censydiam2_Wyciszenie)
        temp14 = self.foper.Or(temp13, level_Censydiam3_Przynaleznosc)
        temp15 = self.foper.Or(temp14, level_Censydiam4_Dzielenie)
        temp16 = self.foper.Or(temp15, level_Censydiam1_Kontrola)
        temp17 = self.foper.Or(temp16, level_Censydiam2_Wyciszenie)
        temp18 = self.foper.Or(temp17, level_Censydiam3_Przynaleznosc)
        temp19 = self.foper.Or(temp18, temp12)
        temp20 = self.foper.Or(temp19, level_Censydiam2_Wyciszenie)
        temp21 = self.foper.Or(temp20, level_Censydiam3_Przynaleznosc)
        temp22 = self.foper.Or(temp21, level_Censydiam4_Dzielenie)
        rule2_activation = temp22
        rule2_Tresc_przekazu_Kontrola = self.foper.Inference(rule2_activation, self.memb_Tresc_przekazu_Kontrola)

        #
        # Reguła IF [censydiam1 IS zabawa] THEN [tresc_przekazu IS zabawa]
        temp23 = self.foper.And(level_Censydiam1_Zabawa, level_Censydiam1_Zabawa)

        temp24 = self.foper.Or(level_Censydiam1_Zabawa, temp23)
        rule3_activation = temp24
        rule3_Tresc_przekazu_Zabawa = self.foper.Inference(rule3_activation, self.memb_Tresc_przekazu_Zabawa)

        #
        # Reguła IF [censydiam1 IS kontrola] THEN [tresc_przekazu IS kontrola]
        temp25 = self.foper.And(level_Censydiam1_Kontrola, level_Censydiam1_Kontrola)

        temp26 = self.foper.Or(level_Censydiam1_Kontrola, temp25)
        rule4_activation = temp26
        rule4_Tresc_przekazu_Kontrola = self.foper.Inference(rule4_activation, self.memb_Tresc_przekazu_Kontrola)

        #
        # Agregacja wyników wnioskowania w ramach tych samych wartości lingwistycznych zmiennych wyjściowych
        conclusion = self.foper.NeutralUnion(self.x_Tresc_przekazu)
        conclusion = self.foper.Union(conclusion, rule1_Tresc_przekazu_Zabawa)
        conclusion = self.foper.Union(conclusion, rule3_Tresc_przekazu_Zabawa)
        self.conclusion_Tresc_przekazu_Zabawa = conclusion
        conclusion = self.foper.NeutralUnion(self.x_Tresc_przekazu)
        conclusion = self.foper.Union(conclusion, rule2_Tresc_przekazu_Kontrola)
        conclusion = self.foper.Union(conclusion, rule4_Tresc_przekazu_Kontrola)
        self.conclusion_Tresc_przekazu_Kontrola = conclusion

        #
        # Wyostrzanie zmiennych wyjściowych
        aggregate = self.foper.NeutralAggregate(self.x_Tresc_przekazu)
        aggregate = self.foper.Aggregation(aggregate, self.conclusion_Tresc_przekazu_Kontrola)
        aggregate = self.foper.Aggregation(aggregate, self.conclusion_Tresc_przekazu_Zabawa)
        self.__aggregated_Tresc_przekazu = aggregate
        self.output_Tresc_przekazu = self.foper.Centroid(self.x_Tresc_przekazu, aggregate)

        #
        # przygotowanie słownika wyników
        result = dict(Tresc_przekazu = self.output_Tresc_przekazu)
        return result


    def ShowAllVariables(self):
        fig, axes = plt.subplots(nrows=4 + 1, figsize=(8, 3 * (4 + 1)))
        if not hasattr(axes, "__len__"):
            axes = [axes]

        axes[0].plot(self.x_Censydiam1, self.memb_Censydiam1_Zabawa, 'blue', linewidth=1.5, label='zabawa')
        axes[0].plot(self.x_Censydiam1, self.memb_Censydiam1_Kontrola, 'red', linewidth=1.5, label='kontrola')
        axes[0].set_title('WE: Description-1EAE9877??')
        axes[0].legend()

        axes[1].plot(self.x_Censydiam2, self.memb_Censydiam2_Witalnosc, 'blue', linewidth=1.5, label='witalnosc')
        axes[1].plot(self.x_Censydiam2, self.memb_Censydiam2_Wyciszenie, 'red', linewidth=1.5, label='wyciszenie')
        axes[1].set_title('WE: Description-6DD9A966')
        axes[1].legend()

        axes[2].plot(self.x_Censydiam3, self.memb_Censydiam3_Status, 'blue', linewidth=1.5, label='status')
        axes[2].plot(self.x_Censydiam3, self.memb_Censydiam3_Przynaleznosc, 'red', linewidth=1.5, label='przynaleznosc')
        axes[2].set_title('WE: Description-6DD9A966')
        axes[2].legend()

        axes[3].plot(self.x_Censydiam4, self.memb_Censydiam4_Dzielenie, 'blue', linewidth=1.5, label='dzielenie')
        axes[3].plot(self.x_Censydiam4, self.memb_Censydiam4_Wyroznianie, 'red', linewidth=1.5, label='wyroznianie')
        axes[3].set_title('WE: Description-6DD9A966')
        axes[3].legend()

        axes[4+0].plot(self.x_Tresc_przekazu, self.memb_Tresc_przekazu_Kontrola, 'blue', linewidth=1.5, label='kontrola')
        axes[4+0].plot(self.x_Tresc_przekazu, self.memb_Tresc_przekazu_Zabawa, 'red', linewidth=1.5, label='zabawa')
        axes[4+0].set_title('WY: Description-6DD9A966')
        axes[4+0].legend()

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

        axes[0].fill_between(self.x_Tresc_przekazu, np.zeros_like(self.x_Tresc_przekazu), self.conclusion_Tresc_przekazu_Kontrola, facecolor='blue', alpha=0.5)
        axes[0].plot(self.x_Tresc_przekazu, self.memb_Tresc_przekazu_Kontrola, 'blue', linewidth=0.5, linestyle='--', )
        axes[0].fill_between(self.x_Tresc_przekazu, np.zeros_like(self.x_Tresc_przekazu), self.conclusion_Tresc_przekazu_Zabawa, facecolor='red', alpha=0.5)
        axes[0].plot(self.x_Tresc_przekazu, self.memb_Tresc_przekazu_Zabawa, 'red', linewidth=0.5, linestyle='--', )

        memb = fuzz.interp_membership(self.x_Tresc_przekazu, self.__aggregated_Tresc_przekazu, self.output_Tresc_przekazu)
        axes[0].plot([self.output_Tresc_przekazu]*2, [0, memb], 'k', linewidth=3, alpha=0.9)
        axes[0].set_title('Description-6DD9A966')

        for ax in axes:
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.get_xaxis().tick_bottom()
            ax.get_yaxis().tick_left()

        plt.tight_layout()
        plt.show()


if __name__ == "__main__":

    a = np.array([1,2,3,4])
    b = np.array([5,6,7,8])
    c = np.array([9,10,11,12])
    d = np.hstack((a,b,c,c))





    m0 = Model_Przekaz_tresc()
    m0.ShowAllVariables()
    m0_result = m0.Execute(np.random.choice(m0.x_Censydiam1), np.random.choice(m0.x_Censydiam2), np.random.choice(m0.x_Censydiam3), np.random.choice(m0.x_Censydiam4))
    m0.ShowActivations()
    print(f"Przekaz_tresc: { m0_result }")

