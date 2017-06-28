gPats = [

  # [r'(.*)quit(.*)',
  # ["quit"],["Okay, Let's quit.      "]],

  # direction
  [r'(right|left)',
  ["O_Direction('%1')"],["Okay, I see.      "]],

#initalize
  [r'(.*)clear(.*)',
  ["turtle.clear()"],["Okay, Let's make the screen clean!      "]],

  [r'(.*)clean(.*)',
  ["turtle.clear()"],["Okay, Let's make the screen clean!      "]],

  [r'(.*)home(.*)',
  ["turtle.home()"],["Okay, Let's start from the original place!      "]],

  [r'(.*)original place(.*)',
  ["turtle.home()"],["Okay, Let's start from the original place!      "]],


#circle
  [r'(.*)circle(.*) (\d*) (.*)radius(.*)',
  ["turtle.circle (%3)"],["Okay, Let's draw a circle with the radius in %3 units!      "]],

  [r'(.*)circle(.*) radius(.*) (\d*) (.*)',
  ["turtle.circle (%4)"],["Okay, Let's draw a circle with the radius in %4 units!      "]],

  [r'(.*)circle(.*) radius(.*) (\d*)(.*)',
  ["turtle.circle (%4)"],["Okay, Let's draw a circle with the radius in %4 units!      "]],

  [r'(.*) (\d*) (.*) radius circle(.*)',
  ["turtle.circle (%2)"],["Okay, Let's draw a circle with the radius in %2 units!      "]], 
  
  [r'(.*) (\d*)(.*) radius circle(.*)',
  ["turtle.circle (%2)"],["Okay, Let's draw a circle with the radius in %2 units!      "]],
         
  [r'(\D*)circle(\D*)',
  ["circle_o('Omit')"],["You should tell me how long is the radius!      "]],

#repeat
  [r'(.*)repeat (.*)following (\d*) (.*) for (\d*) time[s]*',
  ["repeat %5: follow%3"],["Okay, Let's repeat the following %3 commands for %5 times! You have to say 'end repeat' when you want to finish the repeat!      "]],

  [r'(.*)repeat the following (.*) for (.*) time[s]*',
  ["repeat %3: follow"],["Okay, Let's start the repeat! You have to say 'end repeat' when you want to finish the repeat     "]],
  
  [r'(.*)repeat following (.*) for (.*) time[s]*',
  ["repeat %3: follow"],["Okay, Let's start the repeat!You have to say 'end repeat' when you want to finish the repeat     "]],

  [r'(.*)do this (\d*) time[s]*',
  ["repeat %3: follow"],["Okay, Let's repeat these for %3 times!       "]],

  [r'(.*)do this for (\d*) time[s]*',
  ["repeat %2: follow"],["Okay, Let's repeat these for %2 times!       "]],
  
  [r'(.*)end(.*)',
  ["end"],["Okay, Let's end the repeat!     "]],

  [r'(.*)repeat (.*)last (\d*)(.*) for (\d*) time(.*)',
  ["repeat('last',%3,%5)"],["Okay, Let's repeat the last %3 commands for %5 times!      "]],

  [r'(.*)repeat (.*)last (\d*)(.*) (\d*) time(.*)',
  ["repeat('last',%3,%5)"],["Okay, Let's repeat the last %3 commands for %5 times!      "]],

  [r'(.*)repeat (.*)last (\d*) commands',
  ["repeat('last',%3,1)"],["Okay, Let's repeat the last %3 commands!      "]],

  # [r'(\D*)repeat(\D*)',
  # ["Omit=Omit+1"],["YOU should tell me repeat the last (number) commands for how many times!      "]],
#  [r'(.*)Let (.*) be (.*) repeat (\d*) time(.*)',
#  ["to %2 repeat %4 [%3]"],["Okay, Let's make %2 to be %3 repeat %4 times!     "]],

#  [r'(.*)Let (.*) be repeat the last (.*) command[s] for (.*) time[s]*(.*)',
#  ["to %2 repeat %4 [%3]"],["Okay, Let's make %2 to be the last %3 commands repeat %4 times!     "]],

  [r'(.*)repeat (.*) for (\d*) time[s](.*)',
  ["repeat('func:%2',0,%3)"],["Okay, Let's repeat %2 for %3 times!      "]],
  
  
#delete
  [r'(.*)the last (.*) is wrong',
  ["turtle.undo()"],["Okay, Let's delete the last command!     "]],

  [r'(.*)delete the last (.*) (command[s]*|step[s]*) (.*)',
  ["for i in range(%2):turtle.undo()"],["Okay, Let's delete the last %2 commands!     "]],

  [r'(.*)last (.*) (.*) (is|are) wrong',
  ["for i in range(%2):turtle.undo()"],["Okay, Let's delete the last %2 commands!     "]],
  
#define
  [r'(.*)let (.*) be the following (command[s]*|step[s]*)',
  ["to %2"],["Okay, Let's make %2 the following steps!    "]],

  [r'(.*)let (.*) be the these (command[s]*|step[s]*)',
  ["to %2"],["Okay, Let's make %2 the following steps!    "]],

  [r'(.*)end (.*)',
  ["end"],["Okay, Let's make this the end of %2!      "]],

  [r'(.*)let this be the end of (.*)',
  ["end"],["Okay, Let's make this the end of %2!      "]],

  [r'(.*)let (.*) be the last (.*) commands',
  ["function('last',%3,'%2')"],["Okay, Let's make %2 the last %3 commands!    "]],

  [r'(.*)let (.*) be the last (.*) steps',
  ["function('last',%3,'%2')"],["Okay, Let's make %2 the last %3 steps!    "]],

  [r'(.*)let (.*) be the following (.*) commands',
  ["to %2 follow%3 end"],["Okay, Let's make %2 the follow %3 commands!    "]],

  [r'(.*)let (.*) be the following (.*) steps',
  ["to %2 follow%3 end"],["Okay, Let's make %2 the follow %3 steps!    "]],

  [r'(.*)let\'s call it (.*)',
  ["to %2 last1 end"],["Okay, let\'s call the last command %2!    "]],
         
#follow
 
  [r'(.*)let (.*) be (.*) and (.*)',
  ["to %2 %3 %4 end"],["Okay, Let's make %2 be %3 followed by %4!     "]],

  [r'(.*)let (.*) be (.*) followed by (.*)',
  ["to %2 %3 %4 end"],["Okay, Let's make %2 be %3 followed by %4!     "]],

#width

  [r'(.*)width(.*) (\d*)(.*)',
  ["turtle.pensize(%3)"],["Okay, Let's make the width be %3!    "]],

  [r'(.*)pen(.*) (thicker|bolder)(.*)',
  ["turtle.pensize(turtle.pensize()+3)"],["Okay, Let's make the pen width thicker!    "]], 

  [r'(.*)pen(.*) lighter(.*)',
  ["turtle.pensize(turtle.pensize()-3)"],["Okay, Let's make the pen width thicker!    "]], 
  
  [r'(\D*)width(\D*)',
  ["Omit=Omit+1"],["You have to say a definite number of the pen width!      "] ],
#color

  [r'(.*)color(.*) be (.*)',
  ["turtle.pencolor('%3')"],["Okay, Let's make the color %3!    "]],

  [r'(.*)(black|red|blue|grey|brown|green|yellow|orange|pink|purple)(.*)',
  ["turtle.pencolor('%2')"],["Okay, Let's make the color %2!    "]],

#penup pendown
  [r'(.*)pen(.*) down(.*)',
  ["turtle.pendown ()"],["Okay, Let's make the pen back on the paper    "]],
  
  [r'(.*)pen(.*) up(.*)',
  ["turtle.penup ()"],["Okay, Let's make the pen off the paper    "]],
  
  [r'(.*)pen off(.*)paper(.*)',
  ["turtle.penup ()"],["Okay, Let's make the pen off the paper    "]],

#forward
  [r'(.*)straight on for (\d*)(.*)',
  ["turtle.fd (%2)"],["Okay, Let's forward %2 steps!     "]],

  [r'(.*)straight on (\d*)(.*)',
  ["turtle.fd (%2)"],["Okay, Let's forward %2 steps!     "]],

  [r'(.*)move on for (\d*)(.*)',
  ["turtle.fd (%2)"],["Okay, Let's forward %2 steps!     "]],
  
  [r'(.*)move on (\d*)(.*)',
  ["turtle.fd (%2)"],["Okay, Let's forward %2 steps!     "]],

  [r'(.*)forward (\d*) (.*)',
  ["turtle.fd (%2)"],["Okay, Let's forward %2 steps!     "]],
         
  [r'(.*)forward(.*) (\d*) (.*)',
  ["turtle.fd (%3)"],["Okay, Let's forward %3 steps!     "]],
         
  [r'(.*)forward (.*) (\d*)',
  ["turtle.fd (%3)"],["Okay, Let's forward %3 steps!     "]],

  [r'(.*)line (.*) (\d*) (.*)',
  ["turtle.fd (%3)"],["Okay, Let's draw a line with length %3!     "]],

  [r'(.*)line (.*) (\d*)(.*)',
  ["turtle.fd (%3)"],["Okay, Let's draw a line with length %3!     "]],

  [r'(.*)line (\d*) (.*)',
  ["turtle.fd (%2)"],["Okay, Let's draw a line with length %3!     "]],

  [r'(.*)line(.*) (\d*) (.*)',
  ["turtle.fd (%3)"],["Okay, Let's draw a line with length %3!     "]],

  [r'(.*) (\d*) (.*) forward (.*)',
  ["turtle.fd (%2)"],["Okay, Let's forward %2 steps!     "]],

  [r'(.*) (\d*) forward (.*)',
  ["turtle.fd (%2)"],["Okay, Let's forward %2 steps!     "]],

  [r'(.*) (\d*) (.*) forward',
  ["turtle.fd (%2)"],["Okay, Let's forward %2 steps!     "]],

  [r'(.*) (\d*) (.*) front(.*)',
  ["turtle.fd (%2)"],["Okay, Let's forward %2 steps!     "]],

  [r'(.*) (\d*) (.*) ahead(.*)',
  ["turtle.fd (%2)"],["Okay, Let's forward %2 steps!     "]],

  [r'(.*) ahead (\d*)(.*)',
  ["turtle.fd (%2)"],["Okay, Let's forward %2 steps!     "]],
         
  [r'(.*) (\d*)(.*) to the front',
  ["turtle.fd (%2)"],["Okay, Let's forward %2 steps!     "]],
   
  [r'(.*) (\d*)(.*) ahead(.*)',
  ["turtle.fd (%2)"],["Okay, Let's forward %2 steps!     "]],

  [r'(.*)(draw|forward|make|build) a line(.*) (\d*)',
  ["turtle.fd (%4)"],["Okay, Let's draw a line with length %4!     "]],
         
  [r'(.*)(draw|forward|make|build) a line(.*) (\d*)(.*)',
  ["turtle.fd (%4)"],["Okay, Let's draw a line with length %4!     "]],
         
  [r'(.*)(draw|forward|make|build) a line(\D*)',
  ["move_o('fd','Omit')"],["You have to say how long you would like to draw!      "]],
#  [r'(.*)forward a line (.*) unit[s]* long',
#  ["fd (%2)"],["Okay, Let's draw a line with length %2!     "]],

#  [r'(.*)forward a line (.*) unit[s]* in length',
#  ["fd (%2)"],["Okay, Let's draw a line with length %2!     "]],


#back
  [r'(.*)backward (\d*) (.*)',
  ["turtle.bk (%2)"],["Okay, Let's backward %2 steps!     "]],

  [r'(.*)backward (.*) (\d*) (.*)',
  ["turtle.bk (%3)"],["Okay, Let's backward %3 steps!     "]],

  [r'(.*)back (\d*) (.*)',
  ["turtle.bk (%2)"],["Okay, Let's backward %2 steps!     "]],

  [r'(.*)back (.*) (\d*) (.*)',
  ["turtle.bk (%3)"],["Okay, Let's backward %3 steps!     "]],

  [r'(.*) (\d*) (.*) (backward|back) (.*)',
  ["turtle.bk (%2)"],["Okay, Let's backward %2 steps!     "]],

  [r'(.*) (\d*) (backward|back) (.*)',
  ["turtle.bk (%2)"],["Okay, Let's backward %2 steps!     "]],

  [r'(.*) (\d*) (.*) (backward|back)',
  ["turtle.bk (%2)"],["Okay, Let's backward %2 steps!     "]],
         
         
  [r'(.*)regress (\d*)(.*)',
  ["turtle.bk (%2)"],["Okay, Let's backward %2 steps!     "]],
         
#  [r'(.*)draw a line of (.*) unit[s]* long',
#  ["bk %2"],["Okay, Let's draw a line with length %2!     "]],
         
#  [r'(.*)draw a line (.*) unit[s]* in length',
#  ["bk %2"],["Okay, Let's draw a line with length %2!     "]],
         
#  [r'(.*)forward a line (.*) unit[s]* long',
#  ["bk %2"],["Okay, Let's draw a line with length %2!     "]],
         
#  [r'(.*)forward a line (.*) unit[s]* in length',
#  ["bk %2"],["Okay, Let's draw a line with length %2!     "]],

#heading
  [r'(.*)(east|south|west|north)(.*)',
  ["turtle.seth (%2)"],["Okay, Let's face to the %2!      "]],



#turn
  [r'(.*)turn (left|right) (\d*)(.*)',
  ["turn_o('%2','%3')"],["Okay, Let's turn %2 %3 degrees!      "]],

  [r'(.*)turn (\d*) (.*) (right|left)(.*)',
  ["turtle.%4 (%2)"],["Okay, Let's turn %4 %3 degrees!      "]], 

  [r'(.*)turn (left|right)',
  ["turtle.%2 (90)"],["Okay, Let's turn %2!     "]],

  [r'(.*)(right|left) turn (of|with) (\d*)(.*)',
  ["turtle.%2 (%4)"],["Okay, Let's rotate %4 degree to the %2!     "]],

  [r'(.*)(right|left) turn (\d*)(.*)',
  ["turtle.%2 (%4)"],["Okay, Let's rotate %4 degree to the %2!     "]],

  # [r'(.*)(right|left) turn(.*)',
  # ["turtle.%2 (90)"],["Okay, Let's rotate %2 degree clockwise!     "]],
  
  [r'(.*)rotate (\d*)(.*) clockwise',
  ["turtle.right (%2)"],["Okay, Let's rotate %2 degree clockwise!     "]],

  [r'(.*)rotate (\d*)(.*) (left|right)',
  ["turtle.%4 (%2)"],["Okay, Let's turn %4 %2 degree!      "]],

  [r'(.*)rotate (\d*)(.*) anticlockwise',
  ["turtle.left (%2)"],["Okay, Let's rotate %2 degree anticlockwise!     "]],

  [r'(\D*)turn(\D*) (right|left)(\D*)',
  ["turn_o('%3'),'Omit'"],["You should give the definite degree of the turn!      "]],

  [r'(\D*)(right|left)(\D*) turn(\D*)',
  ["turn_o('%2','Omit')"],["You should give the definite degree of the turn!      "]],

  [r'(.*)turn (\d*)((^(right|left))*)',
  ["turn_o('Omit','%2')"],["You should give the definite degree of the turn!      "]],

#triangle
  [r'(.*)triangle (.*) (\d*) (.*)',
  ["polygon(3, %3)"],["Okay, Let's draw a triangle edge %2     "]],
         
  [r'(.*)triangle (\d*) (.*)',
  ["polygon(3, %2)"],["Okay, Let's draw a triangle edge %2     "]],

  [r'(.*)triangle (.*) (\d*)',
  ["polygon(3, %3)"],["Okay, Let's draw a triangle edge %2     "]],
         
  [r'(.*)triangle (\d*)',
  ["polygon(3, %2)"],["Okay, Let's draw a triangle edge %2     "]],
         
  [r'(\D*)triangle(\D*)',
  ["polygon(3,'Omit')"],["You have to tell me the length of the edge!     "]],
  
#square  
  [r'(.*)square (.*) (\d*) (.*)',
  ["polygon(4, %3)"],["Okay, Let's draw a square edge %3     "]],

  [r'(.*)square (.*) (\d*)',
  ["polygon(4, %3)"],["Okay, Let's draw a square edge %3     "]],

  [r'(.*)square (\d*) (.*)',
  ["polygon(4, %2)"],["Okay, Let's draw a square edge %2     "]],

  [r'(.*)square (\d*)',
  ["polygon(4, %2)"],["Okay, Let's draw a square edge %2     "]],
  
  [r'(\D*)square(\D*)',
  ["polygon(4,'Omit')"],["You have to tell me the length of the edge!     "]],

#rhombus
  [r'(.*)diamond (.*) (\d*) (.*)',
  ["diamond(120,%3)"],["Okay, Let's draw a diamond edge %3     "]],
  
  [r'(.*)diamond (.*) (\d*)',
  ["diamond(120,%3)"],["Okay, Let's draw a diamond edge %3     "]],
  
  [r'(.*)diamond (\d*) (.*)',
  ["diamond(120,%2)"],["Okay, Let's draw a diamond edge %2     "]],
  
  [r'(.*)diamond (\d*)',
  ["diamond(120,%2)"],["Okay, Let's draw a diamond edge %2     "]],
         
  [r'(\D*)diamond(\D*)',
  ["diamond(120,'Omit')"],["You have to tell me the length of the edge!     "]],
         
# write
  [r'(.*)write(.*)text (\b\w*\b) (.*)',
  ["turtle.write('%3', font=('Arial', 20, 'normal'))"],["Here is the text you want!     "]],

  [r'(.*)write (\b\w*\b) (.*)',
  ["turtle.write('%2', font=('Arial', 20, 'normal'))"],["Here is the text you want!     "]],
   

# number
  [r'(\d*)',
  ["O_Num('%1')"],["Okay, I see.      "]],

  [r'(\d*) (\w*)',
  ["O_Num('%1')"],["Okay, I see.      "]],



# use a colored pen
   ]

gReflections = {
  "or":"|",
  "one":"1",
  "two":"2",
  "three":"3",
  "four":"4",
  "five":"5",
  "six":"6",
  "seven":"7",
  "eight":"8",
  "nine":"9",
  "zero":"0",
  "not a":"non ",
  "become":"be",
  "integer" : "int",
  "character" : "char",
  "am"   : "are",
  "was"  : "were",
  "i"    : "you",
  "i'd"  : "you would",
  "i've"  : "you have",
  "i'll"  : "you will",
  "my"  : "your",
  "are"  : "am",
  "you've": "I have",
  "you'll": "I will",
  "your"  : "my",
  "yours"  : "mine",
  "you"  : "me",
  "me"  : "you",
  "east":"0",
  "south":"270",
  "west":"180",
  "north":"90"
  
}

