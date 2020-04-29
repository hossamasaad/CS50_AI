from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    
    # Rules of The Game [A is Knave or Knight]
    Or(AKnight, AKnave),
    
    # if Aknight then sentence true
    Implication(AKnight, And(AKnave, AKnight)),
    
    # if Aknave then sentence Not true
    Implication(AKnave, Not(And(AKnave, AKnight)))

)



# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(

    # Rules of The Game
    Or(AKnight, AKnave),Or(BKnight, BKnave),
    
    # If AKnight then, AKnave and BKnave
    Implication(AKnight, And(AKnave, BKnave)),
    
    # If AKnave then, BKnight or Not(And(AKnave, BKnave)) 
    Implication(AKnave, Not(And(AKnave, BKnave)))

)



# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    
    # Rules of The Game
    Or(AKnight, AKnave),Or(BKnight, BKnave),
    
    # if AKnight, then Both are the same kinds[B Knight]
    Implication(AKnight, Or( And(AKnight, BKnight), And(AKnave, BKnave))),
    
    # if AKnave, then Both are different kinds[B Knight]
    Implication(AKnave, Not(Or( And(AKnight, BKnight), And(AKnave, BKnave)))),
    
    # if B Knight Then, Both are differnt types[A Knave] 
    Implication(BKnight, Or( And(AKnight, BKnave), And(AKnave, BKnight))),
    
    # if B Knave Then, Both are the same Type[A Knave]
    Implication(BKnave, Not(Or( And(AKnight, BKnave), And(AKnave, BKnight))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Rules of the game
    Or(AKnight, AKnave),Or(BKnight, BKnave),Or(CKnight,CKnave),
    
    
    # if B knight then, there are two cases AKnight, or AKnave
    Implication(BKnight, And(Implication(AKnight, AKnave),Implication(AKnave, Not(AKnave)))),
   
    # if B knave then, there are two cases AKnight, or AKnave
    Implication(BKnave, Not(And(Implication(AKnight, AKnave),Implication(AKnave, Not(AKnave))))),
   
    # if B Knight, C Knave
    Implication(BKnight, CKnave),
    
    # if B Knave, C Knight
    Implication(BKnave, CKnight),

    # if C Knight, A Knight    
    Implication(CKnight, AKnight),
    
    # if C Knave, A Knave
    Implication(CKnave, AKnave),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
