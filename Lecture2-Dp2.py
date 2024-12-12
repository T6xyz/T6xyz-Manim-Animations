from manim import * 
import sys
sys.path.insert(1, '/Users/t6xyz/Desktop/T6xyz-Lectures/misc')
from intro import playIntro

class Lecture2DP(Scene):
    def construct(self):
        # Intro to multi-dimensional DP
        introText = Text("Multidimensional Dynamic Programming", color = WHITE).scale(0.75)
        introBox = SurroundingRectangle(introText, color = BLUE, buff = MED_LARGE_BUFF)
        introObj = VGroup(introText, introBox)
        introObj.shift(2.5 * UP)

        self.play(FadeIn(introObj))
        self.wait(4)
        self.play(FadeOut(introObj))

        # Introduce chain matrix multiplication
        # First define what the cost of multiplying to matrices is

        matrix1Matrix = Matrix([[1, 1, 1], [1, 1, 1]],
            element_alignment_corner=UL,
            left_bracket="(",
            right_bracket=")")
        matrix1Label = MathTex("M1=", color = WHITE).scale(0.7)
        matrix1Label.align_to(matrix1Matrix, LEFT)
        matrix1Label.shift(LEFT)
        m1 = VGroup(matrix1Label, matrix1Matrix)

        matrix2Matrix = Matrix([[1, 1], [1, 1], [1, 1]],
            element_alignment_corner=UL,
            left_bracket="(",
            right_bracket=")")
        matrix2Label = MathTex("M2=", color = WHITE).scale(0.7)
        matrix2Label.align_to(matrix2Matrix, LEFT)
        matrix2Label.shift(LEFT)
        m2 = VGroup(matrix2Label, matrix2Matrix)

        m1.move_to(ORIGIN + 3.5 * LEFT)
        m2.move_to(ORIGIN + 3.5 * RIGHT)

        matrices = VGroup(m1, m2).scale(0.65)
        self.play(FadeIn(matrices))

        textRule = MathTex(r"\text{*Recall matrix multiplication:}", color = WHITE).scale(0.75)
        textFormula = MathTex(r"\text{M x N} \cdot \text{N x V}").scale(0.65)
        textFormula.move_to(textRule.get_center() + DOWN / 2)

        textGroup = VGroup(textFormula, textRule)
        textGroup.move_to(ORIGIN + 1.75 * UP)
        self.play(FadeIn(textGroup))
        m1d = Brace(matrix1Matrix, sharpness = 1)
        m1dt = Text(f"N").next_to(m1d, DOWN).scale(0.5)
        m1bottom = VGroup(m1d, m1dt)

        m2r = Brace(matrix2Matrix, sharpness = 1, direction = RIGHT)
        m2rt = Text(f"N").next_to(m2r, RIGHT).scale(0.5)
        m2right = VGroup(m2r, m2rt)

        braces = VGroup(m1bottom, m2right)
        self.play(FadeIn(braces))
        self.wait(2)
        self.play(FadeOut(braces))





