import System.IO ( stdout, hFlush )

type Point = (Double, Double)
type Edge  = (Point, Point)

calcDistance :: Edge -> Double 
calcDistance ((x1, y1), (x2, y2))
    = sqrt $ (x1 - x2) ** 2 + (y1 - y2) ** 2

pointsToEdges :: [Point] -> [Edge]
pointsToEdges ps
    | length ps < 2 = []
    | otherwise     = (head ps, last ps) : helper ps
    where
    helper [p1, p2]   = [(p1, p2)]
    helper (p1:p2:ps) = (p1, p2) : helper (p2:ps)

calcPerimeter :: [Edge] -> Double
calcPerimeter = sum . map calcDistance

getPoints :: IO [Point]
getPoints = do
    line <- do
        putStr "Enter point coordinates: "
        hFlush stdout >> getLine
    if not $ null line then do
        let (x:y:_) = map read $ words line
        ((x, y):) <$> getPoints
    else return []

main :: IO ()
main = do
    p <- calcPerimeter . pointsToEdges <$> getPoints
    putStrLn $ "Perimeter: " ++ show p