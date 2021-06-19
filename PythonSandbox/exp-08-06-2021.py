#
# Zbiór modeli wygenerowany przez WebFuzzyEditor
# Znacznik czasowy generacji: 06/08/2021 18:11:09
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
    output_TrescPrzekazu = None # type: float # Zmienna: Treść przekazu

    # Dziedziny zmiennych rozmytych
    x_Censydiam1 = None # type: Union[List[float], np.ndarray]
    x_Censydiam2 = None # type: Union[List[float], np.ndarray]
    x_Censydiam3 = None # type: Union[List[float], np.ndarray]
    x_Censydiam4 = None # type: Union[List[float], np.ndarray]
    x_TrescPrzekazu = None # type: Union[List[float], np.ndarray]

    # Wartości przynależności
    memb_Censydiam1_Zabawa = None # type: Union[List[float], np.ndarray]
    memb_Censydiam1_Kontrola = None # type: Union[List[float], np.ndarray]
    memb_Censydiam2_Witalnosc = None # type: Union[List[float], np.ndarray]
    memb_Censydiam2_Wyciszenie = None # type: Union[List[float], np.ndarray]
    memb_Censydiam3_Status = None # type: Union[List[float], np.ndarray]
    memb_Censydiam3_Przynaleznosc = None # type: Union[List[float], np.ndarray]
    memb_Censydiam4_Dzielenie = None # type: Union[List[float], np.ndarray]
    memb_Censydiam4_Wyroznianie = None # type: Union[List[float], np.ndarray]
    memb_TrescPrzekazu_Kontrola = None # type: Union[List[float], np.ndarray]
    memb_TrescPrzekazu_Zabawa = None # type: Union[List[float], np.ndarray]

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
        self.x_TrescPrzekazu = np.arange(0.0000, 10.0000, x_step) # Treść przekazu: Description-6DD9A966

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

        # Wyjście: Tre&#347;&#263; przekazu
        self.memb_TrescPrzekazu_Kontrola = fuzz.trapmf(self.x_TrescPrzekazu, [0.0000, 0.0000, 1.0000, 9.0000])
        self.memb_TrescPrzekazu_Zabawa = fuzz.trapmf(self.x_TrescPrzekazu, [1.0000, 9.0000, 10.0000, 10.0000])

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
        # Reguła IF [censydiam1 IS zabawa] Or [censydiam2 IS witalnosc] Or [censydiam3 IS status] Or [censydiam4 IS wyroznianie] THEN [Tre&#347;&#263; przekazu IS zabawa]
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
        rule1_TrescPrzekazu_Zabawa = self.foper.Inference(rule1_activation, self.memb_TrescPrzekazu_Zabawa)

        #
        # Reguła IF [censydiam1 IS kontrola] Or [censydiam2 IS wyciszenie] Or [censydiam3 IS przynaleznosc] Or [censydiam4 IS dzielenie] THEN [Tre&#347;&#263; przekazu IS kontrola]
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
        rule2_TrescPrzekazu_Kontrola = self.foper.Inference(rule2_activation, self.memb_TrescPrzekazu_Kontrola)

        #
        # Reguła IF [censydiam1 IS zabawa] THEN [Tre&#347;&#263; przekazu IS zabawa]
        temp23 = self.foper.And(level_Censydiam1_Zabawa, level_Censydiam1_Zabawa)

        temp24 = self.foper.Or(level_Censydiam1_Zabawa, temp23)
        rule3_activation = temp24
        rule3_TrescPrzekazu_Zabawa = self.foper.Inference(rule3_activation, self.memb_TrescPrzekazu_Zabawa)

        #
        # Reguła IF [censydiam1 IS zabawa] And [censydiam2 IS witalnosc] THEN [Tre&#347;&#263; przekazu IS zabawa]
        temp25 = self.foper.And(level_Censydiam1_Zabawa, level_Censydiam2_Witalnosc)
        temp26 = self.foper.And(level_Censydiam1_Zabawa, level_Censydiam2_Witalnosc)
        temp27 = self.foper.And(temp26, level_Censydiam1_Zabawa)
        temp28 = self.foper.And(temp27, level_Censydiam2_Witalnosc)

        temp29 = self.foper.Or(temp25, temp28)
        rule4_activation = temp29
        rule4_TrescPrzekazu_Zabawa = self.foper.Inference(rule4_activation, self.memb_TrescPrzekazu_Zabawa)

        #
        # Reguła IF [censydiam1 IS kontrola] THEN [Tre&#347;&#263; przekazu IS kontrola]
        temp30 = self.foper.And(level_Censydiam1_Kontrola, level_Censydiam1_Kontrola)

        temp31 = self.foper.Or(level_Censydiam1_Kontrola, temp30)
        rule5_activation = temp31
        rule5_TrescPrzekazu_Kontrola = self.foper.Inference(rule5_activation, self.memb_TrescPrzekazu_Kontrola)

        #
        # Reguła IF [censydiam1 IS zabawa] And [censydiam4 IS dzielenie] THEN [Tre&#347;&#263; przekazu IS zabawa]
        temp32 = self.foper.And(level_Censydiam1_Zabawa, level_Censydiam4_Dzielenie)
        temp33 = self.foper.And(level_Censydiam1_Zabawa, level_Censydiam4_Dzielenie)
        temp34 = self.foper.And(temp33, level_Censydiam1_Zabawa)
        temp35 = self.foper.And(temp34, level_Censydiam4_Dzielenie)

        temp36 = self.foper.Or(temp32, temp35)
        rule6_activation = temp36
        rule6_TrescPrzekazu_Zabawa = self.foper.Inference(rule6_activation, self.memb_TrescPrzekazu_Zabawa)

        #
        # Reguła IF [censydiam1 IS kontrola] And [censydiam2 IS wyciszenie] THEN [Tre&#347;&#263; przekazu IS kontrola]
        temp37 = self.foper.And(level_Censydiam1_Kontrola, level_Censydiam2_Wyciszenie)
        temp38 = self.foper.And(level_Censydiam1_Kontrola, level_Censydiam2_Wyciszenie)
        temp39 = self.foper.And(temp38, level_Censydiam1_Kontrola)
        temp40 = self.foper.And(temp39, level_Censydiam2_Wyciszenie)

        temp41 = self.foper.Or(temp37, temp40)
        rule7_activation = temp41
        rule7_TrescPrzekazu_Kontrola = self.foper.Inference(rule7_activation, self.memb_TrescPrzekazu_Kontrola)

        #
        # Reguła IF [censydiam1 IS kontrola] And [censydiam4 IS wyroznianie] THEN [Tre&#347;&#263; przekazu IS kontrola]
        temp42 = self.foper.And(level_Censydiam1_Kontrola, level_Censydiam4_Wyroznianie)
        temp43 = self.foper.And(level_Censydiam1_Kontrola, level_Censydiam4_Wyroznianie)
        temp44 = self.foper.And(temp43, level_Censydiam1_Kontrola)
        temp45 = self.foper.And(temp44, level_Censydiam4_Wyroznianie)

        temp46 = self.foper.Or(temp42, temp45)
        rule8_activation = temp46
        rule8_TrescPrzekazu_Kontrola = self.foper.Inference(rule8_activation, self.memb_TrescPrzekazu_Kontrola)

        #
        # Reguła IF [censydiam2 IS witalnosc] THEN [Tre&#347;&#263; przekazu IS zabawa]
        temp47 = self.foper.And(level_Censydiam2_Witalnosc, level_Censydiam2_Witalnosc)

        temp48 = self.foper.Or(level_Censydiam2_Witalnosc, temp47)
        rule9_activation = temp48
        rule9_TrescPrzekazu_Zabawa = self.foper.Inference(rule9_activation, self.memb_TrescPrzekazu_Zabawa)

        #
        # Reguła IF [censydiam4 IS dzielenie] THEN [Tre&#347;&#263; przekazu IS zabawa]
        temp49 = self.foper.And(level_Censydiam4_Dzielenie, level_Censydiam4_Dzielenie)

        temp50 = self.foper.Or(level_Censydiam4_Dzielenie, temp49)
        rule10_activation = temp50
        rule10_TrescPrzekazu_Zabawa = self.foper.Inference(rule10_activation, self.memb_TrescPrzekazu_Zabawa)

        #
        # Reguła IF [censydiam2 IS wyciszenie] THEN [Tre&#347;&#263; przekazu IS kontrola]
        temp51 = self.foper.And(level_Censydiam2_Wyciszenie, level_Censydiam2_Wyciszenie)

        temp52 = self.foper.Or(level_Censydiam2_Wyciszenie, temp51)
        rule11_activation = temp52
        rule11_TrescPrzekazu_Kontrola = self.foper.Inference(rule11_activation, self.memb_TrescPrzekazu_Kontrola)

        #
        # Reguła IF [censydiam4 IS wyroznianie] THEN [Tre&#347;&#263; przekazu IS kontrola]
        temp53 = self.foper.And(level_Censydiam4_Wyroznianie, level_Censydiam4_Wyroznianie)

        temp54 = self.foper.Or(level_Censydiam4_Wyroznianie, temp53)
        rule12_activation = temp54
        rule12_TrescPrzekazu_Kontrola = self.foper.Inference(rule12_activation, self.memb_TrescPrzekazu_Kontrola)

        #
        # Reguła IF [censydiam1 IS zabawa] And [censydiam2 IS witalnosc] And [censydiam4 IS dzielenie] THEN [Tre&#347;&#263; przekazu IS zabawa]
        temp55 = self.foper.And(level_Censydiam1_Zabawa, level_Censydiam2_Witalnosc)
        temp56 = self.foper.And(temp55, level_Censydiam4_Dzielenie)
        temp57 = self.foper.And(level_Censydiam1_Zabawa, level_Censydiam2_Witalnosc)
        temp58 = self.foper.And(temp57, level_Censydiam4_Dzielenie)
        temp59 = self.foper.And(temp58, level_Censydiam1_Zabawa)
        temp60 = self.foper.And(temp59, level_Censydiam2_Witalnosc)
        temp61 = self.foper.And(temp60, level_Censydiam4_Dzielenie)

        temp62 = self.foper.Or(temp56, temp61)
        rule13_activation = temp62
        rule13_TrescPrzekazu_Zabawa = self.foper.Inference(rule13_activation, self.memb_TrescPrzekazu_Zabawa)

        #
        # Reguła IF [censydiam1 IS kontrola] And [censydiam2 IS wyciszenie] And [censydiam4 IS wyroznianie] THEN [Tre&#347;&#263; przekazu IS kontrola]
        temp63 = self.foper.And(level_Censydiam1_Kontrola, level_Censydiam2_Wyciszenie)
        temp64 = self.foper.And(temp63, level_Censydiam4_Wyroznianie)
        temp65 = self.foper.And(level_Censydiam1_Kontrola, level_Censydiam2_Wyciszenie)
        temp66 = self.foper.And(temp65, level_Censydiam4_Wyroznianie)
        temp67 = self.foper.And(temp66, level_Censydiam1_Kontrola)
        temp68 = self.foper.And(temp67, level_Censydiam2_Wyciszenie)
        temp69 = self.foper.And(temp68, level_Censydiam4_Wyroznianie)

        temp70 = self.foper.Or(temp64, temp69)
        rule14_activation = temp70
        rule14_TrescPrzekazu_Kontrola = self.foper.Inference(rule14_activation, self.memb_TrescPrzekazu_Kontrola)

        #
        # Agregacja wyników wnioskowania w ramach tych samych wartości lingwistycznych zmiennych wyjściowych
        conclusion = self.foper.NeutralUnion(self.x_TrescPrzekazu)
        conclusion = self.foper.Union(conclusion, rule1_TrescPrzekazu_Zabawa)
        conclusion = self.foper.Union(conclusion, rule3_TrescPrzekazu_Zabawa)
        conclusion = self.foper.Union(conclusion, rule4_TrescPrzekazu_Zabawa)
        conclusion = self.foper.Union(conclusion, rule6_TrescPrzekazu_Zabawa)
        conclusion = self.foper.Union(conclusion, rule9_TrescPrzekazu_Zabawa)
        conclusion = self.foper.Union(conclusion, rule10_TrescPrzekazu_Zabawa)
        conclusion = self.foper.Union(conclusion, rule13_TrescPrzekazu_Zabawa)
        self.conclusion_TrescPrzekazu_Zabawa = conclusion
        conclusion = self.foper.NeutralUnion(self.x_TrescPrzekazu)
        conclusion = self.foper.Union(conclusion, rule2_TrescPrzekazu_Kontrola)
        conclusion = self.foper.Union(conclusion, rule5_TrescPrzekazu_Kontrola)
        conclusion = self.foper.Union(conclusion, rule7_TrescPrzekazu_Kontrola)
        conclusion = self.foper.Union(conclusion, rule8_TrescPrzekazu_Kontrola)
        conclusion = self.foper.Union(conclusion, rule11_TrescPrzekazu_Kontrola)
        conclusion = self.foper.Union(conclusion, rule12_TrescPrzekazu_Kontrola)
        conclusion = self.foper.Union(conclusion, rule14_TrescPrzekazu_Kontrola)
        self.conclusion_TrescPrzekazu_Kontrola = conclusion

        #
        # Wyostrzanie zmiennych wyjściowych
        aggregate = self.foper.NeutralAggregate(self.x_TrescPrzekazu)
        aggregate = self.foper.Aggregation(aggregate, self.conclusion_TrescPrzekazu_Kontrola)
        aggregate = self.foper.Aggregation(aggregate, self.conclusion_TrescPrzekazu_Zabawa)
        self.__aggregated_TrescPrzekazu = aggregate
        self.output_TrescPrzekazu = self.foper.Centroid(self.x_TrescPrzekazu, aggregate)

        #
        # przygotowanie słownika wyników
        result = dict(TrescPrzekazu = self.output_TrescPrzekazu)
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

        axes[4+0].plot(self.x_TrescPrzekazu, self.memb_TrescPrzekazu_Kontrola, 'blue', linewidth=1.5, label='kontrola')
        axes[4+0].plot(self.x_TrescPrzekazu, self.memb_TrescPrzekazu_Zabawa, 'red', linewidth=1.5, label='zabawa')
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

        axes[0].fill_between(self.x_TrescPrzekazu, np.zeros_like(self.x_TrescPrzekazu), self.conclusion_TrescPrzekazu_Kontrola, facecolor='blue', alpha=0.5)
        axes[0].plot(self.x_TrescPrzekazu, self.memb_TrescPrzekazu_Kontrola, 'blue', linewidth=0.5, linestyle='--', )
        axes[0].fill_between(self.x_TrescPrzekazu, np.zeros_like(self.x_TrescPrzekazu), self.conclusion_TrescPrzekazu_Zabawa, facecolor='red', alpha=0.5)
        axes[0].plot(self.x_TrescPrzekazu, self.memb_TrescPrzekazu_Zabawa, 'red', linewidth=0.5, linestyle='--', )

        memb = fuzz.interp_membership(self.x_TrescPrzekazu, self.__aggregated_TrescPrzekazu, self.output_TrescPrzekazu)
        axes[0].plot([self.output_TrescPrzekazu]*2, [0, memb], 'k', linewidth=3, alpha=0.9)
        axes[0].set_title('Description-6DD9A966')

        for ax in axes:
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.get_xaxis().tick_bottom()
            ax.get_yaxis().tick_left()

        plt.tight_layout()
        plt.show()


##
## Model: 'zlozonosc_informacji'
## Opis:  Description-73894906
##
class Model_Zlozonosc_informacji(object):
    foper = None #type: FuzzyOperation

    # Wartości ostre dla zmiennych wejściowych
    input_Tekst_do_obrazka = None # type: float # Zmienna: tekst_do_obrazka
    input_Nasilenie = None # type: float # Zmienna: nasilenie
    input_Argumenty = None # type: float # Zmienna: argumenty
    input_Liczba_argumentow = None # type: float # Zmienna: liczba_argumentow
    input_Argumentacja = None # type: float # Zmienna: argumentacja

    # Wartości ostre dla zmiennych wyjściowych
    output_Zlozonosc = None # type: float # Zmienna: zlozonosc

    # Dziedziny zmiennych rozmytych
    x_Tekst_do_obrazka = None # type: Union[List[float], np.ndarray]
    x_Nasilenie = None # type: Union[List[float], np.ndarray]
    x_Argumenty = None # type: Union[List[float], np.ndarray]
    x_Liczba_argumentow = None # type: Union[List[float], np.ndarray]
    x_Argumentacja = None # type: Union[List[float], np.ndarray]
    x_Zlozonosc = None # type: Union[List[float], np.ndarray]

    # Wartości przynależności
    memb_Tekst_do_obrazka_Niskie = None # type: Union[List[float], np.ndarray]
    memb_Tekst_do_obrazka_Wysokie = None # type: Union[List[float], np.ndarray]
    memb_Nasilenie_Niskie = None # type: Union[List[float], np.ndarray]
    memb_Nasilenie_Wysokie = None # type: Union[List[float], np.ndarray]
    memb_Argumenty_Jednostronne = None # type: Union[List[float], np.ndarray]
    memb_Argumenty_Obustronne = None # type: Union[List[float], np.ndarray]
    memb_Liczba_argumentow_Niska = None # type: Union[List[float], np.ndarray]
    memb_Liczba_argumentow_Wysoka = None # type: Union[List[float], np.ndarray]
    memb_Argumentacja_Racjonalna = None # type: Union[List[float], np.ndarray]
    memb_Argumentacja_Irracjonalna = None # type: Union[List[float], np.ndarray]
    memb_Zlozonosc_Niska = None # type: Union[List[float], np.ndarray]
    memb_Zlozonosc_Wysoka = None # type: Union[List[float], np.ndarray]

    def __init__(self):
        self.foper = FuzzyOperation()

        self.InitDomain()
        self.InitVariables()
#       self.ShowVariables()

    def InitDomain(self):
        x_step = 0.01
        self.x_Tekst_do_obrazka = np.arange(0.0000, 10.0000, x_step) # tekst_do_obrazka: Description-6DD9A966
        self.x_Nasilenie = np.arange(0.0000, 10.0000, x_step) # nasilenie: Description-6DD9A966
        self.x_Argumenty = np.arange(0.0000, 10.0000, x_step) # argumenty: Description-6DD9A966
        self.x_Liczba_argumentow = np.arange(0.0000, 10.0000, x_step) # liczba_argumentow: Description-6DD9A966
        self.x_Argumentacja = np.arange(0.0000, 10.0000, x_step) # argumentacja: Description-6DD9A966
        self.x_Zlozonosc = np.arange(0.0000, 10.0000, x_step) # zlozonosc: Description-6DD9A966

    def InitVariables(self):

        # Wejście: tekst_do_obrazka
        self.memb_Tekst_do_obrazka_Niskie = fuzz.trapmf(self.x_Tekst_do_obrazka, [0.0000, 0.0000, 1.0000, 9.0000])
        self.memb_Tekst_do_obrazka_Wysokie = fuzz.trapmf(self.x_Tekst_do_obrazka, [1.0000, 9.0000, 10.0000, 10.0000])

        # Wejście: nasilenie
        self.memb_Nasilenie_Niskie = fuzz.trapmf(self.x_Nasilenie, [0.0000, 0.0000, 1.0000, 9.0000])
        self.memb_Nasilenie_Wysokie = fuzz.trapmf(self.x_Nasilenie, [1.0000, 9.0000, 10.0000, 10.0000])

        # Wejście: argumenty
        self.memb_Argumenty_Jednostronne = fuzz.trapmf(self.x_Argumenty, [0.0000, 0.0000, 1.0000, 9.0000])
        self.memb_Argumenty_Obustronne = fuzz.trapmf(self.x_Argumenty, [1.0000, 9.0000, 10.0000, 10.0000])

        # Wejście: liczba_argumentow
        self.memb_Liczba_argumentow_Niska = fuzz.trapmf(self.x_Liczba_argumentow, [0.0000, 0.0000, 1.0000, 9.0000])
        self.memb_Liczba_argumentow_Wysoka = fuzz.trapmf(self.x_Liczba_argumentow, [1.0000, 9.0000, 10.0000, 10.0000])

        # Wejście: argumentacja
        self.memb_Argumentacja_Racjonalna = fuzz.trapmf(self.x_Argumentacja, [0.0000, 0.0000, 1.0000, 9.0000])
        self.memb_Argumentacja_Irracjonalna = fuzz.trapmf(self.x_Argumentacja, [1.0000, 9.0000, 10.0000, 10.0000])

        # Wyjście: zlozonosc
        self.memb_Zlozonosc_Niska = fuzz.trapmf(self.x_Zlozonosc, [0.0000, 0.0000, 1.0000, 9.0000])
        self.memb_Zlozonosc_Wysoka = fuzz.trapmf(self.x_Zlozonosc, [1.0000, 9.0000, 10.0000, 10.0000])

    def Execute(self, input_Tekst_do_obrazka: float, input_Nasilenie: float, input_Argumenty: float, input_Liczba_argumentow: float, input_Argumentacja: float):
        self.input_Tekst_do_obrazka = input_Tekst_do_obrazka
        self.input_Nasilenie = input_Nasilenie
        self.input_Argumenty = input_Argumenty
        self.input_Liczba_argumentow = input_Liczba_argumentow
        self.input_Argumentacja = input_Argumentacja

        # Wyznacz poziomy przynależności
        level_Tekst_do_obrazka_Niskie = fuzz.interp_membership(self.x_Tekst_do_obrazka, self.memb_Tekst_do_obrazka_Niskie, self.input_Tekst_do_obrazka)
        level_Tekst_do_obrazka_Wysokie = fuzz.interp_membership(self.x_Tekst_do_obrazka, self.memb_Tekst_do_obrazka_Wysokie, self.input_Tekst_do_obrazka)
        level_Nasilenie_Niskie = fuzz.interp_membership(self.x_Nasilenie, self.memb_Nasilenie_Niskie, self.input_Nasilenie)
        level_Nasilenie_Wysokie = fuzz.interp_membership(self.x_Nasilenie, self.memb_Nasilenie_Wysokie, self.input_Nasilenie)
        level_Argumenty_Jednostronne = fuzz.interp_membership(self.x_Argumenty, self.memb_Argumenty_Jednostronne, self.input_Argumenty)
        level_Argumenty_Obustronne = fuzz.interp_membership(self.x_Argumenty, self.memb_Argumenty_Obustronne, self.input_Argumenty)
        level_Liczba_argumentow_Niska = fuzz.interp_membership(self.x_Liczba_argumentow, self.memb_Liczba_argumentow_Niska, self.input_Liczba_argumentow)
        level_Liczba_argumentow_Wysoka = fuzz.interp_membership(self.x_Liczba_argumentow, self.memb_Liczba_argumentow_Wysoka, self.input_Liczba_argumentow)
        level_Argumentacja_Racjonalna = fuzz.interp_membership(self.x_Argumentacja, self.memb_Argumentacja_Racjonalna, self.input_Argumentacja)
        level_Argumentacja_Irracjonalna = fuzz.interp_membership(self.x_Argumentacja, self.memb_Argumentacja_Irracjonalna, self.input_Argumentacja)

        #
        # Tutaj wnioskowanie ....

        #
        # Reguła IF [tekst_do_obrazka IS niskie] Or [nasilenie IS niskie] Or [argumenty IS jednostronne] Or [liczba_argumentow IS niska] Or [argumentacja IS irracjonalna] THEN [zlozonosc IS niska]
        temp71 = self.foper.And(level_Argumentacja_Irracjonalna, level_Tekst_do_obrazka_Niskie)

        temp72 = self.foper.Or(level_Tekst_do_obrazka_Niskie, level_Nasilenie_Niskie)
        temp73 = self.foper.Or(temp72, level_Argumenty_Jednostronne)
        temp74 = self.foper.Or(temp73, level_Liczba_argumentow_Niska)
        temp75 = self.foper.Or(temp74, level_Argumentacja_Irracjonalna)
        temp76 = self.foper.Or(temp75, level_Tekst_do_obrazka_Niskie)
        temp77 = self.foper.Or(temp76, level_Nasilenie_Niskie)
        temp78 = self.foper.Or(temp77, level_Argumenty_Jednostronne)
        temp79 = self.foper.Or(temp78, level_Liczba_argumentow_Niska)
        temp80 = self.foper.Or(temp79, temp71)
        temp81 = self.foper.Or(temp80, level_Nasilenie_Niskie)
        temp82 = self.foper.Or(temp81, level_Argumenty_Jednostronne)
        temp83 = self.foper.Or(temp82, level_Liczba_argumentow_Niska)
        temp84 = self.foper.Or(temp83, level_Argumentacja_Irracjonalna)
        rule15_activation = temp84
        rule15_Zlozonosc_Niska = self.foper.Inference(rule15_activation, self.memb_Zlozonosc_Niska)

        #
        # Reguła IF [tekst_do_obrazka IS wysokie] Or [nasilenie IS wysokie] Or [argumenty IS obustronne] Or [liczba_argumentow IS wysoka] Or [argumentacja IS racjonalna] THEN [zlozonosc IS wysoka]
        temp85 = self.foper.And(level_Argumentacja_Racjonalna, level_Tekst_do_obrazka_Wysokie)

        temp86 = self.foper.Or(level_Tekst_do_obrazka_Wysokie, level_Nasilenie_Wysokie)
        temp87 = self.foper.Or(temp86, level_Argumenty_Obustronne)
        temp88 = self.foper.Or(temp87, level_Liczba_argumentow_Wysoka)
        temp89 = self.foper.Or(temp88, level_Argumentacja_Racjonalna)
        temp90 = self.foper.Or(temp89, level_Tekst_do_obrazka_Wysokie)
        temp91 = self.foper.Or(temp90, level_Nasilenie_Wysokie)
        temp92 = self.foper.Or(temp91, level_Argumenty_Obustronne)
        temp93 = self.foper.Or(temp92, level_Liczba_argumentow_Wysoka)
        temp94 = self.foper.Or(temp93, temp85)
        temp95 = self.foper.Or(temp94, level_Nasilenie_Wysokie)
        temp96 = self.foper.Or(temp95, level_Argumenty_Obustronne)
        temp97 = self.foper.Or(temp96, level_Liczba_argumentow_Wysoka)
        temp98 = self.foper.Or(temp97, level_Argumentacja_Racjonalna)
        rule16_activation = temp98
        rule16_Zlozonosc_Wysoka = self.foper.Inference(rule16_activation, self.memb_Zlozonosc_Wysoka)

        #
        # Reguła IF [tekst_do_obrazka IS wysokie] And [nasilenie IS wysokie] And [argumenty IS obustronne] And [liczba_argumentow IS wysoka] And [argumentacja IS racjonalna] THEN [zlozonosc IS wysoka]
        temp99 = self.foper.And(level_Tekst_do_obrazka_Wysokie, level_Nasilenie_Wysokie)
        temp100 = self.foper.And(temp99, level_Argumenty_Obustronne)
        temp101 = self.foper.And(temp100, level_Liczba_argumentow_Wysoka)
        temp102 = self.foper.And(temp101, level_Argumentacja_Racjonalna)
        temp103 = self.foper.And(level_Tekst_do_obrazka_Wysokie, level_Nasilenie_Wysokie)
        temp104 = self.foper.And(temp103, level_Argumenty_Obustronne)
        temp105 = self.foper.And(temp104, level_Liczba_argumentow_Wysoka)
        temp106 = self.foper.And(temp105, level_Argumentacja_Racjonalna)
        temp107 = self.foper.And(temp106, level_Tekst_do_obrazka_Wysokie)
        temp108 = self.foper.And(temp107, level_Nasilenie_Wysokie)
        temp109 = self.foper.And(temp108, level_Argumenty_Obustronne)
        temp110 = self.foper.And(temp109, level_Liczba_argumentow_Wysoka)
        temp111 = self.foper.And(temp110, level_Argumentacja_Racjonalna)

        temp112 = self.foper.Or(temp102, temp111)
        rule17_activation = temp112
        rule17_Zlozonosc_Wysoka = self.foper.Inference(rule17_activation, self.memb_Zlozonosc_Wysoka)

        #
        # Reguła IF [tekst_do_obrazka IS niskie] And [nasilenie IS niskie] And [argumenty IS jednostronne] And [liczba_argumentow IS niska] And [argumentacja IS racjonalna] THEN [zlozonosc IS niska]
        temp113 = self.foper.And(level_Tekst_do_obrazka_Niskie, level_Nasilenie_Niskie)
        temp114 = self.foper.And(temp113, level_Argumenty_Jednostronne)
        temp115 = self.foper.And(temp114, level_Liczba_argumentow_Niska)
        temp116 = self.foper.And(temp115, level_Argumentacja_Racjonalna)
        temp117 = self.foper.And(level_Tekst_do_obrazka_Niskie, level_Nasilenie_Niskie)
        temp118 = self.foper.And(temp117, level_Argumenty_Jednostronne)
        temp119 = self.foper.And(temp118, level_Liczba_argumentow_Niska)
        temp120 = self.foper.And(temp119, level_Argumentacja_Racjonalna)
        temp121 = self.foper.And(temp120, level_Tekst_do_obrazka_Niskie)
        temp122 = self.foper.And(temp121, level_Nasilenie_Niskie)
        temp123 = self.foper.And(temp122, level_Argumenty_Jednostronne)
        temp124 = self.foper.And(temp123, level_Liczba_argumentow_Niska)
        temp125 = self.foper.And(temp124, level_Argumentacja_Racjonalna)

        temp126 = self.foper.Or(temp116, temp125)
        rule18_activation = temp126
        rule18_Zlozonosc_Niska = self.foper.Inference(rule18_activation, self.memb_Zlozonosc_Niska)

        #
        # Reguła IF [tekst_do_obrazka IS wysokie] And [nasilenie IS wysokie] THEN [zlozonosc IS wysoka]
        temp127 = self.foper.And(level_Tekst_do_obrazka_Wysokie, level_Nasilenie_Wysokie)
        temp128 = self.foper.And(level_Tekst_do_obrazka_Wysokie, level_Nasilenie_Wysokie)
        temp129 = self.foper.And(temp128, level_Tekst_do_obrazka_Wysokie)
        temp130 = self.foper.And(temp129, level_Nasilenie_Wysokie)

        temp131 = self.foper.Or(temp127, temp130)
        rule19_activation = temp131
        rule19_Zlozonosc_Wysoka = self.foper.Inference(rule19_activation, self.memb_Zlozonosc_Wysoka)

        #
        # Reguła IF [tekst_do_obrazka IS niskie] And [nasilenie IS niskie] THEN [zlozonosc IS niska]
        temp132 = self.foper.And(level_Tekst_do_obrazka_Niskie, level_Nasilenie_Niskie)
        temp133 = self.foper.And(level_Tekst_do_obrazka_Niskie, level_Nasilenie_Niskie)
        temp134 = self.foper.And(temp133, level_Tekst_do_obrazka_Niskie)
        temp135 = self.foper.And(temp134, level_Nasilenie_Niskie)

        temp136 = self.foper.Or(temp132, temp135)
        rule20_activation = temp136
        rule20_Zlozonosc_Niska = self.foper.Inference(rule20_activation, self.memb_Zlozonosc_Niska)

        #
        # Agregacja wyników wnioskowania w ramach tych samych wartości lingwistycznych zmiennych wyjściowych
        conclusion = self.foper.NeutralUnion(self.x_Zlozonosc)
        conclusion = self.foper.Union(conclusion, rule15_Zlozonosc_Niska)
        conclusion = self.foper.Union(conclusion, rule18_Zlozonosc_Niska)
        conclusion = self.foper.Union(conclusion, rule20_Zlozonosc_Niska)
        self.conclusion_Zlozonosc_Niska = conclusion
        conclusion = self.foper.NeutralUnion(self.x_Zlozonosc)
        conclusion = self.foper.Union(conclusion, rule16_Zlozonosc_Wysoka)
        conclusion = self.foper.Union(conclusion, rule17_Zlozonosc_Wysoka)
        conclusion = self.foper.Union(conclusion, rule19_Zlozonosc_Wysoka)
        self.conclusion_Zlozonosc_Wysoka = conclusion

        #
        # Wyostrzanie zmiennych wyjściowych
        aggregate = self.foper.NeutralAggregate(self.x_Zlozonosc)
        aggregate = self.foper.Aggregation(aggregate, self.conclusion_Zlozonosc_Niska)
        aggregate = self.foper.Aggregation(aggregate, self.conclusion_Zlozonosc_Wysoka)
        self.__aggregated_Zlozonosc = aggregate
        self.output_Zlozonosc = self.foper.Centroid(self.x_Zlozonosc, aggregate)

        #
        # przygotowanie słownika wyników
        result = dict(Zlozonosc = self.output_Zlozonosc)
        return result


    def ShowAllVariables(self):
        fig, axes = plt.subplots(nrows=5 + 1, figsize=(8, 3 * (5 + 1)))
        if not hasattr(axes, "__len__"):
            axes = [axes]

        axes[0].plot(self.x_Tekst_do_obrazka, self.memb_Tekst_do_obrazka_Niskie, 'blue', linewidth=1.5, label='niskie')
        axes[0].plot(self.x_Tekst_do_obrazka, self.memb_Tekst_do_obrazka_Wysokie, 'red', linewidth=1.5, label='wysokie')
        axes[0].set_title('WE: Description-6DD9A966')
        axes[0].legend()

        axes[1].plot(self.x_Nasilenie, self.memb_Nasilenie_Niskie, 'blue', linewidth=1.5, label='niskie')
        axes[1].plot(self.x_Nasilenie, self.memb_Nasilenie_Wysokie, 'red', linewidth=1.5, label='wysokie')
        axes[1].set_title('WE: Description-6DD9A966')
        axes[1].legend()

        axes[2].plot(self.x_Argumenty, self.memb_Argumenty_Jednostronne, 'blue', linewidth=1.5, label='jednostronne')
        axes[2].plot(self.x_Argumenty, self.memb_Argumenty_Obustronne, 'red', linewidth=1.5, label='obustronne')
        axes[2].set_title('WE: Description-6DD9A966')
        axes[2].legend()

        axes[3].plot(self.x_Liczba_argumentow, self.memb_Liczba_argumentow_Niska, 'blue', linewidth=1.5, label='niska')
        axes[3].plot(self.x_Liczba_argumentow, self.memb_Liczba_argumentow_Wysoka, 'red', linewidth=1.5, label='wysoka')
        axes[3].set_title('WE: Description-6DD9A966')
        axes[3].legend()

        axes[4].plot(self.x_Argumentacja, self.memb_Argumentacja_Racjonalna, 'blue', linewidth=1.5, label='racjonalna')
        axes[4].plot(self.x_Argumentacja, self.memb_Argumentacja_Irracjonalna, 'red', linewidth=1.5, label='irracjonalna')
        axes[4].set_title('WE: Description-6DD9A966')
        axes[4].legend()

        axes[5+0].plot(self.x_Zlozonosc, self.memb_Zlozonosc_Niska, 'blue', linewidth=1.5, label='niska')
        axes[5+0].plot(self.x_Zlozonosc, self.memb_Zlozonosc_Wysoka, 'red', linewidth=1.5, label='wysoka')
        axes[5+0].set_title('WY: Description-6DD9A966')
        axes[5+0].legend()

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

        axes[0].fill_between(self.x_Zlozonosc, np.zeros_like(self.x_Zlozonosc), self.conclusion_Zlozonosc_Niska, facecolor='blue', alpha=0.5)
        axes[0].plot(self.x_Zlozonosc, self.memb_Zlozonosc_Niska, 'blue', linewidth=0.5, linestyle='--', )
        axes[0].fill_between(self.x_Zlozonosc, np.zeros_like(self.x_Zlozonosc), self.conclusion_Zlozonosc_Wysoka, facecolor='red', alpha=0.5)
        axes[0].plot(self.x_Zlozonosc, self.memb_Zlozonosc_Wysoka, 'red', linewidth=0.5, linestyle='--', )

        memb = fuzz.interp_membership(self.x_Zlozonosc, self.__aggregated_Zlozonosc, self.output_Zlozonosc)
        axes[0].plot([self.output_Zlozonosc]*2, [0, memb], 'k', linewidth=3, alpha=0.9)
        axes[0].set_title('Description-6DD9A966')

        for ax in axes:
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.get_xaxis().tick_bottom()
            ax.get_yaxis().tick_left()

        plt.tight_layout()
        plt.show()


##
## Model: 'produkt_zaangazowanie'
## Opis:  Description-225FCD6F
##
class Model_Produkt_zaangazowanie(object):
    foper = None #type: FuzzyOperation

    # Wartości ostre dla zmiennych wejściowych
    input_Produkt_zaangazowanie = None # type: float # Zmienna: produkt_zaangazowanie
    input_Warianty = None # type: float # Zmienna: warianty
    input_Indywidualizacja = None # type: float # Zmienna: indywidualizacja

    # Wartości ostre dla zmiennych wyjściowych
    output_Zlozonosc = None # type: float # Zmienna: zlozonosc

    # Dziedziny zmiennych rozmytych
    x_Produkt_zaangazowanie = None # type: Union[List[float], np.ndarray]
    x_Warianty = None # type: Union[List[float], np.ndarray]
    x_Indywidualizacja = None # type: Union[List[float], np.ndarray]
    x_Zlozonosc = None # type: Union[List[float], np.ndarray]

    # Wartości przynależności
    memb_Produkt_zaangazowanie_Niska = None # type: Union[List[float], np.ndarray]
    memb_Produkt_zaangazowanie_Srednia = None # type: Union[List[float], np.ndarray]
    memb_Produkt_zaangazowanie_Wysoka = None # type: Union[List[float], np.ndarray]
    memb_Warianty_Niska = None # type: Union[List[float], np.ndarray]
    memb_Warianty_Srednia = None # type: Union[List[float], np.ndarray]
    memb_Warianty_Wysoka = None # type: Union[List[float], np.ndarray]
    memb_Indywidualizacja_Niska = None # type: Union[List[float], np.ndarray]
    memb_Indywidualizacja_Srednia = None # type: Union[List[float], np.ndarray]
    memb_Indywidualizacja_Wysoka = None # type: Union[List[float], np.ndarray]
    memb_Zlozonosc_Niska = None # type: Union[List[float], np.ndarray]
    memb_Zlozonosc_Wysoka = None # type: Union[List[float], np.ndarray]

    def __init__(self):
        self.foper = FuzzyOperation()

        self.InitDomain()
        self.InitVariables()
#       self.ShowVariables()

    def InitDomain(self):
        x_step = 0.01
        self.x_Produkt_zaangazowanie = np.arange(0.0000, 10.0000, x_step) # produkt_zaangazowanie: Description-7E5A204B
        self.x_Warianty = np.arange(0.0000, 10.0000, x_step) # warianty: Description-7E5A204B
        self.x_Indywidualizacja = np.arange(0.0000, 10.0000, x_step) # indywidualizacja: Description-7E5A204B
        self.x_Zlozonosc = np.arange(0.0000, 10.0000, x_step) # zlozonosc: Description-6DD9A966

    def InitVariables(self):

        # Wejście: produkt_zaangazowanie
        self.memb_Produkt_zaangazowanie_Niska = fuzz.trapmf(self.x_Produkt_zaangazowanie, [0.0000, 0.0000, 1.0000, 5.0000])
        self.memb_Produkt_zaangazowanie_Srednia = fuzz.trapmf(self.x_Produkt_zaangazowanie, [1.0000, 5.0000, 5.0000, 9.0000])
        self.memb_Produkt_zaangazowanie_Wysoka = fuzz.trapmf(self.x_Produkt_zaangazowanie, [5.0000, 9.0000, 10.0000, 10.0000])

        # Wejście: warianty
        self.memb_Warianty_Niska = fuzz.trapmf(self.x_Warianty, [0.0000, 0.0000, 1.0000, 5.0000])
        self.memb_Warianty_Srednia = fuzz.trapmf(self.x_Warianty, [1.0000, 5.0000, 5.0000, 9.0000])
        self.memb_Warianty_Wysoka = fuzz.trapmf(self.x_Warianty, [5.0000, 9.0000, 10.0000, 10.0000])

        # Wejście: indywidualizacja
        self.memb_Indywidualizacja_Niska = fuzz.trapmf(self.x_Indywidualizacja, [0.0000, 0.0000, 1.0000, 5.0000])
        self.memb_Indywidualizacja_Srednia = fuzz.trapmf(self.x_Indywidualizacja, [1.0000, 5.0000, 5.0000, 9.0000])
        self.memb_Indywidualizacja_Wysoka = fuzz.trapmf(self.x_Indywidualizacja, [5.0000, 9.0000, 10.0000, 10.0000])

        # Wyjście: zlozonosc
        self.memb_Zlozonosc_Niska = fuzz.trapmf(self.x_Zlozonosc, [0.0000, 0.0000, 1.0000, 9.0000])
        self.memb_Zlozonosc_Wysoka = fuzz.trapmf(self.x_Zlozonosc, [1.0000, 9.0000, 10.0000, 10.0000])

    def Execute(self, input_Produkt_zaangazowanie: float, input_Warianty: float, input_Indywidualizacja: float):
        self.input_Produkt_zaangazowanie = input_Produkt_zaangazowanie
        self.input_Warianty = input_Warianty
        self.input_Indywidualizacja = input_Indywidualizacja

        # Wyznacz poziomy przynależności
        level_Produkt_zaangazowanie_Niska = fuzz.interp_membership(self.x_Produkt_zaangazowanie, self.memb_Produkt_zaangazowanie_Niska, self.input_Produkt_zaangazowanie)
        level_Produkt_zaangazowanie_Srednia = fuzz.interp_membership(self.x_Produkt_zaangazowanie, self.memb_Produkt_zaangazowanie_Srednia, self.input_Produkt_zaangazowanie)
        level_Produkt_zaangazowanie_Wysoka = fuzz.interp_membership(self.x_Produkt_zaangazowanie, self.memb_Produkt_zaangazowanie_Wysoka, self.input_Produkt_zaangazowanie)
        level_Warianty_Niska = fuzz.interp_membership(self.x_Warianty, self.memb_Warianty_Niska, self.input_Warianty)
        level_Warianty_Srednia = fuzz.interp_membership(self.x_Warianty, self.memb_Warianty_Srednia, self.input_Warianty)
        level_Warianty_Wysoka = fuzz.interp_membership(self.x_Warianty, self.memb_Warianty_Wysoka, self.input_Warianty)
        level_Indywidualizacja_Niska = fuzz.interp_membership(self.x_Indywidualizacja, self.memb_Indywidualizacja_Niska, self.input_Indywidualizacja)
        level_Indywidualizacja_Srednia = fuzz.interp_membership(self.x_Indywidualizacja, self.memb_Indywidualizacja_Srednia, self.input_Indywidualizacja)
        level_Indywidualizacja_Wysoka = fuzz.interp_membership(self.x_Indywidualizacja, self.memb_Indywidualizacja_Wysoka, self.input_Indywidualizacja)

        #
        # Tutaj wnioskowanie ....

        #
        # Reguła IF [produkt_zaangazowanie IS wysoka] Or [warianty IS wysoka] Or [indywidualizacja IS wysoka] THEN [zlozonosc IS wysoka]
        temp137 = self.foper.And(level_Indywidualizacja_Wysoka, level_Produkt_zaangazowanie_Wysoka)

        temp138 = self.foper.Or(level_Produkt_zaangazowanie_Wysoka, level_Warianty_Wysoka)
        temp139 = self.foper.Or(temp138, level_Indywidualizacja_Wysoka)
        temp140 = self.foper.Or(temp139, level_Produkt_zaangazowanie_Wysoka)
        temp141 = self.foper.Or(temp140, level_Warianty_Wysoka)
        temp142 = self.foper.Or(temp141, temp137)
        temp143 = self.foper.Or(temp142, level_Warianty_Wysoka)
        temp144 = self.foper.Or(temp143, level_Indywidualizacja_Wysoka)
        rule21_activation = temp144
        rule21_Zlozonosc_Wysoka = self.foper.Inference(rule21_activation, self.memb_Zlozonosc_Wysoka)

        #
        # Reguła IF [produkt_zaangazowanie IS niska] Or [warianty IS niska] Or [indywidualizacja IS niska] THEN [zlozonosc IS niska]
        temp145 = self.foper.And(level_Indywidualizacja_Niska, level_Produkt_zaangazowanie_Niska)

        temp146 = self.foper.Or(level_Produkt_zaangazowanie_Niska, level_Warianty_Niska)
        temp147 = self.foper.Or(temp146, level_Indywidualizacja_Niska)
        temp148 = self.foper.Or(temp147, level_Produkt_zaangazowanie_Niska)
        temp149 = self.foper.Or(temp148, level_Warianty_Niska)
        temp150 = self.foper.Or(temp149, temp145)
        temp151 = self.foper.Or(temp150, level_Warianty_Niska)
        temp152 = self.foper.Or(temp151, level_Indywidualizacja_Niska)
        rule22_activation = temp152
        rule22_Zlozonosc_Niska = self.foper.Inference(rule22_activation, self.memb_Zlozonosc_Niska)

        #
        # Reguła IF [produkt_zaangazowanie IS srednia] Or [warianty IS srednia] Or [indywidualizacja IS srednia] THEN [zlozonosc IS niska]
        temp153 = self.foper.And(level_Indywidualizacja_Srednia, level_Produkt_zaangazowanie_Srednia)

        temp154 = self.foper.Or(level_Produkt_zaangazowanie_Srednia, level_Warianty_Srednia)
        temp155 = self.foper.Or(temp154, level_Indywidualizacja_Srednia)
        temp156 = self.foper.Or(temp155, level_Produkt_zaangazowanie_Srednia)
        temp157 = self.foper.Or(temp156, level_Warianty_Srednia)
        temp158 = self.foper.Or(temp157, temp153)
        temp159 = self.foper.Or(temp158, level_Warianty_Srednia)
        temp160 = self.foper.Or(temp159, level_Indywidualizacja_Srednia)
        rule23_activation = temp160
        rule23_Zlozonosc_Niska = self.foper.Inference(rule23_activation, self.memb_Zlozonosc_Niska)

        #
        # Reguła IF [produkt_zaangazowanie IS niska] And [warianty IS niska] And [indywidualizacja IS niska] THEN [zlozonosc IS niska]
        temp161 = self.foper.And(level_Produkt_zaangazowanie_Niska, level_Warianty_Niska)
        temp162 = self.foper.And(temp161, level_Indywidualizacja_Niska)
        temp163 = self.foper.And(level_Produkt_zaangazowanie_Niska, level_Warianty_Niska)
        temp164 = self.foper.And(temp163, level_Indywidualizacja_Niska)
        temp165 = self.foper.And(temp164, level_Produkt_zaangazowanie_Niska)
        temp166 = self.foper.And(temp165, level_Warianty_Niska)
        temp167 = self.foper.And(temp166, level_Indywidualizacja_Niska)

        temp168 = self.foper.Or(temp162, temp167)
        rule24_activation = temp168
        rule24_Zlozonosc_Niska = self.foper.Inference(rule24_activation, self.memb_Zlozonosc_Niska)

        #
        # Reguła IF [produkt_zaangazowanie IS wysoka] And [warianty IS wysoka] And [indywidualizacja IS wysoka] THEN [zlozonosc IS wysoka]
        temp169 = self.foper.And(level_Produkt_zaangazowanie_Wysoka, level_Warianty_Wysoka)
        temp170 = self.foper.And(temp169, level_Indywidualizacja_Wysoka)
        temp171 = self.foper.And(level_Produkt_zaangazowanie_Wysoka, level_Warianty_Wysoka)
        temp172 = self.foper.And(temp171, level_Indywidualizacja_Wysoka)
        temp173 = self.foper.And(temp172, level_Produkt_zaangazowanie_Wysoka)
        temp174 = self.foper.And(temp173, level_Warianty_Wysoka)
        temp175 = self.foper.And(temp174, level_Indywidualizacja_Wysoka)

        temp176 = self.foper.Or(temp170, temp175)
        rule25_activation = temp176
        rule25_Zlozonosc_Wysoka = self.foper.Inference(rule25_activation, self.memb_Zlozonosc_Wysoka)

        #
        # Reguła IF [warianty IS wysoka] And [indywidualizacja IS wysoka] THEN [zlozonosc IS wysoka]
        temp177 = self.foper.And(level_Warianty_Wysoka, level_Indywidualizacja_Wysoka)
        temp178 = self.foper.And(level_Warianty_Wysoka, level_Indywidualizacja_Wysoka)
        temp179 = self.foper.And(temp178, level_Warianty_Wysoka)
        temp180 = self.foper.And(temp179, level_Indywidualizacja_Wysoka)

        temp181 = self.foper.Or(temp177, temp180)
        rule26_activation = temp181
        rule26_Zlozonosc_Wysoka = self.foper.Inference(rule26_activation, self.memb_Zlozonosc_Wysoka)

        #
        # Reguła IF [produkt_zaangazowanie IS niska] And [indywidualizacja IS niska] THEN [zlozonosc IS niska]
        temp182 = self.foper.And(level_Produkt_zaangazowanie_Niska, level_Indywidualizacja_Niska)
        temp183 = self.foper.And(level_Produkt_zaangazowanie_Niska, level_Indywidualizacja_Niska)
        temp184 = self.foper.And(temp183, level_Produkt_zaangazowanie_Niska)
        temp185 = self.foper.And(temp184, level_Indywidualizacja_Niska)

        temp186 = self.foper.Or(temp182, temp185)
        rule27_activation = temp186
        rule27_Zlozonosc_Niska = self.foper.Inference(rule27_activation, self.memb_Zlozonosc_Niska)

        #
        # Agregacja wyników wnioskowania w ramach tych samych wartości lingwistycznych zmiennych wyjściowych
        conclusion = self.foper.NeutralUnion(self.x_Zlozonosc)
        conclusion = self.foper.Union(conclusion, rule21_Zlozonosc_Wysoka)
        conclusion = self.foper.Union(conclusion, rule25_Zlozonosc_Wysoka)
        conclusion = self.foper.Union(conclusion, rule26_Zlozonosc_Wysoka)
        self.conclusion_Zlozonosc_Wysoka = conclusion
        conclusion = self.foper.NeutralUnion(self.x_Zlozonosc)
        conclusion = self.foper.Union(conclusion, rule22_Zlozonosc_Niska)
        conclusion = self.foper.Union(conclusion, rule23_Zlozonosc_Niska)
        conclusion = self.foper.Union(conclusion, rule24_Zlozonosc_Niska)
        conclusion = self.foper.Union(conclusion, rule27_Zlozonosc_Niska)
        self.conclusion_Zlozonosc_Niska = conclusion

        #
        # Wyostrzanie zmiennych wyjściowych
        aggregate = self.foper.NeutralAggregate(self.x_Zlozonosc)
        aggregate = self.foper.Aggregation(aggregate, self.conclusion_Zlozonosc_Niska)
        aggregate = self.foper.Aggregation(aggregate, self.conclusion_Zlozonosc_Wysoka)
        self.__aggregated_Zlozonosc = aggregate
        self.output_Zlozonosc = self.foper.Centroid(self.x_Zlozonosc, aggregate)

        #
        # przygotowanie słownika wyników
        result = dict(Zlozonosc = self.output_Zlozonosc)
        return result


    def ShowAllVariables(self):
        fig, axes = plt.subplots(nrows=3 + 1, figsize=(8, 3 * (3 + 1)))
        if not hasattr(axes, "__len__"):
            axes = [axes]

        axes[0].plot(self.x_Produkt_zaangazowanie, self.memb_Produkt_zaangazowanie_Niska, 'blue', linewidth=1.5, label='niska')
        axes[0].plot(self.x_Produkt_zaangazowanie, self.memb_Produkt_zaangazowanie_Srednia, 'red', linewidth=1.5, label='srednia')
        axes[0].plot(self.x_Produkt_zaangazowanie, self.memb_Produkt_zaangazowanie_Wysoka, 'green', linewidth=1.5, label='wysoka')
        axes[0].set_title('WE: Description-7E5A204B')
        axes[0].legend()

        axes[1].plot(self.x_Warianty, self.memb_Warianty_Niska, 'blue', linewidth=1.5, label='niska')
        axes[1].plot(self.x_Warianty, self.memb_Warianty_Srednia, 'red', linewidth=1.5, label='srednia')
        axes[1].plot(self.x_Warianty, self.memb_Warianty_Wysoka, 'green', linewidth=1.5, label='wysoka')
        axes[1].set_title('WE: Description-7E5A204B')
        axes[1].legend()

        axes[2].plot(self.x_Indywidualizacja, self.memb_Indywidualizacja_Niska, 'blue', linewidth=1.5, label='niska')
        axes[2].plot(self.x_Indywidualizacja, self.memb_Indywidualizacja_Srednia, 'red', linewidth=1.5, label='srednia')
        axes[2].plot(self.x_Indywidualizacja, self.memb_Indywidualizacja_Wysoka, 'green', linewidth=1.5, label='wysoka')
        axes[2].set_title('WE: Description-7E5A204B')
        axes[2].legend()

        axes[3+0].plot(self.x_Zlozonosc, self.memb_Zlozonosc_Niska, 'blue', linewidth=1.5, label='niska')
        axes[3+0].plot(self.x_Zlozonosc, self.memb_Zlozonosc_Wysoka, 'red', linewidth=1.5, label='wysoka')
        axes[3+0].set_title('WY: Description-6DD9A966')
        axes[3+0].legend()

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

        axes[0].fill_between(self.x_Zlozonosc, np.zeros_like(self.x_Zlozonosc), self.conclusion_Zlozonosc_Niska, facecolor='blue', alpha=0.5)
        axes[0].plot(self.x_Zlozonosc, self.memb_Zlozonosc_Niska, 'blue', linewidth=0.5, linestyle='--', )
        axes[0].fill_between(self.x_Zlozonosc, np.zeros_like(self.x_Zlozonosc), self.conclusion_Zlozonosc_Wysoka, facecolor='red', alpha=0.5)
        axes[0].plot(self.x_Zlozonosc, self.memb_Zlozonosc_Wysoka, 'red', linewidth=0.5, linestyle='--', )

        memb = fuzz.interp_membership(self.x_Zlozonosc, self.__aggregated_Zlozonosc, self.output_Zlozonosc)
        axes[0].plot([self.output_Zlozonosc]*2, [0, memb], 'k', linewidth=3, alpha=0.9)
        axes[0].set_title('Description-6DD9A966')

        for ax in axes:
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.get_xaxis().tick_bottom()
            ax.get_yaxis().tick_left()

        plt.tight_layout()
        plt.show()


##
## Model: 'uzytkownik_zachowanie'
## Opis:  Description-539938E7
##
class Model_Uzytkownik_zachowanie(object):
    foper = None #type: FuzzyOperation

    # Wartości ostre dla zmiennych wejściowych
    input_Czas_podjecia_decyzji = None # type: float # Zmienna: czas_podjecia_decyzji
    input_Proporcja = None # type: float # Zmienna: proporcja
    input_Czestotliwosc = None # type: float # Zmienna: czestotliwosc
    input_Produkty_same = None # type: float # Zmienna: produkty_same
    input_Produkty_inne = None # type: float # Zmienna: produkty_inne

    # Wartości ostre dla zmiennych wyjściowych
    output_Uzytkownik_zachowanie = None # type: float # Zmienna: uzytkownik_zachowanie

    # Dziedziny zmiennych rozmytych
    x_Czas_podjecia_decyzji = None # type: Union[List[float], np.ndarray]
    x_Proporcja = None # type: Union[List[float], np.ndarray]
    x_Czestotliwosc = None # type: Union[List[float], np.ndarray]
    x_Produkty_same = None # type: Union[List[float], np.ndarray]
    x_Produkty_inne = None # type: Union[List[float], np.ndarray]
    x_Uzytkownik_zachowanie = None # type: Union[List[float], np.ndarray]

    # Wartości przynależności
    memb_Czas_podjecia_decyzji_Niska = None # type: Union[List[float], np.ndarray]
    memb_Czas_podjecia_decyzji_Srednia = None # type: Union[List[float], np.ndarray]
    memb_Czas_podjecia_decyzji_Wysoka = None # type: Union[List[float], np.ndarray]
    memb_Proporcja_Niska = None # type: Union[List[float], np.ndarray]
    memb_Proporcja_Srednia = None # type: Union[List[float], np.ndarray]
    memb_Proporcja_Wysoka = None # type: Union[List[float], np.ndarray]
    memb_Czestotliwosc_Niska = None # type: Union[List[float], np.ndarray]
    memb_Czestotliwosc_Srednia = None # type: Union[List[float], np.ndarray]
    memb_Czestotliwosc_Wysoka = None # type: Union[List[float], np.ndarray]
    memb_Produkty_same_Niska = None # type: Union[List[float], np.ndarray]
    memb_Produkty_same_Srednia = None # type: Union[List[float], np.ndarray]
    memb_Produkty_same_Wysoka = None # type: Union[List[float], np.ndarray]
    memb_Produkty_inne_Niska = None # type: Union[List[float], np.ndarray]
    memb_Produkty_inne_Srednia = None # type: Union[List[float], np.ndarray]
    memb_Produkty_inne_Wysoka = None # type: Union[List[float], np.ndarray]
    memb_Uzytkownik_zachowanie_Maksymalizm = None # type: Union[List[float], np.ndarray]
    memb_Uzytkownik_zachowanie_Satysfakcja = None # type: Union[List[float], np.ndarray]

    def __init__(self):
        self.foper = FuzzyOperation()

        self.InitDomain()
        self.InitVariables()
#       self.ShowVariables()

    def InitDomain(self):
        x_step = 0.01
        self.x_Czas_podjecia_decyzji = np.arange(0.0000, 10.0000, x_step) # czas_podjecia_decyzji: Description-7E5A204B
        self.x_Proporcja = np.arange(0.0000, 10.0000, x_step) # proporcja: Description-7E5A204B
        self.x_Czestotliwosc = np.arange(0.0000, 10.0000, x_step) # czestotliwosc: Description-7E5A204B
        self.x_Produkty_same = np.arange(0.0000, 10.0000, x_step) # produkty_same: Description-7E5A204B
        self.x_Produkty_inne = np.arange(0.0000, 10.0000, x_step) # produkty_inne: Description-7E5A204B
        self.x_Uzytkownik_zachowanie = np.arange(0.0000, 10.0000, x_step) # uzytkownik_zachowanie: Description-60E2D9B8

    def InitVariables(self):

        # Wejście: czas_podjecia_decyzji
        self.memb_Czas_podjecia_decyzji_Niska = fuzz.trapmf(self.x_Czas_podjecia_decyzji, [0.0000, 0.0000, 1.0000, 5.0000])
        self.memb_Czas_podjecia_decyzji_Srednia = fuzz.trapmf(self.x_Czas_podjecia_decyzji, [1.0000, 5.0000, 5.0000, 9.0000])
        self.memb_Czas_podjecia_decyzji_Wysoka = fuzz.trapmf(self.x_Czas_podjecia_decyzji, [5.0000, 9.0000, 10.0000, 10.0000])

        # Wejście: proporcja
        self.memb_Proporcja_Niska = fuzz.trapmf(self.x_Proporcja, [0.0000, 0.0000, 1.0000, 5.0000])
        self.memb_Proporcja_Srednia = fuzz.trapmf(self.x_Proporcja, [1.0000, 5.0000, 5.0000, 9.0000])
        self.memb_Proporcja_Wysoka = fuzz.trapmf(self.x_Proporcja, [5.0000, 9.0000, 10.0000, 10.0000])

        # Wejście: czestotliwosc
        self.memb_Czestotliwosc_Niska = fuzz.trapmf(self.x_Czestotliwosc, [0.0000, 0.0000, 1.0000, 5.0000])
        self.memb_Czestotliwosc_Srednia = fuzz.trapmf(self.x_Czestotliwosc, [1.0000, 5.0000, 5.0000, 9.0000])
        self.memb_Czestotliwosc_Wysoka = fuzz.trapmf(self.x_Czestotliwosc, [5.0000, 9.0000, 10.0000, 10.0000])

        # Wejście: produkty_same
        self.memb_Produkty_same_Niska = fuzz.trapmf(self.x_Produkty_same, [0.0000, 0.0000, 1.0000, 5.0000])
        self.memb_Produkty_same_Srednia = fuzz.trapmf(self.x_Produkty_same, [1.0000, 5.0000, 5.0000, 9.0000])
        self.memb_Produkty_same_Wysoka = fuzz.trapmf(self.x_Produkty_same, [5.0000, 9.0000, 10.0000, 10.0000])

        # Wejście: produkty_inne
        self.memb_Produkty_inne_Niska = fuzz.trapmf(self.x_Produkty_inne, [0.0000, 0.0000, 1.0000, 5.0000])
        self.memb_Produkty_inne_Srednia = fuzz.trapmf(self.x_Produkty_inne, [1.0000, 5.0000, 5.0000, 9.0000])
        self.memb_Produkty_inne_Wysoka = fuzz.trapmf(self.x_Produkty_inne, [5.0000, 9.0000, 10.0000, 10.0000])

        # Wyjście: uzytkownik_zachowanie
        self.memb_Uzytkownik_zachowanie_Maksymalizm = fuzz.trapmf(self.x_Uzytkownik_zachowanie, [0.0000, 0.0000, 3.0000, 7.0000])
        self.memb_Uzytkownik_zachowanie_Satysfakcja = fuzz.trapmf(self.x_Uzytkownik_zachowanie, [3.0000, 7.0000, 10.0000, 10.0000])

    def Execute(self, input_Czas_podjecia_decyzji: float, input_Proporcja: float, input_Czestotliwosc: float, input_Produkty_same: float, input_Produkty_inne: float):
        self.input_Czas_podjecia_decyzji = input_Czas_podjecia_decyzji
        self.input_Proporcja = input_Proporcja
        self.input_Czestotliwosc = input_Czestotliwosc
        self.input_Produkty_same = input_Produkty_same
        self.input_Produkty_inne = input_Produkty_inne

        # Wyznacz poziomy przynależności
        level_Czas_podjecia_decyzji_Niska = fuzz.interp_membership(self.x_Czas_podjecia_decyzji, self.memb_Czas_podjecia_decyzji_Niska, self.input_Czas_podjecia_decyzji)
        level_Czas_podjecia_decyzji_Srednia = fuzz.interp_membership(self.x_Czas_podjecia_decyzji, self.memb_Czas_podjecia_decyzji_Srednia, self.input_Czas_podjecia_decyzji)
        level_Czas_podjecia_decyzji_Wysoka = fuzz.interp_membership(self.x_Czas_podjecia_decyzji, self.memb_Czas_podjecia_decyzji_Wysoka, self.input_Czas_podjecia_decyzji)
        level_Proporcja_Niska = fuzz.interp_membership(self.x_Proporcja, self.memb_Proporcja_Niska, self.input_Proporcja)
        level_Proporcja_Srednia = fuzz.interp_membership(self.x_Proporcja, self.memb_Proporcja_Srednia, self.input_Proporcja)
        level_Proporcja_Wysoka = fuzz.interp_membership(self.x_Proporcja, self.memb_Proporcja_Wysoka, self.input_Proporcja)
        level_Czestotliwosc_Niska = fuzz.interp_membership(self.x_Czestotliwosc, self.memb_Czestotliwosc_Niska, self.input_Czestotliwosc)
        level_Czestotliwosc_Srednia = fuzz.interp_membership(self.x_Czestotliwosc, self.memb_Czestotliwosc_Srednia, self.input_Czestotliwosc)
        level_Czestotliwosc_Wysoka = fuzz.interp_membership(self.x_Czestotliwosc, self.memb_Czestotliwosc_Wysoka, self.input_Czestotliwosc)
        level_Produkty_same_Niska = fuzz.interp_membership(self.x_Produkty_same, self.memb_Produkty_same_Niska, self.input_Produkty_same)
        level_Produkty_same_Srednia = fuzz.interp_membership(self.x_Produkty_same, self.memb_Produkty_same_Srednia, self.input_Produkty_same)
        level_Produkty_same_Wysoka = fuzz.interp_membership(self.x_Produkty_same, self.memb_Produkty_same_Wysoka, self.input_Produkty_same)
        level_Produkty_inne_Niska = fuzz.interp_membership(self.x_Produkty_inne, self.memb_Produkty_inne_Niska, self.input_Produkty_inne)
        level_Produkty_inne_Srednia = fuzz.interp_membership(self.x_Produkty_inne, self.memb_Produkty_inne_Srednia, self.input_Produkty_inne)
        level_Produkty_inne_Wysoka = fuzz.interp_membership(self.x_Produkty_inne, self.memb_Produkty_inne_Wysoka, self.input_Produkty_inne)

        #
        # Tutaj wnioskowanie ....

        #
        # Reguła IF [czas_podjecia_decyzji IS wysoka] Or [proporcja IS wysoka] Or [czestotliwosc IS wysoka] THEN [uzytkownik_zachowanie IS maksymalizm]
        temp187 = self.foper.And(level_Czestotliwosc_Wysoka, level_Czas_podjecia_decyzji_Wysoka)

        temp188 = self.foper.Or(level_Czas_podjecia_decyzji_Wysoka, level_Proporcja_Wysoka)
        temp189 = self.foper.Or(temp188, level_Czestotliwosc_Wysoka)
        temp190 = self.foper.Or(temp189, level_Czas_podjecia_decyzji_Wysoka)
        temp191 = self.foper.Or(temp190, level_Proporcja_Wysoka)
        temp192 = self.foper.Or(temp191, temp187)
        temp193 = self.foper.Or(temp192, level_Proporcja_Wysoka)
        temp194 = self.foper.Or(temp193, level_Czestotliwosc_Wysoka)
        rule28_activation = temp194
        rule28_Uzytkownik_zachowanie_Maksymalizm = self.foper.Inference(rule28_activation, self.memb_Uzytkownik_zachowanie_Maksymalizm)

        #
        # Reguła IF [czas_podjecia_decyzji IS niska] Or [proporcja IS niska] Or [czestotliwosc IS niska] THEN [uzytkownik_zachowanie IS satysfakcja]
        temp195 = self.foper.And(level_Czestotliwosc_Niska, level_Czas_podjecia_decyzji_Niska)

        temp196 = self.foper.Or(level_Czas_podjecia_decyzji_Niska, level_Proporcja_Niska)
        temp197 = self.foper.Or(temp196, level_Czestotliwosc_Niska)
        temp198 = self.foper.Or(temp197, level_Czas_podjecia_decyzji_Niska)
        temp199 = self.foper.Or(temp198, level_Proporcja_Niska)
        temp200 = self.foper.Or(temp199, temp195)
        temp201 = self.foper.Or(temp200, level_Proporcja_Niska)
        temp202 = self.foper.Or(temp201, level_Czestotliwosc_Niska)
        rule29_activation = temp202
        rule29_Uzytkownik_zachowanie_Satysfakcja = self.foper.Inference(rule29_activation, self.memb_Uzytkownik_zachowanie_Satysfakcja)

        #
        # Reguła IF [produkty_same IS niska] And [produkty_inne IS niska] THEN [uzytkownik_zachowanie IS satysfakcja]
        temp203 = self.foper.And(level_Produkty_same_Niska, level_Produkty_inne_Niska)
        temp204 = self.foper.And(level_Produkty_same_Niska, level_Produkty_inne_Niska)
        temp205 = self.foper.And(temp204, level_Produkty_same_Niska)
        temp206 = self.foper.And(temp205, level_Produkty_inne_Niska)

        temp207 = self.foper.Or(temp203, temp206)
        rule30_activation = temp207
        rule30_Uzytkownik_zachowanie_Satysfakcja = self.foper.Inference(rule30_activation, self.memb_Uzytkownik_zachowanie_Satysfakcja)

        #
        # Reguła IF [produkty_same IS srednia] And [produkty_inne IS srednia] THEN [uzytkownik_zachowanie IS satysfakcja]
        temp208 = self.foper.And(level_Produkty_same_Srednia, level_Produkty_inne_Srednia)
        temp209 = self.foper.And(level_Produkty_same_Srednia, level_Produkty_inne_Srednia)
        temp210 = self.foper.And(temp209, level_Produkty_same_Srednia)
        temp211 = self.foper.And(temp210, level_Produkty_inne_Srednia)

        temp212 = self.foper.Or(temp208, temp211)
        rule31_activation = temp212
        rule31_Uzytkownik_zachowanie_Satysfakcja = self.foper.Inference(rule31_activation, self.memb_Uzytkownik_zachowanie_Satysfakcja)

        #
        # Reguła IF [produkty_same IS wysoka ] And [produkty_inne IS wysoka ] THEN [uzytkownik_zachowanie IS maksymalizm]
        temp213 = self.foper.And(level_Produkty_same_Wysoka, level_Produkty_inne_Wysoka)
        temp214 = self.foper.And(level_Produkty_same_Wysoka, level_Produkty_inne_Wysoka)
        temp215 = self.foper.And(temp214, level_Produkty_same_Wysoka)
        temp216 = self.foper.And(temp215, level_Produkty_inne_Wysoka)

        temp217 = self.foper.Or(temp213, temp216)
        rule32_activation = temp217
        rule32_Uzytkownik_zachowanie_Maksymalizm = self.foper.Inference(rule32_activation, self.memb_Uzytkownik_zachowanie_Maksymalizm)

        #
        # Reguła IF [produkty_same IS wysoka ] And [produkty_inne IS niska] THEN [uzytkownik_zachowanie IS maksymalizm]
        temp218 = self.foper.And(level_Produkty_same_Wysoka, level_Produkty_inne_Niska)
        temp219 = self.foper.And(level_Produkty_same_Wysoka, level_Produkty_inne_Niska)
        temp220 = self.foper.And(temp219, level_Produkty_same_Wysoka)
        temp221 = self.foper.And(temp220, level_Produkty_inne_Niska)

        temp222 = self.foper.Or(temp218, temp221)
        rule33_activation = temp222
        rule33_Uzytkownik_zachowanie_Maksymalizm = self.foper.Inference(rule33_activation, self.memb_Uzytkownik_zachowanie_Maksymalizm)

        #
        # Reguła IF [produkty_same IS wysoka ] And [produkty_inne IS srednia] THEN [uzytkownik_zachowanie IS maksymalizm]
        temp223 = self.foper.And(level_Produkty_same_Wysoka, level_Produkty_inne_Srednia)
        temp224 = self.foper.And(level_Produkty_same_Wysoka, level_Produkty_inne_Srednia)
        temp225 = self.foper.And(temp224, level_Produkty_same_Wysoka)
        temp226 = self.foper.And(temp225, level_Produkty_inne_Srednia)

        temp227 = self.foper.Or(temp223, temp226)
        rule34_activation = temp227
        rule34_Uzytkownik_zachowanie_Maksymalizm = self.foper.Inference(rule34_activation, self.memb_Uzytkownik_zachowanie_Maksymalizm)

        #
        # Agregacja wyników wnioskowania w ramach tych samych wartości lingwistycznych zmiennych wyjściowych
        conclusion = self.foper.NeutralUnion(self.x_Uzytkownik_zachowanie)
        conclusion = self.foper.Union(conclusion, rule28_Uzytkownik_zachowanie_Maksymalizm)
        conclusion = self.foper.Union(conclusion, rule32_Uzytkownik_zachowanie_Maksymalizm)
        conclusion = self.foper.Union(conclusion, rule33_Uzytkownik_zachowanie_Maksymalizm)
        conclusion = self.foper.Union(conclusion, rule34_Uzytkownik_zachowanie_Maksymalizm)
        self.conclusion_Uzytkownik_zachowanie_Maksymalizm = conclusion
        conclusion = self.foper.NeutralUnion(self.x_Uzytkownik_zachowanie)
        conclusion = self.foper.Union(conclusion, rule29_Uzytkownik_zachowanie_Satysfakcja)
        conclusion = self.foper.Union(conclusion, rule30_Uzytkownik_zachowanie_Satysfakcja)
        conclusion = self.foper.Union(conclusion, rule31_Uzytkownik_zachowanie_Satysfakcja)
        self.conclusion_Uzytkownik_zachowanie_Satysfakcja = conclusion

        #
        # Wyostrzanie zmiennych wyjściowych
        aggregate = self.foper.NeutralAggregate(self.x_Uzytkownik_zachowanie)
        aggregate = self.foper.Aggregation(aggregate, self.conclusion_Uzytkownik_zachowanie_Maksymalizm)
        aggregate = self.foper.Aggregation(aggregate, self.conclusion_Uzytkownik_zachowanie_Satysfakcja)
        self.__aggregated_Uzytkownik_zachowanie = aggregate
        self.output_Uzytkownik_zachowanie = self.foper.Centroid(self.x_Uzytkownik_zachowanie, aggregate)

        #
        # przygotowanie słownika wyników
        result = dict(Uzytkownik_zachowanie = self.output_Uzytkownik_zachowanie)
        return result


    def ShowAllVariables(self):
        fig, axes = plt.subplots(nrows=5 + 1, figsize=(8, 3 * (5 + 1)))
        if not hasattr(axes, "__len__"):
            axes = [axes]

        axes[0].plot(self.x_Czas_podjecia_decyzji, self.memb_Czas_podjecia_decyzji_Niska, 'blue', linewidth=1.5, label='niska')
        axes[0].plot(self.x_Czas_podjecia_decyzji, self.memb_Czas_podjecia_decyzji_Srednia, 'red', linewidth=1.5, label='srednia')
        axes[0].plot(self.x_Czas_podjecia_decyzji, self.memb_Czas_podjecia_decyzji_Wysoka, 'green', linewidth=1.5, label='wysoka')
        axes[0].set_title('WE: Description-7E5A204B')
        axes[0].legend()

        axes[1].plot(self.x_Proporcja, self.memb_Proporcja_Niska, 'blue', linewidth=1.5, label='niska')
        axes[1].plot(self.x_Proporcja, self.memb_Proporcja_Srednia, 'red', linewidth=1.5, label='srednia')
        axes[1].plot(self.x_Proporcja, self.memb_Proporcja_Wysoka, 'green', linewidth=1.5, label='wysoka')
        axes[1].set_title('WE: Description-7E5A204B')
        axes[1].legend()

        axes[2].plot(self.x_Czestotliwosc, self.memb_Czestotliwosc_Niska, 'blue', linewidth=1.5, label='niska')
        axes[2].plot(self.x_Czestotliwosc, self.memb_Czestotliwosc_Srednia, 'red', linewidth=1.5, label='srednia')
        axes[2].plot(self.x_Czestotliwosc, self.memb_Czestotliwosc_Wysoka, 'green', linewidth=1.5, label='wysoka')
        axes[2].set_title('WE: Description-7E5A204B')
        axes[2].legend()

        axes[3].plot(self.x_Produkty_same, self.memb_Produkty_same_Niska, 'blue', linewidth=1.5, label='niska')
        axes[3].plot(self.x_Produkty_same, self.memb_Produkty_same_Srednia, 'red', linewidth=1.5, label='srednia')
        axes[3].plot(self.x_Produkty_same, self.memb_Produkty_same_Wysoka, 'green', linewidth=1.5, label='wysoka ')
        axes[3].set_title('WE: Description-7E5A204B')
        axes[3].legend()

        axes[4].plot(self.x_Produkty_inne, self.memb_Produkty_inne_Niska, 'blue', linewidth=1.5, label='niska')
        axes[4].plot(self.x_Produkty_inne, self.memb_Produkty_inne_Srednia, 'red', linewidth=1.5, label='srednia')
        axes[4].plot(self.x_Produkty_inne, self.memb_Produkty_inne_Wysoka, 'green', linewidth=1.5, label='wysoka ')
        axes[4].set_title('WE: Description-7E5A204B')
        axes[4].legend()

        axes[5+0].plot(self.x_Uzytkownik_zachowanie, self.memb_Uzytkownik_zachowanie_Maksymalizm, 'blue', linewidth=1.5, label='maksymalizm')
        axes[5+0].plot(self.x_Uzytkownik_zachowanie, self.memb_Uzytkownik_zachowanie_Satysfakcja, 'red', linewidth=1.5, label='satysfakcja')
        axes[5+0].set_title('WY: Description-60E2D9B8')
        axes[5+0].legend()

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

        axes[0].fill_between(self.x_Uzytkownik_zachowanie, np.zeros_like(self.x_Uzytkownik_zachowanie), self.conclusion_Uzytkownik_zachowanie_Maksymalizm, facecolor='blue', alpha=0.5)
        axes[0].plot(self.x_Uzytkownik_zachowanie, self.memb_Uzytkownik_zachowanie_Maksymalizm, 'blue', linewidth=0.5, linestyle='--', )
        axes[0].fill_between(self.x_Uzytkownik_zachowanie, np.zeros_like(self.x_Uzytkownik_zachowanie), self.conclusion_Uzytkownik_zachowanie_Satysfakcja, facecolor='red', alpha=0.5)
        axes[0].plot(self.x_Uzytkownik_zachowanie, self.memb_Uzytkownik_zachowanie_Satysfakcja, 'red', linewidth=0.5, linestyle='--', )

        memb = fuzz.interp_membership(self.x_Uzytkownik_zachowanie, self.__aggregated_Uzytkownik_zachowanie, self.output_Uzytkownik_zachowanie)
        axes[0].plot([self.output_Uzytkownik_zachowanie]*2, [0, memb], 'k', linewidth=3, alpha=0.9)
        axes[0].set_title('Description-60E2D9B8')

        for ax in axes:
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.get_xaxis().tick_bottom()
            ax.get_yaxis().tick_left()

        plt.tight_layout()
        plt.show()


##
## Model: 'strategia_wyboru'
## Opis:  Description-0BD23E7F
##
class Model_Strategia_wyboru(object):
    foper = None #type: FuzzyOperation

    # Wartości ostre dla zmiennych wejściowych
    input_TrescPrzekazu = None # type: float # Zmienna: Treść przekazu
    input_Zlozonosc = None # type: float # Zmienna: zlozonosc
    input_Produkt_zlozonosc = None # type: float # Zmienna: produkt_zlozonosc
    input_Uzytkownik_zachowanie = None # type: float # Zmienna: uzytkownik_zachowanie

    # Wartości ostre dla zmiennych wyjściowych
    output_Strategia_wyboru = None # type: float # Zmienna: strategia_wyboru

    # Dziedziny zmiennych rozmytych
    x_TrescPrzekazu = None # type: Union[List[float], np.ndarray]
    x_Zlozonosc = None # type: Union[List[float], np.ndarray]
    x_Produkt_zlozonosc = None # type: Union[List[float], np.ndarray]
    x_Uzytkownik_zachowanie = None # type: Union[List[float], np.ndarray]
    x_Strategia_wyboru = None # type: Union[List[float], np.ndarray]

    # Wartości przynależności
    memb_TrescPrzekazu_Kontrola = None # type: Union[List[float], np.ndarray]
    memb_TrescPrzekazu_Zabawa = None # type: Union[List[float], np.ndarray]
    memb_Zlozonosc_Niska = None # type: Union[List[float], np.ndarray]
    memb_Zlozonosc_Wysoka = None # type: Union[List[float], np.ndarray]
    memb_Produkt_zlozonosc_Prosty = None # type: Union[List[float], np.ndarray]
    memb_Produkt_zlozonosc_Zlozony = None # type: Union[List[float], np.ndarray]
    memb_Uzytkownik_zachowanie_Maksymalizm = None # type: Union[List[float], np.ndarray]
    memb_Uzytkownik_zachowanie_Satysfakcja = None # type: Union[List[float], np.ndarray]
    memb_Strategia_wyboru_Maksymalizm = None # type: Union[List[float], np.ndarray]
    memb_Strategia_wyboru_Satysfakcja = None # type: Union[List[float], np.ndarray]

    def __init__(self):
        self.foper = FuzzyOperation()

        self.InitDomain()
        self.InitVariables()
#       self.ShowVariables()

    def InitDomain(self):
        x_step = 0.01
        self.x_TrescPrzekazu = np.arange(0.0000, 10.0000, x_step) # Treść przekazu: Description-6DD9A966
        self.x_Zlozonosc = np.arange(0.0000, 10.0000, x_step) # zlozonosc: Description-6DD9A966
        self.x_Produkt_zlozonosc = np.arange(0.0000, 10.0000, x_step) # produkt_zlozonosc: Description-6DD9A966
        self.x_Uzytkownik_zachowanie = np.arange(0.0000, 10.0000, x_step) # uzytkownik_zachowanie: Description-60E2D9B8
        self.x_Strategia_wyboru = np.arange(0.0000, 10.0000, x_step) # strategia_wyboru: Description-60E2D9B8

    def InitVariables(self):

        # Wejście: Tre&#347;&#263; przekazu
        self.memb_TrescPrzekazu_Kontrola = fuzz.trapmf(self.x_TrescPrzekazu, [0.0000, 0.0000, 1.0000, 9.0000])
        self.memb_TrescPrzekazu_Zabawa = fuzz.trapmf(self.x_TrescPrzekazu, [1.0000, 9.0000, 10.0000, 10.0000])

        # Wejście: zlozonosc
        self.memb_Zlozonosc_Niska = fuzz.trapmf(self.x_Zlozonosc, [0.0000, 0.0000, 1.0000, 9.0000])
        self.memb_Zlozonosc_Wysoka = fuzz.trapmf(self.x_Zlozonosc, [1.0000, 9.0000, 10.0000, 10.0000])

        # Wejście: produkt_zlozonosc
        self.memb_Produkt_zlozonosc_Prosty = fuzz.trapmf(self.x_Produkt_zlozonosc, [0.0000, 0.0000, 1.0000, 9.0000])
        self.memb_Produkt_zlozonosc_Zlozony = fuzz.trapmf(self.x_Produkt_zlozonosc, [1.0000, 9.0000, 10.0000, 10.0000])

        # Wejście: uzytkownik_zachowanie
        self.memb_Uzytkownik_zachowanie_Maksymalizm = fuzz.trapmf(self.x_Uzytkownik_zachowanie, [0.0000, 0.0000, 3.0000, 7.0000])
        self.memb_Uzytkownik_zachowanie_Satysfakcja = fuzz.trapmf(self.x_Uzytkownik_zachowanie, [3.0000, 7.0000, 10.0000, 10.0000])

        # Wyjście: strategia_wyboru
        self.memb_Strategia_wyboru_Maksymalizm = fuzz.trapmf(self.x_Strategia_wyboru, [0.0000, 0.0000, 3.0000, 7.0000])
        self.memb_Strategia_wyboru_Satysfakcja = fuzz.trapmf(self.x_Strategia_wyboru, [3.0000, 7.0000, 10.0000, 10.0000])

    def Execute(self, input_TrescPrzekazu: float, input_Zlozonosc: float, input_Produkt_zlozonosc: float, input_Uzytkownik_zachowanie: float):
        self.input_TrescPrzekazu = input_TrescPrzekazu
        self.input_Zlozonosc = input_Zlozonosc
        self.input_Produkt_zlozonosc = input_Produkt_zlozonosc
        self.input_Uzytkownik_zachowanie = input_Uzytkownik_zachowanie

        # Wyznacz poziomy przynależności
        level_TrescPrzekazu_Kontrola = fuzz.interp_membership(self.x_TrescPrzekazu, self.memb_TrescPrzekazu_Kontrola, self.input_TrescPrzekazu)
        level_TrescPrzekazu_Zabawa = fuzz.interp_membership(self.x_TrescPrzekazu, self.memb_TrescPrzekazu_Zabawa, self.input_TrescPrzekazu)
        level_Zlozonosc_Niska = fuzz.interp_membership(self.x_Zlozonosc, self.memb_Zlozonosc_Niska, self.input_Zlozonosc)
        level_Zlozonosc_Wysoka = fuzz.interp_membership(self.x_Zlozonosc, self.memb_Zlozonosc_Wysoka, self.input_Zlozonosc)
        level_Produkt_zlozonosc_Prosty = fuzz.interp_membership(self.x_Produkt_zlozonosc, self.memb_Produkt_zlozonosc_Prosty, self.input_Produkt_zlozonosc)
        level_Produkt_zlozonosc_Zlozony = fuzz.interp_membership(self.x_Produkt_zlozonosc, self.memb_Produkt_zlozonosc_Zlozony, self.input_Produkt_zlozonosc)
        level_Uzytkownik_zachowanie_Maksymalizm = fuzz.interp_membership(self.x_Uzytkownik_zachowanie, self.memb_Uzytkownik_zachowanie_Maksymalizm, self.input_Uzytkownik_zachowanie)
        level_Uzytkownik_zachowanie_Satysfakcja = fuzz.interp_membership(self.x_Uzytkownik_zachowanie, self.memb_Uzytkownik_zachowanie_Satysfakcja, self.input_Uzytkownik_zachowanie)

        #
        # Tutaj wnioskowanie ....

        #
        # Reguła IF [Tre&#347;&#263; przekazu IS kontrola] And [zlozonosc IS niska] And [produkt_zlozonosc IS prosty] And [uzytkownik_zachowanie IS maksymalizm] THEN [strategia_wyboru IS maksymalizm]
        temp228 = self.foper.And(level_TrescPrzekazu_Kontrola, level_Zlozonosc_Niska)
        temp229 = self.foper.And(temp228, level_Produkt_zlozonosc_Prosty)
        temp230 = self.foper.And(temp229, level_Uzytkownik_zachowanie_Maksymalizm)
        temp231 = self.foper.And(level_TrescPrzekazu_Kontrola, level_Zlozonosc_Niska)
        temp232 = self.foper.And(temp231, level_Produkt_zlozonosc_Prosty)
        temp233 = self.foper.And(temp232, level_Uzytkownik_zachowanie_Maksymalizm)
        temp234 = self.foper.And(temp233, level_TrescPrzekazu_Kontrola)
        temp235 = self.foper.And(temp234, level_Zlozonosc_Niska)
        temp236 = self.foper.And(temp235, level_Produkt_zlozonosc_Prosty)
        temp237 = self.foper.And(temp236, level_Uzytkownik_zachowanie_Maksymalizm)

        temp238 = self.foper.Or(temp230, temp237)
        rule35_activation = temp238
        rule35_Strategia_wyboru_Maksymalizm = self.foper.Inference(rule35_activation, self.memb_Strategia_wyboru_Maksymalizm)

        #
        # Reguła IF [Tre&#347;&#263; przekazu IS zabawa] And [zlozonosc IS wysoka] And [produkt_zlozonosc IS zlozony] And [uzytkownik_zachowanie IS satysfakcja] THEN [strategia_wyboru IS satysfakcja]
        temp239 = self.foper.And(level_TrescPrzekazu_Zabawa, level_Zlozonosc_Wysoka)
        temp240 = self.foper.And(temp239, level_Produkt_zlozonosc_Zlozony)
        temp241 = self.foper.And(temp240, level_Uzytkownik_zachowanie_Satysfakcja)
        temp242 = self.foper.And(level_TrescPrzekazu_Zabawa, level_Zlozonosc_Wysoka)
        temp243 = self.foper.And(temp242, level_Produkt_zlozonosc_Zlozony)
        temp244 = self.foper.And(temp243, level_Uzytkownik_zachowanie_Satysfakcja)
        temp245 = self.foper.And(temp244, level_TrescPrzekazu_Zabawa)
        temp246 = self.foper.And(temp245, level_Zlozonosc_Wysoka)
        temp247 = self.foper.And(temp246, level_Produkt_zlozonosc_Zlozony)
        temp248 = self.foper.And(temp247, level_Uzytkownik_zachowanie_Satysfakcja)

        temp249 = self.foper.Or(temp241, temp248)
        rule36_activation = temp249
        rule36_Strategia_wyboru_Satysfakcja = self.foper.Inference(rule36_activation, self.memb_Strategia_wyboru_Satysfakcja)

        #
        # Agregacja wyników wnioskowania w ramach tych samych wartości lingwistycznych zmiennych wyjściowych
        conclusion = self.foper.NeutralUnion(self.x_Strategia_wyboru)
        conclusion = self.foper.Union(conclusion, rule35_Strategia_wyboru_Maksymalizm)
        self.conclusion_Strategia_wyboru_Maksymalizm = conclusion
        conclusion = self.foper.NeutralUnion(self.x_Strategia_wyboru)
        conclusion = self.foper.Union(conclusion, rule36_Strategia_wyboru_Satysfakcja)
        self.conclusion_Strategia_wyboru_Satysfakcja = conclusion

        #
        # Wyostrzanie zmiennych wyjściowych
        aggregate = self.foper.NeutralAggregate(self.x_Strategia_wyboru)
        aggregate = self.foper.Aggregation(aggregate, self.conclusion_Strategia_wyboru_Maksymalizm)
        aggregate = self.foper.Aggregation(aggregate, self.conclusion_Strategia_wyboru_Satysfakcja)
        self.__aggregated_Strategia_wyboru = aggregate
        self.output_Strategia_wyboru = self.foper.Centroid(self.x_Strategia_wyboru, aggregate)

        #
        # przygotowanie słownika wyników
        result = dict(Strategia_wyboru = self.output_Strategia_wyboru)
        return result


    def ShowAllVariables(self):
        fig, axes = plt.subplots(nrows=4 + 1, figsize=(8, 3 * (4 + 1)))
        if not hasattr(axes, "__len__"):
            axes = [axes]

        axes[0].plot(self.x_TrescPrzekazu, self.memb_TrescPrzekazu_Kontrola, 'blue', linewidth=1.5, label='kontrola')
        axes[0].plot(self.x_TrescPrzekazu, self.memb_TrescPrzekazu_Zabawa, 'red', linewidth=1.5, label='zabawa')
        axes[0].set_title('WE: Description-6DD9A966')
        axes[0].legend()

        axes[1].plot(self.x_Zlozonosc, self.memb_Zlozonosc_Niska, 'blue', linewidth=1.5, label='niska')
        axes[1].plot(self.x_Zlozonosc, self.memb_Zlozonosc_Wysoka, 'red', linewidth=1.5, label='wysoka')
        axes[1].set_title('WE: Description-6DD9A966')
        axes[1].legend()

        axes[2].plot(self.x_Produkt_zlozonosc, self.memb_Produkt_zlozonosc_Prosty, 'blue', linewidth=1.5, label='prosty')
        axes[2].plot(self.x_Produkt_zlozonosc, self.memb_Produkt_zlozonosc_Zlozony, 'red', linewidth=1.5, label='zlozony')
        axes[2].set_title('WE: Description-6DD9A966')
        axes[2].legend()

        axes[3].plot(self.x_Uzytkownik_zachowanie, self.memb_Uzytkownik_zachowanie_Maksymalizm, 'blue', linewidth=1.5, label='maksymalizm')
        axes[3].plot(self.x_Uzytkownik_zachowanie, self.memb_Uzytkownik_zachowanie_Satysfakcja, 'red', linewidth=1.5, label='satysfakcja')
        axes[3].set_title('WE: Description-60E2D9B8')
        axes[3].legend()

        axes[4+0].plot(self.x_Strategia_wyboru, self.memb_Strategia_wyboru_Maksymalizm, 'blue', linewidth=1.5, label='maksymalizm')
        axes[4+0].plot(self.x_Strategia_wyboru, self.memb_Strategia_wyboru_Satysfakcja, 'red', linewidth=1.5, label='satysfakcja')
        axes[4+0].set_title('WY: Description-60E2D9B8')
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

        axes[0].fill_between(self.x_Strategia_wyboru, np.zeros_like(self.x_Strategia_wyboru), self.conclusion_Strategia_wyboru_Maksymalizm, facecolor='blue', alpha=0.5)
        axes[0].plot(self.x_Strategia_wyboru, self.memb_Strategia_wyboru_Maksymalizm, 'blue', linewidth=0.5, linestyle='--', )
        axes[0].fill_between(self.x_Strategia_wyboru, np.zeros_like(self.x_Strategia_wyboru), self.conclusion_Strategia_wyboru_Satysfakcja, facecolor='red', alpha=0.5)
        axes[0].plot(self.x_Strategia_wyboru, self.memb_Strategia_wyboru_Satysfakcja, 'red', linewidth=0.5, linestyle='--', )

        memb = fuzz.interp_membership(self.x_Strategia_wyboru, self.__aggregated_Strategia_wyboru, self.output_Strategia_wyboru)
        axes[0].plot([self.output_Strategia_wyboru]*2, [0, memb], 'k', linewidth=3, alpha=0.9)
        axes[0].set_title('Description-60E2D9B8')

        for ax in axes:
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.get_xaxis().tick_bottom()
            ax.get_yaxis().tick_left()

        plt.tight_layout()
        plt.show()


##
## Model: 'widocznosc'
## Opis:  Description-22BC05DA
##
class Model_Widocznosc(object):
    foper = None #type: FuzzyOperation

    # Wartości ostre dla zmiennych wejściowych
    input_Widocznosc_uzytkowania = None # type: float # Zmienna: widocznosc_uzytkowania
    input_Popularnosc = None # type: float # Zmienna: popularnosc
    input_Widocznosc_logo = None # type: float # Zmienna: widocznosc_logo
    input_Produkt_luksusowy = None # type: float # Zmienna: produkt_luksusowy
    input_Ekskluzywnosc_produktu = None # type: float # Zmienna: ekskluzywnosc_produktu

    # Wartości ostre dla zmiennych wyjściowych
    output_Potrzeba_statusu = None # type: float # Zmienna: potrzeba_statusu

    # Dziedziny zmiennych rozmytych
    x_Widocznosc_uzytkowania = None # type: Union[List[float], np.ndarray]
    x_Popularnosc = None # type: Union[List[float], np.ndarray]
    x_Widocznosc_logo = None # type: Union[List[float], np.ndarray]
    x_Produkt_luksusowy = None # type: Union[List[float], np.ndarray]
    x_Ekskluzywnosc_produktu = None # type: Union[List[float], np.ndarray]
    x_Potrzeba_statusu = None # type: Union[List[float], np.ndarray]

    # Wartości przynależności
    memb_Widocznosc_uzytkowania_Niska = None # type: Union[List[float], np.ndarray]
    memb_Widocznosc_uzytkowania_Srednia = None # type: Union[List[float], np.ndarray]
    memb_Widocznosc_uzytkowania_Wysoka = None # type: Union[List[float], np.ndarray]
    memb_Popularnosc_Niska = None # type: Union[List[float], np.ndarray]
    memb_Popularnosc_Srednia = None # type: Union[List[float], np.ndarray]
    memb_Popularnosc_Wysoka = None # type: Union[List[float], np.ndarray]
    memb_Widocznosc_logo_Niska = None # type: Union[List[float], np.ndarray]
    memb_Widocznosc_logo_Srednia = None # type: Union[List[float], np.ndarray]
    memb_Widocznosc_logo_Wysoka = None # type: Union[List[float], np.ndarray]
    memb_Produkt_luksusowy_Nie = None # type: Union[List[float], np.ndarray]
    memb_Produkt_luksusowy_Tak = None # type: Union[List[float], np.ndarray]
    memb_Ekskluzywnosc_produktu_Pierwszej_potrzeby = None # type: Union[List[float], np.ndarray]
    memb_Ekskluzywnosc_produktu_Luksusowy = None # type: Union[List[float], np.ndarray]
    memb_Potrzeba_statusu_Niska = None # type: Union[List[float], np.ndarray]
    memb_Potrzeba_statusu_Wysoka = None # type: Union[List[float], np.ndarray]

    def __init__(self):
        self.foper = FuzzyOperation()

        self.InitDomain()
        self.InitVariables()
#       self.ShowVariables()

    def InitDomain(self):
        x_step = 0.01
        self.x_Widocznosc_uzytkowania = np.arange(0.0000, 10.0000, x_step) # widocznosc_uzytkowania: Description-7E5A204B
        self.x_Popularnosc = np.arange(0.0000, 10.0000, x_step) # popularnosc: Description-7E5A204B
        self.x_Widocznosc_logo = np.arange(0.0000, 10.0000, x_step) # widocznosc_logo: Description-7E5A204B
        self.x_Produkt_luksusowy = np.arange(0.0000, 10.0000, x_step) # produkt_luksusowy: Description-6DD9A966
        self.x_Ekskluzywnosc_produktu = np.arange(0.0000, 10.0000, x_step) # ekskluzywnosc_produktu: Description-6DD9A966
        self.x_Potrzeba_statusu = np.arange(0.0000, 10.0000, x_step) # potrzeba_statusu: Description-60E2D9B8

    def InitVariables(self):

        # Wejście: widocznosc_uzytkowania
        self.memb_Widocznosc_uzytkowania_Niska = fuzz.trapmf(self.x_Widocznosc_uzytkowania, [0.0000, 0.0000, 1.0000, 5.0000])
        self.memb_Widocznosc_uzytkowania_Srednia = fuzz.trapmf(self.x_Widocznosc_uzytkowania, [1.0000, 5.0000, 5.0000, 9.0000])
        self.memb_Widocznosc_uzytkowania_Wysoka = fuzz.trapmf(self.x_Widocznosc_uzytkowania, [5.0000, 9.0000, 10.0000, 10.0000])

        # Wejście: popularnosc
        self.memb_Popularnosc_Niska = fuzz.trapmf(self.x_Popularnosc, [0.0000, 0.0000, 1.0000, 5.0000])
        self.memb_Popularnosc_Srednia = fuzz.trapmf(self.x_Popularnosc, [1.0000, 5.0000, 5.0000, 9.0000])
        self.memb_Popularnosc_Wysoka = fuzz.trapmf(self.x_Popularnosc, [5.0000, 9.0000, 10.0000, 10.0000])

        # Wejście: widocznosc_logo
        self.memb_Widocznosc_logo_Niska = fuzz.trapmf(self.x_Widocznosc_logo, [0.0000, 0.0000, 1.0000, 5.0000])
        self.memb_Widocznosc_logo_Srednia = fuzz.trapmf(self.x_Widocznosc_logo, [1.0000, 5.0000, 5.0000, 9.0000])
        self.memb_Widocznosc_logo_Wysoka = fuzz.trapmf(self.x_Widocznosc_logo, [5.0000, 9.0000, 10.0000, 10.0000])

        # Wejście: produkt_luksusowy
        self.memb_Produkt_luksusowy_Nie = fuzz.trapmf(self.x_Produkt_luksusowy, [0.0000, 0.0000, 1.0000, 9.0000])
        self.memb_Produkt_luksusowy_Tak = fuzz.trapmf(self.x_Produkt_luksusowy, [1.0000, 9.0000, 10.0000, 10.0000])

        # Wejście: ekskluzywnosc_produktu
        self.memb_Ekskluzywnosc_produktu_Pierwszej_potrzeby = fuzz.trapmf(self.x_Ekskluzywnosc_produktu, [0.0000, 0.0000, 1.0000, 9.0000])
        self.memb_Ekskluzywnosc_produktu_Luksusowy = fuzz.trapmf(self.x_Ekskluzywnosc_produktu, [1.0000, 9.0000, 10.0000, 10.0000])

        # Wyjście: potrzeba_statusu
        self.memb_Potrzeba_statusu_Niska = fuzz.trapmf(self.x_Potrzeba_statusu, [0.0000, 0.0000, 3.0000, 7.0000])
        self.memb_Potrzeba_statusu_Wysoka = fuzz.trapmf(self.x_Potrzeba_statusu, [3.0000, 7.0000, 10.0000, 10.0000])

    def Execute(self, input_Widocznosc_uzytkowania: float, input_Popularnosc: float, input_Widocznosc_logo: float, input_Produkt_luksusowy: float, input_Ekskluzywnosc_produktu: float):
        self.input_Widocznosc_uzytkowania = input_Widocznosc_uzytkowania
        self.input_Popularnosc = input_Popularnosc
        self.input_Widocznosc_logo = input_Widocznosc_logo
        self.input_Produkt_luksusowy = input_Produkt_luksusowy
        self.input_Ekskluzywnosc_produktu = input_Ekskluzywnosc_produktu

        # Wyznacz poziomy przynależności
        level_Widocznosc_uzytkowania_Niska = fuzz.interp_membership(self.x_Widocznosc_uzytkowania, self.memb_Widocznosc_uzytkowania_Niska, self.input_Widocznosc_uzytkowania)
        level_Widocznosc_uzytkowania_Srednia = fuzz.interp_membership(self.x_Widocznosc_uzytkowania, self.memb_Widocznosc_uzytkowania_Srednia, self.input_Widocznosc_uzytkowania)
        level_Widocznosc_uzytkowania_Wysoka = fuzz.interp_membership(self.x_Widocznosc_uzytkowania, self.memb_Widocznosc_uzytkowania_Wysoka, self.input_Widocznosc_uzytkowania)
        level_Popularnosc_Niska = fuzz.interp_membership(self.x_Popularnosc, self.memb_Popularnosc_Niska, self.input_Popularnosc)
        level_Popularnosc_Srednia = fuzz.interp_membership(self.x_Popularnosc, self.memb_Popularnosc_Srednia, self.input_Popularnosc)
        level_Popularnosc_Wysoka = fuzz.interp_membership(self.x_Popularnosc, self.memb_Popularnosc_Wysoka, self.input_Popularnosc)
        level_Widocznosc_logo_Niska = fuzz.interp_membership(self.x_Widocznosc_logo, self.memb_Widocznosc_logo_Niska, self.input_Widocznosc_logo)
        level_Widocznosc_logo_Srednia = fuzz.interp_membership(self.x_Widocznosc_logo, self.memb_Widocznosc_logo_Srednia, self.input_Widocznosc_logo)
        level_Widocznosc_logo_Wysoka = fuzz.interp_membership(self.x_Widocznosc_logo, self.memb_Widocznosc_logo_Wysoka, self.input_Widocznosc_logo)
        level_Produkt_luksusowy_Nie = fuzz.interp_membership(self.x_Produkt_luksusowy, self.memb_Produkt_luksusowy_Nie, self.input_Produkt_luksusowy)
        level_Produkt_luksusowy_Tak = fuzz.interp_membership(self.x_Produkt_luksusowy, self.memb_Produkt_luksusowy_Tak, self.input_Produkt_luksusowy)
        level_Ekskluzywnosc_produktu_Pierwszej_potrzeby = fuzz.interp_membership(self.x_Ekskluzywnosc_produktu, self.memb_Ekskluzywnosc_produktu_Pierwszej_potrzeby, self.input_Ekskluzywnosc_produktu)
        level_Ekskluzywnosc_produktu_Luksusowy = fuzz.interp_membership(self.x_Ekskluzywnosc_produktu, self.memb_Ekskluzywnosc_produktu_Luksusowy, self.input_Ekskluzywnosc_produktu)

        #
        # Tutaj wnioskowanie ....

        #
        # Reguła IF [widocznosc_uzytkowania IS niska] And [popularnosc IS niska] And [widocznosc_logo IS niska] And [produkt_luksusowy IS nie] And [ekskluzywnosc_produktu IS pierwszej_potrzeby] THEN [potrzeba_statusu IS niska]
        temp250 = self.foper.And(level_Widocznosc_uzytkowania_Niska, level_Popularnosc_Niska)
        temp251 = self.foper.And(temp250, level_Widocznosc_logo_Niska)
        temp252 = self.foper.And(temp251, level_Produkt_luksusowy_Nie)
        temp253 = self.foper.And(temp252, level_Ekskluzywnosc_produktu_Pierwszej_potrzeby)
        temp254 = self.foper.And(level_Widocznosc_uzytkowania_Niska, level_Popularnosc_Niska)
        temp255 = self.foper.And(temp254, level_Widocznosc_logo_Niska)
        temp256 = self.foper.And(temp255, level_Produkt_luksusowy_Nie)
        temp257 = self.foper.And(temp256, level_Ekskluzywnosc_produktu_Pierwszej_potrzeby)
        temp258 = self.foper.And(temp257, level_Widocznosc_uzytkowania_Niska)
        temp259 = self.foper.And(temp258, level_Popularnosc_Niska)
        temp260 = self.foper.And(temp259, level_Widocznosc_logo_Niska)
        temp261 = self.foper.And(temp260, level_Produkt_luksusowy_Nie)
        temp262 = self.foper.And(temp261, level_Ekskluzywnosc_produktu_Pierwszej_potrzeby)

        temp263 = self.foper.Or(temp253, temp262)
        rule37_activation = temp263
        rule37_Potrzeba_statusu_Niska = self.foper.Inference(rule37_activation, self.memb_Potrzeba_statusu_Niska)

        #
        # Agregacja wyników wnioskowania w ramach tych samych wartości lingwistycznych zmiennych wyjściowych
        conclusion = self.foper.NeutralUnion(self.x_Potrzeba_statusu)
        conclusion = self.foper.Union(conclusion, rule37_Potrzeba_statusu_Niska)
        self.conclusion_Potrzeba_statusu_Niska = conclusion

        #
        # Wyostrzanie zmiennych wyjściowych
        aggregate = self.foper.NeutralAggregate(self.x_Potrzeba_statusu)
        aggregate = self.foper.Aggregation(aggregate, self.conclusion_Potrzeba_statusu_Niska)
        aggregate = self.foper.Aggregation(aggregate, self.conclusion_Potrzeba_statusu_Wysoka)
        self.__aggregated_Potrzeba_statusu = aggregate
        self.output_Potrzeba_statusu = self.foper.Centroid(self.x_Potrzeba_statusu, aggregate)

        #
        # przygotowanie słownika wyników
        result = dict(Potrzeba_statusu = self.output_Potrzeba_statusu)
        return result


    def ShowAllVariables(self):
        fig, axes = plt.subplots(nrows=5 + 1, figsize=(8, 3 * (5 + 1)))
        if not hasattr(axes, "__len__"):
            axes = [axes]

        axes[0].plot(self.x_Widocznosc_uzytkowania, self.memb_Widocznosc_uzytkowania_Niska, 'blue', linewidth=1.5, label='niska')
        axes[0].plot(self.x_Widocznosc_uzytkowania, self.memb_Widocznosc_uzytkowania_Srednia, 'red', linewidth=1.5, label='srednia')
        axes[0].plot(self.x_Widocznosc_uzytkowania, self.memb_Widocznosc_uzytkowania_Wysoka, 'green', linewidth=1.5, label='wysoka')
        axes[0].set_title('WE: Description-7E5A204B')
        axes[0].legend()

        axes[1].plot(self.x_Popularnosc, self.memb_Popularnosc_Niska, 'blue', linewidth=1.5, label='niska')
        axes[1].plot(self.x_Popularnosc, self.memb_Popularnosc_Srednia, 'red', linewidth=1.5, label='srednia')
        axes[1].plot(self.x_Popularnosc, self.memb_Popularnosc_Wysoka, 'green', linewidth=1.5, label='wysoka')
        axes[1].set_title('WE: Description-7E5A204B')
        axes[1].legend()

        axes[2].plot(self.x_Widocznosc_logo, self.memb_Widocznosc_logo_Niska, 'blue', linewidth=1.5, label='niska')
        axes[2].plot(self.x_Widocznosc_logo, self.memb_Widocznosc_logo_Srednia, 'red', linewidth=1.5, label='srednia')
        axes[2].plot(self.x_Widocznosc_logo, self.memb_Widocznosc_logo_Wysoka, 'green', linewidth=1.5, label='wysoka')
        axes[2].set_title('WE: Description-7E5A204B')
        axes[2].legend()

        axes[3].plot(self.x_Produkt_luksusowy, self.memb_Produkt_luksusowy_Nie, 'blue', linewidth=1.5, label='nie')
        axes[3].plot(self.x_Produkt_luksusowy, self.memb_Produkt_luksusowy_Tak, 'red', linewidth=1.5, label='tak')
        axes[3].set_title('WE: Description-6DD9A966')
        axes[3].legend()

        axes[4].plot(self.x_Ekskluzywnosc_produktu, self.memb_Ekskluzywnosc_produktu_Pierwszej_potrzeby, 'blue', linewidth=1.5, label='pierwszej_potrzeby')
        axes[4].plot(self.x_Ekskluzywnosc_produktu, self.memb_Ekskluzywnosc_produktu_Luksusowy, 'red', linewidth=1.5, label='luksusowy')
        axes[4].set_title('WE: Description-6DD9A966')
        axes[4].legend()

        axes[5+0].plot(self.x_Potrzeba_statusu, self.memb_Potrzeba_statusu_Niska, 'blue', linewidth=1.5, label='niska')
        axes[5+0].plot(self.x_Potrzeba_statusu, self.memb_Potrzeba_statusu_Wysoka, 'red', linewidth=1.5, label='wysoka')
        axes[5+0].set_title('WY: Description-60E2D9B8')
        axes[5+0].legend()

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

        axes[0].fill_between(self.x_Potrzeba_statusu, np.zeros_like(self.x_Potrzeba_statusu), self.conclusion_Potrzeba_statusu_Niska, facecolor='blue', alpha=0.5)
        axes[0].plot(self.x_Potrzeba_statusu, self.memb_Potrzeba_statusu_Niska, 'blue', linewidth=0.5, linestyle='--', )
        axes[0].fill_between(self.x_Potrzeba_statusu, np.zeros_like(self.x_Potrzeba_statusu), self.conclusion_Potrzeba_statusu_Wysoka, facecolor='red', alpha=0.5)
        axes[0].plot(self.x_Potrzeba_statusu, self.memb_Potrzeba_statusu_Wysoka, 'red', linewidth=0.5, linestyle='--', )

        memb = fuzz.interp_membership(self.x_Potrzeba_statusu, self.__aggregated_Potrzeba_statusu, self.output_Potrzeba_statusu)
        axes[0].plot([self.output_Potrzeba_statusu]*2, [0, memb], 'k', linewidth=3, alpha=0.9)
        axes[0].set_title('Description-60E2D9B8')

        for ax in axes:
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.get_xaxis().tick_bottom()
            ax.get_yaxis().tick_left()

        plt.tight_layout()
        plt.show()


##
## Model: 'marka'
## Opis:  Description-34C62260
##
class Model_Marka(object):
    foper = None #type: FuzzyOperation

    # Wartości ostre dla zmiennych wejściowych
    input_Znajomosc = None # type: float # Zmienna: Znajomość
    input_StatusMarki = None # type: float # Zmienna: Status marki

    # Wartości ostre dla zmiennych wyjściowych
    output_Motywacja = None # type: float # Zmienna: motywacja

    # Dziedziny zmiennych rozmytych
    x_Znajomosc = None # type: Union[List[float], np.ndarray]
    x_StatusMarki = None # type: Union[List[float], np.ndarray]
    x_Motywacja = None # type: Union[List[float], np.ndarray]

    # Wartości przynależności
    memb_Znajomosc_Niska = None # type: Union[List[float], np.ndarray]
    memb_Znajomosc_Srednia = None # type: Union[List[float], np.ndarray]
    memb_Znajomosc_Wysoka = None # type: Union[List[float], np.ndarray]
    memb_StatusMarki_Nowa = None # type: Union[List[float], np.ndarray]
    memb_StatusMarki_Rebranding = None # type: Union[List[float], np.ndarray]
    memb_StatusMarki_Istniejaca = None # type: Union[List[float], np.ndarray]
    memb_Motywacja_Zasady = None # type: Union[List[float], np.ndarray]
    memb_Motywacja_Status = None # type: Union[List[float], np.ndarray]
    memb_Motywacja_Dzialanie = None # type: Union[List[float], np.ndarray]

    def __init__(self):
        self.foper = FuzzyOperation()

        self.InitDomain()
        self.InitVariables()
#       self.ShowVariables()

    def InitDomain(self):
        x_step = 0.01
        self.x_Znajomosc = np.arange(0.0000, 10.0000, x_step) # Znajomość: Description-7E5A204B
        self.x_StatusMarki = np.arange(0.0000, 6.0000, x_step) # Status marki: Description-6AED46EB
        self.x_Motywacja = np.arange(0.0000, 6.0000, x_step) # motywacja: Description-6AED46EB

    def InitVariables(self):

        # Wejście: Znajomo&#347;&#263;
        self.memb_Znajomosc_Niska = fuzz.trapmf(self.x_Znajomosc, [0.0000, 0.0000, 1.0000, 5.0000])
        self.memb_Znajomosc_Srednia = fuzz.trapmf(self.x_Znajomosc, [1.0000, 5.0000, 5.0000, 9.0000])
        self.memb_Znajomosc_Wysoka = fuzz.trapmf(self.x_Znajomosc, [5.0000, 9.0000, 10.0000, 10.0000])

        # Wejście: Status marki
        self.memb_StatusMarki_Nowa = fuzz.trapmf(self.x_StatusMarki, [0.0000, 1.0000, 2.0000, 2.0000])
        self.memb_StatusMarki_Rebranding = fuzz.trapmf(self.x_StatusMarki, [2.0000, 3.0000, 4.0000, 4.0000])
        self.memb_StatusMarki_Istniejaca = fuzz.trapmf(self.x_StatusMarki, [4.0000, 5.0000, 6.0000, 6.0000])

        # Wyjście: motywacja
        self.memb_Motywacja_Zasady = fuzz.trapmf(self.x_Motywacja, [0.0000, 1.0000, 2.0000, 2.0000])
        self.memb_Motywacja_Status = fuzz.trapmf(self.x_Motywacja, [2.0000, 3.0000, 4.0000, 4.0000])
        self.memb_Motywacja_Dzialanie = fuzz.trapmf(self.x_Motywacja, [4.0000, 5.0000, 6.0000, 6.0000])

    def Execute(self, input_Znajomosc: float, input_StatusMarki: float):
        self.input_Znajomosc = input_Znajomosc
        self.input_StatusMarki = input_StatusMarki

        # Wyznacz poziomy przynależności
        level_Znajomosc_Niska = fuzz.interp_membership(self.x_Znajomosc, self.memb_Znajomosc_Niska, self.input_Znajomosc)
        level_Znajomosc_Srednia = fuzz.interp_membership(self.x_Znajomosc, self.memb_Znajomosc_Srednia, self.input_Znajomosc)
        level_Znajomosc_Wysoka = fuzz.interp_membership(self.x_Znajomosc, self.memb_Znajomosc_Wysoka, self.input_Znajomosc)
        level_StatusMarki_Nowa = fuzz.interp_membership(self.x_StatusMarki, self.memb_StatusMarki_Nowa, self.input_StatusMarki)
        level_StatusMarki_Rebranding = fuzz.interp_membership(self.x_StatusMarki, self.memb_StatusMarki_Rebranding, self.input_StatusMarki)
        level_StatusMarki_Istniejaca = fuzz.interp_membership(self.x_StatusMarki, self.memb_StatusMarki_Istniejaca, self.input_StatusMarki)

        #
        # Tutaj wnioskowanie ....

        #
        # Reguła IF [Znajomo&#347;&#263; IS niska] And [Status marki IS nowa] THEN [motywacja IS zasady]
        temp264 = self.foper.And(level_Znajomosc_Niska, level_StatusMarki_Nowa)
        temp265 = self.foper.And(level_Znajomosc_Niska, level_StatusMarki_Nowa)
        temp266 = self.foper.And(temp265, level_Znajomosc_Niska)
        temp267 = self.foper.And(temp266, level_StatusMarki_Nowa)

        temp268 = self.foper.Or(temp264, temp267)
        rule38_activation = temp268
        rule38_Motywacja_Zasady = self.foper.Inference(rule38_activation, self.memb_Motywacja_Zasady)

        #
        # Agregacja wyników wnioskowania w ramach tych samych wartości lingwistycznych zmiennych wyjściowych
        conclusion = self.foper.NeutralUnion(self.x_Motywacja)
        conclusion = self.foper.Union(conclusion, rule38_Motywacja_Zasady)
        self.conclusion_Motywacja_Zasady = conclusion

        #
        # Wyostrzanie zmiennych wyjściowych
        aggregate = self.foper.NeutralAggregate(self.x_Motywacja)
        aggregate = self.foper.Aggregation(aggregate, self.conclusion_Motywacja_Zasady)
        aggregate = self.foper.Aggregation(aggregate, self.conclusion_Motywacja_Status)
        aggregate = self.foper.Aggregation(aggregate, self.conclusion_Motywacja_Dzialanie)
        self.__aggregated_Motywacja = aggregate
        self.output_Motywacja = self.foper.Centroid(self.x_Motywacja, aggregate)

        #
        # przygotowanie słownika wyników
        result = dict(Motywacja = self.output_Motywacja)
        return result


    def ShowAllVariables(self):
        fig, axes = plt.subplots(nrows=2 + 1, figsize=(8, 3 * (2 + 1)))
        if not hasattr(axes, "__len__"):
            axes = [axes]

        axes[0].plot(self.x_Znajomosc, self.memb_Znajomosc_Niska, 'blue', linewidth=1.5, label='niska')
        axes[0].plot(self.x_Znajomosc, self.memb_Znajomosc_Srednia, 'red', linewidth=1.5, label='srednia')
        axes[0].plot(self.x_Znajomosc, self.memb_Znajomosc_Wysoka, 'green', linewidth=1.5, label='wysoka')
        axes[0].set_title('WE: Description-7E5A204B')
        axes[0].legend()

        axes[1].plot(self.x_StatusMarki, self.memb_StatusMarki_Nowa, 'blue', linewidth=1.5, label='nowa')
        axes[1].plot(self.x_StatusMarki, self.memb_StatusMarki_Rebranding, 'red', linewidth=1.5, label='rebranding')
        axes[1].plot(self.x_StatusMarki, self.memb_StatusMarki_Istniejaca, 'green', linewidth=1.5, label='istniejąca')
        axes[1].set_title('WE: Description-6AED46EB')
        axes[1].legend()

        axes[2+0].plot(self.x_Motywacja, self.memb_Motywacja_Zasady, 'blue', linewidth=1.5, label='zasady')
        axes[2+0].plot(self.x_Motywacja, self.memb_Motywacja_Status, 'red', linewidth=1.5, label='status')
        axes[2+0].plot(self.x_Motywacja, self.memb_Motywacja_Dzialanie, 'green', linewidth=1.5, label='dzialanie')
        axes[2+0].set_title('WY: Description-6AED46EB')
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

        axes[0].fill_between(self.x_Motywacja, np.zeros_like(self.x_Motywacja), self.conclusion_Motywacja_Zasady, facecolor='blue', alpha=0.5)
        axes[0].plot(self.x_Motywacja, self.memb_Motywacja_Zasady, 'blue', linewidth=0.5, linestyle='--', )
        axes[0].fill_between(self.x_Motywacja, np.zeros_like(self.x_Motywacja), self.conclusion_Motywacja_Status, facecolor='red', alpha=0.5)
        axes[0].plot(self.x_Motywacja, self.memb_Motywacja_Status, 'red', linewidth=0.5, linestyle='--', )
        axes[0].fill_between(self.x_Motywacja, np.zeros_like(self.x_Motywacja), self.conclusion_Motywacja_Dzialanie, facecolor='green', alpha=0.5)
        axes[0].plot(self.x_Motywacja, self.memb_Motywacja_Dzialanie, 'green', linewidth=0.5, linestyle='--', )

        memb = fuzz.interp_membership(self.x_Motywacja, self.__aggregated_Motywacja, self.output_Motywacja)
        axes[0].plot([self.output_Motywacja]*2, [0, memb], 'k', linewidth=3, alpha=0.9)
        axes[0].set_title('Description-6AED46EB')

        for ax in axes:
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.get_xaxis().tick_bottom()
            ax.get_yaxis().tick_left()

        plt.tight_layout()
        plt.show()


if __name__ == "__main__":

    m0 = Model_Przekaz_tresc()
    m0.ShowAllVariables()
    m0_result = m0.Execute(np.random.choice(m0.x_Censydiam1), np.random.choice(m0.x_Censydiam2), np.random.choice(m0.x_Censydiam3), np.random.choice(m0.x_Censydiam4))
    m0.ShowActivations()
    print(f"Przekaz_tresc: { m0_result }")


    m1 = Model_Zlozonosc_informacji()
    m1.ShowAllVariables()
    m1_result = m1.Execute(np.random.choice(m1.x_Tekst_do_obrazka), np.random.choice(m1.x_Nasilenie), np.random.choice(m1.x_Argumenty), np.random.choice(m1.x_Liczba_argumentow), np.random.choice(m1.x_Argumentacja))
    m1.ShowActivations()
    print(f"Zlozonosc_informacji: { m1_result }")


    m2 = Model_Produkt_zaangazowanie()
    m2.ShowAllVariables()
    m2_result = m2.Execute(np.random.choice(m2.x_Produkt_zaangazowanie), np.random.choice(m2.x_Warianty), np.random.choice(m2.x_Indywidualizacja))
    m2.ShowActivations()
    print(f"Produkt_zaangazowanie: { m2_result }")


    m3 = Model_Uzytkownik_zachowanie()
    m3.ShowAllVariables()
    m3_result = m3.Execute(np.random.choice(m3.x_Czas_podjecia_decyzji), np.random.choice(m3.x_Proporcja), np.random.choice(m3.x_Czestotliwosc), np.random.choice(m3.x_Produkty_same), np.random.choice(m3.x_Produkty_inne))
    m3.ShowActivations()
    print(f"Uzytkownik_zachowanie: { m3_result }")


    m4 = Model_Strategia_wyboru()
    m4.ShowAllVariables()
    m4_result = m4.Execute(np.random.choice(m4.x_TrescPrzekazu), np.random.choice(m4.x_Zlozonosc), np.random.choice(m4.x_Produkt_zlozonosc), np.random.choice(m4.x_Uzytkownik_zachowanie))
    m4.ShowActivations()
    print(f"Strategia_wyboru: { m4_result }")


    m5 = Model_Widocznosc()
    m5.ShowAllVariables()
    m5_result = m5.Execute(np.random.choice(m5.x_Widocznosc_uzytkowania), np.random.choice(m5.x_Popularnosc), np.random.choice(m5.x_Widocznosc_logo), np.random.choice(m5.x_Produkt_luksusowy), np.random.choice(m5.x_Ekskluzywnosc_produktu))
    m5.ShowActivations()
    print(f"Widocznosc: { m5_result }")


    m6 = Model_Marka()
    m6.ShowAllVariables()
    m6_result = m6.Execute(np.random.choice(m6.x_Znajomosc), np.random.choice(m6.x_StatusMarki))
    m6.ShowActivations()
    print(f"Marka: { m6_result }")

