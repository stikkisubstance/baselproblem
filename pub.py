# Introduction
print('Mathematician Euler solved a problem, namely the Basel problem, concerning the infinite sum of inverse squares, i.e. sum of n^-2 from n=1 to n=infinity.\nHe found out that the answer is (pi^2)/6, which is approximately 1.6449.')
print('This solution to the problem is also the most convenient way to calculate pi, which this program is used for.')
print('Therefore, to find the exact value of n for the formula "Σ(n^-2) = (pi^2)/6" ,this program is designed to show all steps to find it, automating them at the same time.')
print('The ultimate goal for this program is to find the value of infinity, or the nearest value, by simplest means.\n  ')
start = str(input('Please input the letter D (uppercase only) to start the calculation: '))

# Constants & Variables
pi = 3.14159265359
n = 0
c = 0
t = 0

# Calculation
if start == 'D':
    while True:
        n = n + 1  # Number (cumul)
        c = c + 1  # Count (cumul, suppose n = c)
        h = n ** -2  # N term
        t = t + h  # Sum of terms (cumul)
        x = (6 * t) ** 0.5  # pi of n
        l = pi - x  # comparison
        print('Current Number (n):',float(n))
        print('n^-2 = ',h)
        print('sum of n^-2 terms:',t)
        print('Current calculated pi (x):',x)
        print('pi - x (l):',l)
        print('   ')
        print('   ')

        if l == 0:
            print('To find pi, we need to sum up to ',c,'.')

else:
    print('Invalid input, program end.')