
def funnyfunction(first_word,second_word,third_word):
    print("The word created is: " + first_word + second_word + third_word)
    return first_word + second_word + third_word


def wordprinter(sample_word):
    for x in range(0, len(sample_word)):
        print("The letter in ", x, " is ", sample_word[x])


wordprinter(funnyfunction('chicken', 'fish', 'fart'))

# # How to use Lambdas?
#
# numbers_from_x = sorted([45, 34, 2, 3, 4, 20, -10], key=lambda x: abs(10-x))
# print(numbers_from_x)
#
# numbers_from_x = sorted([0, -5, 20, -25, 36, -80, 100, -180], key=lambda x: x%7)
# print(numbers_from_x)
#
# def do_stuff(n):
#     return lambda x: (x + n) * n
# f = do_stuff(3)
# print(f(4))
#
# my_list = [1, 2, 3, 4, 5, 6]
# squared_list = map(lambda x: x ** 2, my_list)
# print(list(squared_list))
#
# square_root = lambda x: x ** 0.5
# print(square_root(4))
#
# import math
# def square_root(x): return math.sqrt(x)
# print(square_root(4))
#
#
