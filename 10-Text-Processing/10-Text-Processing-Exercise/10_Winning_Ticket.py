def check_ticket(ticket: str) -> str:
    if len(ticket) != 20:
        return "invalid ticket"
    winning_symbols = ('@', '#', '$', '^')
    left_part = ticket[:10]
    right_part = ticket[10:]
    for match_symbol in winning_symbols:
        for uninterrupted_match_length in range(10, 5, -1):
            match_symbol_repetition = uninterrupted_match_length * match_symbol
            # Case where we have a winning ticket
            if match_symbol_repetition in left_part and match_symbol_repetition in right_part:
                # Case Jackpot
                if uninterrupted_match_length == 10:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!'
                # Case just a winning ticket
                return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]
for current_ticket in tickets:
    print(check_ticket(current_ticket))



# ver 2

def find_match(part):
    for symbol in "@#$^":
        for count in range(10, 5, -1):
            if symbol * count in part:
                return symbol, count
    return "", 0


tickets = input().split(", ")
for ticket in tickets:
    ticket = ticket.strip()

    if len(ticket) != 20:
        print("invalid ticket")
        continue

    left = ticket[:10]
    right = ticket[10:]

    left_symbol, left_count = find_match(left)
    right_symbol, right_count = find_match(right)

    if left_symbol == right_symbol and left_symbol != "":
        match_count = min(left_count, right_count)

        if match_count == 10:
            print(f'ticket "{ticket}" - {match_count}{left_symbol} Jackpot!')
        else:
            print(f'ticket "{ticket}" - {match_count}{left_symbol}')
    else:
        print(f'ticket "{ticket}" - no match')