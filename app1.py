import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

# Calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

def power(x, y):
    return math.pow(x, y)

def square_root(x):
    if x < 0:
        return "Cannot take square root of a negative number!"
    return math.sqrt(x)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

# Function to plot graphs
def plot_function(func, title, start, end):
    x = np.linspace(start, end, 400)
    y = func(np.radians(x))  # Convert to radians for trigonometric functions
    plt.figure()
    plt.plot(x, y)
    plt.title(f'Graph of {title}')
    plt.xlabel('x (degrees)')
    plt.ylabel(f'{title}(x)')
    plt.grid(True)
    st.pyplot(plt)

# Streamlit App Interface
st.title("Scientific Graphic Calculator")

# Select operation
operation = st.selectbox("Choose an operation:", 
                         ["Add", "Subtract", "Multiply", "Divide", "Power (x^y)", "Square Root", "Sine", "Cosine", "Tangent", "Plot Sine Graph", "Plot Cosine Graph", "Plot Tangent Graph"])

if operation in ["Add", "Subtract", "Multiply", "Divide", "Power (x^y)"]:
    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)
    
    if st.button("Calculate"):
        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)
        elif operation == "Power (x^y)":
            result = power(num1, num2)
        
        st.write(f"Result: {result}")

elif operation == "Square Root":
    num = st.number_input("Enter number", value=0.0)
    
    if st.button("Calculate"):
        result = square_root(num)
        st.write(f"Square Root of {num} = {result}")

elif operation in ["Sine", "Cosine", "Tangent"]:
    angle = st.number_input("Enter angle in degrees", value=0.0)
    
    if st.button("Calculate"):
        if operation == "Sine":
            result = sine(angle)
        elif operation == "Cosine":
            result = cosine(angle)
        elif operation == "Tangent":
            result = tangent(angle)
        
        st.write(f"{operation}({angle}) = {result}")

# Plotting section for graphs
elif operation == "Plot Sine Graph":
    if st.button("Plot Sine Graph"):
        plot_function(np.sin, "Sine", -360, 360)

elif operation == "Plot Cosine Graph":
    if st.button("Plot Cosine Graph"):
        plot_function(np.cos, "Cosine", -360, 360)

elif operation == "Plot Tangent Graph":
    if st.button("Plot Tangent Graph"):
        plot_function(np.tan, "Tangent", -360, 360)
