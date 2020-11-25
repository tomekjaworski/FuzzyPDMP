#
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt


class FuzzyOperation(object):
    or_connective = None
    and_connective = None
    negation = None

    def __init__(self, or_connective = None, and_connective = None, negation = None):
        self.or_connective = or_connective or (lambda x, y: x if x > y else y)
        self.and_connective = and_connective or (lambda x, y: x if x < y else y)
        self.negation = lambda x: 1 - x


    def AND(self, *args):
        if len(args) == 0:
            raise ValueError("args")

        v = args[0]
        for i in range(1, len(args)):
            v = self.and_connective(v, args[i])
        return v

    def OR(self, *args):
        if len(args) == 0:
            raise ValueError("args")

        v = args[0]
        for i in range(1, len(args)):
            v = self.or_connective(v, args[i])
        return v

    def NOT(self, *args):
        if len(args) != 1:
            raise ValueError("args")

        return self.negation(args[0])


class Model(object):

    input_serv = None # type: float # aaaaa
    input_qual = None  # type: float # aaaaa

    def __init__(self):
        self.InitDomain()
        self.InitVariables()

    def InitDomain(self):
        self.x_qual = np.arange(0, 11, 0.1)
        self.x_serv = np.arange(0, 11, 0.1)
        self.x_tip  = np.arange(0, 26, 0.1)

    def InitVariables(self):
        # Generate fuzzy membership functions
        self.qual_lo = fuzz.trimf(self.x_qual, [0, 0, 5])
        self.qual_md = fuzz.trimf(self.x_qual, [0, 5, 10])
        self.qual_hi = fuzz.trimf(self.x_qual, [5, 10, 10])
        self.serv_lo = fuzz.trimf(self.x_serv, [0, 0, 5])
        self.serv_md = fuzz.trimf(self.x_serv, [0, 5, 10])
        self.serv_hi = fuzz.trimf(self.x_serv, [5, 10, 10])
        self.tip_lo = fuzz.trimf(self.x_tip, [0, 0, 13])
        self.tip_md = fuzz.trimf(self.x_tip, [0, 13, 25])
        self.tip_hi = fuzz.trimf(self.x_tip, [13, 25, 25])

    def ShowVariables(self):
        fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))

        ax0.plot(self.x_qual, self.qual_lo, 'b', linewidth=1.5, label='Bad')
        ax0.plot(self.x_qual, self.qual_md, 'g', linewidth=1.5, label='Decent')
        ax0.plot(self.x_qual, self.qual_hi, 'r', linewidth=1.5, label='Great')
        ax0.set_title('Food quality')
        ax0.legend()

        ax1.plot(self.x_serv, self.serv_lo, 'b', linewidth=1.5, label='Poor')
        ax1.plot(self.x_serv, self.serv_md, 'g', linewidth=1.5, label='Acceptable')
        ax1.plot(self.x_serv, self.serv_hi, 'r', linewidth=1.5, label='Amazing')
        ax1.set_title('Service quality')
        ax1.legend()

        ax2.plot(self.x_tip, self.tip_lo, 'b', linewidth=1.5, label='Low')
        ax2.plot(self.x_tip, self.tip_md, 'g', linewidth=1.5, label='Medium')
        ax2.plot(self.x_tip, self.tip_hi, 'r', linewidth=1.5, label='High')
        ax2.set_title('Tip amount')
        ax2.legend()

        # Turn off top/right axes
        for ax in (ax0, ax1, ax2):
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.get_xaxis().tick_bottom()
            ax.get_yaxis().tick_left()

        plt.tight_layout()
        plt.show()


    def SetVariable_qual(self, value: float):
        self.input_qual = value

    def SetVariable_serv(self, value: float):
        self.input_serv = value


    def Execute(self, input_qual: float, input_serv: float):

        self.input_qual = input_qual
        self.input_serv = input_serv

        # We need the activation of our fuzzy membership functions at these values.
        # The exact values 6.5 and 9.8 do not exist on our universes...
        # This is what fuzz.interp_membership exists for!
        qual_level_lo = fuzz.interp_membership(self.x_qual, self.qual_lo, self.input_qual)
        qual_level_md = fuzz.interp_membership(self.x_qual, self.qual_md, self.input_qual)
        qual_level_hi = fuzz.interp_membership(self.x_qual, self.qual_hi, self.input_qual)

        serv_level_lo = fuzz.interp_membership(self.x_serv, self.serv_lo, self.input_serv)
        serv_level_md = fuzz.interp_membership(self.x_serv, self.serv_md, self.input_serv)
        serv_level_hi = fuzz.interp_membership(self.x_serv, self.serv_hi, self.input_serv)



        # Now we take our rules and apply them. Rule 1 concerns bad food OR service.
        # The OR operator means we take the maximum of these two.
        active_rule1 = np.fmax(qual_level_lo, serv_level_lo, serv_level_lo)

        # Now we apply this by clipping the top off the corresponding output
        # membership function with `np.fmin`
        self.output_tip_lo = np.fmin(active_rule1, self.tip_lo)  # removed entirely to 0

        # For rule 2 we connect acceptable service to medium tipping
        self.output_tip_md = np.fmin(serv_level_md, self.tip_md)

        # For rule 3 we connect high service OR high food with high tipping
        active_rule3 = np.fmax(qual_level_hi, serv_level_hi)
        self.output_tip_hi = np.fmin(active_rule3, self.tip_hi)

    def ShowActivations(self):
        # Visualize this
        #fig, ax0 = plt.subplots(figsize=(8, 3))
        fig, axis = plt.subplots(nrows=1, figsize=(8, 1*3))
        if not hasattr(axis, "__len__"):
            axis = [axis]

        tip0 = np.zeros_like(self.x_tip)

        axis[0].fill_between(self.x_tip, tip0, self.output_tip_lo, facecolor='b', alpha=0.7)
        axis[0].plot(self.x_tip, self.tip_lo, 'b', linewidth=0.5, linestyle='--', )
        axis[0].fill_between(self.x_tip, tip0, self.output_tip_md, facecolor='g', alpha=0.7)
        axis[0].plot(self.x_tip, self.tip_md, 'g', linewidth=0.5, linestyle='--')
        axis[0].fill_between(self.x_tip, tip0, self.output_tip_hi, facecolor='r', alpha=0.7)
        axis[0].plot(self.x_tip, self.tip_hi, 'r', linewidth=0.5, linestyle='--')
        axis[0].set_title('Output membership activity')

        # Turn off top/right axes
        for ax in axis:
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.get_xaxis().tick_bottom()
            ax.get_yaxis().tick_left()

        plt.tight_layout()
        plt.show()


if __name__ == "__main__":

    op = FuzzyOperation()
    a = op.NOT(1)
    a = op.AND(1,2,3)
    a = op.OR(1, 2, 3)

    m1 = Model()
    m1.ShowVariables()
    m1.Execute(6.5, 9.8)
    m1.ShowActivations()