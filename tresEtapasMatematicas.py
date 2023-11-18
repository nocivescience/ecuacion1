from manim import *
import sympy as sp
class DescriptionScene(Scene):
    def construct(self):
        tabla=Table(
            [["Cuatro etapas de la matemática"],
            ["1. Definición de la función"],
            ["2. Derivación de la función"],
            ["3. Graficación de la función y su derivada"],
            ["4. Animación de la función y su derivada"]]
        )
        self.play(Write(tabla))
        self.wait(2)

class CuatroEtapasScene(Scene):
    def construct(self):
        titulo= Title("Cuatro etapas de la matemática")
        self.play(Write(titulo))
        description1= VGroup(
            Text("1. Procesos con aritmética y álgebra"),
            MathTex(r"a+b=c"),
        )
        description1.arrange(DOWN)
        self.play(Write(description1))
        self.wait(2)
        description2= VGroup(
            Text("2. Procesos con cálculo"),
            MathTex(r"\int_{-\infty}^{\infty} e^{-x^2} dx=\sqrt{\pi}"),
        )
        description2.arrange(DOWN)
        self.play(ReplacementTransform(description1,description2))
        self.wait(2)
        description3= VGroup(
            Text("3. Procesos con programación"),
            Tex(r"Algoritmos lógicos"),
        )
        description3.arrange(DOWN)
        self.play(ReplacementTransform(description2,description3))
        self.wait(2)
        description4= VGroup(
            Text("4. Procesos con Ecuaciones diferenciales"),
            MathTex(r"\frac{\partial^2}{\partial x}x^n+ \frac{\partial}{\partial x} x^n=nx^{n-1}"),
        )
        description4.arrange(DOWN)
        self.play(ReplacementTransform(description3,description4))
        self.wait(2)
        self.play(ShowPassingFlashWithThinningStrokeWidth(description4))
        self.wait(2)

class SeveralFunctionScene(Scene):
    def construct(self):
        #creating a function with sympy
        x_func = lambda x: sp.sin(x)
        dx_func = lambda x: sp.diff(x_func(x), x)
        axes= Axes(
            x_range=[-PI,PI,1],
            y_range=[-1,1,1],
            x_length=10,
            y_length=6,
            axis_config={"include_tip": False}
        )
        self.play(FadeIn(axes))
        function1= axes.plot(x_func)
        self.play(Create(function1))
        self.wait(2)
        function2= axes.plot(lambda x: dx_func(x))
        self.play(ReplacementTransform(function1,function2))
        self.wait(2)