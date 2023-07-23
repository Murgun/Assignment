from maths import Math, CustomException

try:
    math_obj = Math(23, 45)
    print("Addition:", math_obj.add())
    print("Subtraction:", math_obj.subtract())
    print("Multiplication:", math_obj.multiply())
    print("Division:", math_obj.divide())


except ZeroDivisionError as e:
    print("Error:", e)

except CustomException as e:
    print("Custom Exception:", e)