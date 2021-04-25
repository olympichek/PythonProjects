daysInMonth :: Int -> Int -> Either String Int
daysInMonth 2 y
    | y `mod` 400 == 0 = Right 29
    | y `mod` 100 == 0 = Right 28
    | y `mod` 4   == 0 = Right 29
    | otherwise        = Right 28
daysInMonth m y
    | m < 0 || m > 12 = Left "Month should be between 1 and 12!"
    | otherwise       = Right $ if m `elem` m31 then 31 else 30 
    where m31 = [1, 3, 5, 7, 8, 10, 12]

main :: IO ()
main = do
    m <- putStrLn "Enter month:" >> readLn
    y <- putStrLn "Enter year:"  >> readLn
    putStrLn $ case daysInMonth m y of
        Right d -> "Days in this month: " ++ show d
        Left  e -> e