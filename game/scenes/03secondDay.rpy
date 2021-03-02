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

default t_visited = False
default m_visited = False
default n_visited = False
default p_visited = False

label secondDay:
  "Quien iba a pensar que entraría a un club así"
  "Incluse hasta tiré waifus"
  "Y..."
  "¿Lo disfruté?"
  "No digas idioteces, estas son puras cosas que hacen los otakus que no se bañan..."
  "Llego al club, y veo que ya están los otros miembros"
  p "Oh, ¡hola [povname]!"
  tu "Hola..."
  p "¿Cómo te fue ayer?"
  tu "Decente creo"
  tu "Me salió una buena, pero no estoy seguro"
  p "¿Oh ya veo, quién te salió?"
  tu "Mmmmmm. Me salió [waifu_name]"
  p "Wow, eso sí que es suerte. Sería bueno que se la regalaras a alguien, sé que les va a encantar"
  p "Claro... No te olvides de mí..."
  tu "Claro..."
  tu "Primero los saludaré y luego decido a quién se la voy a regalar"
  p "¿Cómo usted diga?"
  jump selection

label selection:

  if t_visited and m_visited and n_visited and p_visited:
    jump afterSharing

  $ menu = adv_menu

  menu:
    "¿A quién debería saludar?"

    "Tomás":
      if t_visited:
        "Ya lo saludé..."
        jump selection
      else:
        $ t_visited = True
        jump act1Tomas
    "Mau":
      if m_visited:
        "Ya lo saludé..."
      else:
        $ m_visited = True
        jump act1Mau
    "Naki":
      if n_visited:
        "Ya lo saludé"
      else:
        $ n_visited = True
        jump act1Naki
    "Pabel":
      if p_visited:
        "Ya lo saludé"
      else:
        $ p_visited = True
        jump act1Pabel


label act1Tomas:
  tu "Hola Tomás"
  t "Hola [povname], ¿qué pasó?"
  t "Ni vengas a pedirme kakera o waifus porque no te voy a dar nada"
  "¿De qué habla?"
  tu "Nono, no vine a eso. Solo vine a saludarte. A conocerte..."
  t "Oh, ya veo"
  t "Está bien"
  t "Oye pero deberías saber una cosa"
  t "Dentro de este club, soy el contador"
  t "Y si estás tan interesado en conocerme, deberías saber lo importante que soy yo para poder mantener una economía estable
  en el servidor"
  t "Parte de mi trabajo es cobrar los impuestos"
  t "Y como tú ya eres un miembro oficial del club, es necesario que también contribuyas a los impuestos"
  "¡¿Tengo que pagarles ahora?!"
  t "Así que para poder seguir estando en el club necesito que me deposites 100 kakera"
  "¿Kakera?"
  "¿A qué se refiere?"
  tu "¿Qué es Kakera?"
  t "Oh, ya veo. No sabes"
  t "Es el dinero que se usa dentro del club"
  t "Puedes usar el comando {i}$dk{/i} si quieres conseguir un poco. Debería de bastar para depositarme"
  tu "Ya veo..."
  t "¿Qué esperas? Hazlo"
  t "..."
  "Ok, cada minuto que estoy aquí, se pone más y más raro"
  "Igual, no me queda de otra"


  $ command = ''
  while command != "$dk" and command != "$dailykakera":
      if command != '':
          "No... así no era"
      $ command = renpy.input("Usa $dk")

  "{b}{i} Se ha añadido 217 kakera a tu cuenta {/b}{/i}"

  t "Listo, ¿ya ves? Era así se sencillo"
  t "Ahora dame 100 de los 217 que ganaste"
  tu "Espera espera"
  tu "Sigo sin entender por qué te tengo que dar dinero, yo solo vine a saludarte"
  t "Oh"
  t "¿Y eso qué?"
  t "Te acabo de decir. Es parte de la economía de este club"
  t "Si lo dejamos de hacer, se rompe. Te necesitamos"
  tu "..."
  tu "Está bien, creo"
  tu "¿Cómo te doy el dinero?"
  t "$gk @tomas 100"
  tu "Ok, pues..."

  $ attempts = 0
  $ command = ''
  while command != "$gk @tomas 100":
      if command != '':
        if "pabel" or "pavo" in command:
          t "¿Por qué le tratas de dar a Pabel, no ves que él ya tiene suficiente con su espantosa suerte?" 
          tu "P...Perdon"
        else:
          $ attemtps += 1
          if attempts >= 3:
            "{b}¿Eres idiota?{/b}"
          else:
            "No... así no era"
      $ command = renpy.input("$gk @tomas 100")

  t "Genial, así podré comprarme Silver IV"
  tu "¿Silver qué?"
  t "Oh, nada de qué preocuparse, probablemente Pabel luego te explique eso"
  t "Bueno, ya te puedes ir..."
  t "Ya platicamos mucho por hoy"
  tu "Eh, ¡pero si no platicamos nada!"
  t "{b}ADIOS{/b}" # AUTOMATICO
  
  jump selection
    
label act1Naki:

  tu "Hola, Naki"
  n "Mmmmm. Hola. ¿Qué pasó?"
  tu "Oh, nada. Solo quería saludarte"
  n "Ah ya veo"
  tu "Qué estás haciendo"
  n "Shhhhh...."
  n "Speedrun check"
  tu "Speedrun, ¿qué?"
  n "Shh...."
  n "Este puede ser nuevo World Record"
  tu "O sea..."
  n "Ajá"
  tu "¿¡A qué te refieres!?"
  n "Ah, es que ando jugando Mario 64 y le estoy haciendo speedrun"
  tu "Oh... Ya veo"
  tu "¿Cuánto tiempo llevas practicando?"
  n "Shh..."
  n "..."
  n "....."
  n "......."
  n "NOOOO YA VALIO"
  n "Me voy..."
  n "Me voy, me voy, me voy"
  tu "Nonono, espera"

  jump selection

label act1Mau:
  tu "Hola, Mau"
  m "Hola"
  tu "¿Qué haces?"
  m "Trabajando en PogU"
  tu "¿P...Pog U?"
  tu "¿El meme?"
  m "No, el bot"
  tu "¿Bot?"
  m "Nunca has usado discord, ¿verdad?"
  tu "N...No. Siempre que quería hablar con mis amigos, usaba el chat de voz integrado en LoL"
  m "Ya veo... Qué se te puede hacer..."
  m "Pues un bot es literal una cuenta de Discord que tienen un objetivo específico"
  m "Lo que permite que saquemos Waifus es un bot"
  m "Hay muchísimos bots y yo estoy trabajando en uno que te deja recolectar cartas de nosotros"
  tu "¿Cartas de ustedes?"
  m "Sí, imágenes súper cringe de nosotros que da risa. Está divertido. Deberías probarlo"
  tu "¿Cómo hago eso?"
  m "Fácil. Cada 3 minutos sale una carta con una imagen de nosotros, cuando salga, tienes que usar
  _get para atrapar la carta que esté activa. Pero tienes que ser rápido, porque solo uno se la puede quedar"
  tu "Ya veo..."
  m "Voy a encender a PogU para que lo pruebes, pero apenas estoy iniciando con él. Así que todavía no muestra las
  imágenes, pero pronto lo hará"
  tu "Ok..."
  "Un {b}Naki Guitar{/b} ha aparecido. Atrápalo con {b}_get{/b}"

  $ attempts = 0
  $ command = ''
  while command != "_get":
    if command != '':
      $ attemtps += 1
      if attempts >= 3:
        "{b}¿Eres idiota?{/b}"
      else:
        "No... así no era"
    $ command = renpy.input("_get")

  "TypeError: unsupported operand type(s) for /: 'str' and 'str'"
  m "Oh"
  m "Parece que no funcionó..."
  m "Estas cosas siempre pasan, jeje"
  tu "Ya veo..."
  tu "¿Cuánto piensas terminarlo?"
  m "Todavía no sé"
  m "Tengo que agregarle muchísimas cosas"
  m "Y arreglar los errores..."
  m "Dios, tengo que hacer un buen de cosas"
  m "Bueno ya te puedes ir"
  "Ahora me está corriendo..."
  tu "Bueno pues... Regresaré con los otros..."
  tu "Adios"

  jump selection 


label act1Pabel:

  tu "Hola, Pabel"
  p "Holaa, [povname]"
  p "¿Qué onda? ¿Qué te trae por aquí?"
  tu "Oh nada, solo quería saludarte"
  p "Oh ya veo"
  p "¿Qué tal? ¿Qué te ha parecido el club?"
  tu "Pues... Está interesante. Creo..."
  p "No te veo muy convencido"
  tu "Hmmmm, perdón..."
  p "Está bien que te sientas nervioso, es tu segundo día"
  tu "No... sí. Pero es que todavía no le entiendo esto de las waifus"
  p "Oh, ya veo. Pues hay bastantes cosas interesantes que las hacen divertidas"
  p "Por ejemplo, puedes usar Kakera para comprar badges. Estas potencializan tus oportunidades de conseguir
  mejores Waifus"
  p "Por eso Tomás está tan insistente con conseguir kakera"
  p "De hecho le cobra a todo el mundo..."
  p "Pero bueno, ¿qué se puede hacer?"
  p "Si ahorras suficiente Kakera puedes comprar una Silver Badge, que aumenta las posibilidaes de conseguir
  una waifu de una wishlist"
  p "Pero cuesta bastante..."
  p "Hmmm..."
  p "Ahorita que lo pienso"
  p "Mejor no hagas nada"
  p "Es de jotos los que usan Badges"
  "¡¿Entonces para qué me dio esa explicación?!"
  p "Jeje"
  p "Me pude haber ahorrado la explicación, ¿verdad?"
  p "Perdón"
  tu "Jeje, no pasa nada"
  "Son un club de raritos..."
  p "Te voy a dar un tip, [povname]"
  p "Puedes checar la wishlist de los demás en el botón de abajo" 
  p "Si quieres hacerte muy amigo de alguien, consigue una Waifu de su wishlist"
  p "No queremos que te vayas del club sin tener algún amigo, ¿verdad?"
  tu "No... Claro que no"
  tu "Bueno, regreso con los demás..."
  p "Adioss"
  jump selection




label afterSharing:

  "Ya saludé a todos."
  "Sí son una bola de raritos..."
  "Pero bueno, no se me puede olvidar mi objetivo..."
  "Creo que ahora los conozco un poquito más"
  "{i}*ring*{/i}"
  "Oh, si"
  "La Waifu que saqué..."
  "¿A quién debería regalar mi waifu?"
  
  menu:
    "Tomás":
      jump waifuTomas
    "Mau":
      jump waifuMau
    "Naki":
      jump waifuNaki
    "Pabel":
      jump waifuPabel

label waifuTomas:
  tu "Hola de nuevo, Tomás"
  t "Hola otra vez, ser inferior"
  "¿Eh?"
  "Sabía que meterme a este club fue un error..."
  tu "¿S...Ser inferior?"
  t  "¿Qué pasó?"
  "..."
  tu "Este mmm..."
  tu "Te quería..."
  tu "{size=10}Regalar una waifu{/size}"
  t "¿Una qué?"
  "Dios... No me hagas decirlo otra vez..."
  tu "U...Una"
  tu "{b} UNA WAIFU {/b}"
  t "Ah, eso..."
  t "Pues como vas. No pienso darte ni una kakera por ella"
  t "¿Quién es por cierto?"
  "Es demasiado abaricioso..."
  tu "Es [waifu_name]"

  if waifu[1] != 3:
    $ friendTomas += 1
    t "Oh... Ya veo"
    t "Si me ibas a traer pura trash, me hubieras avisado desde antes"
    t "Igual dámela. Son kakeras gratis"
    t "Dámela pues"
    "Le estoy haciendo un regalo, ¡¿Y TODAVÍA SE QUEJA?!"
    "Dios..."
    tu "Mmmmm, ¿cómo te la doy?"
    t "$give @tomas [waifu_name]"
    tu "Ya veo..."

    $ attempts = 0
    $ command = ''
    while command != "$give @tomas {}".format(waifu_name):
        if command != '':
          $ attempts += 1
          if "pabel" or "pavo" in command:
            if attempts >= 3:
              t "Te odio..."
            else:
              t "¿Por qué le tratas de dar a Pabel, no ves que él ya tiene suficiente con su espantosa suerte?" 
              tu "P...Perdon"
          else:
            if attempts >= 3:
              "{b}¿Eres idiota?{/b}"
            else:
              "No... así no era"
        $ command = renpy.input("$give @tomas [waifu_name]")  

    t "Gracias..."
    t "{i}$divorce [waifu_name]{/i}"
    t "{i}{b} Se ha añadido 543 kakera a la cuenta de @tomas {/b}{/i}"
    t "Genial, no la necesito a ella"
    tu "¿L...La acabas de vender?"
    t "Si... ¿para qué más la quería?"
    "No puedo creerlo... Mejor regreso con los otros"    

  else:
    $ friendTomas += 2
    t "NO ME LA CREO BROOOO"
    t "Superrrr, ¿neta me la vas a regalar?"
    t "La estuve buscando por demasiado tiempo, hasta la tengo en mi Wishlist"
    t "La neta, qué buena onda eres bro"
    "Ohhh, ¡Parece que le gustó!"
    "¡Genial!"
    t "¿Seguro que me la quieres regalar?"
    tu "Sisi, ¿cómo lo hago?"
    t "$give @tomas [waifu_name]"
    tu "Ya veo, dame un momento"

    $ attempts = 0
    $ command = ''
    while command != "$give @tomas {}".format(waifu_name):
        if command != '':
          $ attempts += 1
          if "pabel" or "pavo" in command:
            if attempts >= 3:
              t "Te odio..."
            else:
              t "¿Por qué le tratas de dar a Pabel, no ves que él ya tiene suficiente con su espantosa suerte?" 
              tu "P...Perdon"
          else:
            if attempts >= 3:
              "{b}¿Eres idiota?{/b}"
            else:
              "No... así no era"
        $ command = renpy.input("$give @tomas [waifu_name]") 

    tu "Creo que ya está, ¡Gracias!"


  tu "Bueno... Ya me voy"
  t "Espera... Yo también tengo algo que darte"
  t "Me salió ayer y creo que te podría gustar..."
  "Oh... Eso sí me interesa"
  tu "¿Quién te salió?"
  t "Sadao Maou"
  "Sepa quién sea"
  tu "Oh, ¿okey?"
  t "Ten..."
  t "{i}$give @[povname] Sadao Maou{/i}"
  tu "Oh, gracias. Creo..."
  tu "Regresaré con los demás"
  jump ccChoser


label waifuNaki:
  tu "Hola otra vez, Naki"
  n "Oh, hola"
  n  "¿Qué pasó?"
  "..."
  tu "Este mmm..."
  tu "Te quería..."
  tu "{size=10}Regalar una waifu{/size}"
  n "¿Una qué?"
  "Dios... No me hagas decirlo otra vez..."
  tu "U...Una"
  tu "{b} UNA WAIFU {/b}"
  n "Ah, eso..."
  n "¿Yo para qué quiero eso?"
  tu "Emmm, pues creí que te iba a gustar"
  n "I don't care"
  "Naki no parece gustarle mucho esto..."
  tu "Es [waifu_name]"
  
  if waifu[1] != 2:
    n "Oh, nice"
    tu "Emmm, es de tu Wishlist"
    tu "¿La quieres?"
    n "Emmm, me da igual. Pero... si quieres"
    tu ""
  else:




label ccChoser:
