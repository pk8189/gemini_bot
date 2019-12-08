# A genetic algorithm trained to trade crypto on Gemini


### The approach
**Gene**: an action represented by constant integers (-1 = sell, 0 = do nothing, 1 = buy)
**Individual**: a combintation of actions leading to a gain over TBD minutes/hours.
**Population**: a collection of individuals
**Parents**: two collections to be merged.


**Mating pool**: a collection of parents that are used to create our next population (thus creating the next generation of routes)
**Fitness**: a function that tells us how good each route is (in our case, how short the distance is)
**Mutation**: a way to introduce variation in our population by randomly swapping two cities in a route
**Elitism**: a way to carry the best individuals into the next generation\



Article notes:
poetry init
conda create --name gemini_bot python=3.7
poetry install