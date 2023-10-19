class Party:
    def __init__(self):
        self.people = []

party = Party()
line_input = input()
while line_input != "End":
    party.people.append(line_input)
    line_input = input()
print(f"Going: {', '.join(party.people)}" )
print(f"Total: {len(party.people)}")
