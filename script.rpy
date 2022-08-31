# Script of the visual novel.

# Character names and font colors

define f = Character("Florecita")
define c = Character("Caballito")
define g = Character("Gatito")
define p = Character("Cerdito")
define k = Character("Cabrita")
define o = Character("Ovejitas")
define m = Character("Mamá de Florecita")
define a = Character("Animalito negro", color="#00ff00")
define cn = Character("Copo de Nieve")
define bn = Character("Blanca Nieves")

# The game starts here.

label start:

    play music intro_carefree volume 0.1

    # Intro scene: The farm from above, at night. The little horse is seen from afar

    show granja noche1
    with dissolve

    "Era de noche en la granja"
    "Todos los animales estaban dormidos"
   
    show caballo chiquito at Position(xpos = 0.82, xanchor=0.5, ypos=0.47, yanchor=0.5) 
    with dissolve

    "El caballito estaba dormido..."

    # Close up of the horse. He is dreaming

    #hide granja noche1
    hide caballo chiquito
    #show corral caballos
    show caballo dormido at Position(xpos = 0.75, xanchor=0.5, ypos=0.67, yanchor=0.5) 
    with dissolve
    
    $renpy.sound.play("C:/Users/Mauricio Maldonado/Documents/renPyProjects/Florecita/game/audio/snoring_whistle.mp3", loop=True, relative_volume=0.5)
    #play sound snoring_whistle volume 0.1

    show globo zanahorias at Position(xpos = 0.47, xanchor=0.5, ypos=0.50, yanchor=0.5) 
    with dissolve

    "soñando con dulces zanahorias..."

    hide globo zanahorias 
    with dissolve
    
    show globo heno at Position(xpos = 0.78, xanchor=0.5, ypos=0.25, yanchor=0.5) 
    with dissolve

    "y fresco heno"

    hide globo heno 
    with dissolve

    "Cuando de repente, escuchó un sonido"

    # Florecita enters the scene.

    play sound sheep_baa volume 0.5
    
    show florecita facingright at Position(xpos = 0.27, xanchor=0.5, ypos=0.67, yanchor=0.5) 
    with easeinleft 

    a "Beee, beee"

    play sound horse_whinny volume 0.5
    "Medio dormido, abrió los ojos"

    show caballo boquiabierto

    c "¿Qué clase de animal eres?" 

    c "Como tu pelo es oscuro casi no te puedo ver!"
    a "Soy Florecita, y estoy perdida"

    show caballo feliz

    c "Ahhh, no te preocupes!"
    c "Yo te voy a ayudar a encontrar a tu familia."

    show caballo serio
    
    c "Yo conozco a alguien que tiene el pelo negro como tú."

    show caballo chiquito at Position(xpos = 0.82, xanchor=0.5, ypos=0.47, yanchor=0.5) with dissolve
    show florecita chiquita at Position(xpos = 0.75, xanchor=0.5, ypos=0.50, yanchor=0.5) with dissolve
    show cerdo dormidosombra at Position(xpos = 0.3, xanchor=0.5, ypos=0.25, yanchor=0.5) with dissolve


    "Entonces el caballito y Florecita fueron al granero a visitar a la familia de los gatos."

    show caballo chiquitoright at Position(xpos = 0.35, xanchor=0.5, ypos=0.67, yanchor=0.5) with dissolve
    show florecita chiquita at Position(xpos = 0.30, xanchor=0.5, ypos=0.67, yanchor=0.5) with dissolve

    call conLosGatos

label conLosGatos:

    play music dancing_skeletons volume 0.1

    "(En el granero)"

    hide granja noche1
    hide caballo chiquitoright
    hide florecita chiquita
    hide cerdo dormidosombra
    show granero noche

    "(En el granero)"

    show gato negro at Position(xpos = 0.75, xanchor=0.5, ypos=0.67, yanchor=0.5) with dissolve
    show caballo serioright at Position(xpos = 0.20, xanchor=0.5, ypos=0.67, yanchor=0.5) with easeinleft 
    show florecita facingright at Position(xpos = 0.35, xanchor=0.5, ypos=0.75, yanchor=0.5) with easeinleft 

    "\"¿En qué puedo ayudarlos?\" preguntó el gatito que no esperaba visitas."

    f "Soy Florecita y estoy perdida."
    f "Estoy buscando a mi familia, pero... no creo que seas tú."
    f "Tú eres mucho más pequeño que yo."
    g "Ahhh, no te preocupes!" 
    g "Yo conozco a alguien que es grande como tú."

    "Entonces el caballito, el gatito y Florecita fueron a visitar a los cerditos."

    hide gato negro with dissolve
    hide caballo serioright with dissolve
    hide florecita facingright with dissolve
    hide granero noche
    show granja noche1
    show cerdo dormidosombra at Position(xpos = 0.3, xanchor=0.5, ypos=0.25, yanchor=0.5) with dissolve

    "Yendo a visitar a los cerditos"

    play music intro_carefree volume 0.1

  
    show caballo chiquitoright at Position(xpos = 0.35, xanchor=0.5, ypos=0.67, yanchor=0.5) with dissolve
    show florecita chiquita at Position(xpos = 0.30, xanchor=0.5, ypos=0.67, yanchor=0.5) with dissolve
    show gato chiquito at Position(xpos = 0.25, xanchor=0.5, ypos=0.7, yanchor=0.5) with dissolve
    show cerdo dormidocolor at Position(xpos = 0.3, xanchor=0.5, ypos=0.25, yanchor=0.5) with dissolve

    "Yendo a visitar a los cerditos"

    call conLosCerdos

label conLosCerdos:

    "\"Oink, oink!\" dijo el cerdito, que no esperaba visitas."
    p "¿En qué puedo ayudarlos?"
    f "Soy Florecita y estoy perdida."
    f "Estoy buscando a mi familia, pero... no creo que seas tú."
    f "Tú hablas diferente. Yo hago bee, bee."
    p "Ahhh, no te preocupes!"
    p "Yo conozco a alguien que habla como tú."
    "Entonces el caballito, el gatito, el cerdito y Florecita fueron a visitar a las cabritas."

    "Yendo a visitar a las cabritas"

    "Yendo a visitar a las cabritas"

    call conLasCabras

label conLasCabras:

    "\"Mee, mee! dijo\" la cabrita que no esperaba visitas."
    k "¿En qué puedo ayudarlos?"
    f "Soy Florecita y estoy perdida."
    f "Estoy buscando a mi familia, pero... no creo que seas tú."
    f "Oh, ya no sé a dónde pertenezco."
    c "¿Florecita te pertenece?" 
    "Preguntó el caballito."
    k "Pues... es cierto que hablamos parecido..."
    k "Pero nosotros no tenemos un abrigo tan esponjoso"
    k "pero no te preocupes! yo conozco a alguien que tiene el pelo suave como tú."

    "Entonces el caballito, el gatito, el cerdito, la cabrita y Florecita fueron a visitar a el corral de las ovejas."

    "Yendo a visitar a las ovejas"

    "Yendo a visitar a las ovejas"

    call conLasOvejas

label conLasOvejas:

    o "Hermana, hermana! ya estas aquí!"
    "Dijeron Copo de Nieve y Blanca Nieves"
    c "¿Hermana? ¿Eres una oveja?"
    "\"Florecita es una oveja muy especial\" dijo una voz dulce"
    "Era la mamá de Florecita!"
    m "Muchas gracias por traerla a casa, pero... es tarde"
    m "Es hora de que los caballitos..."
    m "los gatitos..."
    m "los cerditos..."
    m "las cabritas..."
    m "y las ovejitas..."
    m "se vayan a dormir."

# Introducir aqui una seleccion.(a) Ir a dormir (b) pero mami, queremos jugar!

    jump dormir_o_no

label dormir_o_no:

    menu:

        "Que quieres hacer?"

        "Ir a dormir":
            jump adormir

        "Pero mami, queremos jugar!":
            jump ajugar

label adormir:

    "Ir a dormir"

    "A dormir, a dormir" 

    return

label ajugar:

    o "Pero mami, queremos jugar!"
        
    m "Esta bien, pero solo un ratito"
    cn "Yo conozco a alguien que sabe muchos juegos."
    bn "Vayamos!"
    "Entonces el caballito"
    "el gatito"
    "el cerdito"
    "la cabrita"
    "las ovejitas y Florecita"
    "fueron a visitar el corral de las vaquitas"

    return
