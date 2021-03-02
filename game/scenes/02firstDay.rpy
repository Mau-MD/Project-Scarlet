# Main
define n = Character("Naki")
define p = Character("Pabel")
define t = Character("Tomas")
define m = Character("Mau")

# Secondary
define d = Character("Director")
define pa = Character("El Grande Padre")
define b = Character("El Buki")

define u = Character("???")

# Tu
define tu = Character("[povname]")


label firstDay:

    "Aquí estoy, en una nueva escuela"
    "No me queda de otra"
    "Tengo que conseguir amigos"
    "Siempre es una molestia ser alguien nuevo"
    "Todos se acercan a ti y te hacen preguntas incómodas"
    "¡Ya me quiero ir de aquí!"
    "Ahí viene otro..."
    u "Hola"
    tu "Hola..."
    u "Veo que eres nuevo por aquí"
    tu "Sí..."
    b "Soy Buki, es un gusto conocerte. Cuéntame, ¿qué te gusta hacer?"
    "Oh"
    "Nunca me habían preguntando sobre mis gustos..."
    tu "Pues..."
    tu "Juego League of Legends"
    b "Oh, ¡genial! Yo también lo juego"
    "Mis ojos se iluminan, nunca había conocido a alguien cercano que lo jugara"
    tu "Oh, ¿enserio?"
    "Lo digo intentando ocultar mi admiración"
    b "¡Sí! Por qué no vienes con nosotros, te van a caer bien"
    tu "¿L...Los otros?"
    b "Síi, son otros cuatro amigos. Tienen gustos parecidos a los míos, te van a caer bien"
    tu "Ya veo..."
    "No quiero"
    "No quiero"
    "No quiero"
    "Pero..."
    "Tengo qué"
    "Tengo que conseguir amigos, ese es mi único objetivo"
    "Además, no pierdo nada, si tienen gustos parecidos no debería haber problema"
    "Creo..."
    b "Entonces, ¿vas a venir?"
    tu "Mmmm... Sí, ¿por qué no?"

    "Llegamos a un salón"
    "Oigo gritos"
    "Persona 1" "Nooooo, no puedo creer que me hayas snipeado Kirito"
    "Persona 2" "Ni modo bro, así es esto"
    "Persona 3" "Ya cállense"
    "Persona 4" "Te lo compro a 1000 de kakera"
    "¿Qué está pasando aquí?"
    b "Ah, no les hagas caso, andan jugando algo..."
    b "Chicos, vengan, traje a alguien nuevo"
    "Persona 1" "Chicos, dejen de hacer roll, vamos a saludar a esa persona"
    "Persona 2" "Hmmmm"

    p "Hola, ¡soy Pabel!"
    "..."
    p "¡Preséntense chicos! No se queden ahí"
    t "Ahh, yo soy Tomás"
    m "Yo soy Mau"
    "Istvan" "Me llamo Istvan"
    m "Dile Naki"
    n "..."

    tu "Hola chicos"
    p "¿Para qué lo trajiste Buki?"
    p "¡Oh! ¡Espera! ¡¿Es acaso un miembro nuevo del club?!"
    tu "¿¿Ehhh??"
    tu "Espera, espera, espera, ¿club?"
    p "Síiii, este es el club de ???"
    p "Bueno..."
    p "Todavía no es un club oficial porque solo somos 4 miembros, necesitamos ser almenos 5"
    p "Pero... si te unes..."
    p "¡Podríamos serlo!"
    "Oh dios, según yo solo vine a conocerlos y ahora esto..."
    tu "E...Este no vine para eso"
    p "Oh..."
    p "Ya veo..."
    p "Podrías considerarlo"
    p "P-por favor"
    tu "¿Por qué no se une el Buki?"
    b "Estoy comprometido en otro club"
    "Ahhhh"
    "A ver"
    "Esta es mi oportunidad"
    "Tengo que hacer amigos"
    "Tal vez podría unirme al club..."
    "Quizá"
    p "¿Ya lo pensaste?"
    "¿Eh?"
    "Creí que me iba a dejar pensar durante un tiempo"
    "¡¿Pero quiere una respuesta ahora?!"
    "Diosss"
    p "¿Entonces?"

    menu:
        "¿Te vas a unir al club?"
        "Sí":
            p "Siuuuuuuu, sabía que ibas a decir que sí"
            "No es como que tuviera otra opción..."
            tu "Sí... estoy muy emocionado"
            p "Bueno pues, primeramente tienes que crearte una cuenta de Discord"
            p "Es lo único que usamos aquí"
            tu "Ya veo..."
            $ povname = renpy.input("Ingresa tu nombre de usuario")
            p "Genial, ahora en adelante te llamaremos [povname]"
            "Bueno, almenos así no tendré la necesidad de compartir mi nombre real..."
            p "Pues te vamos a explicar que hacemos en este club"
            p "Sacamos waifus"
            tu "¿Eh?"
            tu "Sacan... ¿qué?"
            t "Waifus"
            "Creo que me acabo de meter al club equivocado"
            p "Cada cierta hora podemos hacer roll de 8 waifus"
            p "Existen más de 50,000 waifus diferentes que puedes conseguir, pero no todas son buenas"
            p "Aproximadamente hay unas 200 buenas"
            p "Entonces hay una probabilidad de..."
            p "De..."
            n "1/250"
            p "Sí, eso. Es muy poco probable que te toque una buena"
            p "Entonces, ajá. Eso es lo divertido de este juego, el estar cada hora tirando y viendo
            si te sale una buena"
            p "Cada miembro del club tiene también su propia wishlist"
            p "Si consigues una que le interese a alguno, probablemente se haga muy
            amigo tuyo"
            # Mencionar que puedes ver la wishlist...
            p "Pero bueno, al final esa es decisión tuya, ¿no?"
            p "Por último, para sacar Waifus puedes usar 3 comandos diferentes"
            p "$w, $wa o $waifu"
            p "El que más se te acomode a ti"
            n "También puedes sacar Husbandos"
            m "Cállate Naki"
            t "Eso es de jotos"
            p "Jeje, no les hagas caso. Intenta sacar una waifu."

            $ command = ''
            while command != "$w" and command != "$wa" and command != "$waifu":
                if command != '':
                    "No... así no era"
                $ command = renpy.input("Usa $w, $wa o $waifu")

            p "¡Perfecto!"
            p "Traquilo, fue una prueba, no te consumió ningún roll"
            p "¿Y bueno qué te pareció?"
            "..."
            "¿En serio hay algo positivo en todo esto?"
            "Las personas de mi nuevo club son todos unos otakus"
            "No puedo creerlo..."
            "Igual"
            "Tengo una misión"
            "Entiendo el sacrificio que tengo que hacer"
            "Creo"
            tu "Me parece... bien. Creo"
            p "Perfecto"
            p "Qué tal si sacas tus waifus y nos platicas qué te tocó mañana"
            t "Me parece bien, ya sabes. Avísame si sale una de One Piece o Naruto"
            m "A mí si sale alguna de Steins Gate o de Your Lie in April"
            n "Who cares"
            p "No te olvides de mí... Avísame si sale alguna de Attack on Titan"
            $ persistent.wishlist_activated = True
            p "Igual, si quieres saber qué waifus queremos, siempre puedes checar en el botón de wishlist de abajo"
            "Demasiada información para mi cabeza"
            "Igual, no pierdo nada con intentarle..."
            "Creo"
            
            jump game1

        "No":
            jump final1
