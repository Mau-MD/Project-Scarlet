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

default level1NakiVisited = False
default level1PabelVisited = False
default level1MauVisited = False
default level1TomasVisited = False

default level2NakiVisited = False
default level2PabelVisited = False
default level2MauVisited = False
default level2TomasVisited = False

default level3NakiVisited = False
default level3PabelVisited = False
default level3MauVisited = False
default level3TomasVisited = False

label ccChoser:
  # Level 3 CC
  if friendMau == 6 and not level3MauVisited:
    level3MauVisited = True
    pass
  elif friendTomas == 6 and not level3TomasVisited:
    level3TomasVisited = True
    pass
  elif friendPabel == 6 and not level3PabelVisited:
    level3PabelVisited = True
    pass
  elif friendNaki == 6 and not level3NakiVisited:
    level3NakiVisited = True
    pass
  # Level 2 CC
  elif friendMau == 4 and not level2MauVisited:
    level2MauVisited = True
    pass
  elif friendTomas == 4 and not level2TomasVisited:
    level2TomasVisited = True
    pass
  elif friendPabel == 4 and not level2PabelVisited:
    level2PabelVisited = True
    pass
  elif friendNaki == 4 and not level2NakiVisited:
    level2NakiVisited = True
    pass
  # Level 1 CC
  elif friendMau == 2 and not level1MauVisited:
    level1MauVisited = True
    pass
  elif friendTomas == 2 and not level1TomasVisited:
    level1TomasVisited = True
    jump level1Tomas
  elif friendPabel == 2 and not level1PabelVisited:
    level1PabelVisited = True
    jump level1Pabel
  elif friendNaki == 2 and not level1NakiVisited:
    level1NakiVisited = True
    jump level1Naki
  # No CC
  else:
    pass # End of day

label level1Tomas:
  t "Emm... Hola [povname]"
  tu "Oh, hola otra vez, Tomás"
  tu "¿Qué pasó?"
  t "Pues... Te quería agradecer por la Waifu que me acabas de dar"
  t "F...Fue un lindo detalle"
  t "El creador de One Piece estará orgulloso de ti"
  tu "¿Eh?"
  t "Bueno pues..."
  t "Lo que te quería decir es si quería jugar unas partidad de Rocket League conmigo"
  t "Me gusta mucho ese juego, pero creo que sería mejor si lo juego con alguien..."
  "¿Rocket League?"
  "¿Quiere que juege Rocket League con él?"
  "P...Pero qué pasa si la riego"
  "Yo no soy bueno del todo..."
  "¡¿Qué tal si la riego?!"
  "Todo por lo que he luchado se iría a la basura"
  "No puedo permitir que esto pase..."
  tu "Este... Pues sí podría jugar un rato"
  t "Oh, ¡genial!"
  t "Ven"
  tu "Ahhhhh"

  # Transition
  tu "¿Dónde estamos?"
  t "Este es el cuarto de juegos del club"
  t "Tenemos de todo"
  t "Hollow Knight, Rocket League, Destiny y muchas cosas más"
  tu "Ya veo..."
  tu "No sabía que podían tener eso en un club"
  t "Ya ves"
  tu "Eso está permitido"
  t "Hmn...."
  t "No estoy seguro, pero no importa"
  t "El punto es que vamos a jugar juntos"
  t "Primeramente"

  menu:
    "Xbox":
      "God"
    "Playstation":
      "Pussy"
  
  t "Bueno, igual. Pon tu cuenta de Xbox para que podamos jugar"
  $ xbox_name = renpy.input("Ingresa el nombre de tu cuenta de Xbox")
  $ xbox_pass = renpy.input("Ingresa tu contraseña de tu cuenta de Xbox")
  "Ingresa tu código de verificación de dos pasos que acaba de llegar a tu celu..." # Stop 3 Sec
  tu "{b}¿Ne estás intentando robar la cuenta?{/b}"
  t "Nono"
  t "Era broma"
  t "De compas"
  "Estaba en lo correcto"
  "Sabía que no tenía que confiar en nadie"
  "Son todos..."
  t "¿Vas a jugar o qué? Señor [povname]"
  t "O mejor dicho"
  t "[xbox_name]"
  t "Que nombre tan cagado"
  tu "Oye"
  t "Jajaja, es broma"
  tu "..."
  t "Me deberás de tratar bien de ahora en adelante si quieres que no diga tu contraseña"
  tu ".........."
  t "No es cierto. Bueno pues"
  t "."
  t ".."
  t "..."
  t "¿ERES GRAN MAESTRO EN ROCKET LEAGUE?"
  "Sabía que era mala idea"
  t "TENEMOS QUE JUGAR YA"
  t "YAYAYA"
  tu "¿Ok...?"

  "Y así fue pasando el día"
  "Seguimos jugando"
  "Tomás siempre quedaba en último"
  "No es tan bueno como yo pensé..."
  "Igual"
  "Creo que me estoy divirtiendo"
  "Creo que lo estoy disfrutando"
  "Quizá estar con personas no es tan malo"
  "Quizá..."

  t "Oye"
  t "Sí eres muy bueno"
  t "Pero ya va a cerrar la escuela"
  t "Creo que sería bueno que ya nos fuéramos"
  t "¿Tú que opinas?"

  tu "Pues... sí"
  tu "No podemos quedarnos más tiempo..."
  "Dumbass"
  tu "Vámonos pues"
  t "Va"
  t "Entonces nos vemos mañana"
  t "No se te olvide sacar Waifus"
  t "Vamos a ver si sale alguna de mi Wishlist otra vez"
  t "Digo"
  t "No te estoy obligando ni nada..."
  t "Bueno, ya me voy"
  t "Adios..."
  tu "Adios"

  "Cierto, tengo que sacar Waifus. Bueno, vamos para allá"

  jump game1
  
label level1Naki:
  n "Hola [povname]"
  tu "Hola otra vez, Naki"
  n "Emmm, pues te quería dar las gracias por la Waifu..."
  n "Pero no me importa del todo, ¿eh?"
  tu "Jeje, claro claro"
  tu "¿Qué pasó?"
  n "Pues..."
  n "Voy a jugar Hollow Knight por 324 vez"
  n "Quería ver si quieres jugar conmigo"
  tu "¿Hollow Knight?"
  tu "¿Ese no es un juego de consolas?"
  n "Sí"
  tu "¿Y cómo vamos a jugar?"
  tu "Estamos en la escuela..."
  n "Oh, tenemos un cuarto de juegos"
  tu "Espera... ¿Eso es legal?"
  n "Quizá..."
  n "Pero no importa, siempre lo hemos hecho y nunca nos han dicho nada"
  n "Si nadie se entera, todo estará bien"
  n "Vamos"
  tu "Ok..."

  n "Este es el cuarto de juegos"
  n "Tenemos de todo"
  n "Hollow Knight, Rocket League, Minecraft, etc."
  n "Pero... Primeramente"

  menu:
    "Playstation":
      n "Sabía que ibas a decir eso"

    "Xbox":
      n "X-Trash"

  n "Bueno, no es necesario que pongas tu cuenta"
  n "Simplemente puedes jugar como invitado"
  n "Ten, agarra el dualshock, vamos a jugar en el Play"
  tu "Ya veo..."
  tu "¿Y de qué trata Hollow Knight?"
  n "Es un juego de plataformas"
  n "Te va a gustar"
  "Jamás había oído de él"
  "Quizá sí esté interesante..."
  "Vamos a ver"

  "Pasaron las horas y seguimos jugando"
  "Jamás pensé que un juego así estaría tan entretenido"
  "Las visuales son simplemente hermosas"
  "Llevamos un buen rato y ya hemos matado a 3 jefes"
  "No es un juego fácil"
  "Pero Naki se mueve como si lo fuera"
  "Como si quisiera terminar el juego lo más rápido posible"
  "Debe ser parte de su naturaleza"
  "Es raro que yo juegue en consola"
  "Es raro que yo juegue otra cosa que no sea LoL"
  "Pero es divertido"
  "Es divertido pasar el tiempo con alguien"
  "Quizá lo que pensaba de las personas no era cierto"
  "Quizá..."
  
  n "Oye"
  n "Ya nos tenemos que ir"
  n "Van a cerrar la escuela"
  n "Y tenemos que guardar las consolas y las teles"
  n "No queremos que nos descrubran..."

  tu "Oh, sí, claro"
  
  "Lo ayudé a recoger todo y cuando estaba a punto de irme..."
  n "Oye"
  n "No se te olvide sacar tus waifus"
  n "Veremos si te vuelve a salir otra de mis Wishlist..."
  n "Digo"
  n "No te estoy presionando para nada, claro..."
  n "Igual"
  n "Bueno"
  n "Nos vemos"

  "Cierto"
  "Tengo que sacar Waifus"
  "Vamos a ver qué me sale"

  jump game1

label level1Pabel:
  p "Hola [povname], ¿cómo estás?"
  tu "Hola otra vez Pabel, ¿qué pasó?"
  p "Oh, nada. Solo quería saludarte"
  tu "Ya veo... Aunque ya me has saludo muchas veces hoy"
  p "Bueno..."
  p "Es que..."
  p "Realmente te quería a jugar Roblox conmigo"
  tu "Oh, ¿Roblox?"
  tu "¿El juego de computadora para Niños?"
  p "NOOOO"
  p "O sea"
  p "Sí..."
  p "Pero no es para niños..."
  p "No importa"
  p "¿Quieres jugarlo?"
  p "Es divertido..."
  p "Es un juego llamado 'Heroes Justice'"
  p "Está interesante..."
  p "Es de farmear"
  tu "Oh..."
  "Pues, realmente no estaría perdiendo nada"
  "Si le gustó a Pabel, quizá si esté divertido"
  tu "No pierdo nada, podemos intentarle"
  p "Súper"
  p "Pero te toca usar la computadora de la esculea"
  p "Yo pido el Xbox"
  tu "¿Xbox?"
  p "Oh, sí. No te dijimos"
  p "Tenemos un cuarto de juegos aquí"
  p "Tenemos de todo"
  tu "¿Eso es legal?"
  p "Mmmmm"
  p "Es legal mientras nadie sepa"
  p "Supongo..."
  p "Pero tú no te preocupes por eso"
  p "Lo llevamos haciendo un buen de tiempo y no ha pasado nada"
  p "Entonces no hay nada de qué preocuparse"
  p "Ven, sígueme"
  tu "Ok..."

  tu "Woow. De verdad tienen de todo"
  p "Te dije"
  p "Puedes jugar lo que quieras. Rocket League, Roblox, etc."
  p "Es divertido"
  tu "Entonces, ¿me toca jugar en la compu de la escuela?"
  p "Si... Va algo lenta pero igual creo que lo corre"
  p "Creo..."
  p "Oh bueno, ¿en dónde quieres jugar?"

  menu:
    "Computadora de la escuela":
      p "Vaaa. Gracias jeje"
    "Xbox":
      p "Va, entonces tienes que poner tu cuenta de Xbox"
      tu "No tengo..."
      p "Oh, nimodo. Tendrás entonces que jugar en la computadora de la escuela"
      "¿Se alegró?"

  p "Bueno, primeramente crea una cuenta"

  $roblox_username = renpy.input("Ingresa tu nombre de usuario de Roblox")

  p "Genial, ahora en adelante te llamaremos"
  p "[roblox_username]"
  p "No es cierto, jaja. Está muy estúpido ese nombre. Prefiero decirte [povname]"
  p "Bueno pues, podemos empezar a jugar"

  p "Este eres tú"
  p "Tienes que girar la ruleta para conseguir tu quirk"

  # Screen girar ruleta
  $ quirk_name = "One For All"

  p "Genial, conseguiste [quirk_name], es de los más raros del juego. De hecho yo también tengo ese"
  tu "Genial"
  p "Ahora, tienes que hacer..."
  p "Y luego..."
  p "Ven acá..."

  "El tiempo pasó"
  "El juego está relativamente entretenido"
  "No hay mucho que hacer"
  "Pero entretiene"
  "Quizá es bueno para los momentos donde no hay nada que hacer"
  "Pero igual"
  "Me la estoy pasando bien..."
  "Me la estoy pasando bien con Pabel..."
  "Quizá me equivoqué"
  "Tal vez las personas no son como yo pensaba"
  "Tal vez..."

  p "Oye [povname]"
  tu "¿Eh?"
  tu "Oh..."
  tu "Perdón"
  tu "¿Qué pasó?"
  p "Ya nos tenemos que ir"
  p "Van a cerrar la escuela"
  tu "Oh, entonces deja te ayudo a guardar"

  p "Pues. Ya me voy"
  p "Hmmm..."
  p "No se te olvidé sacar Waifus"
  p "No estoy diciendo que me tengas que regalar la que te salga..."
  p "Cero presión"
  p "Bueno, ya me voy"
  p "Hasta la próxima"
  tu "Adiós..."

  "Cierto, tengo que sacar Waifus"
  "Vamos a ver qué me toca"
  "Y les platico a los chicos qué me salio mañana"

  jump game1

  label level1Mau:
    m "Hey, qué tal [povname]"
    tu "Hola"
    