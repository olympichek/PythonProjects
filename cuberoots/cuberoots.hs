import Data.Complex ( Complex(..), realPart )

a, b, c, d, p, q       :: Complex Double
_Q, alpha, beta        :: Complex Double
y1, y2, y3, x1, x2, x3 :: Complex Double

a = -8
b = 57
c = -124
d = 81

p = (3*a*c - b**2) / (3 * a**2)
q = (2 * b**3 - 9*a*b*c + 27 * a**2 * d) / (27 * a**3)

_Q = (p / 3) ** 3 + (q / 2) ** 3

alpha = (-(q / 2) + sqrt _Q) ** (1 / 3)
beta  = (-(q / 2) - sqrt _Q) ** (1 / 3)

y1 = alpha + beta
y2 = -((alpha + beta) / 2) + (0 :+ 1) * ((alpha - beta) / 2) * sqrt 3
y3 = -((alpha + beta) / 2) - (0 :+ 1) * ((alpha - beta) / 2) * sqrt 3

x1 = y1 - b / (3 * a)
x2 = y2 - b / (3 * a)
x3 = y3 - b / (3 * a)

main :: IO ()
main = mapM_ print [x1, x2, x3]
-- main = mapM_ (print . realPart) [x1, x2, x3]
