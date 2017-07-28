Libby = 0
Xander = 0
Libby_Xander = 0

#choice1= input("1. Start Game or 2. QUIT \n")
print("Welcome to our Dating Sim! press 1 for the first option and 2 for the second!\n")
choice1= input("Type GO to start the game.\n")
if choice1 == "GO":
    print("Your life with your two best friends, Libby and Xander has gone pretty smoothly. However, Libby started acting out yesterday when you decided to not come to the mall with her and Xander and you two got into a fight. What do you do?\n")

    ####################################################################################

    choice2= input("1.Apologize to Libby or 2.Let her deal, what's her problem?\n")
    if choice2== "1":
        print("You decided to send her a 'Sorry' text. She accepted your apology. Xander rolls his eyes at the girl drama.\n")
        print("Your relationship with Libby went up! Your relationship with Xander went down...\n")
        Libby = Libby + 1
        Xander = Xander - 1

    ####################################################################################

        choice3= input("Trying to get the gang back together, Xander offers to take Libby, yourself and a guy of your choice out on a double date. Libby happily accepts. 1. Be jealous. She KNOWS you like him! or 2. About time she's making a move!\n")
        if choice3== "2":
            print("You 'accidentally' bump Libby into Xander. They're both mostly confused, but they blush anyways. You feel like a little cupid.\n")
            print("Libby and Xander's relationship went up! Your relationship with Libby went up!\n")
            Libby = Libby + 3
            print("He asks you if you would like to join. What do you say?\n")

    #####################################################################################

            choice6= input("1. Nah, you guys go ahead without me. Have fun! or 2. Ummm... Well actually, Libby and I had plans.\n")
            if choice6== "1":
                print("Libby punches you in the shoulder but nods. They hold hands and say goodbye to you, as they start walking to your favorite ice cream shop.\n")
                print("As you part ways, you feel happy for them, but shed a tear for your sad, single self.\n")
                print("Your relationships with both Libby and Xander went up!\n")
                Libby = Libby + 4
                Xander = Xander + 2
                print("You got the 'foreveralone' ending. Play for more endings!\n")

    #####################################################################################

            elif choice6== "2":
                print("Libby blinks. 'We did?' she asks? You roll your eyes and lead her to your favorite ice cream shop, leaving Xander bewildered by his newfound ditching.\n")
                print("Your relationship with Libby went up!\n")
                Libby = Libby + 2
                print("After settling in at your seats, you notice Libby is being a little quiet.\n")
                print("You ask whats wrong, and she hesitates -- then she asks\n")
                print("'Do you like me? Like, LIKE like me?'")

                choice10= input("1. Damn straight! Which coincidentally, we are not! 2.Nope. Sorry Libby.\n")
                if choice10 == "1":
                    if Libby >= 5:
                        print("Libby beams, and holds your hand!\n")
                        print("Together, you finish your ice cream and set off into the sunset as an awesome lesbian power couple.\n")
                        print("Congratulations! You got Libby's ending. Play for more endings!\n")

    #####################################################################################

                elif choice10 == "2":
                    print("Libby runs away from the ice cream store.\n")
                    print("She blocks you out of embarassment, and you never speak again.\n")
                    print("Congratulations! You broke Libby's heart. Play more for different endings!\n")

    #####################################################################################

        elif choice3== "1":
            print("You decide to voice your thoughts on this proposition. You ask her how she could betray you like this and she just storms off crying.\n")
            print("Your relationship with Libby went down. I mean like DOWN down.\n")
            Libby = Libby - 5
            print("You tell Xander she felt sick. He asks you out to get ice cream!\n")
            print("Relationship with Xander went up!")
            Xander = Xander + 1

            choice8= input("1. YES!! or 2. Nah...\n")
                #XANDERS ROUTE
            if choice8== "2":
                print("You say goodbye, and head home.\n")
                print("Relationship with Xander went down!\n")
                print("You spend the rest of the day playing video games. As the day comes to an end, you find you didn't spend much time with your friends. Maybe if you got closer to them, something might happen? After all, this is a dating sim-like game whose goal is to romance fictional characters. Why would you spend your gametime doing nothing? Now, GO PLAY THE GAME!\n")

    #####################################################################################

            elif choice8== "1":
                print("You spend the rest of the day with Xander, eating ice cream and talking about life. He asks you what you think of him. What do you say?\n")

                choice12= input("1. I like him! 2. Just friends.\n")
                if choice12== "1":
                    print("Relationship with Xander went WAYYYY up!\n")
                    Xander = Xander + 5
                    if Xander >= 5:
                        print("You tell him you like him, he breaths a sigh of relief. Turns out he liked you too!\n")
                        print("You take a couple selfies, change your FaceBook relationship statuses, and go home giddy as ever.\n")
                        print("Congratulations!\n")
                        print("You got Xanders' ending! Play for other endings!\n")
                    if Xander < 5:
                        print("You tell him you like him, but he tells you he'd rather be 'just friends'. He leaves in a rush, escaping the dead silence and the stale air that falls in the ice cream store after your unfortunate rejection by a fictional character.\n")
                        print("Congrats.\n")
                        print("You just got rejected, son! Play again for more endings!\n")

    #####################################################################################

                elif choice12== "2":
                    print("He looks dissapointed, but he says he understands. He leaves, dejected, as he wishes things had been different.\n")
                    print("Wow. Friendzoned, huh. Okay. You got the ending wherre you friendzone your friend. Because why would you go down his ending to just completely reject him. But then again, we put that option there in the first place. Play for other endings!\n")

    ####################################################################################
    ####################################################################################
    ####################################################################################

    elif choice2== "2":
        print("You decide to ignore Libby for now and complain about her to Xander, who is a surprisingly good listener.\n")
        print("Your Relationship with Xander went up! Your relationship with Libby went down...\n")
        Libby = Libby - 2
        Xander = Xander + 1
        print("The next day, you see Xander and Libby at school. It looks like she's flirting with him!\n")

    #####################################################################################

        choice4= input("1. Be jealous. She KNOWS you like him! or 2. About time she's making a move!\n")
        if choice4== "2":
            print("You 'accidentally' bump Libby into Xander. They're both mostly confused, but they blush anyways. You feel like a little cupid.\n")
            print("Libby and Xander's relationship went up! Your relationship with Libby went up!\n")
            Libby = Libby + 3
            print("He asks Libby if she'd like to go out, but she's too shy to answer. What do you say?\n")

    #####################################################################################

            choice7= input("1.'Of COURSE she'd like to go with you! *wink wink* or 2. Nah, Libby and I had plans.\n")
            if choice7== "1":
                print("Libby punches you in the shoulder but nods. They hold hands and say goodbye to you, as they start walking to your favorite ice cream shop.\n")
                print("As you part ways, you feel happy for them, but shed a tear for your sad, single self.\n")
                print("Your relationships with both Libby and Xander went up!\n")
                Libby = Libby + 4
                Xander = Xander + 2
                print("You got the 'foreveralone' ending. Play for more endings!\n")

    #####################################################################################

            elif choice7== "2":
                print("Libby blinks. 'We did?' she asks? You roll your eyes and lead her to your favorite ice cream shop, leaving Xander bewildered by his newfound ditching.\n")
                print("Your relationship with Libby went up!\n")
                Libby = Libby + 2
                print("After settling in at your seats, you notice Libby is being a little quiet.\n")
                print("You ask whats wrong, and she hesitates-- then she asks\n")
                print("'Do you like me? Like, LIKE like me?'")

                choice11= input("1. Damn straight! Which coincidentally, we are not! 2.Nope. Sorry Libby.\n")
                if choice11 == "1":
                    if Libby >= 5:
                        print("Libby beams, and holds your hand!\n")
                        print("Together, you finish your ice cream and set off into the sunset as an awesome lesbian power couple.\n")
                        print("Congratulations! You got Libby's ending. Play for more endings!\n")

    #####################################################################################

                elif choice11 == "2":
                    print("Libby runs away from the ice cream store.\n")
                    print("She blocks you out of embarassment, and you never speak again.\n")
                    print("Congratulations! You broke Libby's heart. Play more for different endings!\n")

    #####################################################################################

        elif choice4== "1":
            print("You decide to approach the 'couple' and you pull Libby aside. You ask her how she could betray you like this and she just storms off crying.\n")
            print("Your relationship with Libby went down. I mean like DOWN down.\n")
            Libby = Libby - 5
            print("You tell Xander she felt sick. He asks you out to get ice cream!\n")
            print("Relationship with Xander went up!")
            Xander = Xander + 1

            choice5= input("1. YES!! or 2. Nah...\n")
                #XANDERS ROUTE
            if choice5== "2":
                print("You say goodbye, and head home.\n")
                print("Relationship with Xander went down!\n")
                print("You spend the rest of the day playing video games. As the day comes to an end, you find you didn't spend much time with your friends. Maybe if you got closer to them, something might happen? After all, this is a dating sim-like game whose goal is to romance fictional characters. Why would you spend your gametime doing nothing? Now, GO PLAY THE GAME!\n")

    #####################################################################################

            elif choice5== "1":
                print("You spend the rest of the day with Xander, eating ice cream and talking about life. He asks you what you think of him. What do you say?\n")

                choice9= input("1. I like him! 2. Just friends.\n")
                if choice9== "1":
                    print("Relationship with Xander went WAYYYY up!\n")
                    Xander = Xander + 5
                    if Xander >= 5:
                        print("You tell him you like him, he breaths a sigh of relief. Turns out he liked you too!\n")
                        print("You take a couple selfies, change your FaceBook relationship statuses, and go home giddy as ever.\n")
                        print("Congratulations!\n")
                        print("You got Xanders' ending! Play for other endings!\n")
                    if Xander < 5:
                        print("You tell him you like him, but he tell you he'd rather be 'just friends'. He leaves in a rush, escaping the dead silence and the stale air that falls in the ice cream store after your unfortunate rejection by a fictional character.\n")
                        print("Congrats.\n")
                        print("You just got rejected, son! Play again for more endings!\n")

    #####################################################################################

                elif choice9== "2":
                    print("He looks dissapointed, but he says he understands. He leaves, dejected, as he wishes things had been different.\n")
                    print("Wow. Friendzoned, huh. Okay. You got the ending wherre you friendzone your friend. Because why would you go down his ending to just completely reject him. But then again, we put that option there in the first place. Play for other endings!\n")
