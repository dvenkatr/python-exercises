from enum import IntEnum, auto

class Category(IntEnum):
    HighCard = auto()
    OnePair = auto()
    TwoPair = auto()
    ThreeKind = auto()
    Straight = auto()
    Flush = auto()
    FullHouse = auto()
    FourKind = auto()
    StraightFlush = auto()
    FiveKind = auto()

def best_hands(hands):

    best_hands = []
    first_round = True

    # For each hand, find the category and compare it with the current best hand.

    for hand in hands:
        ranks, category = find_category(hand.replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14').split())

        print(ranks, category)

        if first_round:
            best_category = category
            best_hands = [hand]
            best_ranks = ranks
            first_round = False

        elif category > best_category:
            best_category = category
            best_hands = [hand]
            best_ranks = ranks

        elif category == best_category:
            best_hands, best_ranks = break_tie(best_hands[0], best_ranks, hand, ranks)

    return best_hands

def find_category(hand):

    sorted_ranks, rank_count, suit_count = sort_hand(hand)

    # Five of a kind = same rank. 
    # Impossible in a single card deck (without a joker). 
    # Joker is not considered in this solution.
    # e.g. [5H, 5D, 5C, 5S, 5H] or 5H, 5D, 5C, 5S, Joker]
    if len(rank_count) == 1:
        return sorted_ranks, Category.FiveKind

    # Straight flush = same suit, in sequence.
    # e.g. [5H, 6H, 7H, 8H, 9H]
    # Flush = same suit, not in sequence.
    # e.g. [4H, 8H, 9H, 10H, JH]
    if len(suit_count) == 1:
        # Is the sequence is A, 2, 3, 4, 5 then A should be treated as 1
        if is_sequence(sorted_ranks):
            if min(sorted_ranks) == 2 and max(sorted_ranks) == 14:
                sorted_ranks.remove(14)
                sorted_ranks.insert(0, 1)
            return sorted_ranks, Category.StraightFlush
        else:
            return sorted_ranks, Category.Flush

    # Four of a kind = 4 cards of one rank.
    # e.g. [5H, 5D, 5C, 5S, any]
    # Full house = 3 cards of one rank, 2 of another rank.
    # e.g. [5H, 5D, 5C, 6S, 6H]
    if len(rank_count) == 2:
        if 4 in rank_count.values():
            return sorted_ranks, Category.FourKind
        elif 3 in rank_count.values() and 2 in rank_count.values():
            return sorted_ranks, Category.FullHouse

    # Straight = not the same suit, in sequence.
    # e.g. [5H, 6D, 7C, 8S, 9H]
    # Is the sequence is A, 2, 3, 4, 5 then A should be treated as 1
    if is_sequence(sorted_ranks):
        if min(sorted_ranks) == 2 and max(sorted_ranks) == 14:
                sorted_ranks.remove(14)
                sorted_ranks.insert(0, 1)
        return sorted_ranks, Category.Straight

    # Three of a kind = 3 cards of one rank.
    # e.g. [5H, 5D, 5C, 7H, 8D]
    # Two pair = 2 cards of one rank, 2 cards of another.
    # e.g. [5H, 5D, 6C, 6D, 7H]
    if len(rank_count) == 3:
        if 3 in rank_count.values():
            return sorted_ranks, Category.ThreeKind
        else:
            return sorted_ranks, Category.TwoPair

    # Two pair = 2 cards of one rank.
    # e.g. [5H, 5D, 6C, 7D, 8C]
    if len(rank_count) == 4:
        return sorted_ranks, Category.OnePair

    return sorted_ranks, Category.HighCard

# If the categories for two hands are the same, break the tie.
def break_tie(best_hand, best_ranks, hand, ranks):
    
    # Evaluate the rank in order to break the tie.

    # 2, 3, 4, 5, 6 is the smallest sequence.
    # Account for 2, 3, 4, 5, 6 < A, 2, 3, 4, 5.

    if best_ranks > ranks:
        return [best_hand], best_ranks
    elif best_ranks < ranks:
        return [hand], ranks
    else:    
        return [best_hand, hand], best_ranks

# Check if the cards are in sequence.
# A, 2, 3, 4, 5 and 10, J, Q, K, A are valid.
def is_sequence(ranks):

    # Account for 10, J, Q, K, A
    if min(ranks) == 2 and max(ranks) == 14:
        for i in range(1,4):
            if min(ranks) + i not in ranks:
                return False
        return True

    else:
        for i in range(1,5):
            if min(ranks) + i not in ranks:
                return False
        return True

def sort_hand(hand):

     # Split the ranks and suits into separate lists.
    # e.g. # e.g. [10, 2, 2, 11, 2] and [H, H, D, S, C]

    ranks = []
    suits = []

    for card in hand:
        ranks.append(int(card[0:-1]))
        suits.append(card[-1])

    # Get a count of each rank and suit in a dict.
    # e.g. {10 : 1, 2 : 3, 11 : 1} and {H : 2, D : 1, S : 1, C : 1}

    rank_count = {rank : ranks.count(rank) for rank in set(ranks)}
    suit_count = {suit : suits.count(suit) for suit in set(suits)}

    # Convert the rank and the rank count to a list of tuples, sorted by count, then rank.
    # e.g. [(2, 3) (11,1), (10, 1)]

    rank_count_tuple = rank_count.items()
    sorted_tuples = sorted(rank_count_tuple, key = lambda i : (i[1], i[0]), reverse = True)

    # Create a rank list sorted in the order that the ranks would be evaluated in a tie.
    # e.g. [2, 2, 2, 11, 10]

    sorted_ranks = []
    for i in range(0, len(sorted_tuples)):
        sorted_ranks += [sorted_tuples[i][0]] * sorted_tuples[i][1]

    return sorted_ranks, rank_count, suit_count
