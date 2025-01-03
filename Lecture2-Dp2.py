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
        self.wait(2)
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

        state1TotalCost = MathTex(r"\text{total cost = 24}").scale(0.8)
        state1TotalCost.move_to(matrixExample1.get_center() + 4.5 * RIGHT)

        state1Text = MathTex(r"\text{(} S_{1} \text{D)E}", color = WHITE).scale(1.3)

        state1Text[0][0].set_color(BLUE)
        state1Text[0][4].set_color(BLUE)
        state1Text.align_to(l[0], LEFT)
        state1Text.shift(2 * DOWN)

        state0 = VGroup(matrixExample1, totalCostText, arr)
        state1 = VGroup(arrState1, state1TotalCost, state1Text)

        squareGroup = VGroup(l[0], l[1])

        self.play(FadeIn(state1Cost))
        self.play(squareGroup.animate.set_fill(color = WHITE, opacity = 0.2))
        self.wait(2)

        self.play(FadeOut(state1Cost))
        self.play(squareGroup.animate.set_fill(color = WHITE, opacity = 0))
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

        state2TotalCost = MathTex(r"\text{total cost = 36}").scale(0.8)
        state2TotalCost.move_to(state1TotalCost.get_center())

        state2Text = MathTex(r"S_{2}E}", color = WHITE).scale(1.3)
        state2Text.align_to(l[0], LEFT)
        state2Text.shift(2 * DOWN)

        state2 = VGroup(arrState2, state2Text, state2TotalCost)
        squareGroup = VGroup(lState1[0], lState1[1])

        self.wait(3)
        self.play(FadeIn(state2Cost))
        self.play(squareGroup.animate.set_fill(color = WHITE, opacity = 0.2))
        self.wait(2)
        self.play(FadeOut(state2Cost))
        self.play(squareGroup.animate.set_fill(color = WHITE, opacity = 0))
        arrState1.remove(name)
        self.play(ReplacementTransform(state1, state2))
        self.wait()
        # State 3

        state3Cost = MathTex(r"2\cdot2\cdot2").scale(0.8)
        state3Cost.move_to(state2Text.get_center() + UP / 1.25)

        state3TotalCost = MathTex(r"\text{Total Cost = 44}").scale(0.8)
        state3TotalCost.move_to(state2TotalCost.get_center())

        squareGroup = VGroup(lState2[0], lState2[1])

        self.wait(3)
        self.play(FadeIn(state3Cost))
        self.play(squareGroup.animate.set_fill(color = WHITE, opacity = 0.2))
        self.wait(2)
        self.play(FadeOut(state3Cost))
        self.play(squareGroup.animate.set_fill(color = WHITE, opacity = 0))
        state2End = VGroup(state2, name1)
        self.play(ReplacementTransform(state2End, state3TotalCost))
        self.wait(0.5)
        self.play(state3TotalCost.animate.move_to(ORIGIN))
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

        totalCostText = MathTex(r"\text{total cost = 0}").scale(0.8)
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

        state1TotalCost = MathTex(r"\text{total cost = 24}").scale(0.8)
        state1TotalCost.move_to(matrixNotation.get_center() + 4.5 * RIGHT)

        state1Text = MathTex(r"S_{1}\text{(DE)}", color = WHITE).scale(1.3)

        state1Text[0][2].set_color(BLUE)
        state1Text[0][5].set_color(BLUE)
        state1Text.align_to(l[0], LEFT)
        state1Text.shift(2 * DOWN)

        state0 = VGroup(matrixNotation, totalCostText, arr)
        state1 = VGroup(arrState1, state1TotalCost, state1Text)
        squareGroup = VGroup(l[0], l[1])

        self.play(FadeIn(state1Cost))
        self.play(squareGroup.animate.set_fill(color = WHITE, opacity = 0.2))
        self.wait(2)
        self.play(FadeOut(state1Cost))
        self.play(squareGroup.animate.set_fill(color = WHITE, opacity = 0))
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

        state2TotalCost = MathTex(r"\text{total cost = 36}").scale(0.8)
        state2TotalCost.move_to(state1TotalCost.get_center())

        state2Text = MathTex(r"S_{1}S_{2}}", color = WHITE).scale(1.3)
        state2Text.align_to(l[0], LEFT)
        state2Text.shift(2 * DOWN)

        state2 = VGroup(arrState2, state2Text, state2TotalCost)
        squareGroup = VGroup(lState1[1], lState1[2])

        self.wait(3)
        self.play(FadeIn(state2Cost))
        self.play(squareGroup.animate.set_fill(color = WHITE, opacity = 0.2))
        self.wait(2)
        self.play(FadeOut(state2Cost))
        self.play(squareGroup.animate.set_fill(color = WHITE, opacity = 0))
        arrState1.remove(name)
        self.play(ReplacementTransform(state1, state2))
        self.wait()

        # State 3
        state3Cost = MathTex(r"2\cdot3\cdot2").scale(0.8)
        state3Cost.move_to(state2Text.get_center() + UP / 1.25)

        state3TotalCost = MathTex(r"\text{total cost = 56}").scale(0.8)
        state3TotalCost.move_to(state2TotalCost.get_center())
        squareGroup = VGroup(lState2[0], lState2[1])

        self.wait(3)
        self.play(FadeIn(state3Cost))
        self.play(squareGroup.animate.set_fill(color = WHITE, opacity = 0.2))
        self.wait(2)
        self.play(FadeOut(state3Cost))
        self.play(squareGroup.animate.set_fill(color = WHITE, opacity = 0))
        state2End = VGroup(state2, name1)
        self.play(ReplacementTransform(state2End, state3TotalCost))
        self.wait(0.5)
        self.play(state3TotalCost.animate.move_to(ORIGIN))
        self.wait(4)

        self.play(FadeOut(state3TotalCost))
        self.wait(2)

        question = MathTex(r"\text{Brute Force?}", color = WHITE)
        question.move_to(ORIGIN)

        self.play(FadeIn(question))
        self.wait(4.5)
        bruteForceRuntime = MathTex(r"\mathcal{O}(n!)").scale(1.2)
        bruteForceRuntime.shift(DOWN / 2)
        clarification = MathTex(r"\text{*A.length = n}").scale(0.4)
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
        arr.shift(2 * UP)

        matrixNotation = MathTex(r"\text{BCDE}", color = WHITE).scale(1.3)
        matrixNotation.align_to(l[0], LEFT)
        name1 = Text("A' =").scale(0.75)
        matrixNotation.shift(0.5 * DOWN)
        name1.align_to(name, RIGHT)
        name1.shift(0.5 * DOWN)
        matrixString = VGroup(matrixNotation, name1)
        matrixString.move_to(ORIGIN + UP)

        self.play(FadeIn(matrixString))


        # Introduce DP solution
        cut1 = MathTex(r"\text{(B)(CDE)}", color = WHITE).scale(1.3)
        cut1[0][0].set_color(BLUE)
        cut1[0][2].set_color(BLUE)
        cut1[0][3].set_color(BLUE)
        cut1[0][7].set_color(BLUE)
        cut1.align_to(l[0], LEFT)
        cut1.move_to(matrixNotation.get_center())

        cut1Brace1Obj = Brace(cut1[0][0:3], sharpness = 1)
        cut1Brace1Text = MathTex(r"\text{Min. cost to multiply B}").next_to(cut1Brace1Obj, DOWN).scale(0.35).shift(LEFT / 2)
        cut1Brace2Obj = Brace(cut1[0][3:8], sharpness = 1)
        cut1Brace2Text = MathTex(r"\text{Min. cost to multiply CDE}").next_to(cut1Brace2Obj, DOWN).scale(0.35).shift(RIGHT / 3)
        cut1Braces = VGroup(cut1Brace1Obj, cut1Brace1Text, cut1Brace2Obj, cut1Brace2Text)
        cut1Group = VGroup(cut1, cut1Braces)

        cut2 = MathTex(r"\text{(BC)(DE)}", color = WHITE).scale(1.3)
        cut2[0][0].set_color(BLUE)
        cut2[0][3].set_color(BLUE)
        cut2[0][4].set_color(BLUE)
        cut2[0][7].set_color(BLUE)
        cut2.align_to(l[0], LEFT)
        cut2.move_to(cut1.get_center())

        cut2Brace1Obj = Brace(cut2[0][0:4], sharpness = 1)
        cut2Brace1Text = MathTex(r"\text{Min. cost to multiply BC}").next_to(cut2Brace1Obj, DOWN).scale(0.35).shift(LEFT / 3)
        cut2Brace2Obj = Brace(cut2[0][4:8], sharpness = 1)
        cut2Brace2Text = MathTex(r"\text{Min. cost to multiply DE}").next_to(cut2Brace2Obj, DOWN).scale(0.35).shift(RIGHT / 2)
        cut2Braces = VGroup(cut2Brace1Obj, cut2Brace1Text, cut2Brace2Obj, cut2Brace2Text)
        cut2Group = VGroup(cut2, cut2Braces)

        cut3 = MathTex(r"\text{(BCD)(E)}", color = WHITE).scale(1.3)
        cut3[0][0].set_color(BLUE)
        cut3[0][4].set_color(BLUE)
        cut3[0][5].set_color(BLUE)
        cut3[0][7].set_color(BLUE)
        cut3.align_to(l[0], LEFT)
        cut3.move_to(cut2.get_center())

        cut3Brace1Obj = Brace(cut3[0][0:5], sharpness = 1)
        cut3Brace1Text = MathTex(r"\text{Min. cost to multiply BCD}").next_to(cut3Brace1Obj, DOWN).scale(0.35).shift(LEFT / 3)
        cut3Brace2Obj = Brace(cut3[0][5:8], sharpness = 1)
        cut3Brace2Text = MathTex(r"\text{Min. cost to multiply E}").next_to(cut3Brace2Obj, DOWN).scale(0.35).shift(RIGHT / 2)
        cut3Braces = VGroup(cut3Brace1Obj, cut3Brace1Text, cut3Brace2Obj, cut3Brace2Text)
        cut3Group = VGroup(cut3, cut3Braces)

        self.wait(3)
        self.play(FadeOut(matrixString))
        matrixNotation.remove(name1)
        name1.align_to(cut1[0][0], LEFT).shift(LEFT)
        cut1Group.add(name1)
        
        self.play(FadeIn(cut1Group))
        self.wait(4)
        self.play(FadeOut(cut1Group))
        cut1Group.remove(name1)
        name1.align_to(cut2[0][0], LEFT).shift(LEFT)
        cut2Group.add(name1)

        self.play(FadeIn(cut2Group))
        self.wait(4)
        self.play(FadeOut(cut2Group))
        cut2Group.remove(name1)
        name1.align_to(cut3[0][0], LEFT).shift(LEFT)
        cut3Group.add(name1)

        self.play(FadeIn(cut3Group))
        self.wait(4)
        
        showDP = SurroundingRectangle(cut3[0][0:5], color = BLUE, stroke_width = 1.15, buff = 0.04)
        showDP2 = SurroundingRectangle(cut3[0][5:8], color = BLUE, stroke_width = 1.15, buff = 0.04)
        brace = Brace(cut3[0][0:8], direction = DOWN, sharpness = 1)
        text = Tex(r"""\begin{align*}
&\text{If we solve these two smaller, sub-problems, we can then} \\
&\text{use them to find a solution to a larger problem!}
\end{align*}""", color = WHITE).scale(0.4).next_to(brace, DOWN)
        subProblems = VGroup(showDP, showDP2, brace, text)
        self.play(FadeOut(cut3Braces))
        self.play(FadeIn(subProblems))
        self.wait(4)

        end = VGroup(cut3, subProblems, name1)
        self.play(FadeOut(end))
        self.wait()

        text = MathTex(r"\text{What about the cost to multiply the resulting matrices from our sub-problems together?}", color = WHITE).scale(0.6)
        text.move_to(ORIGIN + UP)
        self.play(FadeIn(text))
        self.wait(4)
        self.play(FadeOut(text))
        arr.move_to(ORIGIN)
        self.play(FadeIn(arr))

        # Example 1
        # State 1
        lState1 = [Square(side_length = 1, stroke_width = 1.0) for _ in range(3)]
        arrState1 = VGroup(*lState1).scale(1.0)
        arrState1.arrange(direction = RIGHT, buff = 0)

        c0S1 = MathTex(r"(2, 4)", color = BLUE).scale(0.75)
        c0S1.move_to(lState1[0].get_center())
        c1S1 = MathTex(r"(4, 2)", color = BLUE).scale(0.75)
        c1S1.move_to(lState1[1].get_center())
        c2S1 = MathTex(r"(2, 2)", color = BLUE).scale(0.75)
        c2S1.move_to(lState1[2].get_center())

        arrState1.add(c0S1, c1S1, c2S1)
        arrState1.move_to(arr.get_center())
        arrState1.add(name)

        group = VGroup(l[1], l[2])
        self.play(group.animate.set_fill(color = WHITE, opacity = 0.2))
        self.wait(2)
        self.play(ReplacementTransform(arr, arrState1), run_time = 1.25)
        # State 2
        lState2 = [Square(side_length = 1, stroke_width = 1.0) for _ in range(2)]
        arrState2 = VGroup(*lState2).scale(1.0)
        arrState2.arrange(direction = RIGHT, buff = 0)

        c0S2 = MathTex(r"(2, 2)", color = BLUE).scale(0.75)
        c0S2.move_to(lState2[0].get_center())
        c1S2 = MathTex(r"(2, 2)", color = BLUE).scale(0.75)
        c1S2.move_to(lState2[1].get_center())

        arrState2.add(c0S2, c1S2)
        arrState2.move_to(arr.get_center())
        arrState2.add(name)

        group = VGroup(lState1[0], lState1[1])
        self.play(group.animate.set_fill(color = WHITE, opacity = 0.2))
        self.wait(2)
        self.play(ReplacementTransform(arrState1, arrState2), run_time = 1.25)
        # State 3
        lState3 = [Square(side_length = 1, stroke_width = 1.0) for _ in range(1)]
        arrState3 = VGroup(*lState3).scale(1.0)
        arrState3.arrange(direction = RIGHT, buff = 0)

        c0S3 = MathTex(r"(2, 2)", color = BLUE).scale(0.75)
        c0S3.move_to(lState3[0].get_center())

        arrState3.add(c0S3)
        arrState3.move_to(arrState2.get_center())
        arrState3.add(name)

        group = VGroup(lState2[0], lState2[1])
        self.play(group.animate.set_fill(color = WHITE, opacity = 0.2))
        self.wait(2)
        self.play(ReplacementTransform(arrState2, arrState3), run_time = 1.25)
        self.play(arrState3.animate.move_to(ORIGIN))
        self.wait(3)
        self.play(FadeOut(arrState3))

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
        arr.move_to(ORIGIN)

        self.play(FadeIn(arr))
        self.wait(3)

        # Example 2
        # State 1
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

        group = VGroup(l[0], l[1])
        self.play(group.animate.set_fill(color = WHITE, opacity = 0.2))
        self.wait(2)
        self.play(ReplacementTransform(arr, arrState1), run_time = 1.25)
        self.wait(2)
        # State 2
        lState2 = [Square(side_length = 1, stroke_width = 1.0) for _ in range(2)]
        arrState2 = VGroup(*lState2).scale(1.0)
        arrState2.arrange(direction = RIGHT, buff = 0)

        c0S2 = MathTex(r"(2, 3)", color = BLUE).scale(0.75)
        c0S2.move_to(lState2[0].get_center())
        c1S2 = MathTex(r"(3, 2)", color = BLUE).scale(0.75)
        c1S2.move_to(lState2[1].get_center())

        arrState2.add(c0S2, c1S2)
        arrState2.move_to(arr.get_center())
        arrState2.add(name)

        group = VGroup(lState1[1], lState1[2])
        self.play(group.animate.set_fill(color = WHITE, opacity = 0.2))
        self.wait(2)
        self.play(ReplacementTransform(arrState1, arrState2), run_time = 1.25)
        self.wait(2)
        lState3 = [Square(side_length = 1, stroke_width = 1.0) for _ in range(1)]
        arrState3 = VGroup(*lState3).scale(1.0)
        arrState3.arrange(direction = RIGHT, buff = 0)

        c0S3 = MathTex(r"(2, 2)", color = BLUE).scale(0.75)
        c0S3.move_to(lState3[0].get_center())

        arrState3.add(c0S3)
        arrState3.move_to(arrState2.get_center())
        arrState3.add(name)

        group = VGroup(lState2[0], lState2[1])
        self.play(group.animate.set_fill(color = WHITE, opacity = 0.2))
        self.wait(2)
        self.play(ReplacementTransform(arrState2, arrState3), run_time = 1.25)
        self.play(arrState3.animate.move_to(ORIGIN))
        self.wait(3)
        self.play(FadeOut(arrState3))
        # Show Multiplication
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
        brace = Brace(arr, direction = DOWN, sharpness = 1)
        textStart = MathTex(r"\text{start}").scale(0.5)
        textStart.move_to(l[0].get_center() + UP / 1.25)

        textEnd = MathTex(r"\text{end}").scale(0.5)
        textEnd.move_to(l[3].get_center() + UP / 1.25)
        
        arr.add(c0, c1, c2, c3)
        arr.move_to(ORIGIN)
        text = Tex(r"""\begin{align*}
&\text{The resulting matrix dimensions will be A[start][0] x A[end][1],}\\
&\text{regardless of the order of multiplication}
\end{align*}""").next_to(brace, DOWN).scale(0.6)

        g = VGroup(brace, text, textStart, textEnd)

        self.play(FadeIn(arr))
        temp = VGroup(l[0], l[3])
        self.play(temp.animate.set_fill(color = WHITE, opacity = 0.2))
        self.play(FadeIn(g))
        self.wait(4)
        end = VGroup(g, arr)
        self.play(FadeOut(end))
        self.wait(4)

        text = MathTex(r"\text{Let dp[i][j] represent the minimum cost to multiply matrices A[i ... j]}").scale(0.6)
        text.move_to(ORIGIN)
        self.play(FadeIn(text))
        self.wait(5)
        self.play(FadeOut(text))
        text = MathTex(r"\text{What is our recurrence?}").scale(0.8)
        self.play(FadeIn(text))
        self.wait(4)
        self.play(FadeOut(text))

        textBounds = MathTex(r"i \leq k < j").scale(0.6)
        
        dpRecurrence = MathTex(r"\text{dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + (A[i][0] * A[k][1] * A[j][1]))}").scale(0.6)
        textBounds.next_to(dpRecurrence, 2 * UP)
        textBounds.align_to(dpRecurrence, LEFT)
        dpRecurrence.move_to(ORIGIN)
        g = VGroup(dpRecurrence, textBounds)
        self.play(FadeIn(dpRecurrence[0][0:8]))
        self.wait(1.5)
        self.play(FadeIn(dpRecurrence[0][8:13]))
        self.wait(1.5)
        self.play(FadeIn(dpRecurrence[0][13:22]))
        self.wait(1.5)

        # 1st Sub Problem
        sp1Brace = Brace(dpRecurrence[0][22:30], direction = DOWN, sharpness = 1)
        sp1Text = MathTex(r"\text{minimum cost to multiply matrices A[i ... k]}").next_to(sp1Brace, DOWN).scale(0.4)

        sp1Group = VGroup(textBounds, dpRecurrence[0][22:30], sp1Brace, sp1Text)
        self.play(FadeIn(sp1Group))
        self.wait(3)
        sp1Group.remove(sp1Brace, sp1Text)
        end = VGroup(sp1Brace, sp1Text)
        self.play(FadeOut(end))
        self.wait()
        # 2nd Sub Problem
        sp2Brace = Brace(dpRecurrence[0][31:41], direction = DOWN, sharpness = 1)
        sp2Text = MathTex(r"\text{minimum cost to multiply matrices A[k + 1 ... j]}").next_to(sp2Brace, DOWN).scale(0.4)
        sp2Group = VGroup(dpRecurrence[0][30:41], sp2Brace, sp2Text)
        self.play(FadeIn(sp2Group))
        self.wait(3)
        sp2Group.remove(sp2Brace, sp2Text)
        end = VGroup(sp2Brace, sp2Text)
        self.play(FadeOut(end))
        self.wait()

        # Animate cost

        leftHalf = Rectangle(height = 0.8, width = 3, color = BLUE, stroke_width = 0.9).scale(0.75)
        leftHalf.set_fill(color = WHITE, opacity = 0.2)
        leftHalf.move_to(ORIGIN + LEFT + 2 * DOWN)
        lr = MathTex(r"A[i][0]", color = WHITE).next_to(leftHalf, LEFT).scale(0.5)
        lc = MathTex(r"A[k][1]", color = WHITE).next_to(leftHalf, UP).scale(0.5)
        lc.shift(RIGHT / 1.35 + DOWN / 5)
        lr.shift(RIGHT / 5)

        braceLeft = Brace(leftHalf, direction = DOWN, sharpness = 1.0)
        braceLeftText = MathTex(r"\text{left sub-problem}").next_to(braceLeft, DOWN).scale(0.4)

        left = VGroup(leftHalf, lr, lc, braceLeft, braceLeftText)

        self.play(FadeIn(left))

        rightHalf = Rectangle(height = 0.8, width = 2.5, color = BLUE, stroke_width = 0.9).next_to(leftHalf, RIGHT).scale(0.75)
        rightHalf.set_fill(color = WHITE, opacity = 0.2)
        
        rr = MathTex(r"A[k + 1][0]", color = WHITE).next_to(rightHalf, UP).scale(0.5)
        rc = MathTex(r"A[j][1]", color = WHITE).next_to(rightHalf, RIGHT).scale(0.5)
        rr.move_to(lc.get_center() + 1.5 * RIGHT)
        rc.shift(LEFT / 5)

        braceRight = Brace(rightHalf, direction = DOWN, sharpness = 1.0)
        braceRightText = MathTex(r"\text{right sub-problem}").next_to(braceRight, DOWN).scale(0.4)

        right = VGroup(rightHalf, rr, rc, braceRight, braceRightText)

        self.play(FadeIn(right))

        box1 = SurroundingRectangle(lr, color = BLUE, stroke_width = 1.15, buff = 0.1)
        box2 = SurroundingRectangle(lc, color = BLUE, stroke_width = 1.15, buff = 0.1)
        box3 = SurroundingRectangle(rc, color = BLUE, stroke_width = 1.15, buff = 0.1)

        boxes = VGroup(box1, box2, box3)

        self.play(FadeIn(boxes))

        end = VGroup(boxes, left, right)
        self.wait(2)

        self.play(FadeOut(end))
        self.play(FadeIn(dpRecurrence[0][41:len(dpRecurrence[0])]))
        self.wait(4)

        self.play(FadeOut(g))

        text = MathTex(r"\text{What about our base cases?}").scale(0.8)
        self.wait()
        self.play(FadeIn(text))
        self.wait(4)
        self.play(FadeOut(text))

        text = Tex(r"""\begin{align*}
&\text{If the number of matrices from A[i ... j] = 1 or (i, j)}\\
&\text{is out of bounds (i.e. j $<$ i), then the cost is 0}
\end{align*}""").scale(0.7)
        text.move_to(ORIGIN)
        self.play(FadeIn(text))
        self.wait(6)
        self.play(FadeOut(text))

        self.wait()
        text = MathTex(r"\text{What about our topological ordering?}").scale(0.8)
        text.move_to(ORIGIN)

        self.play(FadeIn(text))
        self.wait(3)
        self.play(FadeOut(text))

        # Explain topological ordering
        leftHalf = Rectangle(height = 0.8, width = 3, color = BLUE, stroke_width = 1.75).scale(1.0)
        leftHalf.set_fill(color = WHITE, opacity = 0.15)
        leftHalf.move_to(ORIGIN + 2 * LEFT + UP / 2)

        l = [Circle(radius = 0.03, stroke_width = 1, fill_color = WHITE, color = WHITE, fill_opacity = 1.0) for _ in range(size)]
        dotsLeft = VGroup(*l).scale(1.0)
        dotsLeft.arrange(direction = RIGHT, buff = 0.15)
        dotsLeft.next_to(leftHalf, LEFT)

        textStart = MathTex(r"i").scale(0.5)
        textStart.next_to(leftHalf, UP / 2)
        textStart.shift(1.5 * LEFT)

        textMid = MathTex(r"k").scale(0.5)
        textMid.next_to(textStart, RIGHT)
        textMid.shift(2.65 * RIGHT)

        leftBraceObj = Brace(leftHalf, sharpness = 1.0, direction = DOWN)
        leftBraceText = MathTex(r"\text{sub-array A[i ... k]}").scale(0.4).next_to(leftBraceObj, DOWN)
        leftBrace = VGroup(leftBraceObj, leftBraceText)

        left = VGroup(leftHalf, dotsLeft, textStart, textMid)

        rightHalf = Rectangle(height = 0.8, width = 3, color = BLUE, stroke_width = 1.75).next_to(leftHalf, RIGHT).scale(1.0)
        rightHalf.set_fill(color = WHITE, opacity = 0.15)

        l2 = [Circle(radius = 0.03, stroke_width = 1, fill_color = WHITE, color = WHITE, fill_opacity = 1.0) for _ in range(size)]
        dotsRight = VGroup(*l2).scale(1.0)
        dotsRight.arrange(direction = RIGHT, buff = 0.15)
        dotsRight.next_to(rightHalf, RIGHT)

        text2Start = MathTex(r"k + 1").scale(0.5)
        text2Start.next_to(textMid, RIGHT)

        text2Mid = MathTex(r"j").scale(0.5)
        text2Mid.next_to(text2Start, RIGHT)
        text2Mid.shift(2.1 * RIGHT)

        rightBraceObj = Brace(rightHalf, sharpness = 1.0, direction = DOWN)
        rightBraceText = MathTex(r"\text{sub-array A[k + 1 ... j]}").scale(0.4).next_to(rightBraceObj, DOWN)
        rightBrace = VGroup(rightBraceObj, rightBraceText)

        right = VGroup(rightHalf, dotsRight, text2Mid, text2Start)

        temp = VGroup(left, right)
        self.play(FadeIn(temp))
        self.wait(2)
        braces = VGroup(leftBrace, rightBrace)
        self.play(FadeIn(braces))
        self.wait(4)

        self.play(FadeOut(braces))
        text = Tex(r"""
\begin{align*}
&\text{for i = n - 1 ... 0:}\\
&\hspace{6mm} \text{for j = i ... n - 1:}
\end{align*}
""").scale(0.7)
        text.move_to(ORIGIN + DOWN)
        self.play(FadeIn(text))
        self.wait(5)
        
        end = VGroup(text, temp)
        self.play(FadeOut(end))

        # Introduce code for chain matrix multiplication

        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{listings}")
        matrixCode = r"""
\begin{lstlisting}[language=Python]
def func(int[][] A):
    int n = A.length
    int[][] dp = new int[n][n]

    for (int i = 0; i < n; i++):
        for (int j = 0; j < n; j++):
            dp[i][j] = INFINITY
            if j <= i:
                dp[i][j] = 0
    
    for (int i = n - 1; i >= 0 i--):
        for (int j = i; j < n; j++):
            for (int k = i; k < n; k++):
                int cost = A[i][0] * A[k][1] * A[j][1]

                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + cost)
    
    return dp[0][n - 1]
\end{lstlisting}
"""
        tex = Tex(matrixCode, tex_template = myTemplate, font_size = 21).scale(.95)
        tex.shift(UP / 2)
        self.wait(1.5)
        self.play(FadeIn(tex[0][0:18]))
        self.wait(1.5)

        self.play(FadeIn(tex[0][18:53]))
        self.wait(1.5)    

        self.play(FadeIn(tex[0][53:127]))
        self.wait(1.5)

        self.play(FadeIn(tex[0][127:169]))
        self.wait(1.5)

        self.play(FadeIn(tex[0][169:267]))
        self.wait(1.5)
        self.play(FadeIn(tex[0][267:len(matrixCode)]))

        self.wait(5)
        self.play(tex.animate.shift(LEFT / 2))

        runtimeState1 = MathTex(r"\mathcal{O}(n^2)").scale(0.85)
        runtimeState2 = MathTex(r"\mathcal{O}(n^2 + n^3)").scale(0.85)
        runtimeFinal = MathTex(r"\mathcal{O}(n^3)").scale(0.85)

        runtimeState1.move_to(ORIGIN + 2 * RIGHT + UP)
        runtimeState2.move_to(runtimeState1.get_center())
        runtimeFinal.move_to(runtimeState2.get_center())

        box1 = SurroundingRectangle(tex[0][53:127], color = BLUE, stroke_width = 1)
        box2 = SurroundingRectangle(tex[0][127:267], color = BLUE, stroke_width = 1)

        self.play(FadeIn(box1))
        self.play(FadeIn(runtimeState1))
        self.wait(3)

        self.play(FadeOut(box1))
        self.play(FadeIn(box2))
        self.play(ReplacementTransform(runtimeState1, runtimeState2))
        self.wait(3)
        self.play(FadeOut(box2))

        self.play(ReplacementTransform(runtimeState2, runtimeFinal))
        self.wait(5)

        end = VGroup(tex, runtimeFinal)
        self.play(FadeOut(end))
        self.wait(5)

        # Burst balloons question
        burstBalloonsQuestion = Tex(r"""
\begin{align*}
&\text{Given a list of balloons A, where A[i] represents the number of coins in $i^{th}$ balloon, you are able to}\\
&\text{burst a balloon i to recieve A[i - 1] * A[i] * A[i + 1] points. Find the maximum score you can receive}\\
&\text{by bursting all the balloons. (if i - 1 or i + 1 goes out-of-bounds, treat it as a balloon with 1 coin)}\\
\end{align*}
""",color = WHITE).scale(0.45)
        burstBalloonsQuestionBox = SurroundingRectangle(burstBalloonsQuestion, color = BLUE, buff = MED_LARGE_BUFF)
        
        burstBalloonsQuestionObj = VGroup(burstBalloonsQuestion, burstBalloonsQuestionBox)
        burstBalloonsQuestionObj.shift(2.5 * UP)

        self.play(FadeIn(burstBalloonsQuestionObj))
        self.wait(4)

        # Shows balloons array
        
        l = [Square(side_length = 1, stroke_width = 1.0) for _ in range(5)]
        arr = VGroup(*l).scale(1.0)
        arr.arrange(direction = RIGHT, buff = 0)

        c0 = MathTex(r"5", color = BLUE).scale(0.75)
        c0.move_to(l[0].get_center())
        c1 = MathTex(r"3", color = BLUE).scale(0.75)
        c1.move_to(l[1].get_center())
        c2 = MathTex(r"1", color = BLUE).scale(0.75)
        c2.move_to(l[2].get_center())
        c3 = MathTex(r"2", color = BLUE).scale(0.75)
        c3.move_to(l[3].get_center())
        c4 = MathTex(r"7", color = BLUE).scale(0.75)
        c4.move_to(l[4].get_center())

        arr.add(c0, c1, c2, c3, c4)
        arr.move_to(ORIGIN + LEFT + DOWN / 2)
        score = MathTex(r"\text{score = 0}", color = WHITE).scale(0.7).next_to(arr, RIGHT)
        score.shift(RIGHT)

        state0 = VGroup(arr, score)

        self.play(FadeIn(state0))

        # Example
        l1 = [Square(side_length = 1, stroke_width = 1.0) for _ in range(4)]
        l2 = [Square(side_length = 1, stroke_width = 1.0) for _ in range(3)]
        l3 = [Square(side_length = 1, stroke_width = 1.0) for _ in range(2)]
        l4 = [Square(side_length = 1, stroke_width = 1.0) for _ in range(1)]

        arr1 = VGroup(*l1).scale(1.0)
        arr2 = VGroup(*l2).scale(1.0)
        arr3 = VGroup(*l3).scale(1.0)
        arr4 = VGroup(*l4).scale(1.0)

        arr1.arrange(direction = RIGHT, buff = 0)
        arr2.arrange(direction = RIGHT, buff = 0)
        arr3.arrange(direction = RIGHT, buff = 0)
        arr4.arrange(direction = RIGHT, buff = 0)

        c0s1 = MathTex(r"5", color = BLUE).scale(0.75)
        c0s1.move_to(l1[0].get_center())
        c1s1 = MathTex(r"1", color = BLUE).scale(0.75)
        c1s1.move_to(l1[1].get_center())
        c2s1 = MathTex(r"2", color = BLUE).scale(0.75)
        c2s1.move_to(l1[2].get_center())
        c3s1 = MathTex(r"7", color = BLUE).scale(0.75)
        c3s1.move_to(l1[3].get_center())

        state1Score = MathTex(r"\text{score = 15}", color = WHITE).scale(0.7)
        arr1.add(c0s1, c1s1, c2s1, c3s1)

        arr1.move_to(arr.get_center())
        state1Score.move_to(score.get_center())

        state1 = VGroup(arr1, state1Score)

        self.wait(4)
        self.play(l[1].animate.set_fill(color = WHITE, opacity = 0.2))
        self.wait(1.5)

        g = VGroup(l[0], l[2])
        self.play(g.animate.set_fill(color = WHITE, opacity = 0.2))
        before = MathTex(r"\text{score = } 5 \cdot 3 \cdot 1", color = WHITE).scale(0.7)
        before.move_to(score.get_center())
        state0.remove(score)
        self.play(ReplacementTransform(score, before))

        state0.add(before)
        self.wait(1.5)

        self.play(ReplacementTransform(state0, state1))

        # State 2
        c0s2 = MathTex(r"5", color = BLUE).scale(0.75)
        c0s2.move_to(l2[0].get_center())
        c1s2 = MathTex(r"1", color = BLUE).scale(0.75)
        c1s2.move_to(l2[1].get_center())
        c2s2 = MathTex(r"7", color = BLUE).scale(0.75)
        c2s2.move_to(l2[2].get_center())

        state2Score = MathTex(r"\text{score = 29}", color = WHITE).scale(0.7)
        arr2.add(c0s2, c1s2, c2s2)

        arr2.move_to(arr1.get_center())
        state2Score.move_to(state1Score.get_center())
        state2 = VGroup(arr2, state2Score)

        self.wait(2)

        self.play(l1[2].animate.set_fill(color = WHITE, opacity = 0.2))
        self.wait(1.5)
        g = VGroup(l1[1], l1[3])
        self.play(g.animate.set_fill(color = WHITE, opacity = 0.2))
        before = MathTex(r"\text{score = 15 + } 1 \cdot 2 \cdot 7", color = WHITE).scale(0.7)
        before.move_to(state1Score.get_center())
        state1.remove(state1Score)
        self.play(ReplacementTransform(state1Score, before))
        self.wait(1.5)
        state1.add(before)
        self.play(ReplacementTransform(state1, state2))

        # State 3
        self.wait(2)

        c0s3 = MathTex(r"1", color = BLUE).scale(0.75)
        c0s3.move_to(l3[0].get_center())
        c1s3 = MathTex(r"7", color = BLUE).scale(0.75)
        c1s3.move_to(l3[1].get_center())

        state3Score = MathTex(r"\text{score = 34}", color = WHITE).scale(0.7)
        arr3.add(c0s3, c1s3)
        arr3.move_to(arr2.get_center())
        state3Score.move_to(state2Score.get_center())

        state3 = VGroup(arr3, state3Score)

        self.play(l2[0].animate.set_fill(color = WHITE, opacity = 0.2))
        helper = MathTex(r"\text{Since i - 1 is out of bounds, we treat is as a balloon of value 1}").scale(0.4)
        helper.move_to(ORIGIN + 1.5 * DOWN)
        g = VGroup(l2[1])
        self.play(g.animate.set_fill(color = WHITE, opacity = 0.2))
        self.play(FadeIn(helper))
        before = MathTex(r"\text{score = 29 + } 1 \cdot 5 \cdot 1", color = WHITE).scale(0.7)
        before.move_to(state2Score.get_center())
        self.wait()
        self.play(FadeOut(helper))
        state2.remove(state2Score)
        self.play(ReplacementTransform(state2Score, before))
        self.wait(1.5)
        state2.add(before)
        self.play(ReplacementTransform(state2, state3))

        

        # State 4
        self.wait(2)
        c0s4 = MathTex(r"1", color = BLUE).scale(0.75)
        c0s4.move_to(l4[0].get_center())
        state4Score = MathTex(r"\text{score = 41}", color = WHITE).scale(0.7)
        arr4.add(c0s4)
        arr4.move_to(arr3.get_center())
        state4Score.move_to(state3Score.get_center())

        state4 = VGroup(arr4, state4Score)
        self.play(l3[1].animate.set_fill(color = WHITE, opacity = 0.2))
        helper = MathTex(r"\text{Since i + 1 is out of bounds, we treat is as a balloon of value 1}").scale(0.4)
        helper.move_to(ORIGIN + 1.5 * DOWN)
        g = VGroup(l3[0])
        self.play(g.animate.set_fill(color = WHITE, opacity = 0.2))
        self.play(FadeIn(helper))
        before = MathTex(r"\text{score = 34 + } 1 \cdot 7 \cdot 1", color = WHITE).scale(0.7)
        before.move_to(state3Score.get_center())
        self.wait(1.5)
        self.play(FadeOut(helper))
        self.wait()
        state3.remove(state3Score)
        self.play(ReplacementTransform(state3Score, before))
        self.wait(1.5)
        state3.add(before)
        self.play(ReplacementTransform(state3, state4))

        # State 5
        self.wait(2)
        self.play(l4[0].animate.set_fill(color = WHITE, opacity = 0.2))

        state5Score = MathTex(r"\text{score = 42}", color = WHITE).scale(0.7)
        state5Score.move_to(state4Score.get_center())

        helper = MathTex(r"\text{Since i + 1 and i - 1 are out of bounds, we treat both of them as balloons of value 1}", color = WHITE).scale(0.4)
        helper.move_to(ORIGIN + 1.5 * DOWN)
        self.play(FadeIn(helper))

        before = MathTex(r"\text{score = 41 + } 1 \cdot 1 \cdot 1", color = WHITE).scale(0.7)
        before.move_to(state4Score.get_center())
        self.wait(1.5)
        self.play(FadeOut(helper))
        state4.remove(state4Score)
        self.play(ReplacementTransform(state4Score, before))
        self.wait(1.5)
        self.play(FadeOut(arr4))
        self.play(ReplacementTransform(before, state5Score))
        self.wait()
        self.play(state5Score.animate.move_to(ORIGIN))
        self.wait(2)
        self.play(FadeOut(state5Score))

        # Explain why array shrinking is not possible

        l = [Square(side_length = 1, stroke_width = 1.0) for _ in range(4)]
        arr0 = VGroup(*l).scale(1.0)
        arr0.arrange(direction = RIGHT, buff = 0)
        c0s0 = MathTex(r"5", color = BLUE).scale(0.75)
        c0s0.move_to(l[0].get_center())
        c1s0 = MathTex(r"3", color = BLUE).scale(0.75)
        c1s0.move_to(l[1].get_center())
        c2s0 = MathTex(r"1", color = BLUE).scale(0.75)
        c2s0.move_to(l[2].get_center())
        c3s0 = MathTex(r"2", color = BLUE).scale(0.75)
        c3s0.move_to(l[3].get_center())

        arr0.add(c0s0, c1s0, c2s0, c3s0)
        arr0.move_to(arr.get_center())
        arr0.shift(RIGHT / 2)

        self.play(FadeIn(arr0))
        self.wait(3)

        tempSquare = Square(side_length = 1.0, stroke_width = 1, color = RED)
        tempSquare.set_fill(color = RED, opacity = 0.2)
        tempSquare.move_to(l[2].get_center())
        t = VGroup(l[2], c2s0)
        self.play(Transform(t, tempSquare))
        brace = Brace(arr0, color = WHITE, direction = DOWN, sharpness = 1)
        text = MathTex(r"\text{These two subarrays become separated even though they should be next to each other!}").scale(0.5).next_to(brace, DOWN)

        temp = VGroup(brace, text)
        self.play(FadeIn(temp))
        self.wait(5)
        end = VGroup(arr0, temp, t)
        self.play(FadeOut(end))

        text = Tex(r"\text{How can we approach this problem in a different way?}").scale(0.7)
        text.move_to(ORIGIN + DOWN)
        self.play(FadeIn(text))
        self.wait(3)
        self.play(FadeOut(text))

        # Show new approach
        center = Square(side_length = 1, color = WHITE, stroke_width = 1.5)
        center.set_fill(color = WHITE, opacity = 0.2)
        left = Rectangle(height = 1, width = 2.2, stroke_width = 1.2, color = BLUE).next_to(center, LEFT, buff = 0.01)
        left.set_fill(color = BLUE, opacity = 0.2)
        right = Rectangle(height = 1, width = 2.2, stroke_width = 1.2, color = BLUE).next_to(center, RIGHT, buff = 0.01)
        right.set_fill(color = BLUE, opacity = 0.2)
        

        leftSquare = Square(side_length = 1, color = WHITE, stroke_width = 1.5).next_to(left, LEFT, buff = 0.01)
        leftSquare.set_fill(color = WHITE, opacity = 0.2)
        rightSquare = Square(side_length = 1, color = WHITE, stroke_width = 1.5).next_to(right, RIGHT, buff = 0.01)
        rightSquare.set_fill(color = WHITE, opacity = 0.2)

        c0 = MathTex(r"1", color = BLUE).scale(0.75)
        c0.move_to(center.get_center())
        c1 = MathTex(r"2", color = BLUE).scale(0.75)
        c1.move_to(leftSquare.get_center())
        c2 = MathTex(r"3", color = BLUE).scale(0.75)
        c2.move_to(rightSquare.get_center())

        textStart = MathTex(r"i").scale(0.6)
        textLeftStart = MathTex(r"i - 1").scale(0.5)
        textLeftStart.move_to(leftSquare.get_center() + UP / 1.5)
        textRightEnd = MathTex(r"j + 1").scale(0.5)
        textRightEnd.move_to(rightSquare.get_center() + UP / 1.5)
        textMid = MathTex(r"k").scale(0.6)
        textMid.move_to(center.get_center() + UP / 1.5)
        textStart.move_to(left.get_center() + UP / 1.5 + LEFT)
        textEnd = MathTex(r"j").scale(0.5)
        textEnd.move_to(right.get_center() + UP / 1.5 + RIGHT)
        newGroup = VGroup(center, left, right, textEnd, textStart, leftSquare, rightSquare, c0, c1, c2, textMid, textLeftStart, textRightEnd)
        newGroup.move_to(ORIGIN + DOWN / 2)

        self.play(FadeIn(newGroup, run_time = 1.25))
        self.wait(5)

        braceLeft = Brace(left, direction = DOWN, sharpness = 1)
        leftText = MathTex(r"\text{the max profit obtainable my bursting balloons i ... k - 1}").scale(0.4).next_to(braceLeft, direction = DOWN)
        leftBraceGroup = VGroup(braceLeft, leftText)
        braceRight = Brace(right, direction = DOWN, sharpness = 1)
        rightText = MathTex(r"\text{the max profit obtainable my bursting balloons k + 1 ... j}").scale(0.4).next_to(braceRight, direction = DOWN)
        rightBraceGroup = VGroup(braceRight, rightText)
        self.play(FadeIn(leftBraceGroup))
        self.wait(4)
        self.play(FadeOut(leftBraceGroup))
        self.play(FadeIn(rightBraceGroup))
        self.wait(4)
        self.play(FadeOut(rightBraceGroup))
        self.wait(2)
        end = VGroup(left, right, textStart, textEnd)
        self.play(FadeOut(end))
        
        temp = VGroup(textLeftStart, leftSquare, c1)
        self.play(temp.animate.shift([center.get_x() - leftSquare.get_x() - 1.0115, 0, 0]))
        self.wait()
        temp = VGroup(textRightEnd, rightSquare, c2)
        self.play(temp.animate.shift([center.get_x() - rightSquare.get_x() + 1.0115, 0, 0]))
        self.wait(2)
        score = MathTex(r"2 \cdot 1 \cdot 3").scale(0.6)
        score.move_to(center.get_center() + 1.5 * UP)
        finalScore = MathTex(r"6").scale(0.6)
        finalScore.move_to(score.get_center())
        self.play(center.animate.set_color(color = RED))
        self.play(FadeIn(score))
        self.wait(2)
        self.play(ReplacementTransform(score, finalScore))
        self.wait(2)
        self.play(center.animate.set_color(color = WHITE))

        end = VGroup(center, leftSquare, rightSquare, c0, c1, c2, textMid, textLeftStart, textRightEnd, finalScore, burstBalloonsQuestionObj)
        self.play(FadeOut(end))
        self.wait(2.5)

        center = Square(side_length = 1, color = WHITE, stroke_width = 1.5)
        center.set_fill(color = WHITE, opacity = 0.2)
        left = Rectangle(height = 1, width = 2.2, stroke_width = 1.2, color = BLUE).next_to(center, LEFT, buff = 0.01)
        left.set_fill(color = BLUE, opacity = 0.2)
        right = Rectangle(height = 1, width = 2.2, stroke_width = 1.2, color = BLUE).next_to(center, RIGHT, buff = 0.01)
        right.set_fill(color = BLUE, opacity = 0.2)
        

        leftSquare = Square(side_length = 1, color = WHITE, stroke_width = 1.5).next_to(left, LEFT, buff = 0.01)
        leftSquare.set_fill(color = WHITE, opacity = 0.2)
        rightSquare = Square(side_length = 1, color = WHITE, stroke_width = 1.5).next_to(right, RIGHT, buff = 0.01)
        rightSquare.set_fill(color = WHITE, opacity = 0.2)

        c0 = MathTex(r"1", color = BLUE).scale(0.75)
        c0.move_to(center.get_center())
        c1 = MathTex(r"2", color = BLUE).scale(0.75)
        c1.move_to(leftSquare.get_center())
        c2 = MathTex(r"3", color = BLUE).scale(0.75)
        c2.move_to(rightSquare.get_center())

        textStart = MathTex(r"i").scale(0.6)
        textLeftStart = MathTex(r"i - 1").scale(0.5)
        textLeftStart.move_to(leftSquare.get_center() + UP / 1.5)
        textRightEnd = MathTex(r"j + 1").scale(0.5)
        textRightEnd.move_to(rightSquare.get_center() + UP / 1.5)
        textMid = MathTex(r"k").scale(0.6)
        textMid.move_to(center.get_center() + UP / 1.5)
        textStart.move_to(left.get_center() + UP / 1.5 + LEFT)
        textEnd = MathTex(r"j").scale(0.5)
        textEnd.move_to(right.get_center() + UP / 1.5 + RIGHT)
        newGroup = VGroup(center, left, right, textEnd, textStart, leftSquare, rightSquare, c0, c1, c2, textMid, textLeftStart, textRightEnd)
        newGroup.move_to(ORIGIN + DOWN / 2)

        stateDefinition = MathTex(r"\text{let dp[i][j] represent the maximum profit that can be obtained by bursting balloons A[i ... j]}").scale(0.55)
        stateDefinition.move_to(ORIGIN)
        self.play(FadeIn(stateDefinition))
        self.wait(5)
        self.play(FadeOut(stateDefinition))

        text = MathTex(r"\text{What is our recurrence?}").scale(0.8)
        self.play(FadeIn(text))
        self.wait(4)
        self.play(FadeOut(text))



        # Show recurrence
        c0 = MathTex(r"A[k]", color = BLUE).scale(0.45)
        c0.move_to(center.get_center())
        c1 = MathTex(r"A[i - 1]", color = BLUE).scale(0.45)
        c1.move_to(leftSquare.get_center())
        c2 = MathTex(r"A[j + 1]", color = BLUE).scale(0.45)
        c2.move_to(rightSquare.get_center())

        newGroup = VGroup(center, left, right, textEnd, textStart, leftSquare, rightSquare, c0, c1, c2, textMid, textLeftStart, textRightEnd)
        newGroup.move_to(ORIGIN + 1.5 * UP)

        self.play(FadeIn(newGroup))

        recurrenceBalloons = MathTex(r"\text{dp[i][j] = max(dp[i][j], dp[i][k - 1] + dp[k + 1][j] + A[i - 1] * A[k] * A[j + 1])}").scale(0.55)
        recurrenceBalloons.move_to(newGroup.get_center() + 2.5 * DOWN)
        helper1 = MathTex(r"i \leq k \leq j").scale(0.55).next_to(recurrenceBalloons, UP, buff = 0.5)
        helper1.shift(4 * LEFT)
        self.wait(3)
        self.play(FadeIn(recurrenceBalloons[0][0:9]))
        self.wait(1.5)
        self.play(FadeIn(recurrenceBalloons[0][9:22]))
        self.wait(1.5)

        # Show left sub problem
        braceLeftObj = Brace(left, sharpness = 1, direction = DOWN)
        braceLeftText = MathTex(r"\text{the maximum profit obtainable by bursting balloons A[i ... k - 1]}").scale(0.4).next_to(braceLeftObj, direction = DOWN)

        braceLeft = VGroup(braceLeftObj, braceLeftText)
        self.play(FadeIn(braceLeft))
        self.wait(2)
        temp = VGroup(helper1, recurrenceBalloons[0][22:32])
        self.play(FadeOut(braceLeft))
        self.play(FadeIn(temp))
        self.wait(1.5)

        braceRightObj = Brace(right, sharpness = 1, direction = DOWN)
        braceRightText = MathTex(r"\text{the maximum profit obtainable by bursting balloons A[k + 1 ... j]}").scale(0.4).next_to(braceRightObj, direction = DOWN)
        braceRight = VGroup(braceRightObj, braceRightText)
        self.play(FadeIn(braceRight))
        self.wait(2)
        self.play(FadeOut(braceRight))
        self.play(FadeIn(recurrenceBalloons[0][32:43]))
        self.wait(1.5)
        temp = VGroup(left, textStart)
        self.play(FadeOut(temp))
        temp = VGroup(c1, textLeftStart, leftSquare)
        self.play(temp.animate.shift([center.get_x() - leftSquare.get_x() - 1.0115, 0, 0]))
        self.wait(1.5)

        temp = VGroup(right, textEnd)
        self.play(FadeOut(temp))
        temp = VGroup(c2, textRightEnd, rightSquare)

        self.play(temp.animate.shift([center.get_x() - rightSquare.get_x() + 1.0115, 0, 0]))

        tempGroup = VGroup(leftSquare, center, rightSquare)
        cBrace = Brace(tempGroup, direction = DOWN, sharpness = 1)
        clarification = MathTex(r"\text{if i - 1 or j + 1 is out of bounds, then we treat it as a balloon of value 1}").scale(0.35).next_to(cBrace, direction = DOWN)

        cGroup = VGroup(cBrace, clarification)
        self.wait(1.5)
        self.play(FadeIn(cGroup))
        self.wait(4)
        self.play(FadeOut(cGroup))
        self.play(center.animate.set_color(color = RED))

        score = MathTex(r"\text{A[i - 1] * A[k] * A[j + 1]}").scale(0.4)
        score.move_to(center.get_center() + DOWN)
        self.wait(1.5)
        self.play(FadeIn(score))
        self.wait(1.5)

        end = VGroup(score, c0, c1, c2, leftSquare, center, rightSquare, textLeftStart, textMid, textRightEnd)
        self.play(FadeOut(end))
        self.play(FadeIn(recurrenceBalloons[0][43:len(recurrenceBalloons[0])]))
        self.wait()
        temp = VGroup(recurrenceBalloons, helper1)
        self.play(temp.animate.shift(UP))
        self.wait(5)
        self.play(FadeOut(temp))

        text = MathTex(r"\text{What are our base cases?}").scale(0.8)
        self.play(FadeIn(text))
        self.wait(4)
        self.play(FadeOut(text))

        text = MathTex(r"\text{if i $>$ j, then that means that we are out of bounds, so the max profit obtainable is 0}").scale(0.5)
        text.move_to(ORIGIN + UP / 2)
        self.play(FadeIn(text))
        self.wait(5)
        self.play(FadeOut(text))

        text = MathTex(r"\text{What about our topological ordering?}").scale(0.8)
        text.move_to(ORIGIN)

        self.play(FadeIn(text))
        self.wait(3)
        self.play(FadeOut(text))

        # Topological Ordering
        center = Square(side_length = 1, color = WHITE, stroke_width = 1.5)
        center.set_fill(color = WHITE, opacity = 0.2)
        left = Rectangle(height = 1, width = 2.2, stroke_width = 1.2, color = BLUE).next_to(center, LEFT, buff = 0.01)
        left.set_fill(color = BLUE, opacity = 0.2)
        right = Rectangle(height = 1, width = 2.2, stroke_width = 1.2, color = BLUE).next_to(center, RIGHT, buff = 0.01)
        right.set_fill(color = BLUE, opacity = 0.2)
        

        textStart = MathTex(r"i").scale(0.6)
        textMid = MathTex(r"k").scale(0.6)
        textMid.move_to(center.get_center() + UP / 1.5)
        textStart.move_to(left.get_center() + UP / 1.5 + LEFT)
        textEnd = MathTex(r"j").scale(0.5)
        textEnd.move_to(right.get_center() + UP / 1.5 + RIGHT)
        newGroup = VGroup(center, left, right, textStart, textMid, textEnd)
        newGroup.move_to(ORIGIN + UP)
        self.play(FadeIn(newGroup))

        braceLeftObj = Brace(left, direction = DOWN, sharpness = 1)
        textLeft = MathTex(r"\text{dp[i ... k - 1]}").scale(0.4).next_to(braceLeftObj, direction = DOWN)
        braceRightObj = Brace(right, direction = DOWN, sharpness = 1)
        textRight = MathTex(r"\text{dp[k + 1 ... j]}").scale(0.4).next_to(braceRightObj, direction = DOWN)

        braces = VGroup(braceLeftObj, textLeft, braceRightObj, textRight)
        self.wait(2)
        self.play(FadeIn(braces))
        self.wait(4)
        self.play(FadeOut(braces))
        text = Tex(r"""
\begin{align*}
&\text{for i = n - 1 ... 0:}\\
&\hspace{6mm} \text{for j = i ... n - 1:}\\
&\hspace{12mm} \text{for k = i ... j:}
\end{align*}
""").scale(0.6)
        text.move_to(ORIGIN + 1.5 * DOWN)
        self.play(FadeIn(text[0][0:26]))
        self.wait(6)
        self.play(FadeIn(text[0][26:len(text[0])]))
        self.wait(3)

        end = VGroup(text, newGroup)
        self.play(FadeOut(end))
        self.wait(3)

        # Introduce burst balloons code
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{listings}")
        matrixCode = r"""
\begin{lstlisting}[language=Python]
def func(int[][] A):
    int n = A.length
    int[][] dp = new int[n][n]

    for (int i = n - 1; i >= 0; i--):
        for (int j = i; j < n; j++):
            for (int k = i; k <= j; k++):
                int left = 0
                int right = 0
                int leftCoins = 1
                int rightCoins = 1

                if i - 1 >= 0:
                    leftCoins = A[i - 1]
                
                if j + 1 < n:
                    rightCoins = A[j + 1]
                
                if i <= k - 1:
                    left = dp[i][k - 1]
                
                if k + 1 <= j:
                    right = dp[k + 1][j]
                
                dp[i][j] = max(dp[i][j], left + right + (leftCoins * A[k] * rightCoins))
    
    return dp[0][n - 1]
\end{lstlisting}
"""
        tex = Tex(matrixCode, tex_template = myTemplate, font_size = 21).scale(.8)
        self.play(FadeIn(tex[0][0:18]))
        self.wait(2)
        self.play(FadeIn(tex[0][18:53]))
        self.wait(2)
        self.play(FadeIn(tex[0][53:117]))
        self.wait(2)
        self.play(FadeIn(tex[0][117:165]))
        self.wait(2)
        self.play(FadeIn(tex[0][165:190]))
        self.wait(2)
        self.play(FadeIn(tex[0][190:215]))
        self.wait(2)
        self.play(FadeIn(tex[0][215:239]))
        self.wait(2)
        self.play(FadeIn(tex[0][239:264]))
        self.wait(2)
        self.play(FadeIn(tex[0][264:325]))
        self.wait(2)
        self.play(FadeIn(tex[0][325:len(tex[0])]))
        self.wait(3)
        rec = SurroundingRectangle(tex[0][53:325], color = BLUE, stroke_width = 1.2)
        self.play(FadeIn(rec))
        self.wait(2)
        text = MathTex(r"\mathcal{O}(n^3)").scale(0.85)
        text.move_to(ORIGIN + 2 * RIGHT + UP)
        self.play(FadeOut(rec))
        self.play(FadeIn(text))
        self.wait(3)
        end = VGroup(text, tex)
        self.play(FadeOut(end))
        self.wait(2)

        # LeetCode binary tree dp