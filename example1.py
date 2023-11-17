from manim import *
import sympy as sp

class FunctionScene(Scene):
    def construct(self):
        x = sp.symbols('x')
        f = sp.sin(x)
        df_dx = sp.diff(f, x)

        axes=Axes(
            x_range=[-4,4,1],
            y_range=[-1,1,1],
            x_length=8,
            y_length=4,
            axis_config={"include_tip":False}
        )

        # Convertir funciones simbólicas a funciones lambda de NumPy
        f_np = sp.lambdify(x, f, modules=['numpy'])
        df_dx_np = sp.lambdify(x, df_dx, modules=['numpy'])



        # Crear gráficos
        graph_f = axes.plot(f_np, x_range=[-np.pi, np.pi], color=BLUE)
        graph_df_dx = axes.plot(df_dx_np, x_range=[-np.pi, np.pi], color=RED)

        # Crear ejes

        # Mostrar ejes y gráficos
        self.play(Create(axes), Create(graph_f), Create(graph_df_dx))
        self.wait()