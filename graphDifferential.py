from manim import *
import sympy as sp

class DifferentialEquation(Scene):
    def construct(self):
        fx= lambda x: 4*np.exp(x)+5*np.exp(x)
        axes=Axes(
            x_range=[-4,4,1],
            y_range=[-70,70,10],
            x_length=8,
            y_length=4,
            axis_config={"include_tip":False}
        )
        graph_fx=axes.plot(fx)
        for mob in [axes, graph_fx]:
            self.play(Create(mob))
        self.wait()