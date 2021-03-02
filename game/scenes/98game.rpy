# Main
define n = Character("Naki")
define p = Character("Pabel")
define t = Character("Tomas")
define m = Character("Mau")

# Secondary
define d = Character("Director")
define pa = Character("El Grande Padre")
define b = Character("El Buki")

# Tu
define nn = nvl_narrator


label game1:

    $ menu = nvl_menu

    python:
        waifus = [("Mai Sakurajima", 1), ("Mikasa Ackerman", 1), ("Hange Zöe", 1), ("Kaguya Shinomiya", 1),
                  ("Shrek", 2), ("Thanos", 2), ("Akinator", 2), ("Zelda", 2),
                  ("Hana Uzaki", 3), ("Nami", 3), ("The Love Pillar", 3), ("Hinata", 3),
                  ("Megumin", 4), ("Makise Kurisu", 4), ("Kaori Miyazono", 4), ("Aqua", 4)]

    nn "Parece que tengo que clamear waifus"
    nn "¿Cómo le hacía?"

    $ rolls_left = 8
    while rolls_left > 0:

        nvl clear
        $ command = ''
        while command != "$w" and command != "$wa" and command != "$waifu":
            if command != '':
                nn "Así no era... puedo checar el historial."
                nvl clear
            $ command = renpy.input("Saca una waifu")

        # $ renpy.random.seed(rolls_left)
        $ number = renpy.random.randint(0,1)
        if number == 0:
            nn "Me salio pura trash..."
        else:
            $ waifu = renpy.random.choice(waifus)
            $ waifu_name = waifu[0]

            nn "Oh, me salio [waifu_name]"
            nn "¿La clameo?"

            menu:
                "Sí":
                    nn "Va."
                    $ rolls_left = 0
                "No":
                    nn "A lo mejor sale una mejor..."

        $ rolls_left -= 1

    nn "Ya no puedo clamer más por hoy. Verémos qué me sale mañana"

    $ menu = adv_menu
    jump secondDay
