#i created an online books store
book_detective = "The Adventures of Sherlock Holmes"
detective_price = 30
detective_discount = (30*90/100)
description_detective = """A literary character created by Arthur Conan Doyle,
                  The legendary detective Sherlock Holmes is still very popular
                  benefits from Conan Doyle wrote 4 novels and 56 short stories
                  on Sherlock Holmes, and each of them has become a classic of the detective genre.
                  Of the entangled crime, Dr. Watson tells us,
                  However, neither he nor the reader understands until the end of the investigation.
                  How a detective solves the most mysterious crime before the end of the story
                  He himself does not explain the secret of the "deductive method".

                  "The Adventures of Sherlock Holmes" combines 11 stories,
                  In which the events described happened when Dr. Watson Sherlock
                  He lived with Holmes on Baker Street."""

book_novel = "One Hundred Years of Solitude"
novel_price = 25
novel_discount = (30*90/100)
description_novel = """  One Hundred Years of Solitude", in a fictional world,
                         Macondo was born in the 40s of the 19th century and until the 30s of the 20th century,
                         That is, it lasts a whole century. During this century, six generations will change in the settlement.
                         Don't consider six generations a joke. If we look at Greek mythology,
                         Here are four generations: out of chaos comes order, then comes Uranus,
                         Kronos and finally Zeus. People appear in the fifth generation,
                         And the degeneration and fall of the golden people, their iron
                         Becoming human occurs in the sixth generation. That's what Marques knows!"""

book_adventure = "secret island"
adventure_price = 18
advanture_discount = (30*95/100)
description_adventure = """Adventures of five brave people stranded on a secret island
                             It is a kind of sequel to the novel "80,000 Kilometers Under Water".
                             As far as the knot of strange news spinning underwater
                             It is on this secret island that it opens. The novel is being read
                             In short, it tells the story of Engineer Smith and his
                             About friends who sneak out of the POW camp
                             They will succeed and leave the war territory with a balloon. Good luck to them
                             banished to an uninhabited island,
                             Thanks to perseverance and inventive talent in a few years
                             They will turn it into a prosperous door. However, if not for the newcomers
                             Invisible mercy, they could not last long - the heroes of this invisible
                             The Merciful will be sought until the last pages of the book, and whoever he turns out to be,
                             The reader will recognize it by himself if he follows the clues in the novel..."""
book_historical = "Great Battles of Georgia"
historical_price = 50
historical_discount = (30*95/100)
description_historical = """Professor Jabba Samushia included in this book only
                             Famous and large-scale battles in which especially
                             The military talent of the Commander-in-Chief, the attitude and dedication of the Georgian warrior can be seen.
                             Which is made even more visible by numerous illustrations and documentary materials.
                             The book is also interesting in that it includes works by Sasireti, Bassiani,
                             Battles localized by the author of Shamkor and Garnis."""

interesed = input("which genre are you interesed in? ")
if interesed == "detective":
    print ("we only have", book_detective)

    intereser_description = input("you are interesed in the description of the book? ")
    if intereser_description == "yes":
        print(description_detective)
    elif intereser_description == "no":
        print ("it's sad")
    buy = input("you want to buy? ")
    if buy == "yes":
        print ("this book is worth it", detective_price, "gel" " 10 procent discount ",detective_discount, "gel")
    elif buy == "no":
        print ("it's sad")


if interesed == "novel":
    print ("we only have", book_novel)
    intereser_description = input("you are interesed in the description of the book? ")
    if intereser_description == "yes":
        print(description_novel)
    elif intereser_description == "no":
        print ("it's sad")
    buy = input("you want to buy? ")
    if buy == "yes":
        print ("this book is worth it", novel_price, "gel" " 10 procent discount ",novel_discount, "gel")
    elif buy == "no":
        print ("it's sad")

if interesed == "adventure":
    print ("we only have", book_adventure)
    intereser_description = input("you are interesed in the description of the book? ")
    if intereser_description == "yes":
        print(description_adventure)
    elif intereser_description == "no":
        print ("it's sad")
    buy = input("you want to buy? ")
    if buy == "yes":
        print ("this book is worth it", adventure_price, "gel" " 5 procent discount ",advanture_discount, "gel")
    elif buy == "no":
        print ("it's sad")

if interesed == "historical":
    print ("we only have", book_historical)
    intereser_description = input("you are interesed in the description of the book? ")
    if intereser_description == "yes":
        print(description_historical)
    elif intereser_description == "no":
        print ("it's sad")
    buy = input("you want to buy? ")
    if buy == "yes":
        print ("this book is worth it", historical_price, "gel" " 5 procent discount ",historical_discount, "gel")
    elif buy == "no":
        print ("it's sad")