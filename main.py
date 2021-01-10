{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import math\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "$\\cos(x) + 0.05x^3 + \\log_2{x^2}$      \n",
    "при $x = 10$\n",
    "\n",
    "$x_1^2\\cos(x_2) + 0.05x_2^3 + 3x_1^3\\log_2{x_2^2}$       \n",
    "при $(10, 1)$\n",
    "\n",
    "$\\cos(x) + 0.05x^3 + \\log_2{x^2}$      \n",
    "при $\\epsilon = 0.001$\n",
    "\n",
    "$x_1^2\\cos(x_2) + 0.05x_2^3 + 3x_1^3\\log_2{x_2^2}$.      \n",
    "при $\\epsilon = 0.001$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def fun(x):\n",
    "    return x**2 + 1\n",
    "\n",
    "def d_fun(x):\n",
    "    h = 1e-5\n",
    "    return (fun(x+h)-fun(x-h))/(2*h)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "def F1(x):\n",
    "    return math.cos(x) + 0.05*x**3 + math.log2(x**2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def F2(x1,x2):\n",
    "    return x1**2*math.cos(x2) + 0.05*x2**3 + math.log2(x2**2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def F3(x):\n",
    "    return math.cos(x) + 0.05*x**3 + math.log2(x**2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "def F4(x1,x2):\n",
    "    return x1**2*math.cos(x2) + 0.05*x2**3 + math.log2(x2**2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "посчитать значений производной функции $\\cos(x) + 0.05x^3 + \\log_2{x^2}$ в точке $x = 10$. Ответ округлить до 2-го знака. Пожалуйста назовите функцию derivation, функция должна принимать точку, в которой нужно вычислить значение производной, и функцию, производную которой мы хотим вычислить."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "def derivation(x, fun):\n",
    "    h = 1e-5\n",
    "    return round((fun(x+h)-fun(x))/(h),2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "15.83"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "derivation(10,F1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "посчитать значение градиента функции $x_1^2\\cos(x_2) + 0.05x_2^3 + 3x_1^3\\log_2{x_2^2}$ в точке $(10, 1)$. Пожалуйста назовите функцию gradient, функция должна принимать список с координатами точки, в которой нужно вычислить значение производной, и функцию, производную которой мы хотим вычислить. Ответ округлить до 2-го знака."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "def gradient(point, fun):\n",
    "    x1 = point[0]\n",
    "    x2 = point[1]\n",
    "    h = 1e-5\n",
    "    return [round((fun(x1+h,x2)-fun(x1,x2))/(h),2),round((fun(x1,x2+h)-fun(x1,x2))/(h),2)]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[10.81, -81.11]"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "point = [10,1]\n",
    "gradient(point, F2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def gradient_optimization_one_dim(x):\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def gradient_optimization_multi_dim(x):\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
