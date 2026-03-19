tickets = input().split(", ")
winning_symbols = ['@', '#', '$', '^']

for ticket in tickets:
    ticket = ticket.strip()

    if len(ticket) != 20:
        print(f"invalid ticket")

        for symbol in winning_symbols:
            if symbol in ticket and symbol.count() == 20:
                print(f"ticket {ticket} - {symbol}")


    print(ticket)

