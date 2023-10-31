def check_ticket(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    winnings_symbol = ["@", "#", "$", "^"]
    left_part = ticket[:10]
    right_part = ticket[10:]
    for match_symbol in winnings_symbol:
        for uninterrupted_match_length in range(10, 5, -1):
            winnings_symbol_repetition = match_symbol * uninterrupted_match_length
            if winnings_symbol_repetition in left_part and winnings_symbol_repetition in right_part:
                if uninterrupted_match_length == 10:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!'
                return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}'
    return f'ticket "{ticket}" - no match'

tickets = [ticket.strip() for ticket in input().split(", ")]
for ticket in tickets:
    print(check_ticket(ticket))