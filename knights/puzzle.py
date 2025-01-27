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
    # A is either a knight or a knave, but not both.
    Or(AKnave, AKnight),
    Not(And(AKnight, AKnave)),

    # If A is a knight, their statement must be true.
    Implication(AKnight, And(AKnight, AKnave)),

    # If A is a knave, their statement must be false.
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A is either a knight or a knave, but not both.
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # B is either a knight or a knave, but not both.
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # If A is a knight, their statement about both being knaves must be true.
    Implication(AKnight, And(AKnave, BKnave)),

    # If A is a knave, their statement about both being knaves must be false.
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A is either a knight or a knave, but not both.
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # B is either a knight or a knave, but not both.
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # If A is a knight, their statement about being the same kind must be true.
    Implication(AKnight, Biconditional(AKnight, BKnight)),

    # If A is a knave, their statement about being the same kind must be false.
    Implication(AKnave, Not(Biconditional(AKnight, BKnight))),

    # If B is a knight, their statement about being different kinds must be true.
    Implication(BKnight, Not(Biconditional(AKnight, BKnight))),

    # If B is a knave, their statement about being different kinds must be false.
    Implication(BKnave, Biconditional(AKnight, BKnight))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave.'"
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # A is either a knight or a knave, but not both.
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # B is either a knight or a knave, but not both.
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # C is either a knight or a knave, but not both.
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    # If B is a knight, their statement about A saying "I am a knave" must be true.
    Implication(BKnight, Biconditional(AKnight, AKnave)),

    # If B is a knave, their statement about A saying "I am a knave" must be false.
    Implication(BKnave, Not(Biconditional(AKnight, AKnave))),

    # If B is a knight, their statement about C being a knave must be true.
    Implication(BKnight, CKnave),

    # If B is a knave, their statement about C being a knave must be false.
    Implication(BKnave, Not(CKnave)),

    # If C is a knight, their statement about A being a knight must be true.
    Implication(CKnight, AKnight),

    # If C is a knave, their statement about A being a knight must be false.
    Implication(CKnave, Not(AKnight))
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
