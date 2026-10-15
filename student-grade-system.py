# Student Grade System- by Abibat
students = {"John": 85, "Mary":62
            def get_grade(score):
              if score>= 70:
                return "A - Excellent"
              elif score>=60:
                return"B - Very Good"
                else
                return"C - Needs Work"
                for name, score in students.items():
                  print(f"{name}: {score} = {get_grade(score)}")
