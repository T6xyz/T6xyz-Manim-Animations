from manim import * 
import sys
sys.path.insert(1, '/Users/t6xyz/Desktop/T6xyz-Lectures/misc')
from intro import playIntro

class LectureDP1(Scene):
    def construct(self):

        # 1. Intro to the lecture "intro to dynammic programming"
        introText = Text("Intro To Dynamic Programming",color = WHITE).scale(0.75)
        introBox = SurroundingRectangle(introText, color = BLUE, buff = MED_LARGE_BUFF)
        introObj = VGroup(introText, introBox)
        introObj.shift(2.25 * UP)

        self.play(FadeIn(introObj))
        self.wait(3)
        self.play(FadeOut(introObj))
        # 2. Fibonnaci Intro
        introQuestion = MathTex(r"\text{Given an integer n, where n} \geq \text{0, find the nth fibonnaci number.}",color = WHITE).scale(0.75)
        introQuestionBox = SurroundingRectangle(introQuestion, color = BLUE, buff = MED_LARGE_BUFF)
        
        introQuestionObj = VGroup(introQuestionBox, introQuestion)
        introQuestionObj.shift(2.5 * UP)

        self.play(FadeIn(introQuestionObj))
        self.wait(4)
        # 3. Define fibonacci
        fibonnaciDef = MathTex(r"F_n = F_{n-1} + F_{n-2}", color = WHITE).scale(0.75)
        fibonnaciDef.shift(1.25 * UP)
        self.play(FadeIn(fibonnaciDef))
        self.wait(2)

        fibBC1 = MathTex(r"F_1 = 1", color = WHITE).scale(0.75)
        fibBC2 = MathTex(r"F_0 = 0", color = WHITE).scale(0.75)

        fibBC1.move_to(fibonnaciDef.get_center() + LEFT + (DOWN / 2))
        fibBC2.move_to(fibBC1.get_center() + (DOWN / 2))
        
        self.play(FadeIn(fibBC1))
        self.wait(1.5)
        self.play(FadeIn(fibBC2))
        self.wait(2)

        fibEquations = VGroup(fibonnaciDef, fibBC1, fibBC2)
        self.play(fibEquations.animate.shift(3.9 * LEFT))
        self.wait(3)

        # 4. Pseudocode for Brute Force 
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{listings}")
        fibCode = r"""
\begin{lstlisting}[language=Python]
def F(int n):
    if (n == 0):
        return 0

    if (n == 1):
        return 1

    return F(n - 1) + F(n - 2)
\end{lstlisting}
"""
        tex = Tex(fibCode, tex_template = myTemplate, font_size = 23)
        tex.shift(RIGHT)
        self.play(FadeIn(tex[0][0:11]))
        self.wait(2)
        self.play(FadeIn(tex[0][11:27]))
        self.wait(2)
        self.play(FadeIn(tex[0][27:43]))
        self.wait(2)
        self.play(FadeIn(tex[0][43:63]))

        
        

        # 5. Runtime analysis 
        self.play(FadeOut(fibEquations))
        self.play(tex.animate.shift(4 * LEFT))

        t1 = MathTex(r"F(4)", color = WHITE).scale(0.75)
        t2 = MathTex(r"F(3)", color = WHITE).scale(0.75)
        t3 = MathTex(r"F(2)", color = WHITE).scale(0.75)
        t4 = MathTex(r"F(2)", color = WHITE).scale(0.75)
        t5 = MathTex(r"F(1)", color = WHITE).scale(0.75)
        t6 = MathTex(r"F(1)", color = WHITE).scale(0.75)
        t7 = MathTex(r"F(0)", color = WHITE).scale(0.75)
        t8 = MathTex(r"F(1)", color = WHITE).scale(0.75)
        t9 = MathTex(r"F(0)", color = WHITE).scale(0.75)

        t1.shift(1.5 * RIGHT + UP)
        t2.move_to(t1.get_center() + 2.5 * LEFT + DOWN)
        t3.move_to(t1.get_center() + 2.5 * RIGHT + DOWN)
        t4.move_to(t2.get_center() + 1.5 * LEFT + DOWN)
        t5.move_to(t2.get_center() + 1.5 * RIGHT + DOWN)
        t6.move_to(t3.get_center() + 1.5 * LEFT + DOWN)
        t7.move_to(t3.get_center() + 1.5 * RIGHT + DOWN)
        t8.move_to(t4.get_center() + LEFT + DOWN)
        t9.move_to(t4.get_center() + RIGHT + DOWN)


        a1 = Arrow(start = t1.get_center(), end = t2.get_center(), color = WHITE, buff = 50, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.60)
        a2 = Arrow(start = t1.get_center(), end = t3.get_center(), color = WHITE, buff = 50, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.60)
        a3 = Arrow(start = t2.get_center(), end = t4.get_center(), color = WHITE, buff = 50, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.60)
        a4 = Arrow(start = t2.get_center(), end = t5.get_center(), color = WHITE, buff = 50, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.60)
        a5 = Arrow(start = t3.get_center(), end = t6.get_center(), color = WHITE, buff = 50, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.60)
        a6 = Arrow(start = t3.get_center(), end = t7.get_center(), color = WHITE, buff = 50, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.60)
        a7 = Arrow(start = t4.get_center(), end = t8.get_center(), color = WHITE, buff = 50, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.60)
        a8 = Arrow(start = t4.get_center(), end = t9.get_center(), color = WHITE, buff = 50, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.60)

        treeExample = Text("Example:  find  F(4)", color = WHITE).scale(0.75)
        treeExample.move_to(t1.get_center() + (UP / 1.1))
        temp = VGroup(treeExample, t1, t2, t3, t4, t5, t6, t7, t8, t9, a1, a2, a3, a4, a5, a6, a7, a8).scale(0.60)
        
        temp.shift(2 * RIGHT)
        self.play(FadeIn(temp))
        self.wait(3)

        height = DoubleArrow( end = 1.82 * DOWN + LEFT, buff=0, tip_length=0.1, stroke_width = 0.6)
        height.shift(0.9 * RIGHT + (UP / 1.6))
        heightText = MathTex("n", color = WHITE).scale(0.6)
        heightText.move_to(height.get_center() + (LEFT / 6.5))

        levels = VGroup(height, heightText)
        self.play(FadeIn(levels))
        self.wait(2)

        levelBox = Rectangle(width = .9, height = .35, color = BLUE, stroke_width = 2)
        levelBox.move_to(t1.get_center())
        self.play(FadeIn(levelBox))
        self.wait()
        self.play(levelBox.animate.stretch_to_fit_width(3.8))
        self.play(levelBox.animate.shift(DOWN / 1.65))
        self.wait()
        self.play(levelBox.animate.stretch_to_fit_width(5.5))
        self.play(levelBox.animate.shift(DOWN / 1.65))
        self.wait()
        self.play(levelBox.animate.stretch_to_fit_width(1.9))
        self.play(levelBox.animate.shift(DOWN / 1.65 + 2.36 * LEFT))
        self.wait()
        self.play(FadeOut(levelBox))

        self.wait(2)
        runtimeEx1 = MathTex(r"\mathcal{O}(2^n)", color = WHITE).scale(0.7)
        runtimeEx1.shift(RIGHT / 2.25 + 2 * DOWN)
        self.play(FadeIn(runtimeEx1))
        self.wait(2)
        self.play(runtimeEx1.animate.set_color(RED))
        tempText = Text("This is pretty bad... imagine if we had n = 60", color = WHITE).scale(0.3)
        tempText.move_to(runtimeEx1.get_center() + 2.5 * RIGHT)
        self.play(FadeIn(tempText))
        self.wait(4)

        textQuestion = Text("Is there a more optimal solution?").scale(0.75)
        self.wait()

        endItems = VGroup(tempText, runtimeEx1, levels, temp, tex)
        self.play(FadeOut(endItems))
        self.play(FadeIn(textQuestion))
        self.wait(3)

        textAnswer = Text("Yes, we can use dynamic programming").scale(0.75)
        self.play(FadeOut(textQuestion))
        self.play(FadeIn(textAnswer))
        self.wait(2)

        endFibQuestion = VGroup(introQuestionObj, textAnswer)
        self.play(FadeOut(endFibQuestion))

        # 6. Introduce Dynamic Programming

        self.wait(3)
        questionWhatIsDP = Text("So, what exactly is dynamic programming?").scale(0.75)
        self.play(FadeIn(questionWhatIsDP))
        self.wait(2)
        self.play(FadeOut(questionWhatIsDP))

        self.wait()

        whatIsDP = Text("Dynamic Programming is the concept of solving smaller, simpler, and often " + 
                        "overlapping sub-problems \nand utilizing the solutions to those sub-problems to solve a larger, more complex problem.", line_spacing = 1.5).scale(0.4)

        self.play(FadeIn(whatIsDP))
        self.wait(6)

        # 7. The two types of DP

        self.play(FadeOut(whatIsDP))
        self.wait(3)

        topDownVsBottomUp = Text("Top-Down DP vs Bottom-Up DP").scale(0.75)
        box = SurroundingRectangle(topDownVsBottomUp, color = BLUE, buff = MED_LARGE_BUFF)
        smallNote = Text("* DP is the shorthand notation for dynamic programming").scale(0.25)
        smallNote.move_to(box.get_center() + DOWN)

        comparisonGroup = VGroup(topDownVsBottomUp, box, smallNote)

        self.play(FadeIn(comparisonGroup))
        self.play(comparisonGroup.animate.shift(2.5 * UP))
        self.wait(2)

        # Add bulleted lists
        topDownText = Text("Top-Down DP:").scale(0.45)
        topDownText.move_to(comparisonGroup.get_center() + 1.5 * DOWN + 2.2 * LEFT)
        self.play(FadeIn(topDownText))

        topDownDP = BulletedList("Start from the larger sub-problem first and build up to smaller sub-problems", 
                                 "Solve sub-problems via recursion", 
                                 "Utilizes memoization to store sub-problem solutions").scale(0.45)
        bottomUpText = Text("Bottom-Up DP:").scale(0.45)
        bottomUpDP = BulletedList("Start from the bases cases and build up to larger sub-problems", 
                                  "Solve sub-problems via iteration",
                                  "Typically uses an array to store sub-problem solutions").scale(0.45)
        # Top-down DP animations
        topDownDP.move_to(comparisonGroup.get_center() + 2.5 * DOWN + RIGHT)
        self.play(FadeIn(topDownDP))
        self.wait()
        # Bottom-up DP animations
        bottomUpText.move_to(comparisonGroup.get_center() + 3.5 * DOWN + 2.2 * LEFT)
        self.play(FadeIn(bottomUpText))
        bottomUpDP.move_to(comparisonGroup.get_center() + 4.5 * DOWN + RIGHT / 3.15)
        self.play(FadeIn(bottomUpDP))
        self.wait()


        remove = VGroup(topDownText, topDownDP)
        self.play(FadeOut(remove))
        bottomUP = VGroup(bottomUpDP, bottomUpText)
        self.play(bottomUP.animate.shift(2.15 * UP))
        self.wait(4)
        end = VGroup(bottomUP, comparisonGroup)
        self.play(FadeOut(end))
        self.wait()


        #8. 4 main parts of a DP problem

        fourTypesText = Text("Four Main Components of a DP Solution").scale(0.75)
        box = SurroundingRectangle(fourTypesText, color = BLUE, buff = MED_LARGE_BUFF)
        fourTypes = VGroup(fourTypesText, box)
        self.play(DrawBorderThenFill(fourTypes))
        self.play(fourTypes.animate.shift(2.5 * UP))
        self.wait()

        # 1. Table Definition
        tableDef = Text("State Definition:").scale(0.45)
        tableDefText = Text("The representation of each sub-problem").scale(0.45)

        # 2. Base Cases
        baseCaseDef = Text("Base Case/s:").scale(0.45)
        baseCaseDefText = Text("The simplest sub-problems which need little to no computation to solve").scale(0.45)


        # 3. Recurrence
        recurrenceDef = Text("Recurrence: ").scale(0.45)
        recurrenceDefText = Text("How we relate smaller sub-problems to solve a larger sub-problem ").scale(0.45)


        # 4. Topological ordering
        orderingDef = Text("Topological ordering: ").scale(0.45)
        orderingDefText = Text("The way we run our iterations such that it satisfies our recurrence").scale(0.45)

        dpTexts = VGroup(tableDef, tableDefText,
                         baseCaseDef, baseCaseDefText,
                         recurrenceDef, recurrenceDefText,
                         orderingDef, orderingDefText)
        
        dpTexts.arrange(DOWN, center = False, aligned_edge = LEFT)
        dpTexts.shift(3 * LEFT + UP)
        tableDefText.shift(RIGHT / 2)
        baseCaseDefText.shift(RIGHT / 2)
        orderingDefText.shift(RIGHT / 2)
        recurrenceDefText.shift(RIGHT / 2)

        self.play(FadeIn(tableDef))
        self.play(FadeIn(tableDefText))
        self.wait(3)

        self.play(FadeIn(baseCaseDef))
        self.play(FadeIn(baseCaseDefText))
        self.wait(3)

        self.play(FadeIn(recurrenceDef))
        self.play(FadeIn(recurrenceDefText))
        self.wait(3)

        self.play(FadeIn(orderingDef))
        self.play(FadeIn(orderingDefText))
        self.wait(3)

        self.wait(2)
        end = VGroup(dpTexts, fourTypes)
        self.play(FadeOut(end))

        ################################################################################################

        # Revisit Fibonacci example
        self.play(FadeIn(introQuestionObj))
        self.play(FadeIn(fibEquations))
        self.wait()

        # Create Decision Tree
        dtText = Text("Decision Tree:").scale(0.5)
        dtText.move_to(dtText.get_center() + 3.75 * RIGHT + 1.25 * UP)
        self.play(FadeIn(dtText))
        self.wait()

        n1 = MathTex(r"4", color = WHITE)
        n2 = MathTex(r"3", color = WHITE)
        n3 = MathTex(r"2", color = WHITE)
        n4 = MathTex(r"2", color = WHITE)
        n5 = MathTex(r"1", color = WHITE)
        n6 = MathTex(r"1", color = WHITE)
        n7 = MathTex(r"0", color = WHITE)
        n8 = MathTex(r"1", color = WHITE)
        n9 = MathTex(r"0", color = WHITE)
        duplicateFib1 = n3
        duplicateFib2 = n4

        n1.move_to(dtText.get_center() + UP / 4 + RIGHT / 4)

        n2.move_to(n1.get_center() + 2.5 * LEFT + DOWN)
        n3.move_to(n1.get_center() + 2.5 * RIGHT + DOWN)
        n4.move_to(n2.get_center() + 1.5 * LEFT + DOWN)
        n5.move_to(n2.get_center() + 1.5 * RIGHT + DOWN)
        n6.move_to(n3.get_center() + 1.5 * LEFT + DOWN)
        n7.move_to(n3.get_center() + 1.5 * RIGHT + DOWN)
        n8.move_to(n4.get_center() + LEFT + DOWN)
        n9.move_to(n4.get_center() + RIGHT + DOWN)

        a1 = Arrow(start = n1.get_center(), end = n2.get_center(), color = WHITE, buff = 55, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        a2 = Arrow(start = n1.get_center(), end = n3.get_center(), color = WHITE, buff = 55, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        a3 = Arrow(start = n2.get_center(), end = n4.get_center(), color = WHITE, buff = 55, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        a4 = Arrow(start = n2.get_center(), end = n5.get_center(), color = WHITE, buff = 55, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        a5 = Arrow(start = n3.get_center(), end = n6.get_center(), color = WHITE, buff = 55, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        a6 = Arrow(start = n3.get_center(), end = n7.get_center(), color = WHITE, buff = 55, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        a7 = Arrow(start = n4.get_center(), end = n8.get_center(), color = WHITE, buff = 55, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        a8 = Arrow(start = n4.get_center(), end = n9.get_center(), color = WHITE, buff = 55, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)

        g = VGroup(n1, n2, n3, n4, n5, n6, n7, n8, n9,
                   a1, a2, a3, a4, a5, a6, a7, a8).scale(0.5)
        self.play(FadeIn(n1))
        self.wait(2)

        n1L = VGroup(a1, n2)
        n1R = VGroup(a2, n3)
        self.play(FadeIn(n1L))
        self.wait()
        self.play(FadeIn(n1R))
        self.wait(2)

        n2L = VGroup(a3, n4)
        n2R = VGroup(a4, n5)
        self.play(FadeIn(n2L))
        self.wait()
        self.play(FadeIn(n2R))
        self.wait(2)

        n3L = VGroup(a5, n6)
        n3R = VGroup(a6, n7)
        self.play(FadeIn(n3L))
        self.wait()
        self.play(FadeIn(n3R))
        self.wait(2)

        n4L = VGroup(a7, n8)
        n4R = VGroup(a8, n9)
        self.play(FadeIn(n4L))
        self.wait()
        self.play(FadeIn(n4R))
        self.wait(2)
        ###################################################################
        # Transformed Fibonacci Tree
        ###################################################################
        nt1 = Text(r"dp[4]", color = WHITE).scale(0.65)
        nt2 = Text(r"dp[3]", color = WHITE).scale(0.65)
        nt3 = Text(r"dp[2]", color = WHITE).scale(0.65)
        nt4 = Text(r"dp[2]", color = WHITE).scale(0.65)
        nt5 = Text(r"dp[1]", color = WHITE).scale(0.65)
        nt6 = Text(r"dp[1]", color = WHITE).scale(0.65)
        nt7 = Text(r"dp[0]", color = WHITE).scale(0.65)
        nt8 = Text(r"dp[1]", color = WHITE).scale(0.65)
        nt9 = Text(r"dp[0]", color = WHITE).scale(0.65)
        duplicateFib1 = nt3
        duplicateFib2 = nt4

        nt1.move_to(dtText.get_center() + UP / 4 + RIGHT / 4)

        nt2.move_to(nt1.get_center() + 2.5 * LEFT + DOWN)
        nt3.move_to(nt1.get_center() + 2.5 * RIGHT + DOWN)
        nt4.move_to(nt2.get_center() + 1.5 * LEFT + DOWN)
        nt5.move_to(nt2.get_center() + 1.5 * RIGHT + DOWN)
        nt6.move_to(nt3.get_center() + 1.5 * LEFT + DOWN)
        nt7.move_to(nt3.get_center() + 1.5 * RIGHT + DOWN)
        nt8.move_to(nt4.get_center() + LEFT + DOWN)
        nt9.move_to(nt4.get_center() + RIGHT + DOWN)

        at1 = Arrow(start = nt1.get_center(), end = nt2.get_center(), color = WHITE, buff = 85, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        at2 = Arrow(start = nt1.get_center(), end = nt3.get_center(), color = WHITE, buff = 85, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        at3 = Arrow(start = nt2.get_center(), end = nt4.get_center(), color = WHITE, buff = 85, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        at4 = Arrow(start = nt2.get_center(), end = nt5.get_center(), color = WHITE, buff = 85, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        at5 = Arrow(start = nt3.get_center(), end = nt6.get_center(), color = WHITE, buff = 85, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        at6 = Arrow(start = nt3.get_center(), end = nt7.get_center(), color = WHITE, buff = 85, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        at7 = Arrow(start = nt4.get_center(), end = nt8.get_center(), color = WHITE, buff = 85, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        at8 = Arrow(start = nt4.get_center(), end = nt9.get_center(), color = WHITE, buff = 85, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)

        g2 = VGroup(nt1, nt2, nt3, nt4, nt5, nt6, nt7, nt8, nt9,
            at1, at2, at3, at4, at5, at6, at7, at8).scale(0.5)
        
        stateFib = Text("State:").scale(0.4)
        stateFibText = Text("Let dp[i] represent the i-th Fibonnaci number").scale(0.4)
        baseCaseFib = Text("Base Cases:").scale(0.4)
        baseCaseFibText = Text("dp[0] = 0 and dp[1] = 1").scale(0.4)
        recurrenceFib = Text("Recurrence:").scale(0.4)
        recurrenceFibText = Text("dp[i] = dp[i - 1] + dp[i - 2]").scale(0.4)
        orderingFib = Text("Topological Ordering").scale(0.4)
        orderingFibText = Text("need to solve for i - 1 and i - 2 before solving for i").scale(0.4)

        x = VGroup(stateFib, stateFibText,
                   baseCaseFib, baseCaseFibText,
                   recurrenceFib, recurrenceFibText,
                   orderingFib, orderingFibText).arrange(direction = DOWN, aligned_edge = LEFT).scale(0.9).next_to(ORIGIN,DR)
        x.shift(6 * LEFT)
        stateFibText.shift(RIGHT / 2)
        baseCaseFibText.shift(RIGHT / 2)
        recurrenceFibText.shift(RIGHT / 2)
        orderingFibText.shift(RIGHT / 2)
        
        temp = VGroup(stateFib, stateFibText)
        self.play(FadeIn(temp))
        self.play(ReplacementTransform(g, g2))
        self.wait(3)

        # Clear up what are the base cases are
        s1 = Rectangle(width = 1.3, height = 1, color = BLUE, stroke_width = 0.8)
        s2 = Rectangle(width = 0.6, height = 0.4, color = BLUE, stroke_width = 0.8)
        s3 = Rectangle(width = 2.3, height = 0.4, color = BLUE, stroke_width = 0.8)
        s4 = Rectangle(width = 1.6, height = 0.4, color = BLUE, stroke_width = 0.8)
        s1.move_to(fibEquations.get_center() + LEFT + DOWN / 4.5)
        s2.move_to(n5.get_center())
        s3.move_to(n6.get_center() + RIGHT / 1.3)
        s4.move_to(n8.get_center() + RIGHT / 2)

        baseCaseGroup = VGroup(s1, s2, s3, s4)
        self.play(FadeIn(baseCaseGroup))
        self.wait(3)
        self.play(FadeOut(baseCaseGroup))
        temp = VGroup(baseCaseFib, baseCaseFibText)
        self.play(FadeIn(temp))
        self.wait(3)

        # Recurrence 
        s1 = Rectangle(width = 3.25, height = 0.5 , color = BLUE, stroke_width = 0.8)
        s2 = Rectangle(width = 3.2, height = 0.9, color = BLUE, stroke_width = 0.8)
        s1.shift(3.9 * LEFT + 1.26 * UP)
        s2.move_to(n1.get_center() + DOWN / 3.2)

        recurrenceGroup = VGroup(s1, s2)
        self.play(FadeIn(recurrenceGroup))
        self.wait(2)
        self.play(s2.animate.stretch_to_fit_width(2.4))
        self.play(s2.animate.shift(DOWN / 2.2 + 1.3 * LEFT))
        self.wait()
        self.play(s2.animate.shift(2.6 * RIGHT))
        self.wait(2)
        self.play(FadeOut(recurrenceGroup))
        temp = VGroup(recurrenceFibText, recurrenceFib)
        self.play(FadeIn(temp))
        self.wait(3)
        # Topological Ordering
        firstIndex = Rectangle(height = 1, width = 0.5, color = WHITE)
        suffix = Rectangle(height = 1, width = 3, color = BLUE)
        index0 = MathTex("i", color = BLUE).scale(0.7)
        indexSuffix = MathTex("0 ... i - 1", color = BLUE).scale(0.7)
        firstIndex.set_fill(color = WHITE, opacity = 0.2)
        suffix.set_fill(color = BLUE, opacity = 0.2)
        arr = VGroup(firstIndex, suffix).arrange(direction = LEFT, buff = 0).scale(0.9)
        index0.move_to(firstIndex.get_center() + UP / 1.5)
        indexSuffix.move_to(suffix.get_center() + UP / 1.5)
        arr.add(index0, indexSuffix)
        temp = VGroup(dtText, g2)
        arr.move_to(g2.get_center())
        self.play(FadeOut(temp))
        self.wait()
        self.play(FadeIn(arr))
        self.wait(2.5)
        self.play(FadeOut(arr))
        temp = VGroup(orderingFib, orderingFibText)
        self.play(FadeIn(temp))
        self.wait(2.5)

        end = VGroup(x, fibEquations)
        self.play(FadeOut(end))
        self.wait(3)

        # fib DP code
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{listings}")
        fibCode = r"""
\begin{lstlisting}[language=Python]
def F(int n):
    if (n == 0):
        return 0

    if (n == 1):
        return 1

    int[] dp = new int[n + 1]
    dp[0] = 0
    dp[1] = 1

    for (int i = 2; i <= n; i++):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]
\end{lstlisting}
"""
        tex = Tex(fibCode, tex_template = myTemplate, font_size = 23)
        tex.shift(DOWN / 1.75)
        self.play(FadeIn(tex[0][0:11]))
        self.wait()
        self.play(FadeIn(tex[0][11:43]))
        self.wait()
        self.play(FadeIn(tex[0][43:62]))
        self.wait()
        self.play(FadeIn(tex[0][62:76]))
        self.wait()
        self.play(FadeIn(tex[0][76:97]))
        self.wait()
        self.play(FadeIn(tex[0][97:118]))
        self.wait()
        self.play(FadeIn(tex[0][118:131]))
        self.wait(3)

        self.play(tex.animate.shift(2.25 * LEFT))
        self.wait()
        s1 = Rectangle(height = 0.8, width = 5, color = BLUE, stroke_width = 2)
        s1.shift(1.9 * DOWN + 2 * LEFT)
        self.play(FadeIn(s1))
        self.wait(2)
        self.play(FadeOut(s1))

        newRuntime = MathTex(r"\mathcal{O}(n)", color = WHITE).scale(0.7)
        newRuntime.shift(1 * RIGHT)
        self.play(FadeIn(newRuntime))

        exp = Tex(r"This is way faster then our previous runtime of $\mathcal{O}(2^n)$!").scale(0.4)
        exp.move_to(newRuntime.get_center() + 2.9 * RIGHT)
        self.play(newRuntime.animate.set_color(GREEN))
        self.play(FadeIn(exp))
        self.wait(4)

        end = VGroup(newRuntime, exp, tex, introQuestionObj)
        self.play(FadeOut(end))
        self.wait(3)

        secondQuestion = Tex(r"Given a matrix of size m x n, find the number of paths starting from (0, 0) to (m - 1, n - 1) given that you can only move down or right.").scale(0.70)
        secondQuestionBox = SurroundingRectangle(secondQuestion, color = BLUE, buff = MED_LARGE_BUFF)
        secondQuestionObj = VGroup(secondQuestion, secondQuestionBox)
        secondQuestionObj.shift(2.5 * UP)
        self.play(FadeIn(secondQuestionObj)) 
        self.wait()
        size = 5
        l = [Square(side_length = 0.8, stroke_width = 0.95) for _ in range(size ** 2)]
        squares = VGroup(*l).scale(0.65)

        squares.arrange_in_grid(rows = size, cols = size, buff = 0)
        rowTag = MathTex("m").scale(0.7)
        colTag = MathTex("n").scale(0.7)

        rowTag.move_to(squares.get_center() + 1.55 * LEFT)
        colTag.move_to(squares.get_center() + 1.5 * UP)
        squares.add(rowTag)
        squares.add(colTag)
        squares.shift(3.5 * LEFT + DOWN / 2)

        self.play(FadeIn(squares))
        examplePath1 = VGroup(l[0], l[1], l[2], l[3], l[4], l[9], l[14], l[19], l[24])
        examplePath2 = VGroup(l[0], l[5], l[6], l[11], l[12], l[17], l[18], l[19], l[24])
        examplePath3 = VGroup(l[0], l[5], l[10], l[15], l[16], l[17], l[18], l[19], l[24])
        self.play(examplePath1.animate.set_fill(color = BLUE, opacity = 0.4))
        self.wait()
        self.play(examplePath1.animate.set_fill(color = BLUE, opacity = 0))
        self.wait(0.5)
        self.play(examplePath2.animate.set_fill(color = BLUE, opacity = 0.4))
        self.wait()
        self.play(examplePath2.animate.set_fill(color = BLUE, opacity = 0))
        self.wait(0.5)
        self.play(examplePath3.animate.set_fill(color = BLUE, opacity = 0.4))
        self.wait()
        self.play(examplePath3.animate.set_fill(color = BLUE, opacity = 0))
        self.wait(1.5)
        

        tmp = Text("Backtracking using DFS?").scale(0.55)
        tmp.shift(1.25 * RIGHT)

        self.play(FadeIn(tmp))
        self.wait(2)
        self.play(tmp.animate.set_color(RED))
        self.wait(3)
        self.play(FadeOut(tmp))
        dtText.shift(1.5 * LEFT)
        self.play(FadeIn(dtText))
        n1 = Text(r"(0, 0)").scale(0.55)
        n2 = Text(r"(1, 0)").scale(0.55)
        n3 = Text(r"(0, 1)").scale(0.55)
        n4 = Text(r"(2, 0)").scale(0.55)
        n5 = Text(r"(1, 1)").scale(0.55)
        n6 = Text(r"(1, 1)").scale(0.55)
        n7 = Text(r"(0, 2)").scale(0.55)

        n2.move_to(n1.get_center() + 2.5 * LEFT + DOWN)
        n3.move_to(n1.get_center() + 2.5 * RIGHT + DOWN)
        n4.move_to(n2.get_center() + 1.5 * LEFT + DOWN)
        n5.move_to(n2.get_center() + 1.5 * RIGHT + DOWN)
        n6.move_to(n3.get_center() + 1.5 * LEFT + DOWN)
        n7.move_to(n3.get_center() + 1.5 * RIGHT + DOWN)

        a1 = Arrow(start = n1.get_center(), end = n2.get_center(), color = WHITE, buff = 85, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        a2 = Arrow(start = n1.get_center(), end = n3.get_center(), color = WHITE, buff = 85, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        a3 = Arrow(start = n2.get_center(), end = n4.get_center(), color = WHITE, buff = 85, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        a4 = Arrow(start = n2.get_center(), end = n5.get_center(), color = WHITE, buff = 85, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        a5 = Arrow(start = n3.get_center(), end = n6.get_center(), color = WHITE, buff = 85, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        a6 = Arrow(start = n3.get_center(), end = n7.get_center(), color = WHITE, buff = 85, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)

        dtGroup = VGroup(n1, n2, n3, n4, n5, n6, n7,
        a1, a2, a3, a4, a5, a6).scale(0.6)
        dtGroup.move_to(dtText.get_center() + DOWN)
        # Branch 1
        self.play(FadeIn(n1))
        self.play(l[0].animate.set_fill(color = BLUE, opacity = 0.4))
        self.wait()

        tmp = VGroup(a1, n2)
        self.play(l[5].animate.set_fill(color = BLUE, opacity = 0.4))
        self.play(FadeIn(tmp))
        self.wait()

        tmp = VGroup(a2, n3)
        self.play(l[1].animate.set_fill(color = BLUE, opacity = 0.4))
        self.play(FadeIn(tmp))
        self.wait()

        end = VGroup(l[0], l[5], l[1])
        self.play(end.animate.set_fill(color = BLUE, opacity = 0))
        self.wait()

        # Branch 2
        self.play(l[5].animate.set_fill(color = BLUE, opacity = 0.4))
        self.wait()

        tmp = VGroup(n4, a3)
        self.play(l[10].animate.set_fill(color = BLUE, opacity = 0.4))
        self.play(FadeIn(tmp))
        self.wait()

        tmp = VGroup(n5, a4)
        self.play(l[6].animate.set_fill(color = BLUE, opacity = 0.4))
        self.play(FadeIn(tmp))
        self.wait()

        end = VGroup(l[6], l[5], l[10])
        self.play(end.animate.set_fill(color = BLUE, opacity = 0))
        self.wait()

        # Branch 3
        self.play(l[1].animate.set_fill(color = BLUE, opacity = 0.4))
        self.wait()

        tmp = VGroup(n6, a5)
        self.play(l[6].animate.set_fill(color = BLUE, opacity = 0.4))
        self.play(FadeIn(tmp))
        self.wait()

        tmp = VGroup(n7, a6)
        self.play(l[2].animate.set_fill(color = BLUE, opacity = 0.4))
        self.play(FadeIn(tmp))
        self.wait()

        end = VGroup(l[1], l[6], l[2])
        self.play(end.animate.set_fill(color = BLUE, opacity = 0))
        self.wait()

        c1 = Circle(radius = 0.14, color = WHITE, fill_opacity = 1)
        c2 = Circle(radius = 0.14, color = WHITE, fill_opacity = 1)
        c3 = Circle(radius = 0.14, color = WHITE, fill_opacity = 1)
        cg1 = VGroup(c1, c2, c3).arrange(direction = DOWN, buff = 1.5).scale(0.06)
        cg1.move_to(n4.get_center() + DOWN / 3.25)

        c4 = Circle(radius = 0.14, color = WHITE, fill_opacity = 1)
        c5 = Circle(radius = 0.14, color = WHITE, fill_opacity = 1)
        c6 = Circle(radius = 0.14, color = WHITE, fill_opacity = 1)   
        cg2 = VGroup(c4, c5, c6).arrange(direction = DOWN, buff = 1.5).scale(0.06)
        cg2.move_to(n5.get_center() + DOWN / 3.25)

        c7 = Circle(radius = 0.14, color = WHITE, fill_opacity = 1)
        c8 = Circle(radius = 0.14, color = WHITE, fill_opacity = 1)
        c9 = Circle(radius = 0.14, color = WHITE, fill_opacity = 1)   
        cg3 = VGroup(c7, c8, c9).arrange(direction = DOWN, buff = 1.5).scale(0.06)
        cg3.move_to(n6.get_center() + DOWN / 3.25)

        c10 = Circle(radius = 0.14, color = WHITE, fill_opacity = 1)
        c11 = Circle(radius = 0.14, color = WHITE, fill_opacity = 1)
        c12 = Circle(radius = 0.14, color = WHITE, fill_opacity = 1)   
        cg4 = VGroup(c10, c11, c12).arrange(direction = DOWN, buff = 1.5).scale(0.06)
        cg4.move_to(n7.get_center() + DOWN / 3.25)

        dotGroup = VGroup(cg1, cg2, cg3, cg4)
        self.play(FadeIn(dotGroup))
        self.wait()
        self.play(FadeOut(squares))
        dtGroup.add(dotGroup, dtText)

        self.play(dtGroup.animate.shift(6 * LEFT))
        self.wait()


        reccurenceBox = Rectangle(width = 3.75, height = 1, color = BLUE, stroke_width = 0.8)
        reccurenceBox.move_to(dtText.get_center() + DOWN / 1.5)
        self.play(FadeIn(reccurenceBox))
        self.wait(2)

        self.play(reccurenceBox.animate.stretch_to_fit_width(3))
        self.play(reccurenceBox.animate.stretch_to_fit_height(0.95))
        self.play(reccurenceBox.animate.shift(1.5 * LEFT + DOWN / 1.6))
        self.wait(2)
        self.play(reccurenceBox.animate.shift(3 * RIGHT))
        self.wait(2)
        self.play(FadeOut(reccurenceBox))
        # Show recurrence relationship
        tempText = Text("If we solve for the number of paths if we go down and " +
                         "the number of \npaths if we go right,then we know the number of paths starting at (r, c)", line_spacing = 1.5).scale(0.35)
        tempText.move_to(dtText.get_center() + 6.5 * RIGHT + DOWN)
        self.play(FadeIn(tempText))
        self.wait(3)
        self.play(FadeOut(tempText))
        #############################################################
        n1 = Text(r"dp[0][0]").scale(0.45)
        n2 = Text(r"dp[1][0]").scale(0.45)
        n3 = Text(r"dp[0][1]").scale(0.45)
        n4 = Text(r"dp[2][0]").scale(0.45)
        n5 = Text(r"dp[1][1]").scale(0.45)
        n6 = Text(r"dp[1][1]").scale(0.45)
        n7 = Text(r"dp[0][2]").scale(0.45)

        duplicateMatrix1 = n5
        duplicateMatrix2 = n6

        n2.move_to(n1.get_center() + 2.5 * LEFT + DOWN)
        n3.move_to(n1.get_center() + 2.5 * RIGHT + DOWN)
        n4.move_to(n2.get_center() + 1.5 * LEFT + DOWN)
        n5.move_to(n2.get_center() + 1.5 * RIGHT + DOWN)
        n6.move_to(n3.get_center() + 1.5 * LEFT + DOWN)
        n7.move_to(n3.get_center() + 1.5 * RIGHT + DOWN)

        a1 = Arrow(start = n1.get_center(), end = n2.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        a2 = Arrow(start = n1.get_center(), end = n3.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        a3 = Arrow(start = n2.get_center(), end = n4.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        a4 = Arrow(start = n2.get_center(), end = n5.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        a5 = Arrow(start = n3.get_center(), end = n6.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        a6 = Arrow(start = n3.get_center(), end = n7.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)

        dtGroup2 = VGroup(n1, n2, n3, n4, n5, n6, n7,
        a1, a2, a3, a4, a5, a6).scale(0.6)
        dtGroup2.move_to(dtText.get_center() + DOWN)

        stateMatrixHeader = Text("State:").scale(0.5)
        stateMatrixText = Text("Let dp[r][c] represent the number of paths starting from (r, c)").scale(0.45)

        cg1.move_to(n4.get_center() + DOWN / 3.25)
        cg2.move_to(n5.get_center() + DOWN / 3.25)
        cg3.move_to(n6.get_center() + DOWN / 3.25)
        cg4.move_to(n7.get_center() + DOWN / 3.25)
        dotGroup = VGroup(cg1, cg2, cg3, cg4)
        dtGroup2.add(dotGroup, dtText)

        recurrenceMatrixHeader = Text("Recurrence:").scale(0.5)
        matrixRecurrenceText = Text("dp[r][c] = dp[r + 1][c] + dp[r][c + 1]").scale(0.45)
    
        matrixGroup = VGroup(stateMatrixHeader, stateMatrixText,
                             recurrenceMatrixHeader, matrixRecurrenceText).arrange(direction = DOWN, aligned_edge = LEFT).scale(0.9)
        matrixGroup.move_to(dtText.get_center() + 6.5 * RIGHT + 1.5 * DOWN)
        stateMatrixText.shift(RIGHT / 2)
        matrixRecurrenceText.shift(RIGHT / 2)
        braceLeft = Brace(matrixRecurrenceText[9:19], direction = DOWN, stroke_width = 0.05)
        braceLeftText = braceLeft.get_text(r"Number of paths if we go down").scale(0.45)
        braceLeftGroup = VGroup(braceLeft, braceLeftText)
        braceRight = Brace(matrixRecurrenceText[20:30], direction = DOWN, stroke_width = 0.05)
        braceRightText = braceRight.get_text(r"Number of paths if we go right").scale(0.45)
        braceRightGroup = VGroup(braceRight, braceRightText)

        self.play(FadeIn(stateMatrixHeader))
        self.play(FadeIn(stateMatrixText))
        self.play(Transform(dtGroup, dtGroup2, replace_mobject_with_target_in_scene = False))
        self.wait(2)
        self.play(FadeIn(recurrenceMatrixHeader))
        self.wait()

        self.play(FadeIn(matrixRecurrenceText[0:9]))
        self.wait(2)
        self.play(FadeIn(matrixRecurrenceText[9:19]))
        self.play(FadeIn(braceLeftGroup))
        self.wait(2)

        self.play(FadeOut(braceLeftGroup))
        self.play(FadeIn(matrixRecurrenceText[19:30]))
        self.play(FadeIn(braceRightGroup))
        self.wait(2)
        self.play(FadeOut(braceRightGroup))
        self.wait(3)
        end = VGroup(matrixGroup, dtGroup2, dtGroup)
        self.play(FadeOut(end))

        # Topological ordering
        matrixRecurrenceText.move_to(ORIGIN + 3.5 * LEFT)
        
        matrixBox = Square(side_length = 5, color = BLUE)
        curr = Square(side_length = 0.5, color = WHITE)
        curr.align_to(matrixBox, LEFT)
        curr.align_to(matrixBox, UP)
        matrixBox.set_fill(color = BLUE, opacity = 0.2)
        curr.set_fill(color = WHITE, opacity = 0.2)
        index = MathTex("(r, c)", color = WHITE).scale(0.7)
        index.move_to(curr.get_center() + UP / 1.5)

        indexTop = MathTex("(r, c + 1) ... (r, n - 1)", color = WHITE).scale(0.7)

        indexLeft0 = MathTex("(r + 1, c)", color = WHITE).scale(0.7)
        indexLeft1 = MathTex(".", color = WHITE).scale(0.7)
        indexLeft2 = MathTex(".", color = WHITE).scale(0.7)
        indexLeft3 = MathTex(".", color = WHITE).scale(0.7)
        indexLeft4 = MathTex("(m - 1, c)", color = WHITE).scale(0.7)
    
        indexLeft = VGroup(indexLeft0, indexLeft1, indexLeft2, indexLeft3, indexLeft4).arrange(direction = DOWN, buff = 0.05)
        indexLeft.move_to(curr.get_center() + 1.3 * LEFT + 1.5 * DOWN)
        indexTop.move_to(curr.get_center() + UP / 1.5 + 3 * RIGHT)
        matrixOrderingExample = VGroup(matrixBox, curr, index, indexLeft, indexTop).scale(0.6)
        textMatrixOrdering = Text("We need to solve for (r + 1, c) and (r, c + 1) before we can solve for (r, c). This means" + 
                                  "\n we need to iterate from m - 1 ... r and n - 1 ... c in order to satisfy our recurrence.", color = WHITE, line_spacing = 1.5).scale(0.4)
        
        matrixOrderingExample.move_to(ORIGIN + 2 * RIGHT + DOWN / 2)
        textMatrixOrdering.move_to(ORIGIN)
        self.play(FadeIn(matrixRecurrenceText))
        self.play(FadeIn(matrixOrderingExample))
        self.wait(6)
        temp = VGroup(matrixRecurrenceText, matrixOrderingExample)
        self.play(FadeOut(temp))
        self.play(FadeIn(textMatrixOrdering))
        self.wait(6)
        self.play(FadeOut(textMatrixOrdering))


        whatAreBC = Text("What about our base cases?").scale(0.75)
        self.play(FadeIn(whatAreBC))
        self.wait(4)
        self.play(FadeOut(whatAreBC))
        self.play(FadeIn(squares))
        self.wait(2)

        lastRow = VGroup(l[23], l[22], l[21], l[20])
        lastColumn = VGroup(l[24], l[19], l[14], l[9], l[4])

        self.play(l[24].animate.set_fill(color = BLUE, opacity = 0.4))
        self.wait(2)
        self.play(l[23].animate.set_fill(color = BLUE, opacity = 0.4))
        self.wait(2)
        self.play(l[18].animate.set_fill(color = RED, opacity = 0.4))
        self.wait(2)
        self.play(l[18].animate.set_fill(color = BLUE, opacity = 0))
        self.wait(2)
        self.play(l[22].animate.set_fill(color = BLUE, opacity = 0.4))
        self.wait()
        self.play(l[21].animate.set_fill(color = BLUE, opacity = 0.4))
        self.play(l[20].animate.set_fill(color = BLUE, opacity = 0.4))
        self.wait(3)
        self.play(lastRow.animate.set_fill(color = BLUE, opacity = 0))

        self.play(l[19].animate.set_fill(color = BLUE, opacity = 0.4))
        self.wait(2)
        self.play(l[18].animate.set_fill(color = RED, opacity = 0.4))
        self.wait(2)
        self.play(l[18].animate.set_fill(color = BLUE, opacity = 0))
        self.wait(2)
        self.play(l[14].animate.set_fill(color = BLUE, opacity = 0.4))
        self.wait()
        self.play(l[9].animate.set_fill(color = BLUE, opacity = 0.4))
        self.play(l[4].animate.set_fill(color = BLUE, opacity = 0.4))
        self.wait(3)
        self.play(lastColumn.animate.set_fill(color = BLUE, opacity = 0))
        self.play(FadeOut(squares))


        baseCaseMatrixText = Text("For each (r,  c) that is either in the last row or the " +
                                  "last column, \nthere is only one path to reach (m - 1, n - 1)", line_spacing = 1.5).scale(0.6)
        
        baseCaseMatrixGroup = VGroup(baseCaseMatrixText).arrange(direction = DOWN, aligned_edge = LEFT).scale(0.9).next_to(ORIGIN,DR)
        baseCaseMatrixGroup.move_to(ORIGIN)
        self.play(FadeIn(baseCaseMatrixText))
        self.wait(4)
        self.play(FadeOut(baseCaseMatrixGroup))
        self.wait()

        # Matrix Code
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{listings}")
        matrixCode = r"""
\begin{lstlisting}[language=Python]
def findPaths(int[][] grid):
    int m = grid.length
    int n = grid[0].length
    int[][] dp = new int[m][n]

    for (int c = n - 1; c >= 0; c--):
        dp[m-1][c] = 1
    
    for (int r = m - 1; r >= 0; r--):
        dp[r][n-1] = 1
    
    for (int r = m - 2; r >= 0; r--):
        for (int c = n - 2; c >= 0; c--):
            dp[r][c] = dp[r+1][c] + dp[r][c+1]
    
    return dp[0][0]
\end{lstlisting}
"""
        tex = Tex(matrixCode, tex_template = myTemplate, font_size = 23)
        tex.shift(DOWN + 3 * LEFT)
        self.play(FadeIn(tex[0][0:26]))
        self.wait()
        self.play(FadeIn(tex[0][26:83]))
        self.wait()
        self.play(FadeIn(tex[0][83:118]))
        self.wait()
        self.play(FadeIn(tex[0][118:153]))
        self.wait()
        self.play(FadeIn(tex[0][153:199]))
        self.wait()
        self.play(FadeIn(tex[0][199:229]))
        self.wait()
        self.play(FadeIn(tex[0][229:243]))
        self.wait(2)
        
        # Example run-through of a 4x4 grid
        size = 4
        l = [Square(side_length = 0.8, stroke_width = 0.95) for _ in range(size ** 2)]
        matrixExample = VGroup(*l).scale(0.65)

        matrixExample.arrange_in_grid(rows = size, cols = size, buff = 0)
        name = Text("dp =").scale(0.45)
        name.move_to(matrixExample.get_center() + 1.5 * LEFT)
        problem2Example = VGroup(matrixExample, name)
        problem2Example.move_to(tex.get_center() + 5.5 * RIGHT)

        self.play(FadeIn(problem2Example))
        self.play(tex[0][83:118].animate.set_color(BLUE))

        l11 = MathTex(r"1", color = BLUE).scale(0.5)
        l11.move_to(l[11].get_center())
        l7 = MathTex(r"1", color = BLUE).scale(0.5)
        l7.move_to(l[7].get_center())
        l3 = MathTex(r"1", color = BLUE).scale(0.5)
        l3.move_to(l[3].get_center())
        l15 = MathTex(r"1", color = BLUE).scale(0.5)
        l15.move_to(l[15].get_center())

        lastColumnDP = VGroup(l11, l7, l3, l15)
        self.wait(2)
        self.play(FadeIn(lastColumnDP))
        self.play(tex[0][83:118].animate.set_color(WHITE))


        l14 = MathTex(r"1", color = BLUE).scale(0.5)
        l14.move_to(l[14].get_center())
        l13 = MathTex(r"1", color = BLUE).scale(0.5)
        l13.move_to(l[13].get_center())
        l12 = MathTex(r"1", color = BLUE).scale(0.5)
        l12.move_to(l[12].get_center())
        self.play(tex[0][118:153].animate.set_color(BLUE))
        lastRowDP = VGroup(l14, l13, l12)
        self.wait(2)
        self.play(FadeIn(lastRowDP))
        self.wait()
        self.play(tex[0][118:153].animate.set_color(WHITE))
        

        ans = [20, 10, 4, 1, 10, 6, 3, 1, 4, 3, 2, 1, 1, 1, 1, 1]
        # run iterations
        iterationBox = Square(side_length = 0.8, color = BLUE, stroke_width = 2).scale(0.65)
        end = VGroup(problem2Example, iterationBox, lastColumnDP, lastRowDP)
        iterationBox.move_to(l[10].get_center())
        self.play(tex[0][153:229].animate.set_color(BLUE))
        self.play(FadeIn(iterationBox))
        for i in range(10, -1, -1):
            if i == 3 or i == 7:
                continue    
            self.play(iterationBox.animate.move_to(l[i].get_center()))
            self.wait()
            self.play(l[i + 4].animate.set_fill(color = WHITE, opacity = 0.2))
            self.play(l[i + 1].animate.set_fill(color = WHITE, opacity = 0.2))
            self.wait()
            sum = MathTex(f"{ans[i]}", color = BLUE).scale(0.5)
            sum.move_to(l[i].get_center())
            end.add(sum)
            self.play(FadeIn(sum))
            # tmp = VGroup(l[i + 4], l[i + 1])
            self.play(l[i + 1].animate.set_fill(color = WHITE, opacity = 0))
            self.play(l[i + 4].animate.set_fill(color = WHITE, opacity = 0))
            self.wait()
        self.play(tex[0][153:229].animate.set_color(WHITE))
        self.wait()
        self.play(l[0].animate.set_fill(color = WHITE, opacity = 0.2))
        self.wait()
        self.play(FadeOut(end))
        # Runtime analysis
        bc1Runtime = MathTex(r"\mathcal{O}(n)", color = WHITE).scale(0.7)
        bc2Runtime = MathTex(r"\mathcal{O}(n + m)", color = WHITE).scale(0.7)
        orderRuntime = MathTex(r"\mathcal{O}(n + m + mn)", color = WHITE).scale(0.7)
        finalRuntime = MathTex(r"\mathcal{O}(mn)", color = WHITE).scale(0.7)
        bc1Runtime.move_to(tex.get_center() + 4.5 * RIGHT + UP)
        bc2Runtime.move_to(tex.get_center() + 4.5 * RIGHT + UP)
        orderRuntime.move_to(tex.get_center() + 4.5 * RIGHT + UP)
        finalRuntime.move_to(tex.get_center() + 4.5 * RIGHT + UP)
        
        self.play(tex[0][83:118].animate.set_color(BLUE))
        self.play(FadeIn(bc1Runtime))
        self.wait()

        self.play(tex[0][83:118].animate.set_color(WHITE))
        self.play(tex[0][118:153].animate.set_color(BLUE))
        self.play(Transform(bc1Runtime, bc2Runtime, replace_mobject_with_target_in_scene = False))
        self.wait()

        self.play(tex[0][118:153].animate.set_color(WHITE))
        self.play(tex[0][153:229].animate.set_color(BLUE))
        self.play(Transform(bc1Runtime, orderRuntime, replace_mobject_with_target_in_scene = False))
        self.wait()

        self.play(tex[0][153:229].animate.set_color(WHITE))
        self.play(Transform(bc1Runtime, finalRuntime, replace_mobject_with_target_in_scene = False))
        self.wait()
        self.play(bc1Runtime.animate.set_color(color = GREEN))
        self.wait(3)

        end = VGroup(tex, secondQuestionObj, bc1Runtime)
        self.play(FadeOut(end))
        self.wait(3)

        thirdQuestion = Tex(r"\text{Given an array of integers costs, where costs[i] represents the profit of robbing the i-th house,}" + 
                            r"\\ \text{find the maximum profit a robber can obtain given that they can't rob an adjacent house at any house i.}").scale(0.70)
        thirdQuestionBox = SurroundingRectangle(thirdQuestion, color = BLUE, buff = MED_LARGE_BUFF)
        thirdQuestionObj = VGroup(thirdQuestion, thirdQuestionBox).scale(0.75)
        thirdQuestionObj.shift(2.5 * UP)
        self.play(FadeIn(thirdQuestionObj)) 
        self.wait()
        size = 6

        l = [Square(side_length = 1, stroke_width = 1.0) for _ in range(size)]
        costsArray = VGroup(*l).scale(0.8)

        costsArray.arrange(direction = RIGHT, buff = 0)
        name = Text("costs =").scale(0.55)
        name.move_to(l[0].get_center() + LEFT)
        c0 = MathTex(r"3", color = BLUE).scale(0.75)
        c0.move_to(l[0].get_center())
        c1 = MathTex(r"1", color = BLUE).scale(0.75)
        c1.move_to(l[1].get_center())
        c2 = MathTex(r"4", color = BLUE).scale(0.75)
        c2.move_to(l[2].get_center())
        c3 = MathTex(r"5", color = BLUE).scale(0.75)
        c3.move_to(l[3].get_center())
        c4 = MathTex(r"2", color = BLUE).scale(0.75)
        c4.move_to(l[4].get_center())
        c5 = MathTex(r"3", color = BLUE).scale(0.75)
        c5.move_to(l[5].get_center())
        # 3 1 4 5 2 3
        costsArray.add(name, c0, c1, c2, c3, c4, c5)
        costsArray.shift(UP / 2)
        self.play(FadeIn(costsArray))
        self.wait()

        # 0. Run Example
        self.play(l[1].animate.set_fill(color = WHITE, opacity = 0.2))
        adj = VGroup(l[0], l[2])
        self.play(adj.animate.set_fill(color = RED, opacity = 0.2))
        end = VGroup(adj, l[1])
        self.wait()
        self.play(end.animate.set_fill(color = WHITE, opacity = 0))
        self.wait()

        self.play(l[3].animate.set_fill(color = WHITE, opacity = 0.2))
        adj = VGroup(l[4], l[2])
        self.play(adj.animate.set_fill(color = RED, opacity = 0.2))
        end = VGroup(adj, l[3])
        self.wait()
        self.play(end.animate.set_fill(color = WHITE, opacity = 0))
        self.wait()
        # 1. Run example/create decision tree
        dtText.move_to(l[2].get_center() + DOWN + RIGHT / 2)
        self.play(FadeIn(dtText))

        index = MathTex(r"i", color = BLUE).scale(0.7)
        indexBox = Square(side_length = 1, color = WHITE).scale(0.8)
        indexBox.set_fill(color = WHITE, opacity = 0.2)
        indexBox.move_to(l[0].get_center())
        index.move_to(l[0].get_center() + UP / 1.5)
        indexPointer = VGroup(index, indexBox)

        # Decision Tree
        nBad = Text(r"i = 0", color = RED).scale(0.55)

        n1 = Text(r"i = 0", color = WHITE).scale(0.55)

        n2 = Text(r"i = 1", color = WHITE).scale(0.55)
        n3 = Text(r"i = 2", color = WHITE).scale(0.55)

        n4 = Text(r"i = 2", color = WHITE).scale(0.55)
        n5 = Text(r"i = 3", color = WHITE).scale(0.55)
        n6 = Text(r"i = 3", color = WHITE).scale(0.55)
        n7 = Text(r"i = 4", color = WHITE).scale(0.55)

        n8 = Text(r"i = 3", color = WHITE).scale(0.55)
        n9 = Text(r"i = 4", color = WHITE).scale(0.55)
        n10 = Text(r"i = 4", color = WHITE).scale(0.55)
        n11 = Text(r"i = 5", color = WHITE).scale(0.55)
        n12 = Text(r"i = 4", color = WHITE).scale(0.55)
        n13 = Text(r"i = 5", color = WHITE).scale(0.55)
        n14 = Text(r"i = 5", color = WHITE).scale(0.55)
        n15 = Text(r"+2", color = BLUE).scale(0.55)

        n1.move_to(dtText.get_center() + DOWN / 2)

        n2.move_to(n1.get_center() + 4 * LEFT + DOWN)
        n3.move_to(n1.get_center() + 4 * RIGHT + DOWN)

        nBad.move_to(n2.get_center() + 2.25 * LEFT + DOWN)
        n4.move_to(n2.get_center() + 2.25 * LEFT + DOWN)
        n5.move_to(n2.get_center() + 2.25 * RIGHT + DOWN)
        n6.move_to(n3.get_center() + 2.25 * LEFT + DOWN)
        n7.move_to(n3.get_center() + 2.25 * RIGHT + DOWN)

        n8.move_to(n4.get_center() + LEFT + DOWN)
        n9.move_to(n4.get_center() + RIGHT + DOWN)
        n10.move_to(n5.get_center() + LEFT + DOWN)
        n11.move_to(n5.get_center() + RIGHT + DOWN)
        n12.move_to(n6.get_center() + LEFT + DOWN)
        n13.move_to(n6.get_center() + RIGHT + DOWN)
        n14.move_to(n7.get_center() + LEFT + DOWN)
        n15.move_to(n7.get_center() + RIGHT + DOWN)

        e1 = Arrow(start = n1.get_center(), end = n2.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        e2 = LabeledArrow(label = "+3", label_color = BLUE, start = n1.get_center(), end = n3.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8, label_frame = False).scale(0.7)

        e3 = Arrow(start = n2.get_center(), end = n4.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        e4 = LabeledArrow(label = "+1", label_color = BLUE, start = n2.get_center(), end = n5.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8, label_frame = False).scale(0.7)
        e5 = Arrow(start = n3.get_center(), end = n6.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        e6 = LabeledArrow(label = "+4", label_color = BLUE, start = n3.get_center(), end = n7.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8, label_frame = False).scale(0.7)

        e7 = Arrow(start = n4.get_center(), end = n8.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        e8 = LabeledArrow(label = "+4", label_color = BLUE, start = n4.get_center(), end = n9.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8, label_frame = False).scale(0.7)
        e9 = Arrow(start = n5.get_center(), end = n10.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        e10 = LabeledArrow(label = "+5", label_color = BLUE, start = n5.get_center(), end = n11.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8, label_frame = False).scale(0.7)
        e11 = Arrow(start = n6.get_center(), end = n12.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        e12 = LabeledArrow(label = "+5", label_color = BLUE, start = n6.get_center(), end = n13.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8, label_frame = False).scale(0.7)
        e13 = Arrow(start = n7.get_center(), end = n14.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        e14 = Arrow(start = n7.get_center(), end = n15.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        eBad = Arrow(start = n2.get_center(), end = nBad.get_center(), color = RED, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)

        c1 = Circle(radius = 0.16, color = WHITE, fill_opacity = 1)
        c2 = Circle(radius = 0.16, color = WHITE, fill_opacity = 1)
        c3 = Circle(radius = 0.16, color = WHITE, fill_opacity = 1)
        cg1 = VGroup(c1, c2, c3).arrange(direction = DOWN, buff = 2).scale(0.06)
        cg1.move_to(n8.get_center() + DOWN / 2)

        c4 = Circle(radius = 0.16, color = WHITE, fill_opacity = 1)
        c5 = Circle(radius = 0.16, color = WHITE, fill_opacity = 1)
        c6 = Circle(radius = 0.16, color = WHITE, fill_opacity = 1)
        cg2 = VGroup(c4, c5, c6).arrange(direction = DOWN, buff = 2).scale(0.06)
        cg2.move_to(n9.get_center() + DOWN / 2)

        c7 = Circle(radius = 0.16, color = WHITE, fill_opacity = 1)
        c8 = Circle(radius = 0.16, color = WHITE, fill_opacity = 1)
        c9 = Circle(radius = 0.16, color = WHITE, fill_opacity = 1)
        cg3 = VGroup(c7, c8, c9).arrange(direction = DOWN, buff = 2).scale(0.06)
        cg3.move_to(n10.get_center() + DOWN / 2)

        c10 = Circle(radius = 0.16, color = WHITE, fill_opacity = 1)
        c11 = Circle(radius = 0.16, color = WHITE, fill_opacity = 1)
        c12 = Circle(radius = 0.16, color = WHITE, fill_opacity = 1)
        cg4 = VGroup(c10, c11, c12).arrange(direction = DOWN, buff = 2).scale(0.06)
        cg4.move_to(n11.get_center() + DOWN / 2)

        c13 = Circle(radius = 0.16, color = WHITE, fill_opacity = 1)
        c14 = Circle(radius = 0.16, color = WHITE, fill_opacity = 1)
        c15 = Circle(radius = 0.16, color = WHITE, fill_opacity = 1)
        cg5 = VGroup(c13, c14, c15).arrange(direction = DOWN, buff = 2).scale(0.06)
        cg5.move_to(n12.get_center() + DOWN / 2)

        c16 = Circle(radius = 0.16, color = WHITE, fill_opacity = 1)
        c17 = Circle(radius = 0.16, color = WHITE, fill_opacity = 1)
        c18 = Circle(radius = 0.16, color = WHITE, fill_opacity = 1)
        cg6 = VGroup(c16, c17, c18).arrange(direction = DOWN, buff = 2).scale(0.06)
        cg6.move_to(n13.get_center() + DOWN / 2)

        c19 = Circle(radius = 0.16, color = WHITE, fill_opacity = 1)
        c20 = Circle(radius = 0.16, color = WHITE, fill_opacity = 1)
        c21 = Circle(radius = 0.16, color = WHITE, fill_opacity = 1)
        cg7 = VGroup(c19, c20, c21).arrange(direction = DOWN, buff = 2).scale(0.06)
        cg7.move_to(n14.get_center() + DOWN / 2)

        problem3Tree = VGroup(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, nBad,
                            e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, eBad).scale(0.6)

        problem3Tree.move_to(dtText.get_center() + 1.4 * DOWN + LEFT / 2.12)
        

        # self.play(FadeIn(indexPointer))
        # self.play(FadeIn(problem3Tree))
        # self.play(indexPointer.animate.shift([l[1].get_x() - l[0].get_x(), 0, 0]))
        self.play(FadeIn(n1))
        self.play(FadeIn(indexPointer))
        self.wait()

        arrowGroup = VGroup(e1, n2)
        self.play(l[1].animate.set_fill(color = WHITE, opacity = 0.2))
        self.play(FadeIn(arrowGroup))
        self.wait()
        self.play(l[1].animate.set_fill(color = WHITE, opacity = 0))

        arrowGroup = VGroup(n3, e2)
        self.play(l[2].animate.set_fill(color = WHITE, opacity = 0.2))
        self.play(FadeIn(arrowGroup))
        self.wait()
        self.play(l[2].animate.set_fill(color = WHITE, opacity = 0))

        self.play(indexPointer.animate.shift([l[1].get_x() - l[0].get_x(), 0, 0]))
        self.wait()
        # Bad example case
        arrowGroup = VGroup(nBad, eBad)
        self.play(l[0].animate.set_fill(color = RED, opacity = 0.2))
        self.play(FadeIn(arrowGroup))
        self.wait(3)
        self.play(l[0].animate.set_fill(color = RED, opacity = 0))
        self.play(FadeOut(arrowGroup))
        self.wait()

        arrowGroup = VGroup(e3, n4)
        self.play(l[2].animate.set_fill(color = WHITE, opacity = 0.2))
        self.play(FadeIn(arrowGroup))
        self.play(l[2].animate.set_fill(color = WHITE, opacity = 0))
        arrowGroup = VGroup(n5, e4)
        self.play(l[3].animate.set_fill(color = WHITE, opacity = 0.2))
        self.play(FadeIn(arrowGroup))
        self.play(l[3].animate.set_fill(color = WHITE, opacity = 0))
        self.wait()

        self.play(indexPointer.animate.shift([l[2].get_x() - l[1].get_x(), 0, 0]))
        arrowGroup = VGroup(n6, e5)
        self.play(l[3].animate.set_fill(color = WHITE, opacity = 0.2))
        self.play(FadeIn(arrowGroup))
        self.play(l[3].animate.set_fill(color = WHITE, opacity = 0))
        arrowGroup = VGroup(n7, e6)
        self.play(l[4].animate.set_fill(color = WHITE, opacity = 0.2))
        self.play(FadeIn(arrowGroup))
        self.play(l[4].animate.set_fill(color = WHITE, opacity = 0))
        self.wait()
        
        arrowGroup = VGroup(n8, e7)
        self.play(l[3].animate.set_fill(color = WHITE, opacity = 0.2))
        self.play(FadeIn(arrowGroup))
        self.play(l[3].animate.set_fill(color = WHITE, opacity = 0))
        arrowGroup = VGroup(n9, e8)
        self.play(l[4].animate.set_fill(color = WHITE, opacity = 0.2))
        self.play(FadeIn(arrowGroup))
        self.play(l[4].animate.set_fill(color = WHITE, opacity = 0))
        self.wait()

        self.play(indexPointer.animate.shift([l[3].get_x() - l[2].get_x(), 0, 0]))
        arrowGroup = VGroup(n10, e9)
        self.play(l[4].animate.set_fill(color = WHITE, opacity = 0.2))
        self.play(FadeIn(arrowGroup))
        self.play(l[4].animate.set_fill(color = WHITE, opacity = 0))
        arrowGroup = VGroup(n11, e10)
        self.play(l[5].animate.set_fill(color = WHITE, opacity = 0.2))
        self.play(FadeIn(arrowGroup))
        self.play(l[5].animate.set_fill(color = WHITE, opacity = 0))
        self.wait()


        arrowGroup = VGroup(n12, e11)
        self.play(l[4].animate.set_fill(color = WHITE, opacity = 0.2))
        self.play(FadeIn(arrowGroup))
        self.play(l[4].animate.set_fill(color = WHITE, opacity = 0))
        arrowGroup = VGroup(n13, e12)
        self.play(l[5].animate.set_fill(color = WHITE, opacity = 0.2))
        self.play(FadeIn(arrowGroup))
        self.play(l[5].animate.set_fill(color = WHITE, opacity = 0))
        self.wait()

        self.play(indexPointer.animate.shift([l[4].get_x() - l[3].get_x(), 0, 0]))
        arrowGroup = VGroup(n14, e13)
        self.play(l[5].animate.set_fill(color = WHITE, opacity = 0.2))
        self.play(FadeIn(arrowGroup))
        self.play(l[5].animate.set_fill(color = WHITE, opacity = 0))
        arrowGroup = VGroup(n15, e14)
        self.play(FadeIn(arrowGroup))

        cg1.move_to(n8.get_center() + DOWN / 2)
        cg2.move_to(n9.get_center() + DOWN / 2)
        cg3.move_to(n10.get_center() + DOWN / 2)
        cg4.move_to(n11.get_center() + DOWN / 2)
        cg5.move_to(n12.get_center() + DOWN / 2)
        cg6.move_to(n13.get_center() + DOWN / 2)
        cg7.move_to(n14.get_center() + DOWN / 2)

        dotGroup = VGroup(cg1, cg2, cg3, cg4, cg5, cg6, cg7)
        problem3Tree.add(dotGroup, dtText)
        self.play(FadeIn(dotGroup))
        end = VGroup(costsArray, indexPointer)
        self.play(FadeOut(end))
        problem3Tree.remove(nBad, eBad)
        self.play(problem3Tree.animate.shift(UP / 2))
        self.wait(3)

        stateHouseRobber = Text("Let dp[i] the maximum profit that can be obtained by considering houses i to n - 1").scale(0.45)

        # Transformed decision tree
        n1 = Text(r"dp[0]", color = WHITE).scale(0.55)

        n2 = Text(r"dp[1]", color = WHITE).scale(0.55)
        n3 = Text(r"dp[2]", color = WHITE).scale(0.55)

        n4 = Text(r"dp[2]", color = WHITE).scale(0.55)
        n5 = Text(r"dp[3]", color = WHITE).scale(0.55)
        n6 = Text(r"dp[3]", color = WHITE).scale(0.55)
        n7 = Text(r"dp[4]", color = WHITE).scale(0.55)

        n8 = Text(r"dp[3]", color = WHITE).scale(0.55)
        n9 = Text(r"dp[4]", color = WHITE).scale(0.55)
        n10 = Text(r"dp[4]", color = WHITE).scale(0.55)
        n11 = Text(r"dp[5]", color = WHITE).scale(0.55)
        n12 = Text(r"dp[4]", color = WHITE).scale(0.55)
        n13 = Text(r"dp[5]", color = WHITE).scale(0.55)
        n14 = Text(r"dp[5]", color = WHITE).scale(0.55)
        n15 = Text(r"+2", color = BLUE).scale(0.55)

        n1.move_to(dtText.get_center() + DOWN / 2)

        n2.move_to(n1.get_center() + 4 * LEFT + DOWN)
        n3.move_to(n1.get_center() + 4 * RIGHT + DOWN)

        n4.move_to(n2.get_center() + 2.25 * LEFT + DOWN)
        n5.move_to(n2.get_center() + 2.25 * RIGHT + DOWN)
        n6.move_to(n3.get_center() + 2.25 * LEFT + DOWN)
        n7.move_to(n3.get_center() + 2.25 * RIGHT + DOWN)

        n8.move_to(n4.get_center() + LEFT + DOWN)
        n9.move_to(n4.get_center() + RIGHT + DOWN)
        n10.move_to(n5.get_center() + LEFT + DOWN)
        n11.move_to(n5.get_center() + RIGHT + DOWN)
        n12.move_to(n6.get_center() + LEFT + DOWN)
        n13.move_to(n6.get_center() + RIGHT + DOWN)
        n14.move_to(n7.get_center() + LEFT + DOWN)
        n15.move_to(n7.get_center() + RIGHT + DOWN)

        e1 = Arrow(start = n1.get_center(), end = n2.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        e2 = LabeledArrow(label = "costs[0]", label_color = BLUE, start = n1.get_center(), end = n3.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8, label_frame = False).scale(0.7)

        e3 = Arrow(start = n2.get_center(), end = n4.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        e4 = LabeledArrow(label = "costs[1]", label_color = BLUE, start = n2.get_center(), end = n5.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8, label_frame = False).scale(0.7)
        e5 = Arrow(start = n3.get_center(), end = n6.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        e6 = LabeledArrow(label = "costs[2]", label_color = BLUE, start = n3.get_center(), end = n7.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8, label_frame = False).scale(0.7)

        e7 = Arrow(start = n4.get_center(), end = n8.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        e8 = LabeledArrow(label = "costs[2]", label_color = BLUE, start = n4.get_center(), end = n9.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8, label_frame = False).scale(0.7)
        e9 = Arrow(start = n5.get_center(), end = n10.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        e10 = LabeledArrow(label = "costs[3]", label_color = BLUE, start = n5.get_center(), end = n11.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8, label_frame = False).scale(0.7)
        e11 = Arrow(start = n6.get_center(), end = n12.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        e12 = LabeledArrow(label = "costs[3]", label_color = BLUE, start = n6.get_center(), end = n13.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8, label_frame = False).scale(0.7)
        e13 = Arrow(start = n7.get_center(), end = n14.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        e14 = Arrow(start = n7.get_center(), end = n15.get_center(), color = WHITE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)

        ee2 = LabeledArrow(label = "costs[0]", label_color = BLUE, start = n1.get_center(), end = n3.get_center(), color = BLUE, buff = 195, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8, label_frame = False).scale(0.7)
        houseRobberTree = VGroup(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15,
                                    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, ee2).scale(0.6)

        # houseRobberTree.move_to(dtText.get_center() + 1.5 * DOWN + LEFT / 2.12)
        houseRobberTree.move_to(dtText.get_center() + 1.4 * DOWN + LEFT / 2.12)
        cg1.move_to(n8.get_center() + DOWN / 2)
        cg2.move_to(n9.get_center() + DOWN / 2)
        cg3.move_to(n10.get_center() + DOWN / 2)
        cg4.move_to(n11.get_center() + DOWN / 2)
        cg5.move_to(n12.get_center() + DOWN / 2)
        cg6.move_to(n13.get_center() + DOWN / 2)
        cg7.move_to(n14.get_center() + DOWN / 2)
        dotGroup = VGroup(cg1, cg2, cg3, cg4, cg5, cg6, cg7)
       
        houseRobberTree.add(dotGroup, dtText)
        self.wait(2)
        stateHouseRobber.shift(UP)
        houseRobberTree.remove(ee2)
        self.wait()

        self.play(FadeIn(stateHouseRobber))
        self.play(Transform(problem3Tree, houseRobberTree, replace_mobject_with_target_in_scene = False))
        self.wait(2)
        
        self.play(FadeOut(stateHouseRobber))
        self.wait()
        rc = Tex(r"\text{dp[i] = dp[i + 1]}", color = WHITE).scale(0.6)
        rc2 = Tex(r"\text{dp[i] = max(dp[i + 1], costs[i] + dp[i + 2])}").scale(0.6)
        rc.shift(UP)
        rc2.shift(UP)


        self.play(e1.animate.set_color(BLUE))
        self.play(FadeIn(rc))
        self.wait()
        self.play(e1.animate.set_color(WHITE))
        self.wait()

        self.play(FadeIn(ee2))
        self.play(ReplacementTransform(rc, rc2))
        self.wait()
        self.play(FadeOut(ee2))
        self.play(FadeOut(houseRobberTree, problem3Tree))
        self.wait()
        self.play(FadeOut(rc2))

        self.wait(3)


        firstIndex = Rectangle(height = 1, width = 0.5, color = WHITE)
        prefix = Rectangle(height = 1, width = 3, color = BLUE)
        firstIndex.set_fill(color = WHITE, opacity = 0.2)
        prefix.set_fill(color = BLUE, opacity = 0.2)
        arr = VGroup(firstIndex, prefix).arrange(direction = RIGHT, buff = 0).scale(0.9)
        index0 = MathTex(r"i", color = BLUE).scale(0.7)
        indexEnd = MathTex(r"i + 1 ... n - 1", color = BLUE).scale(0.7)
        index0.move_to(firstIndex.get_center() + UP / 1.5)
        indexEnd.move_to(prefix.get_center() + UP / 1.5)
        arr.add(index0, indexEnd)
        arr.shift(3 * LEFT)
        self.play(FadeIn(arr))
        rc2.move_to(arr.get_center() + 5 * RIGHT + DOWN / 4)
        self.play(FadeIn(rc2))
        tempText = Text("We need to solve for i + 1 and i + 2 in order to solve for i").scale(0.45)
        tempText.move_to(arr.get_center() + 1.5 * DOWN + 1.8 * RIGHT)
        self.play(FadeIn(tempText))
        self.wait(2)
        end = VGroup(tempText, arr, rc2)
        self.play(FadeOut(end))

        questionBaseCases = Text("What are the base cases?").scale(0.75)
        self.play(FadeIn(questionBaseCases))
        self.wait()
        self.play(FadeOut(questionBaseCases))

        baseCase1 = Text("What if n == 1?").scale(0.6)
        bc1 = Tex(r"\text{dp[n - 1] = costs[n - 1]}").scale(0.6)
        baseCase2 = Text("What if n == 2?").scale(0.6)
        bc2 = Tex(r"\text{dp[n - 2] = max(dp[n - 2], dp[n - 1])}").scale(0.6)

        bcGroup = VGroup(baseCase1, bc1, baseCase2, bc2).arrange(direction = DOWN, aligned_edge = LEFT).scale(0.9).next_to(ORIGIN,DR)
        bcGroup.shift(2.5 * LEFT + UP / 2)
        bc1.shift(RIGHT / 2)
        bc2.shift(RIGHT / 2)
        bcGroup.shift(UP / 2)
        temp = VGroup(baseCase2, bc2)
        temp.shift(DOWN / 2)

        self.play(FadeIn(baseCase1))
        self.wait()
        self.play(FadeIn(bc1))
        self.wait()
        self.play(FadeIn(baseCase2))
        self.wait()
        self.play(FadeIn(bc2))
        self.wait(2)
        self.play(FadeOut(bcGroup))

        self.wait(2)

        # House Robber Code
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{listings}")
        matrixCode = r"""
\begin{lstlisting}[language=Python]
def rob(int[] costs):
    int n = costs.length
    int[] dp = new int[n]

    if n == 1:
        return costs[n - 1]
    
    dp[n - 1] = costs[n - 1]
    dp[n - 2] = max(costs[n - 2], costs[n - 1])

    for (int i = n - 3; i >= 0; i--):
        dp[i] = max(dp[i + 1], costs[i] + dp[i + 2])
    
    return dp[0]
\end{lstlisting}
"""
        tex = Tex(matrixCode, tex_template = myTemplate, font_size = 21)
        tex.shift(.5 * DOWN + 2.75 * LEFT)
        self.play(FadeIn(tex[0][0:19]))
        self.wait()
        self.play(FadeIn(tex[0][19:76]))
        self.wait()
        self.play(FadeIn(tex[0][76:128]))
        self.wait()
        self.play(FadeIn(tex[0][128:151]))
        self.wait()
        self.play(FadeIn(tex[0][151:186]))
        self.wait()
        self.play(FadeIn(tex[0][186:198]))
        self.wait()
        
        # Run example
        size = 6
        l = [Square(side_length = 0.8, stroke_width = 1.0) for _ in range(size)]
        costsArray = VGroup(*l).scale(0.8)

        costsArray.arrange(direction = RIGHT, buff = 0)
        name1 = Text("costs =").scale(0.45)
        c0 = MathTex(r"3", color = BLUE).scale(0.55)
        c0.move_to(l[0].get_center())
        c1 = MathTex(r"1", color = BLUE).scale(0.55)
        c1.move_to(l[1].get_center())
        c2 = MathTex(r"4", color = BLUE).scale(0.55)
        c2.move_to(l[2].get_center())
        c3 = MathTex(r"5", color = BLUE).scale(0.55)
        c3.move_to(l[3].get_center())
        c4 = MathTex(r"2", color = BLUE).scale(0.55)
        c4.move_to(l[4].get_center())
        c5 = MathTex(r"3", color = BLUE).scale(0.55)
        c5.move_to(l[5].get_center())
        # 3 1 4 5 2 3
        costsArray.add(c0, c1, c2, c3, c4, c5)

        l2 = [Square(side_length = 0.8, stroke_width = 1.0) for _ in range(size)]
        dp = VGroup(*l2).scale(0.8)
        dp.arrange(direction = RIGHT, buff = 0)
        name2 = Text("dp =").scale(0.45)
    
        
        houseRobberExample = VGroup(costsArray, dp).arrange(direction = DOWN, buff = 1.5)
        dp.align_to(costsArray, LEFT)

        houseRobberExample.shift(4.2 * RIGHT + DOWN / 2)
        houseRobberExample.add(name1)
        name1.move_to(l[0].get_center() + LEFT)
        houseRobberExample.add(name2)
        name2.move_to(l2[0].get_center() + .75 * LEFT)

        self.play(FadeIn(houseRobberExample))
        self.wait()

        
        index = MathTex(r"i", color = BLUE).scale(0.7)
        indexBox = Square(side_length = 0.8, color = WHITE).scale(0.8)
        indexBox.set_fill(color = WHITE, opacity = 0.2)
        indexBox.move_to(l[5].get_center())
        index.move_to(l[5].get_center() + UP / 1.5)
        indexPointerCosts = VGroup(index, indexBox)

        indexDP = MathTex(r"i", color = BLUE).scale(0.7)
        indexBoxDP = Square(side_length = 0.8, color = WHITE).scale(0.8)
        indexBoxDP.set_fill(color = WHITE, opacity = 0.2)
        indexBoxDP.move_to(l2[5].get_center())
        indexDP.move_to(l2[5].get_center() + UP / 1.5)
        indexPointerDP = VGroup(indexDP, indexBoxDP)

        indices = VGroup(indexPointerCosts, indexPointerDP)
        self.play(FadeIn(indices))
        self.wait()

        self.play(tex[0][76:94].animate.set_color(BLUE))
        dp5 = MathTex(r"3", color = BLUE).scale(0.55)
        dp5.move_to(l2[5].get_center())
        self.play(FadeIn(dp5))
        self.play(tex[0][76:94].animate.set_color(WHITE))
        self.play(indices.animate.shift([l[4].get_x() - l[5].get_x(), 0, 0]))
        self.wait()

        maxText = Tex(r"\text{dp[3] = max(3)}").scale(0.55)
        maxText2 = Tex(r"\text{dp[3] = max(2, 3)}").scale(0.55)
        maxText3a = Tex(r"\text{dp[3] = max(3)}").scale(0.55)
        maxText3b = Tex(r"\text{dp[3] = max(3, 5 + 3)}").scale(0.55)
        maxText2a = Tex(r"\text{dp[2] = max(8)}").scale(0.55)
        maxText2b = Tex(r"\text{dp[2] = max(8, 4 + 3)}").scale(0.55)
        maxText1a = Tex(r"\text{dp[1] = max(8)}").scale(0.55)
        maxText1b = Tex(r"\text{dp[1] = max(8, 1 + 8)}").scale(0.55)
        maxText0a = Tex(r"\text{dp[0] = max(9)}").scale(0.55)
        maxText0b = Tex(r"\text{dp[0] = max(9, 3 + 8)}").scale(0.55)
        maxText.move_to(dp.get_center() + 1.2 * UP)
        maxText2.move_to(dp.get_center() + 1.2 * UP)
        maxText3a.move_to(dp.get_center() + 1.2 * UP)
        maxText3b.move_to(dp.get_center() + 1.2 * UP)
        maxText2a.move_to(dp.get_center() + 1.2 * UP)
        maxText2b.move_to(dp.get_center() + 1.2 * UP)
        maxText1a.move_to(dp.get_center() + 1.2 * UP)
        maxText1b.move_to(dp.get_center() + 1.2 * UP)
        maxText0a.move_to(dp.get_center() + 1.2 * UP)
        maxText0b.move_to(dp.get_center() + 1.2 * UP)
        timeComplexityHouseRobber = MathTex(r"\mathcal{O}(n)").scale(0.65)
        timeComplexityHouseRobber.move_to(dp.get_center() + 1.2 * UP + LEFT)
        

        self.play(tex[0][94:128].animate.set_color(BLUE))
        self.play(FadeIn(maxText))
        dp4 = MathTex(r"3", color = BLUE).scale(0.55)
        dp4.move_to(l2[4].get_center())
        self.play(l[5].animate.set_fill(color = WHITE, opacity = 0.2))
        self.play(ReplacementTransform(maxText, maxText2))
        self.play(l[5].animate.set_fill(color = WHITE, opacity = 0))
        self.play(FadeIn(dp4))
        self.play(tex[0][94:128].animate.set_color(WHITE))
        self.play(FadeOut(maxText2))
        self.play(indices.animate.shift([l[3].get_x() - l[4].get_x(), 0, 0]))
        self.wait()

        self.play(tex[0][128:186].animate.set_color(BLUE))
        self.play(l2[4].animate.set_fill(color = WHITE, opacity = 0.2))
        self.play(FadeIn(maxText3a))
        self.wait(0.5)
        self.play(l2[4].animate.set_fill(color = WHITE, opacity = 0))
        self.play(l2[5].animate.set_fill(color = WHITE, opacity = 0.2))
        self.play(ReplacementTransform(maxText3a, maxText3b))
        self.wait(0.5)
        self.play(l2[5].animate.set_fill(color = WHITE, opacity = 0))
        dp3 = MathTex(r"8", color = BLUE).scale(0.55)
        dp3.move_to(l2[3].get_center())
        self.play(FadeIn(dp3))
        self.play(FadeOut(maxText3b))
        self.play(indices.animate.shift([l[2].get_x() - l[3].get_x(), 0, 0]))
        self.wait()

        self.play(l2[3].animate.set_fill(color = WHITE, opacity = 0.2))
        self.play(FadeIn(maxText2a))
        self.wait(0.5)
        self.play(l2[3].animate.set_fill(color = WHITE, opacity = 0))
        self.play(l2[4].animate.set_fill(color = WHITE, opacity = 0.2))
        self.play(ReplacementTransform(maxText2a, maxText2b))
        self.wait(0.5)
        self.play(l2[4].animate.set_fill(color = WHITE, opacity = 0))
        dp2 = MathTex(r"8", color = BLUE).scale(0.55)
        dp2.move_to(l2[2].get_center())
        self.play(FadeIn(dp2))
        self.play(FadeOut(maxText2b))
        self.play(indices.animate.shift([l[1].get_x() - l[2].get_x(), 0, 0]))
        self.wait()

        self.play(l2[2].animate.set_fill(color = WHITE, opacity = 0.2))
        self.play(FadeIn(maxText1a))
        self.wait(0.5)
        self.play(l2[2].animate.set_fill(color = WHITE, opacity = 0))
        self.play(l2[3].animate.set_fill(color = WHITE, opacity = 0.2))
        self.play(ReplacementTransform(maxText1a, maxText1b))
        self.wait(0.5)
        self.play(l2[3].animate.set_fill(color = WHITE, opacity = 0))
        dp1 = MathTex(r"9", color = BLUE).scale(0.55)
        dp1.move_to(l2[1].get_center())
        self.play(FadeIn(dp1))
        self.play(FadeOut(maxText1b))
        self.play(indices.animate.shift([l[0].get_x() - l[1].get_x(), 0, 0]))
        self.wait()

        self.play(l2[1].animate.set_fill(color = WHITE, opacity = 0.2))
        self.play(FadeIn(maxText0a))
        self.wait(0.5)
        self.play(l2[1].animate.set_fill(color = WHITE, opacity = 0))
        self.play(l2[2].animate.set_fill(color = WHITE, opacity = 0.2))
        self.play(ReplacementTransform(maxText0a, maxText0b))
        self.wait(0.5)
        self.play(l2[2].animate.set_fill(color = WHITE, opacity = 0))
        dp0 = MathTex(r"11", color = BLUE).scale(0.55)
        dp0.move_to(l2[0].get_center())
        self.play(FadeIn(dp0))
        self.play(FadeOut(indices))
        self.play(FadeOut(maxText0b))
        self.play(tex[0][128:186].animate.set_color(WHITE))
        self.wait()

        self.play(tex[0][186:197].animate.set_color(BLUE))
        self.play(l2[0].animate.set_fill(color = WHITE, opacity = 0.2))
        self.wait(1.5)
        self.play(l2[0].animate.set_fill(color = WHITE, opacity = 0))
        self.play(tex[0][186:197].animate.set_color(WHITE))
        self.wait()
        
        end = VGroup(houseRobberExample, dp5, dp4, dp3, dp2, dp1, dp0)
        self.play(FadeOut(end))
        self.wait(2)

        self.play(tex[0][128:186].animate.set_color(BLUE))
        self.wait()
        self.play(FadeIn(timeComplexityHouseRobber))
        self.wait(2)
        self.play(timeComplexityHouseRobber.animate.set_color(GREEN))
        self.wait(2)
        end = VGroup(timeComplexityHouseRobber, thirdQuestionObj, tex)
        self.play(FadeOut(end))
        self.wait(3)
        text = Text("What does topological ordering mean more specifically?").scale(0.7)
        self.play(FadeIn(text))
        self.wait(2)
        text2 = Text("Any valid DP decision tree is a DAG (Directed Acyclic Graph)").scale(0.7)
        self.play(FadeOut(text))
        self.play(FadeIn(text2))
        self.wait(4)
        self.play(FadeOut(text2))
        self.wait()

        houseRobberTree.shift(1.25 * UP)
        houseRobberTree.remove(dtText)
        self.play(FadeIn(houseRobberTree))
        self.wait()
        self.play(houseRobberTree.animate.shift(1.5 * UP))

        textBad = Text(r"dp[0]", color = RED).scale(0.55).scale(0.6)
        textBad.move_to(n2.get_center() + 1.5 * LEFT)
        badArrow = Arrow(start = n2.get_center(), end = textBad.get_center(), color = RED, buff = 50, max_tip_length_to_length_ratio = 0.07, stroke_width = 0.8).scale(0.7)
        cycle = Arrow(start = textBad.get_center() + RIGHT / 12, end = n1.get_center(), color = RED, max_tip_length_to_length_ratio = 0.035, stroke_width = 0.8)

        textCycle = Text("This would no longer be a DAG!", color = RED).scale(0.45)
        textCycle.move_to(houseRobberTree.get_center() + 2.25 * DOWN) 

        temp = VGroup(textBad, badArrow, cycle)
        houseRobberTree.add(temp)
        self.play(FadeIn(temp))
        self.wait()
        self.play(FadeIn(textCycle))
        self.wait(4)
        end = VGroup(houseRobberTree, textCycle, temp)
        self.play(FadeOut(end))
        self.wait(2)

        textDPvsDQ = Text("What is the difference between Dynammic Programming and Divide-and-Conquer?").scale(0.5)
        self.play(FadeIn(textDPvsDQ))
        self.wait(2.5)
        self.play(FadeOut(textDPvsDQ))
        self.wait()
        whatIsDC = Text("Divide and Conquer is the concept of solving smaller, simpler, non-overlapping sub-problems \nand then utilizing the solutions of " +
                        "those sub-problems to solve a larger, more complex problem", line_spacing = 1.5).scale(0.4)
        
        whatIsDC[53:68].set_color(BLUE)
        whatIsDP[58:74].set_color(BLUE)
        
        text = VGroup(whatIsDP, whatIsDC).arrange(direction = DOWN, aligned_edge = LEFT, buff = 1.5).scale(0.9).next_to(ORIGIN,DR)
        text.move_to(ORIGIN + UP / 1.2)
        self.play(FadeIn(text))
        self.wait(5)
        self.play(FadeOut(text))

        g2.move_to(ORIGIN)
        duplicateFibS1 = Rectangle(height = 0.8, width = 2, color = BLUE, stroke_width = 0.9)
        duplicateFibS2 = Rectangle(height = 0.8, width = 2, color = BLUE, stroke_width = 0.9)

        duplicateFibS1.move_to(duplicateFib1.get_center() + DOWN / 4)
        duplicateFibS2.move_to(duplicateFib2.get_center() + DOWN / 4)
        temp = VGroup(g2, duplicateFibS2, duplicateFibS1)
        self.play(FadeIn(g2))
        dupes = VGroup(duplicateFibS1, duplicateFibS2)
        self.play(FadeIn(dupes))
        self.wait(2)
        self.play(FadeOut(temp))

        dtGroup2.move_to(ORIGIN + UP / 1.2)
        dtGroup2.remove(dtText)
        duplicateMatrixS1 = Rectangle(height = 0.3, width = 0.92, color = BLUE, stroke_width = 0.9)
        duplicateMatrixS2 = Rectangle(height = 0.3, width = 0.92, color = BLUE, stroke_width = 0.9)
        duplicateMatrixS1.move_to(duplicateMatrix1.get_center())
        duplicateMatrixS2.move_to(duplicateMatrix2.get_center())
        temp = VGroup(dtGroup2, duplicateMatrixS1, duplicateMatrixS2)
        temp.move_to(ORIGIN)
        self.play(FadeIn(dtGroup2))
        dupes = VGroup(duplicateMatrixS1, duplicateMatrixS2)
        self.play(FadeIn(dupes))
        self.wait(2)
        self.play(FadeOut(temp))

        # Binary search example
        a1 = Rectangle(height = 1, width = 5, color = WHITE, stroke_width = 1.5)
        a2 = Rectangle(height = 1, width = 2.5, color = WHITE, stroke_width = 1.5)
        a3 = Rectangle(height = 1, width = 1.25, color = WHITE, stroke_width = 1.5)

        bscg1 = Circle(radius = 0.16, color = BLUE, fill_opacity = 1)
        bscg2 = Circle(radius = 0.16, color = BLUE, fill_opacity = 1)
        bscg3 = Circle(radius = 0.16, color = BLUE, fill_opacity = 1)

        bscg = VGroup(bscg1, bscg2, bscg3).arrange(direction = DOWN, buff = 1).scale(0.2)
        

        
        binarySearchExample = VGroup(a1, a2, a3, bscg).arrange(direction = DOWN, buff = 0.5).scale(0.7)
        binarySearchExample.move_to(ORIGIN + 2 * LEFT)
        a2.align_to(a1, LEFT)
        a3.align_to(a2, RIGHT)
        bscg.move_to(a3.get_center() + DOWN / 1.2)
        textExplain = Text("Each sub-problem in Binary Search is unique!", color = WHITE).scale(0.4)
        textExplain[31:28].set_color(BLUE)
        textExplain.move_to(a3.get_center() + 4 * RIGHT + UP / 2)

        self.play(FadeIn(a1))
        self.wait()
        self.play(FadeIn(a2, target_position = a1))
        self.wait()
        self.play(FadeIn(a3, target_position = a2))
        self.wait()
        self.play(FadeIn(bscg))
        self.play(FadeIn(textExplain))
        self.wait(4)
        end = VGroup(binarySearchExample, textExplain)

        self.play(FadeOut(end))
        self.wait(5)

        # Play outro
        playIntro(self)