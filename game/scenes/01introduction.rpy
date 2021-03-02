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
define tu = Character("[povname]")

label introduction:

    $ povname = "Tú"
    $ adv_menu = menu

    $ persistent.wishlist_activated = False 
    
    "Estoy caminando"
    "Veo incotables caras a lo largo de todo el pasillo"
    "Qué desagradable"
    "Gente riéndo, platicando con sus amigos, o jugando. Simplemente me da asco"
    "La gente debería dejar de existir"
    "La amistad es una mentira"
    "Te hacen creer que eres su amigo, pero al final, te dejan solo"
    "Solo, abandonado y deprimido"
    "¿Por qué la gente sigue buscado tener amigos?"
    "¿Acaso no conocen League of Legends?"
    "Jugarlo no genera estrés, genera felicidad"
    "¿Acaso no lo notan?"
    "Sigo caminando"
    "Veo el director que está enfrente de mí"
    "Cierto, estoy aquí por lo que hice..."
    "El director abre la puerta de su oficina y me da el paso"
    "Su oficina es relativamente normal, no hay nada que llame la atención"
    "El director se sienta y me mira fíjamente a los ojos"
    d "¿Te das cuenta de lo que hiciste?"
    "Lo que hice..."
    "¿Hice algo malo?"
    "Oh... Creo que se refiere a lo que hice en computación"
    tu "No..."
    "Miento"
    "Claro que sé lo que hice. Simplemente fue un impulso"
    "Además, ¿qué me importa lo que estaban viendo en clase?"
    d "Según el reporte de la maestra, estabas jugando League of Legends en clase"
    "Rayos, estoy en problema"
    d "¿Acaso no leíste el reglamento?"
    d "Esta ha sido la 5ta vez que has hecho eso y simplemente no entiendes"
    "Dios, se vienen las planas otra vez"
    d "Tendré que tomar medidas"
    "¿Eh?"
    d "Serás expulsado de la Preparatoria CETYS"
    "."
    ".."
    "..."
    "¡¿QUÉE?!"
    d "Es una decisión que hemos tomado todos los profes"
    d "No te queremos en esta escuela"
    d "No hay nada que nos pueda hacer cambiar de opinion"
    "¡No lo puedo creer!"
    "¡¿Qué le voy a decir a mi papá?!"
    d "Así que bueno. Ve agarrando tus cosas y por favor retírate de nuestras instalaciones"
    "..."
    tu "Sí Señor"
    "Pues ni modo... A afrontar las consecuencias"

    "Vaya, si tan solo hubiera sido un poco más precavido."
    "Pero la partida estaba muy buena"
    "No podía hacer perder a mi equipo por la estúpida clase"

    "Recorro la calle, en camino a mi hogar"
    "CETYS está en un cerro"
    "Puedo ver toda la ciudad desde aquí"
    "La ruidosa y bachienta ciudad"
    "..."
    "Sigo caminando por la calle y veo la escuela vecina"
    "El Anáhuac"
    "¿Acaso alguien lo conoce?"


    "Llego a mi casa y le cuento a mi papá la noticia"
    pa "Pues"
    pa "Lo venía venir..."
    pa "¿Qué piensas hacer?"

    menu:
        "Seguir estudiando":
            tu "Creo que es mejor seguir estudiando, ¿puedo entrar a otra escuela?"
            pa "Me gusta esa actitud"

        "Dejar la escuela":
            tu "Es mejor si me salgo de la escuela y me dedico a otra cosa"
            pa "¿Qué acabas de decir?"
            pa "No sabes hacer nada, ¿y quieres dejar la escuela?"
            pa "Ni en tus sueños"

    pa "No puedes seguir siendo alguien solitario"
    pa "No te va a servir de nada en tu vida"
    pa "Vas a entrar al Anáhuac"
    pa "Y vas a tener un único objetivo"
    pa "{b}Conseguir amigos{/b}"
    "..."
    "¿Mi papá me está obligando a conseguir amigos?"
    "¿Acaso no sabe lo horroroso que es tener amigos?"
    "Me van a traicionar"
    "Siempre pasa lo mismo. No me puede obligar"
    "Pero..."
    "No puedo decirle que no"
    "Me va a ir peor"
    "Horrible"
    tu "Está bien"
    pa "¿Eh? No me esperaba esa reacción"
    tu "Está bien, no me queda de otra"
    tu "Tengo que aprovechar la oportunidad, ¿no?"
    "Me voy a arrepentir"
    "Lo sé"
    "Lo presiento"
    jump firstDay
