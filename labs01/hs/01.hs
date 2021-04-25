convertYears :: Double -> Either String Double
convertYears x
    | x < 0     = Left "Years should be positive!"
    | x <= 2    = Right $ x * k1
    | otherwise = Right $ 2 * k1 + (x - 2) * k2
    where { k1 = 10.5; k2 = 4 }

main :: IO ()
main = do
    putStrLn "Enter human years: "
    y <- convertYears <$> readLn
    putStrLn $ either id (("Dog years: " ++) . show) y