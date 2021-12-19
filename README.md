# Sinnoh-EV-Calculator

Simple EV calculator for use as a Pokemon is EV trained.
Enter simple information to start, then enter names of Pokemon as they are defeated.
Calculator will keep track of EVs, including modifiers such as PokeRus and items.
Despite the name, able to be used with any generation/PokeDex, given that input .txt file is in alphabetical order, with name and EVs separated by spaces (included are the Sinnoh Dex and National PokeDex, with EVs coinciding with Gen IV)

## Inputs:
### Beginning
- Name
- Goal EVs
- Current EVs
- Has PokeRus?
- Has modifier items? ()
### During
- Numbers
    - 1: Save
    - 2: Pokerus status change
    - 3: Change item
    - 4: Change PokeDex
- Name of Pokemon caught

## What are EVs?
Pokemon have 6 stats: HP (Hit Points (health)), Attack, Defense, Special Attack, Special Defense, and Speed. These stats are calculated based on:
1. the Pokemon's species: each Pokemon has its own set of base stats. For example:
    ![comparison of Rampardos vs Lapras's stats](comparison.png "Rampardos vs Lapras Stats")
    On the left is Rampardos's stats, and on the right is Lapras's.
3. its Nature
4. its IVs
5. its EVs
