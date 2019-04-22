
import sys

from fileinfo import raw_input


def calc(term):

    term = term.replace(' ', '')
    term = term.replace('^', '**')
    term = term.replace('=', '')
    term = term.replace('?', '')
    term = term.replace('%', '/100.00')
    term = term.replace('rad', 'radians')
    term = term.replace('mod', '%')

    functions = ['sin', 'cos', 'tan', 'pow', 'cosh', 'sinh', 'tanh', 'sqrt', 'pi', 'radians', 'e']

    term = term.lower()

    for func in functions:
        if func in term:
            withmath = 'math.' + func
            term = term.replace(func, withmath)

    try:

        term = eval(term)

    except ZeroDivisionError:

        print("Can't divide by 0.  Please try again.")

    except NameError:

        print('Invalid input.  Please try again')

    except AttributeError:

        print('Please check usage method and try again.')
    except TypeError:
        print("please enter inputs of correct datatype ")

    return term


def result(term):

    print("\n" + str(calc(term)))


def main():

    print("\nScientific Calculator\n\nFor Example: sin(rad(90)) + 50% * (sqrt(16)) + round(1.42^2)" +
          "- 12mod3\n\nEnter quit to exit")

    if sys.version_info.major >= 3:
        while True:
            k = input("\nWhat is ")
            if k == 'quit':
                break
            result(k)

    else:
        while True:
            k = raw_input("\nWhat is ")
            if k == 'quit':
                break
            result(k)


if __name__ == '__main__':
    main()