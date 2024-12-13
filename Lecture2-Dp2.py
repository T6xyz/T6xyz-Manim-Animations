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
        introObj.shift(2.25 * UP)

        self.play(FadeIn(introObj))
        self.wait(4)
        self.play(FadeOut(introObj))

        # Introduce chain matrix multiplication
        # First define what the cost of multiplying to matrices is

        matrix1Matrix = Matrix([[1, 1, 1], [1, 1, 1]],
            element_alignment_corner=UL,
            left_bracket="(",
            right_bracket=")")
        matrix1Label = MathTex("M_{1}=", color = WHITE).scale(0.75)
        matrix1Label.align_to(matrix1Matrix, LEFT)
        matrix1Label.shift(LEFT)
        m1 = VGroup(matrix1Label, matrix1Matrix)

        matrix2Matrix = Matrix([[1, 1], [1, 1], [1, 1]],
            element_alignment_corner=UL,
            left_bracket="(",
            right_bracket=")")
        matrix2Label = MathTex("M_{2}=", color = WHITE).scale(0.75)
        matrix2Label.align_to(matrix2Matrix, LEFT)
        matrix2Label.shift(LEFT)
        m2 = VGroup(matrix2Label, matrix2Matrix)

        m1.move_to(ORIGIN + 5 * LEFT)
        m2.move_to(ORIGIN + 5 * RIGHT)

        matrices = VGroup(m1, m2).scale(0.65)

        matrix6Matrix = Matrix([[1, 1, 1], [1, 1, 1]],
            element_alignment_corner=UL,
            left_bracket="(",
            right_bracket=")")
        matrix6Label = MathTex("M_{1}=", color = WHITE).scale(0.75)
        matrix6Label.align_to(matrix6Matrix, LEFT)
        matrix6Label.shift(LEFT)
        m6 = VGroup(matrix6Label, matrix6Matrix)
        
        m6 = VGroup(matrix6Label, matrix6Matrix).scale(0.65)

        self.play(FadeIn(matrices))

        textRule = MathTex(r"\text{*Recall matrix multiplication:}", color = WHITE).scale(0.75)
        textFormula = MathTex(r"\text{M x N} \cdot \text{N x V}").scale(0.65)
        textFormula.move_to(textRule.get_center() + DOWN / 2)

        textGroup = VGroup(textFormula, textRule)
        textGroup.move_to(ORIGIN + 2 * UP)
        self.play(FadeIn(textGroup))
        m1d = Brace(matrix1Matrix, sharpness = 1)
        m1dt = Text(f"N").next_to(m1d, DOWN).scale(0.5)
        m1bottom = VGroup(m1d, m1dt)

        m2r = Brace(matrix2Matrix, sharpness = 1, direction = RIGHT)
        m2rt = Text(f"N").next_to(m2r, RIGHT).scale(0.5)
        m2right = VGroup(m2r, m2rt)

        braces = VGroup(m1bottom, m2right)
        self.wait(2)
        self.play(FadeIn(braces))
        self.wait(2)
        braces.add(textGroup)
        self.play(FadeOut(braces))
        self.remove(textGroup)


        column1Matrix = Matrix([[1],[1],[1]],
            element_alignment_corner = UL,
            left_bracket="(", 
            right_bracket=")")
        column1Matrix.set_color(BLUE)

        matrix3Label = MathTex("M_{2}C_{1}=", color = BLUE).scale(0.75)
        matrix3Label.align_to(column1Matrix, LEFT)
        matrix3Label.shift(1.5 * LEFT)

        matrix3 = VGroup(column1Matrix, matrix3Label).scale(0.65)
        matrix3.move_to(ORIGIN + RIGHT / 2)
        
        self.play(FadeIn(matrix3, target_position = matrix2Matrix[0][0]), run_time = 1.75)

        # Replace transform for matrix multiplication
        
        m4Matrix = Matrix([["1 * 1", "1 * 1", "1 * 1"], ["1", "1", "1"]],
            element_alignment_corner = UL,
            left_bracket="(", 
            right_bracket=")")
        m4Label = MathTex("M_{1}=", color = WHITE).scale(0.75)
        m4Label.align_to(m4Matrix, LEFT)
        m4Label.shift(LEFT)

        m4Matrix[0][0].set_color(BLUE)
        m4Matrix[0][1].set_color(BLUE)
        m4Matrix[0][2].set_color(BLUE)
        

        temp = VGroup(m1, matrix3)
        m4 = VGroup(m4Matrix, m4Label).scale(0.65)
        m4.move_to(m1.get_center())
        self.play(ReplacementTransform(temp, m4))
        self.wait()

        self.wait(2)
        m5Matrix = Matrix([["1", "1", "1"], ["1 * 1", "1 * 1", "1 * 1"]],
            element_alignment_corner = UL,
            left_bracket="(", 
            right_bracket=")")
        m5Label = MathTex("M_{1}=", color = WHITE).scale(0.75)
        m5Label.align_to(m5Matrix, LEFT)
        m5Label.shift(LEFT)
        m5Matrix[0][3].set_color(BLUE)
        m5Matrix[0][4].set_color(BLUE)
        m5Matrix[0][5].set_color(BLUE)
    
        m5 = VGroup(m5Matrix, m5Label).scale(0.65)
        m5.move_to(m4.get_center())
        self.play(ReplacementTransform(m4, m5))

        self.wait()
        m6.move_to(m5.get_center())
        self.play(FadeOut(m5, runtime = 0.3))
        self.play(FadeIn(m6))

        m1BraceRight = Brace(matrix6Matrix, sharpness = 1, direction = RIGHT)
        m1BraceRightText = Text(f"M").next_to(m1BraceRight, RIGHT).scale(0.5)

        m1Right = VGroup(m1BraceRight, m1BraceRightText)

        temp = VGroup(m1Right, m1bottom)
        self.wait()

        self.play(FadeIn(temp))
        self.wait(1.5)
        self.play(FadeOut(temp))

        costc = MathTex(r"C_{1}\text{ cost = MN}", color = WHITE).scale(0.65)
        costc.move_to(ORIGIN)
        self.play(FadeIn(costc))
        self.wait()

        braceV = Brace(matrix2Matrix, sharpness = 1, direction = DOWN)
        braceVtext = Text(f"V").next_to(braceV, DOWN).scale(0.5)

        braceVGroup = VGroup(braceV, braceVtext)
        self.play(FadeIn(braceVGroup))
        self.wait(1.5)
        self.play(FadeOut(braceVGroup))
        cost = MathTex(r"\text{cost = MNV}", color = WHITE).scale(0.7)

        cost.move_to(costc.get_center())
        self.play(ReplacementTransform(costc, cost))

        self.wait(2)

        end = VGroup(cost, m6, m2)

        totalCost = Tex(r"\begin{align*}& \text{Cost }M_{A} M_{B} \text{ = MNV, where M is the number of rows in } M_A \text{,} \\ &\text{N is the number of columns in } M_{A} \text{ and the number of rows} \\&\text{in } M_B \text{, and V is the number of columns in } M_B\end{align*}", color = WHITE).scale(0.7)

        self.play(FadeOut(end))
        self.wait(2)
        self.play(FadeIn(totalCost))

        self.wait(4)

        self.play(FadeOut(totalCost))

        self.wait(3)

        # Begin chain matirx multiplication question
        chainMatrixQuestion = Tex(r"""\begin{align*}&\text{Given a list of matrix dimensions A, where A[i][0] represents 
                                  the number of rows in matrix i and A[i][1]}\\&\text{represents the number of columns in matrix i, where } 
                                  0 \leq i \leq A.length - 1 \text{, find the minimum cost to}\\&\text{multiply the matrices together. 
                                  (Assume the dimensions for each matrix in A are valid for multiplication)}\end{align*}""",color = WHITE).scale(0.45)
        chainMatrixQuestionBox = SurroundingRectangle(chainMatrixQuestion, color = BLUE, buff = MED_LARGE_BUFF)
        
        chainMatrixQuestionObj = VGroup(chainMatrixQuestion, chainMatrixQuestionBox)
        chainMatrixQuestionObj.shift(2.5 * UP)

        self.play(FadeIn(chainMatrixQuestionObj))
        self.wait(6)
        matrixProperty = MathTex(r"AB \neq BA").scale(0.9)
        self.play(FadeIn(matrixProperty))

        size = 4
        l = [Square(side_length = 1, stroke_width = 1.0) for _ in range(size)]
        arr = VGroup(*l).scale(1.0)
        arr.arrange(direction = RIGHT, buff = 0)

        c0 = MathTex(r"(2, 4)", color = BLUE).scale(0.75)
        c0.move_to(l[0].get_center())
        c1 = MathTex(r"(4, 3)", color = BLUE).scale(0.75)
        c1.move_to(l[1].get_center())
        c2 = MathTex(r"(3, 2)", color = BLUE).scale(0.75)
        c2.move_to(l[2].get_center())
        c3 = MathTex(r"(2, 2)", color = BLUE).scale(0.75)
        c3.move_to(l[3].get_center())

        name = Text("A =").scale(0.75)
        name.move_to(l[0].get_center() + LEFT)
        arr.add(c0, c1, c2, c3, name)
        self.wait(2)
        self.play(FadeOut(matrixProperty))
        self.wait()
        self.play(FadeIn(arr))

        matrixNotation = MathTex(r"\text{BCDE}", color = WHITE).scale(1.3)
        matrixNotation.align_to(l[0], LEFT)
        name1 = Text("A' =").scale(0.75)
        matrixNotation.shift(2 * DOWN)
        name1.align_to(name, RIGHT)
        name1.shift(2 * DOWN)

        matrixString = VGroup(matrixNotation, name1)

        self.play(FadeIn(matrixString))

        # First Example
        # State 0
        self.wait(3)
        matrixExample1 = MathTex(r"\text{((BC)D)E}", color = WHITE).scale(1.3)
        matrixExample1[0][0].set_color(BLUE)
        matrixExample1[0][1].set_color(BLUE)
        matrixExample1[0][4].set_color(BLUE)
        matrixExample1[0][6].set_color(BLUE)
        matrixExample1.move_to(matrixNotation.get_center() + RIGHT / 2)

        totalCostText = MathTex(r"\text{Total Cost = 0}").scale(0.8)
        totalCostText.move_to(matrixExample1.get_center() + 4.5 * RIGHT)

        self.play(ReplacementTransform(matrixNotation, matrixExample1))
        self.play(FadeIn(totalCostText))

        # State 1
        self.wait()
        lState1 = [Square(side_length = 1, stroke_width = 1.0) for _ in range(3)]
        arrState1 = VGroup(*lState1).scale(1.0)
        arrState1.arrange(direction = RIGHT, buff = 0)

        c0S1 = MathTex(r"(2, 3)", color = BLUE).scale(0.75)
        c0S1.move_to(lState1[0].get_center())
        c1S1 = MathTex(r"(3, 2)", color = BLUE).scale(0.75)
        c1S1.move_to(lState1[1].get_center())
        c2S1 = MathTex(r"(2, 2)", color = BLUE).scale(0.75)
        c2S1.move_to(lState1[2].get_center())

        arrState1.add(c0S1, c1S1, c2S1)
        arrState1.move_to(arr.get_center())
        arrState1.add(name)

        state1Cost = MathTex(r"2\cdot4\cdot3").scale(0.8)
        state1Cost.move_to(matrixExample1.get_center() + UP / 1.25)

        state1TotalCost = MathTex(r"\text{Total Cost = 24}").scale(0.8)
        state1TotalCost.move_to(matrixExample1.get_center() + 4.5 * RIGHT)

        state1Text = MathTex(r"\text{(} S_{1} \text{D)E}", color = WHITE).scale(1.3)

        state1Text[0][0].set_color(BLUE)
        state1Text[0][4].set_color(BLUE)
        state1Text.align_to(l[0], LEFT)
        state1Text.shift(2 * DOWN)

        state0 = VGroup(matrixExample1, totalCostText, arr)
        state1 = VGroup(arrState1, state1TotalCost, state1Text)

        self.play(FadeIn(state1Cost))
        self.wait(2)

        self.play(FadeOut(state1Cost))
        arr.remove(name)
        self.play(ReplacementTransform(state0, state1))
        self.wait()

        # State 2
        lState2 = [Square(side_length = 1, stroke_width = 1.0) for _ in range(2)]
        arrState2 = VGroup(*lState2).scale(1.0)
        arrState2.arrange(direction = RIGHT, buff = 0)

        c0S2 = MathTex(r"(2, 2)", color = BLUE).scale(0.75)
        c0S2.move_to(lState2[0].get_center())
        c1S2 = MathTex(r"(2, 2)", color = BLUE).scale(0.75)
        c1S2.move_to(lState2[1].get_center())

        arrState2.add(c0S2, c1S2)
        arrState2.move_to(arrState1.get_center())
        arrState2.add(name)

        state2Cost = MathTex(r"2\cdot3\cdot2").scale(0.8)
        state2Cost.move_to(state1Text.get_center() + UP / 1.25)

        state2TotalCost = MathTex(r"\text{Total Cost = 36}").scale(0.8)
        state2TotalCost.move_to(state1TotalCost.get_center())

        state2Text = MathTex(r"S_{2}E}", color = WHITE).scale(1.3)
        state2Text.align_to(l[0], LEFT)
        state2Text.shift(2 * DOWN)

        state2 = VGroup(arrState2, state2Text, state2TotalCost)

        self.wait(3)
        self.play(FadeIn(state2Cost))
        self.wait(2)
        self.play(FadeOut(state2Cost))
        arrState1.remove(name)
        self.play(ReplacementTransform(state1, state2))
        self.wait()
        # State 3

        state3Cost = MathTex(r"2\cdot2\cdot2").scale(0.8)
        state3Cost.move_to(state2Text.get_center() + UP / 1.25)

        state3TotalCost = MathTex(r"\text{Total Cost = 44}").scale(0.8)
        state3TotalCost.move_to(state2TotalCost.get_center())

        self.wait(3)
        self.play(FadeIn(state3Cost))
        self.wait(2)
        self.play(FadeOut(state3Cost))
        state2End = VGroup(state2, name1)
        self.play(ReplacementTransform(state2End, state3TotalCost))
        self.wait(0.5)
        self.play(state3TotalCost.animate.move_to(ORIGIN))
        self.play(state3TotalCost.animate.set_color(BLUE))
        self.wait(4)

        # Example 2
        self.play(FadeOut(state3TotalCost))

        l = [Square(side_length = 1, stroke_width = 1.0) for _ in range(size)]
        arr = VGroup(*l).scale(1.0)
        arr.arrange(direction = RIGHT, buff = 0)

        c0 = MathTex(r"(2, 4)", color = BLUE).scale(0.75)
        c0.move_to(l[0].get_center())
        c1 = MathTex(r"(4, 3)", color = BLUE).scale(0.75)
        c1.move_to(l[1].get_center())
        c2 = MathTex(r"(3, 2)", color = BLUE).scale(0.75)
        c2.move_to(l[2].get_center())
        c3 = MathTex(r"(2, 2)", color = BLUE).scale(0.75)
        c3.move_to(l[3].get_center())

        name = Text("A =").scale(0.75)
        name.move_to(l[0].get_center() + LEFT)
        arr.add(c0, c1, c2, c3, name)

        self.play(FadeIn(arr))

        matrixNotation = MathTex(r"\text{(BC)(DE)}", color = WHITE).scale(1.3)
        matrixNotation.align_to(l[0], LEFT)
        name1 = Text("A' =").scale(0.75)
        matrixNotation.shift(2 * DOWN)
        name1.align_to(name, RIGHT)
        name1.shift(2 * DOWN)

        matrixString = VGroup(matrixNotation, name1)
        matrixNotation[0][0].set_color(BLUE)
        matrixNotation[0][3].set_color(BLUE)
        matrixNotation[0][4].set_color(BLUE)
        matrixNotation[0][7].set_color(BLUE)
        self.wait()
        self.play(FadeIn(matrixString))

        totalCostText = MathTex(r"\text{Total Cost = 0}").scale(0.8)
        totalCostText.move_to(matrixNotation.get_center() + 4.5 * RIGHT)
        self.play(FadeIn(totalCostText))

        # State 1
        self.wait()
        lState1 = [Square(side_length = 1, stroke_width = 1.0) for _ in range(3)]
        arrState1 = VGroup(*lState1).scale(1.0)
        arrState1.arrange(direction = RIGHT, buff = 0)

        c0S1 = MathTex(r"(2, 3)", color = BLUE).scale(0.75)
        c0S1.move_to(lState1[0].get_center())
        c1S1 = MathTex(r"(3, 2)", color = BLUE).scale(0.75)
        c1S1.move_to(lState1[1].get_center())
        c2S1 = MathTex(r"(2, 2)", color = BLUE).scale(0.75)
        c2S1.move_to(lState1[2].get_center())

        arrState1.add(c0S1, c1S1, c2S1)
        arrState1.move_to(arr.get_center())
        arrState1.add(name)

        state1Cost = MathTex(r"2\cdot4\cdot3").scale(0.8)
        state1Cost.move_to(matrixNotation.get_center() + UP / 1.25)

        state1TotalCost = MathTex(r"\text{Total Cost = 24}").scale(0.8)
        state1TotalCost.move_to(matrixNotation.get_center() + 4.5 * RIGHT)

        state1Text = MathTex(r"S_{1}\text{(DE)}", color = WHITE).scale(1.3)

        state1Text[0][2].set_color(BLUE)
        state1Text[0][5].set_color(BLUE)
        state1Text.align_to(l[0], LEFT)
        state1Text.shift(2 * DOWN)

        state0 = VGroup(matrixNotation, totalCostText, arr)
        state1 = VGroup(arrState1, state1TotalCost, state1Text)

        self.play(FadeIn(state1Cost))
        self.wait(2)

        self.play(FadeOut(state1Cost))
        arr.remove(name)
        self.play(ReplacementTransform(state0, state1))
        self.wait()

        # State 2
        lState2 = [Square(side_length = 1, stroke_width = 1.0) for _ in range(2)]
        arrState2 = VGroup(*lState2).scale(1.0)
        arrState2.arrange(direction = RIGHT, buff = 0)

        c0S2 = MathTex(r"(2, 3)", color = BLUE).scale(0.75)
        c0S2.move_to(lState2[0].get_center())
        c1S2 = MathTex(r"(3, 2)", color = BLUE).scale(0.75)
        c1S2.move_to(lState2[1].get_center())

        arrState2.add(c0S2, c1S2)
        arrState2.move_to(arrState1.get_center())
        arrState2.add(name)

        state2Cost = MathTex(r"3\cdot2\cdot2").scale(0.8)
        state2Cost.move_to(state1Text.get_center() + UP / 1.25)

        state2TotalCost = MathTex(r"\text{Total Cost = 36}").scale(0.8)
        state2TotalCost.move_to(state1TotalCost.get_center())

        state2Text = MathTex(r"S_{1}S_{2}}", color = WHITE).scale(1.3)
        state2Text.align_to(l[0], LEFT)
        state2Text.shift(2 * DOWN)

        state2 = VGroup(arrState2, state2Text, state2TotalCost)

        self.wait(3)
        self.play(FadeIn(state2Cost))
        self.wait(2)
        self.play(FadeOut(state2Cost))
        arrState1.remove(name)
        self.play(ReplacementTransform(state1, state2))
        self.wait()

        # State 3
        state3Cost = MathTex(r"2\cdot3\cdot2").scale(0.8)
        state3Cost.move_to(state2Text.get_center() + UP / 1.25)

        state3TotalCost = MathTex(r"\text{Total Cost = 56}").scale(0.8)
        state3TotalCost.move_to(state2TotalCost.get_center())

        self.wait(3)
        self.play(FadeIn(state3Cost))
        self.wait(2)
        self.play(FadeOut(state3Cost))
        state2End = VGroup(state2, name1)
        self.play(ReplacementTransform(state2End, state3TotalCost))
        self.wait(0.5)
        self.play(state3TotalCost.animate.move_to(ORIGIN))
        self.play(state3TotalCost.animate.set_color(BLUE))
        self.wait(4)

        self.play(FadeOut(state3TotalCost))
        self.wait(2)

        question = MathTex(r"\text{Brute Force?}", color = WHITE)
        question.move_to(ORIGIN)

        self.play(FadeIn(question))
        self.wait(4.5)
        bruteForceRuntime = MathTex(r"\mathcal{O}(n!)")
        clarification = MathTex(r"\text{*A.length = n}").scale(0.3)
        clarification.move_to(bruteForceRuntime.get_center() + DOWN / 2)

        g = VGroup(bruteForceRuntime, clarification)
        self.play(FadeOut(question))
        self.play(FadeIn(g))
        self.wait(2)
        self.play(bruteForceRuntime.animate.set_color(RED))
        self.wait(4)
        end = VGroup(g, chainMatrixQuestionObj)
        self.play(FadeOut(end))
        self.wait(3)

        # Introduce DP solution

        size = 4
        l = [Square(side_length = 1, stroke_width = 1.0) for _ in range(size)]
        arr = VGroup(*l).scale(1.0)
        arr.arrange(direction = RIGHT, buff = 0)

        c0 = MathTex(r"(2, 4)", color = BLUE).scale(0.75)
        c0.move_to(l[0].get_center())
        c1 = MathTex(r"(4, 3)", color = BLUE).scale(0.75)
        c1.move_to(l[1].get_center())
        c2 = MathTex(r"(3, 2)", color = BLUE).scale(0.75)
        c2.move_to(l[2].get_center())
        c3 = MathTex(r"(2, 2)", color = BLUE).scale(0.75)
        c3.move_to(l[3].get_center())

        name = Text("A =").scale(0.75)
        name.move_to(l[0].get_center() + LEFT)
        arr.add(c0, c1, c2, c3, name)
        arr.shift(UP)

        matrixNotation = MathTex(r"\text{BCDE}", color = WHITE).scale(1.3)
        matrixNotation.align_to(l[0], LEFT)
        name1 = Text("A' =").scale(0.75)
        matrixNotation.shift(DOWN)
        name1.align_to(name, RIGHT)
        name1.shift(DOWN)
        matrixString = VGroup(matrixNotation, name1)

        g = VGroup(arr, matrixString)
        self.play(FadeIn(g))