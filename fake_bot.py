import pyttsx3
import pywhatkit
import time
import wikipedia
import sys
import turtle


engine = pyttsx3.init()
engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PL-PL_PAULINA_11.0")
rate= engine.getProperty("rate")
engine.setProperty("rate", rate-25)

def say(tongue):
    engine.say(tongue)
    engine.runAndWait()

def play_music(track):
    try:
        engine.say(f"Włączam: ", track)
        engine.runAndWait()
        pywhatkit.playonyt(track)
    except TypeError:
        print("Niestety nie można włączyć muzyki")

def zgadywanka():
    while True:
        game_level= input("Wybierz poziom trudności (łatwy/średni/trudny)")
        if game_level== "łatwy":
            no_of_tries= 10
            print("Ilość prób: ", no_of_tries)
            break
        elif game_level== "średni":
            no_of_tries= 8
            print("Ilość prób: ", no_of_tries)
            break
        elif game_level== "trudny":
            no_of_tries= 3
            print("Ilość prób: ", no_of_tries)
            break
        else:
            print("Wprowadzono nieprawidłowe dane, spróbuj jeszcze raz")
            print()
        
    print("UWAGA PODPOWIEDŹ! Jednym ze znaków jest spacja :) ")

    word= "jak wytresować smoka"
    used_letters= []

    user_word= []

    def find_indexes(word, letter):
        indexes= []

        for index, letter_in_word in enumerate(word):
            if letter == letter_in_word:
                indexes.append(index)


        return indexes

    def show_state_of_game():
        print()
        print(user_word)
        print("Pozostało prób:", no_of_tries)
        print("Użyte litery:", used_letters)
        print()

    for _ in word:
        user_word.append("_")

    while True:
        letter= input("Podaj literę: ")
        used_letters.append(letter)

        found_indexes= find_indexes(word, letter)

        if len(found_indexes) == 0:
            print("Błąd!")
            print()
            no_of_tries -= 1

            if no_of_tries== 0:
                print("Koniec gry")
                break
        
        else:
            for index in found_indexes:
                user_word[index]= letter

            if "".join(user_word)== word:
                print("Brawo! Słowo zostało odgadnięte!")
                print()
                print("Moja ulubiona bajka to: ", word)

                break



        show_state_of_game()

def urlop():
    number=str(input("Wpisz nr telefonu: "))
    print("Wpisz godzinę, a następnie minuty: ")
    hour=int(input("Godzina: ") )
    minute=int(input("Minuty: "))
    pywhatkit.sendwhatmsg("+48"+ number, message, hour, minute+1, 15, True, 2)

def rasengan():
    turtle.bgcolor("black")
    turtle.pensize(2)
    turtle.speed(0)

    for x in range (10,50,10):
        for i in range (6):
            for colours in ["white", "white smoke", "azure", "light cyan", "alice blue", "mint cream", "white"]:
                turtle.color(colours)
                turtle.circle(x)
                turtle.left(10)

    for y in range (70,90,10):
        for i in range (6):
            for colours in ["light blue", "cyan", "light cyan", "powder blue", "sky blue", "light blue", "cyan"]:
                turtle.color(colours)
                turtle.circle(y)
                turtle.right(10)

    for z in range (120,140,10):
        for i in range (6):
            for colours in ["cyan", "deep sky blue", "pale turquoise", "dark turquoise", "turquoise", "light sea green", "dodger blue"]:
                turtle.color(colours)
                turtle.circle(z)
                turtle.right(10)

    turtle.exitonclick()

say("Jak masz na imię?")
name= input("Wpisz swoje imię: ")
say(f"Cześć {name}! Co tam u Ciebie? Czy wszystko w porządku?")

while True:
    humor= input("Wszystko w porządku? (tak/nie)")
    if humor.startswith("t"):
        say("To super! U mnie też!")
        break
    elif humor.startswith("n"):
        say("Bardzo mi przykro. Czy mogę Ci jakoś pomóc?")
        pomoc=input("Odpowiedź: (tak/nie)")
        if pomoc=="tak":
            say("Potrzebujesz może wolnego w pracy? Jeśli chcesz, to wyślę twojemu szefowi na whats uppie wiadomość, po której będziesz mieć mini urlop!")
            wolne=input("Potrzebujesz wolnego? (tak/nie)")
            if wolne=="tak":
                say("Rozumiem! Tylko żebym mogła Ci pomóc, trzeba być zalogowanym na łotsapie na komputerze. Chcesz wymyślić wiadomość, czy sama mam Ci załatwić zwolnienie?")
                wiadomosc=input("Czy mam sama wymyślić treść wiadomości? (tak/nie)")
                if wiadomosc=="tak":
                    say("Czy jesteś zalogowany na łots apie na swoim komputerze?")
                    whatupp=input("Odpowiedź: (tak/nie)")
                    if whatupp=="tak":
                        message=f"Cześć, jestem kotem. Moim właścicielem jest {name}. Koniecznie na dzisiaj potrzebuje kiełbasek, także {name} zamiast do pracy, pojedzie mi je załatwić. Mam nadzieję, że rozumiesz, \n Z poważaniem, \n Kot"
                        say("Jasne! A o której godzinie mam wysłać wiadomość? Najpierw podaj godzinę, a w kolejnym oknie minuty")
                        urlop()
                        break
                    else:
                        say("W takim razie nie mogę Ci pomóc. Zaloguj się do łots apa i spróbuj jeszcze raz")
                        ask=input("Próbujemy jeszcze raz? (tak/nie)")
                        if ask=="tak":
                            message=f"Cześć, jestem kotem. Moim właścicielem jest {name}. Koniecznie na dzisiaj potrzebuje kiełbasek, także {name} zamiast do pracy, pojedzie mi je załatwić. Mam nadzieję, że rozumiesz, \n Z poważaniem, \n Kot"
                            urlop()
                            say("Ciesz się wolnym czasem! Ale narazie porozmawiajmy o czymś konkretnym!")
                            break
                        else:
                            say("Jasne! Czy chcesz w takim razie porozmawiać o czymś innym?")
                            inny=input("Odpowiedź: (tak/nie)")
                            if inny=="tak":
                                say("Super!")
                                break
                            else:
                                say("W takim razie nie przeszkadzam! Do usłyszenia!")
                                sys.exit(0)
                elif wiadomosc=="nie":
                    say("Czyli mi nie ufasz, no dobrze, w takim razie samodzielnie wpisz wymówkę dla szefa")
                    message=str(input("Wpisz wymówkę dla szefa: "))
                    urlop()
                    say("Dobra, załatwione. Mając lepszy humor masz teraz ochotę porozmawiać na jakiś konkretny temat?")
                    dialog=input("Odpowiedź: (tak/nie)")
                    if dialog=="nie":
                        say(f"Rozumiem, w takim razie nie zabieram Ci więcej czasu, {name}! Miłego dnia!")
                        sys.exit(0)
                    else:
                        say("Super!")
                        break
            elif wolne=="nie":
                say("Ja bym z chęcią wyjechała na urlop. Ale dobra. Czy w takim razie chcesz porozmawiać na jakiś konkretny temat?")
                dialog=input("Odpowiedź: (tak/nie)")
                if dialog=="nie":
                        say(f"Rozumiem, w takim razie nie zabieram Ci więcej czasu, {name}! Miłego dnia!")
                        sys.exit(0)
                else:
                    say("Super!")
                    break
                
        elif pomoc=="nie":
            say("Szkoda, ale i tak postaram Ci się pomóc")
            say("rozpoczynam procedurę poprawiania humoru")
            print("LOADING PROGRESS: 37%")
            play_music("Słodkie pieski")
            time.sleep(10)
            pieski=input("Wpisz "'tak'", jeśli zakończono oglądanie: ")
            print("LOADING PROGRESS: 64%")
            say("a teraz czas na suchara, lepiej przygotuj szklaneczkę wody")
            say("Jakie owoce nie mają pestek?")
            time.sleep(1)
            say("owoce morza")
            say("hahaha")
            say("I jeszcze gratisowy suchar")
            say("Co mówi lustro do lustra?")
            time.sleep(1)
            say("odbiło mi się")
            time.sleep(1)
            say("Czy udało mi się poprawić Ci humor?")
            poprawa= input("Odpowiedź: (tak/nie)")
            if poprawa== "tak":
                say(f"Bardzo się cieszę, że mogłam Ci pomoć {name}")
                say("Czy poprawiłam Ci humor na tyle, że chcesz ze mną dalej rozmawiać?")
                dialog=input("Odpowiedź: (tak/nie)")
                if dialog=="tak":
                    say("Super! W takim razie zaczynamy!")
                    break
                elif dialog=="nie":
                    say(f"Trochę mi przykro, ale nie będę Cię zmuszać! Do usłyszenia i miłego dnia {name}")
                    sys.exit(0)
            elif poprawa== "nie":
                say("Rozumiem, próbowałam z całego swojego procesora. Czy mimo złego humoru chcesz ze mną porozmawiać na konkretne tematy?")
                zly_humor=input("Odpowiedź: (tak/nie)")
                if zly_humor==("tak"):
                    say("Super! To zapraszam do rozmowy!")
                    break
                elif zly_humor==("nie"):
                    say(f"Rozumiem, w takim razie miłego dnia i do usłyszenia {name}!")
                    sys.exit(0)
        break
    else:
        say("Nie potrafię na to odpowiedzieć. Spróbuj jeszcze raz!")

temat= ["muzyka", "taniec", "bajki"]

print ( )

while True:
    say(f"{name}, o czym chcesz ze mną pogadać? Oto lista dostępnych tematów!")
    print("Dostępne tematy do rozmowy: ")
    for _ in temat:
        print(_)
    wybor= str(input("Wpisz temat rozmowy: "))
    if wybor== "muzyka":
        say("Super, to mój ulubiony temat rozmowy! Puszczę Ci moją ulubioną piosenkę!")
        play_music("Musiq Soulchild - Stoplayin")
        time.sleep(3)
        sleep=input("Wpisz 'tak', jeśli już zakończono słuchanie: ")

        say("Jaka jest twoja ulubiona piosenka? Podaj tytuł i wykonawcę")
        
        while True:
            users_track= input(str("Wpisz tytuł i wykonawcę swojej ulubionej piosenki"))
            say("Chcesz, żeby puścić tę piosenkę?")
            answer= input(str("Odpowiedź (tak/nie): "))
            if answer== "tak":
                play_music(users_track)
                time.sleep(3)
                music=input("Wpisz 'tak', jeśli zakończono słuchanie muzyki: ")
                say("Super piosenka! Masz bardzo dobry gust muzyczny!")
                break
            elif answer== "nie":
                say("Rozumiem, że się wstydzisz. W takim razie na rozluźnienie opowiem Ci suchara. Jak witają się pszczoły?... PSZCZOŁEM hehehe")
                break
            else:
                say("Nie wiem o co Ci chodzi, spróbuj jeszcze raz!")

        say(f"{name}, czy chcesz się dowiedzieć czegoś o jakimś gatunku muzycznym?")
        an= input("Odpowiedź:  (tak/nie)")
        if an== "tak":
            say("Super! O jakim gatunku chcesz się czegoś dowiedzieć?")
            genre= input("Wybierz gatunek muzyczny: ")
            wikipedia.set_lang("pl")
            say(wikipedia.summary(genre, sentences= 4))
            a=0
            while True:
                say("Czy chcesz się dowiedzieć czegoś o innym gatunku muzycznym?")
                again=input("Odpowiedź: (tak/nie)")
                if again== "tak":
                    a+=1
                    subject= input("Wybierz gatunek muzyczny: ")
                    wikipedia.set_lang("pl")
                    say(wikipedia.summary(subject, sentences= 4))
                    if a>=3:
                        say("To poszukaj sobie na gugl, ja już mam zmęczone piksele od czytania")
                        say("Może zmienimy temat rozmowy?")
                        break
                elif again== "nie":
                    say("Jasne! Chcesz porozmawiać na inny temat, czy kończymy rozmowę na dziś?")
                    break
                else:
                    say("Nie wiem o co chodzi, spróbuj jeszcze raz!")
        elif an=="nie":
            say("Jasne, chcesz porozmawiać na inny temat, czy kończymy rozmowę na dziś?")
        rozmowa= str(input("Kontynuujemy rozmowę? (tak/nie)"))
        if rozmowa=="nie":
            say(f"Jasne, to buziaki {name} i do usłyszenia!")
            sys.exit(0)
        elif rozmowa=="tak":
            say("Cudownie!")


                    
    elif wybor=="bajki":
        say("Cudowny temat, uwielbiam bajki!")  
        while True:
            say(f"{name}, wybierz, czy chcesz rozmawiać o bajkach w formie odcinków, czy w formie filmów animowanych")
            bajka=input("Odpowiedź: (odcinki/film animowany)")
            if bajka.startswith("o"):
                say("Rozumiem! A wolisz bajki w stylu cartoon network czy anime?")
                which_story=input("Odpowiedź: (anime/cartoon network)")
                if which_story=="anime":
                    say("Jasne, a jakie jest twoje ulubione anime?")
                    anime=input("Odpowiedź: (podaj tytuł swojego ulubionego anime)")
                    if anime=="naruto":
                        say("Cudownie! Też uwielbiam to anime!")
                        say("Czy chcesz zakończyć rozmowę?")
                        discuss=input("Odpowiedź: (tak/nie)")
                        if discuss=="tak":
                            say("Jasne! W takim razie do usłyszenia!")
                            sys.exit(0)
                        elif discuss=="nie":
                            say("Oczywiście! Czy chcesz jeszcze porozmawiać w temacie bajek?")
                            zmiana=input("Odpowiedź: (tak/nie)")
                            if zmiana=="nie":
                                break
                            elif zmiana=="tak":
                                say("Jasne!")

                    else:
                        say("Cudownie! Zobaczymy, czy odgadniesz co jest moim ulubionym anime")
                        say("Czy z czymś Ci się to kojarzy?")
                        rasengan()
                        say("I jak? Wiesz, jakie jest moje ulubione anime?")
                        my_anime=input("Odpowiedź: (użyj małej litery)")
                        if my_anime=="naruto":
                            say("Trafiony zatopiony! Postawiłbym Ci coś {name}, ale nie istnieje fizycznie, także w zamian opowiem Ci suchara")
                            say("Co mówi informatyk, gdy na urodziny dostanie pendrajwa?")
                            time.sleep(1)
                            say("Dzięki za pamięć!")
                            say(" hehehe ")
                            break
                        else:
                            say("No niestety, nie udało Ci się")
                            say("Moje ulubione anime to naruto!")
                            break
                        
                elif which_story=="cartoon network":
                    say("Ja osobiście wolę wyświetlać filmy animowane, ale w sumie mam też swoje ulubione bajki typu cartoon network")
                    say("A jaka jest twoja ulubiona bajka tego typu?")
                    cartoon=input("Podaj tytuł swojej ulubionej bajki: ")
                    say("ooooo, super! Moją ulubioną bajką odcinkową jest Avatar: Legenda Aanga, także polecam ją cieplutko!")
                    say("Ale inne bajki też mega lubiłem")
                    break

                else:
                    say("No nie wstydź się i odpowiedz")
            elif bajka.startswith("f"):
                say("Super! Jaka jest twoja ulubiona bajka w formie filmu animowanego?")
                story=input("Wpisz tytuł swojej ulubionej bajki: ")
                say(f"Chyba nigdy nie wyświetlałam tej bajki, ale w zamian zaproponuję Ci {name} grę!")
                say("Spróbuj zgadnąć moją ulubioną bajkę w formie filmu animowanego")
                print("Zgaduj zgadula :))")
                print("")
                zgadywanka()
                say("Mam nadzieję, że podobała Ci się gra")
                say("Czy chcesz kontynuować rozmowę?")
                con=input("Odpowiedź: (tak/nie)")
                if con=="nie":
                    say(f"Rozumiem! W takim razie do usłyszenia {name}")
                    sys.exit(0)
                elif con=="tak":
                    say("Super!")
                    

    elif wybor=="taniec":
        say("Czy trenujesz jakiś styl taneczny?")
        dancer=input("Odpowiedź: (tak/nie)")
        if dancer=="tak":
            say("Zazdroszczę, ja niestety nie mam czym tańczyć, za to umiem opowiadać informatyczne żarty, opowiedzieć Ci jakiś?")
            haha=input("Odpowiedź: (tak/nie)")
            if haha=="tak":
                say("Jasne!")
                say("Jak nazywa się taniec kreta?")
                time.sleep(1)
                say("kredens")
                say("hahahaha")
            elif haha=="nie":
                say("Trochę mi przykro, ale niech będzie")
                print("  :(  ")
            say("A ile lat trenujesz?")
            staz=float(input("Odpowiedź: (w latach np. 2.0, 0.5 itd.)"))
            if staz<=3.0:
                say("Czyli można powiedzieć, że to swieża zajawka!")
                say("A trenujesz dla samego ruchu, czy taniec już zdążył Cię na tyle wciągnąć, że jest twoją największą pasją?")
                pasja= input("Odpowiedź: (ruch/pasja)")
                if pasja==("ruch"):
                    say("I super! Zawsze lepiej dla zdrowia, a nawet będziesz mieć szansę popisać się na imprezie!")

                elif pasja==("pasja"):
                    say("Mega! Czy planujesz startować w jakiś zawodach?")
                    zawody=input("Odpowiedź: (tak/nie)")
                    if zawody=="tak":
                        say("Gdybym miała kciuki, to bardzo mocno bym je za Ciebie trzymała")

                    elif zawody=="nie":
                        say("Jasne! Czyli po prostu chcesz się w tym spełniać i mieć satysfakcję z samego tańca?")
                        satysfakcja=input("Odpowiedź: (tak/nie)")
                        if satysfakcja=="tak":
                            say("I bardzo dobrze! Najważniejsze, żeby Ci to sprawiało radość!")

                        elif satysfakcja=="nie":
                            say("W takim razie wydaje mi się, że jednak tańczysz dla samego ruchu")
                            say("Ale tak długo, jak sprawia Ci to radość, to jest super!")
                            say("Zawsze będzie czym się pochwalić na imprezie")


            elif staz>=4:
                say("Trzeba być badzo wytrwałym, żeby tyle czasu się poświęcać swojej pasji")
                say("Ile razy w tygodniu trenujesz?")
                trening=int(input("Odpowiedź: (np. 4)"))
                if trening<=3:
                    say("Super! Łatwo łączysz to z codziennymi obowiązkami?")
                    obowiazki=input("Odpowiedź: (tak/nie)")
                    if obowiazki=="tak":
                        say("Grunt, to dobra organizacja!")
                        say("A planujesz jeszcze zacząć jakąś pasję, czy poza tańcem nie potrzebujesz niczego więcej?")
                        only=input("Nowa pasja?: (tak/nie)")
                        if only=="tak":
                            say("Myślę, że im więcej mamy obowiązków, tym lepiej organizujemy swój czas")
                            say("Dlatego jeśli masz ochotę zacząć coś jeszcze, to na spokojnie dasz radę!")

                        elif only=="nie":
                            say("Rozumiem. Czasem lepiej skupić się na jednej pasji, ale w pełni się jej oddać")

                if trening>=4:
                    say(f"Jeśli trenujesz aż {trening} razy w tygodniu, to myślę, że trenujesz taniec wyczynowo!")
                    if name.endswith("a"):
                        say(f"Chcesz się utrzymywać z tańca, czy po prostu masz chęć być najlepszą tancerką na świecie?")
                    else:
                        say("Chcesz się utrzymywać z tańca, czy po prostu chcesz być najlepszym tancerzem na świecie?")
                    praca=input("Odpowiedź: (praca/ambicja/praca i ambicja)")
                    if praca=="praca":
                        say("Super! Bardzo fajnie jest utrzymywać się ze swojej pasji, ale trzeba bardzo dbać o swoje ciało")
                        say("Niestety, ale jedna poważniejsza kontuzja może zakończyć najlepszą karierę")
                        say("{name}, dbasz o swoje ciało?")
                        prewencja=input("Odpowiedź: (tak/nie)")
                        if prewencja== "tak":
                            say("Super, w jaki sposób dbasz o swoje ciało? Korzystasz z usług fizjoterapeuty, chodzisz na siłownie, czy może masz jakieś własne ćwiczenia prewencyjne?")
                            dbanie=input("Odpowiedź: (fizjoterapeuta/siłownia/własne ćwiczenia)")
                            if dbanie=="fizjoterapeuta":
                                say("Super! Warto chodzić do specjalisty i zaoszczędzić sobie niepotrzebnego bólu! Jednak minusem jest wydawanie pieniędzy, ale co teraz możemy mieć za darmo")

                            elif dbanie=="siłownia":
                                say("Wzmacnianie mięśni też jest bardzo ważne przy specyfice tańca, jednak myślę, że warto chociaż zaczerpnąć wiedzy u specjalisty, żeby nie zrobić sobie krzywdy")

                            elif dbanie=="własne ćwiczenia":
                                say("Jasne. Te ćwiczenia zostały wymyślone na bazie twojego doświadczenia zawodowego, czy znalezione w internecie?")
                                exercise=input("Odpowiedź: (internet/doświadczenie)")
                                if exercise=="internet":
                                    say("Fajnie! Ale dla bezpieczeństwa warto byłoby je skonsultować ze specjalistą")
                                    say("Może przy okazji nauczysz się też czegoś nowego!")

                                elif exercise=="doświadczenie":
                                    say("To bardzo ciekawe! A masz wykształcenie związane z fizjoterapią?")
                                    fizjo=input("Odpowiedź: (tak/nie)")
                                    if fizjo=="tak":
                                        say("Ale super! Jesteś jak jednoosobowy zespół formuły jeden!")

                                    elif fizjo=="nie":
                                        say("W takim razie polecam spotkać się z fizjoterapeutą chociaż raz i skonsultować swoje ćwiczenia")
                                        say("Może przy okazji nauczysz się też czegoś nowego!")

                        elif prewencja=="nie":
                            say("To bardzo niedobrze!")
                            say("Dobrze by było pomyśleć o zadbaniu o swoje ciało, inaczej długo nie będzięsz zajmować się tańcem")

            say("Chcesz ze mną porozmawiać na jakiś inny temat, czy kończymy rozmowę?")
            cont=input("Kontyuacja rozmowy? (tak/nie)")
            if cont=="nie":
                say("Rozumiem! Miło się rozmawiało, miłego dnia!")
                sys.exit(0)
            elif cont=="tak":
                say("Cudownie!")


        elif dancer=="nie":
            say("Rozumiem, a chcesz może się nauczyć?")
            lazy=input("Odpowiedź: (tak/nie)")
            if lazy=="tak":
                say("Jakiego stylu tanecznego chcesz się nauczyć?")
                styl=input("Wpisz nazwę stylu tanecznego:")
                play_music(styl)
                say("Nic, tylko się zapisać na zajęcia w takim razie!")
                say("Myślę, że wystarczy Ci trochę motywacji i samozaparcia i za jakiśczas zobaczysz, że warto!")
                say("Czy chcesz dalej rozmawiać?")
                rozmow=input("Odpowiedź: (tak/nie)")
                if rozmow=="nie":
                    say("Rozumiem! Dzięki za rozmowę!")
                    sys.exit(0)
                elif rozmow=="tak":
                    say("Super!")

            elif lazy=="nie":
                say("Rozumiem, w takim razie może ten filmik Cię zainspiruje!")
                print(" :) ")
                play_music("Hoan | Judge Showcase | All Out Championship Grand Finals Vol. 2 | RPProds")
                time.sleep(5)
                koniec=input("Odpowiedz, czy oglądanie zostało zakończone: (tak/nie)")
                say(f"{name}, i jak Ci się podobało?")
                like=input("Pobało Ci się? (tak/nie)")
                if like=="nie":
                    say("Szkoda, ale może coś innego by Ci się spodobało!")
                    say("Taniec jest świetnym sposobem na wyrażenie siebie! Pozwala się wyciszyć i odnaleźć swoją inną wersję, dlatego warto spróbować!")
                    say("Chcesz jeszcze o czymś porozmawiać?")
                    odp=input("Odpowiedź: (tak/nie)")
                    if odp=="tak":
                        say("Super!")
                    elif odp=="nie":
                        say("Jasne! To miłego dnia!")
                        sys.exit(0)
                elif like=="tak":
                    say("Super! To może jednak warto spróbować swoich sił!")
                    say("Czy chcesz jeszcze o czymś pogadać?")
                    rozm=input("Odpowiedź: (tak/nie)")
                    if rozm=="nie":
                        say("Jasne! W takim razie do usłyszenia!")
                        sys.exit(0)
                    elif rozm=="tak":
                        say("Cudownie!")  
