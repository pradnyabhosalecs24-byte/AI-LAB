
# Forward Chaining using First Order Logic

# Step 1: Initial facts
facts = {
    ("American", "Robert"),
    ("Enemy", "A", "America"),
    ("Missile", "M1"),
    ("Owns", "A", "M1")
}

# Step 2: Forward Chaining
def forward_chaining(facts):

    new_facts = True

    while new_facts:
        new_facts = False

        # Rule 1: Enemy(x, America) -> Hostile(x)
        for f in list(facts):
            if f[0] == "Enemy":
                new = ("Hostile", f[1])
                if new not in facts:
                    facts.add(new)
                    print("Derived:", new)
                    new_facts = True

        # Rule 2: Missile(y) -> Weapon(y)
        for f in list(facts):
            if f[0] == "Missile":
                new = ("Weapon", f[1])
                if new not in facts:
                    facts.add(new)
                    print("Derived:", new)
                    new_facts = True

        # Rule 3: Missile(y) -> Sells(Robert,y,A)
        for f in list(facts):
            if f[0] == "Missile":
                new = ("Sells", "Robert", f[1], "A")
                if new not in facts:
                    facts.add(new)
                    print("Derived:", new)
                    new_facts = True

        # Rule 4: American(x) AND Weapon(y) AND
        # Sells(x,y,z) AND Hostile(z) -> Criminal(x)

        for a in list(facts):
            for w in list(facts):
                for s in list(facts):
                    for h in list(facts):

                        if (a[0] == "American" and
                            w[0] == "Weapon" and
                            s[0] == "Sells" and
                            h[0] == "Hostile"):

                            if (a[1] == s[1] and
                                w[1] == s[2] and
                                h[1] == s[3]):

                                new = ("Criminal", a[1])

                                if new not in facts:
                                    facts.add(new)
                                    print("Derived:", new)
                                    new_facts = True

    return facts


# Step 3: Display initial facts
print("Initial Facts:")
for f in sorted(facts):
    print(f)

# Step 4: Execute Forward Chaining
print("\nApplying Forward Chaining...\n")

result = forward_chaining(facts)

# Step 5: Display both conclusions
print("\nFinal Result:")

if ("Criminal", "Robert") in result:
    print("Robert is a Criminal!")
    print("Robert is not a Criminal: False")
else:
    print("Robert is a Criminal: False")
    print("Robert is not a Criminal!")
