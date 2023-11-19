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

from manim import *
import sympy as sp
import numpy as np

class SeveralFunctionScene(Scene):
    def construct(self):
        # Crear una función con sympy
        x = sp.symbols('x')
        x_func = sp.sin(x)
        
        # Calcular la derivada de la función sin con respecto a x
        dx_func = sp.diff(x_func, x)
        dx_dx_func = sp.diff(dx_func, x)
        
        # Convertir a funciones numéricas para graficar
        sp_x_func = sp.lambdify(x, x_func, modules=['numpy'])
        sp_dx_func = sp.lambdify(x, dx_func, modules=['numpy'])
        sp_dx_dx_func = sp.lambdify(x, dx_dx_func, modules=['numpy'])

        axes = Axes(
            x_range=[-PI, PI, 1],
            y_range=[-1, 1, 1],
            x_length=10,
            y_length=6,
            axis_config={"include_tip": False}
        )

        self.play(FadeIn(axes))
        function1 = axes.plot(sp_x_func).fade(0.5)
        tex_x = MathTex(r"f(x)=\sin(x)").to_corner(UL)
        self.play(Create(function1), Write(tex_x))
        self.wait(2)

        function2 = axes.plot(sp_dx_func).fade(0.5)
        tex_dx = MathTex(r"f'(x)=\cos(x)").to_corner(DL)
        self.play(TransformFromCopy(function1, function2), TransformFromCopy(tex_x, tex_dx))
        self.wait(2)
        function3 = axes.plot(sp_dx_dx_func).fade(0.5)
        tex_dx_dx = MathTex(dx_dx_func).next_to(function3, RIGHT, buff=0.2)
        self.play(TransformFromCopy(function2, function3), TransformFromCopy(tex_dx, tex_dx_dx))
        self.wait(2)

class MoldesScene(Scene):
    CONFIG={
        'triangulo': Triangle(color=RED),
        'cuadrado': Square(color=BLUE),
        'Pentagono': RegularPolygon(5,color=GREEN),
        'hexagono': RegularPolygon(6,color=ORANGE),
        'heptagono': RegularPolygon(7,color=WHITE),
        'octagono': RegularPolygon(8,color=YELLOW),
        'nonagono': RegularPolygon(9,color=PURPLE),
    }
    def construct(self):
        titulo=Title("Características común de las figuras, Polígonos regulares")
        self.play(Write(titulo))
        self.wait(2)
        tabla=MobjectTable(
            [
                [self.CONFIG['triangulo'],self.CONFIG['cuadrado'],self.CONFIG['Pentagono']],
                [self.CONFIG['hexagono'],self.CONFIG['heptagono'],self.CONFIG['octagono']],
            ]
        )
        self.play(Write(tabla[1:]))
        self.wait(2)
        self.play(
            Create(tabla[0][0]),
        )
        self.wait(3)
        self.play(
            TransformFromCopy(tabla[0][0],tabla[0][1]),
            run_time=4
        )
        self.wait(3)
        self.play(
            TransformFromCopy(tabla[0][1],tabla[0][2]),
            run_time=4
        )
        self.wait(3)
        self.play(
            TransformFromCopy(tabla[0][2],tabla[0][3]),
            run_time=4
        )
        self.wait(3)
        self.play(
            TransformFromCopy(tabla[0][3],tabla[0][4]),
            run_time=4
        )
        self.wait(3)
        self.play(
            TransformFromCopy(tabla[0][4],tabla[0][5]),
            run_time=4
        )
        self.wait(3)