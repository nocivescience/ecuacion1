from manim import *
import sympy as sp

class FunctionScene(Scene):
    def construct(self):
        x = sp.symbols('x')
        c_1 = 5  # sp.symbols('c_1')
        f = c_1 * sp.sin(4 * x)  # Corregir la definición de la función

        df_dx = sp.diff(f, x)
        df_dx_2= sp.diff(df_dx, x)
        
        textos= [
            MathTex(r"f(x)=", sp.latex(f)),
            MathTex(r"f'(x)=", sp.latex(df_dx)),
            MathTex(r"f''(x)=", sp.latex(df_dx_2)),
        ]

        for texto in textos:
            texto.set_z_index(1)

        axes=Axes(
            x_range=[-4,4,1],
            y_range=[-70,70,10],
            x_length=8,
            y_length=4,
            axis_config={"include_tip":False}
        )

        # Convertir funciones simbólicas a funciones lambda de NumPy
        f_np = sp.lambdify(x, f, modules=['numpy'])
        df_dx_np = sp.lambdify(x, df_dx, modules=['numpy'])
        df_dx_np_2 = sp.lambdify(x, df_dx_2, modules=['numpy'])

        # Crear gráficos
        graph_f = axes.plot(f_np, x_range=[-np.pi, np.pi], color=BLUE).fade(.3)
        graph_df_dx = axes.plot(df_dx_np, x_range=[-np.pi, np.pi], color=RED).fade(.3)
        fraph_df_dx_2 = axes.plot(df_dx_np_2, x_range=[-np.pi, np.pi], color=GREEN).fade(.3)

        # Mostrar ejes y gráficos
        self.play(Create(axes), Create(graph_f))
        self.play(TransformFromCopy(graph_f, textos[0].next_to(graph_f.get_start(), LEFT)))
        self.play(
            TransformFromCopy(graph_f, graph_df_dx),
            run_time=2
        )
        self.play(TransformFromCopy(graph_df_dx, textos[1].next_to(graph_df_dx.get_center(), UP)))
        self.play(
            TransformFromCopy(graph_df_dx, fraph_df_dx_2),
            run_time=2
        )
        self.play(TransformFromCopy(fraph_df_dx_2, textos[2].next_to(fraph_df_dx_2.get_end(), RIGHT)))
        self.wait()