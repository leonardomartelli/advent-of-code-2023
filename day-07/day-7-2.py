
from functools import cmp_to_key


def get_card_power(card):
    match card:
        case 'A':
            return 13
        case 'K':
            return 12
        case 'Q':
            return 11
        case 'T':
            return 10
        case 'J':
            return 1
        case _:
            return int(card)


def get_hand_power(hand):
    old_hand = hand
    sorted_by_occurrence = [h for h in hand]

    sorted_by_occurrence.sort(
        reverse=True, key=lambda c: 0 if c == 'J' else hand.count(c))

    hand = str.join('', sorted_by_occurrence).replace(
        'J', sorted_by_occurrence[0])

    if 'J' in old_hand and hand != old_hand:
        print(old_hand, hand)

    hand_unique = list(set(hand))
    qnt = len(hand_unique)

    if qnt == 1:
        return 7
    elif qnt == 2:
        count_of_first = hand.count(hand[0])
        if count_of_first == 4 or count_of_first == 1:
            return 6
        else:
            return 5
    elif qnt == 3:
        count_of_first = hand.count(hand_unique[0])
        count_of_last = hand.count(hand_unique[2])

        if count_of_first == 2 or count_of_last == 2:
            return 3
        else:
            return 4

    elif qnt == 4:
        return 2

    return 1


def compare_hand(hb1, hb2):
    hand1 = hb1[0]
    hand2 = hb2[0]

    hand1_order = [c for c in hand1]
    hand1_order.sort(key=get_card_power)

    hand2_order = [c for c in hand2]
    hand2_order.sort(key=get_card_power)

    result = get_hand_power(hand1) - get_hand_power(hand2)

    if result == 0:
        i = 0
        result = get_card_power(hand1[i]) - get_card_power(hand2[i])

        while result == 0:
            i += 1
            result = get_card_power(hand1[i]) - get_card_power(hand2[i])

    return result


puzzle_input_file = open('input.txt', 'r')
puzzle_input = puzzle_input_file.read()


hands_and_bets = puzzle_input.split('\n')

hands = []

for hb in hands_and_bets:
    splitted = hb.split()
    hands.append((splitted[0], splitted[1]))

hands.sort(key=cmp_to_key(compare_hand))

sum = 0

for i in range(len(hands)):
    sum += int(hands[i][1]) * (i + 1)

print(sum)
