#----------------------------------------------------------------------
#  eliza.py
#
#  a cheezy little Eliza knock-off by Joe Strout <joe@strout.net>
#  with some updates by Jeff Epler <jepler@inetnebr.com>
#  hacked into a module and updated by Jez Higgins <jez@jezuk.co.uk>
#  last revised: 28 February 2005
#----------------------------------------------------------------------

import string
import re
import random
import csv
import sys

class eliza:
  
   
  def __init__(self):                                                        # 
    self.keys = map(lambda x:re.compile(x[0], re.IGNORECASE),gPats)
    self.values = map(lambda x:x[2],gPats)
    self.dialog = map(lambda x:x[1],gPats)     
      
          
  
  #----------------------------------------------------------------------
  # translate: take a string, replace any words found in dict.keys()
  #  with the corresponding dict.values()
  #----------------------------------------------------------------------
  def translate(self,str,dict):
    words = string.split(string.lower(str))
    keys = dict.keys();
    for i in range(0,len(words)):
      if words[i] in keys:
        words[i] = dict[words[i]]
      return string.join(words)
    
  #----------------------------------------------------------------------
  #  respond: take a string, a set of regexps, and a corresponding
  #    set of response lists; find a match, and return a randomly
  #    chosen response from the corresponding list.
  #----------------------------------------------------------------------
  def respond(self,str):
    global a
    # find a match among keys
    for i in range(0,len(self.keys)):
      match = self.keys[i].match(str)
      if match:
        # found a match ... stuff with corresponding value
        # chosen randomly from among the available options
        value= random.choice(self.values[i])
        dialog= random.choice(self.dialog[i])
        resp = value + dialog

        posi = string.find(dialog,'%')
        while posi > -1:
          numi = string.atoi(dialog[posi+1:posi+2])
          dialog = dialog[:posi] + \
            self.translate(match.group(numi),gReflections) + \
            dialog[posi+2:]
          posi = string.find(dialog,'%')
    
        if dialog[-2:] == '?.': dialog = dialog[:-2] + '.'
        if dialog[-2:] == '??': dialog = dialog[:-2] + '?'               
        
        a=a+[dialog]
        csvfile = file('/Users/bambool/Documents/Eliza/regular.csv', 'wb')
        writer = csv.writer(csvfile)
        writer.writerow(a)
        csvfile.close()
 
       
        # we've got a response... stuff in reflected text where indicated
        pos = string.find(resp,'%')
        while pos > -1:
          num = string.atoi(resp[pos+1:pos+2])
          resp = resp[:pos] + \
            self.translate(match.group(num),gReflections) + \
            resp[pos+2:]
          pos = string.find(resp,'%')
        # fix munged punctuation at the end
        if resp[-2:] == '?.': resp = resp[:-2] + '.'
        if resp[-2:] == '??': resp = resp[:-2] + '?'
        
        return resp

#----------------------------------------------------------------------
# gReflections, a translation table used to convert things you say
#    into things the computer says back, e.g. "I am" --> "you are"
#----------------------------------------------------------------------
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
  "me"  : "you"
  
}

#--------------------------------please--------------------------------------
# gPats, the main response table.  Each element of the list is a
#  two-element list; the first is a regexp, and the second is a
#  list of possible responses, with group-macros labelled as
#  %1, %2, etc.  
#----------------------------------------------------------------------
gPats = [
#repeat
  [r'(.*)repeat the following for (.*) times(.*)',
  ["repeat %2 ["],["Okay, Let's start the repeat!      "]],

  [r'(.*)end the repeat(.*)',
  ["]"],["Okay, Let's end the repeat!     "]],

  [r'(.*)repeat (.*) for (.*) times(.*)',
  ["repeat %3 [%2]"],["Okay, Let's repeat %2 for %3 times!      "]],

  [r'(.*)Let (.*) be (.*) repeat (.*) times(.*)',
  ["to %2 repeat %4 [%3]"],["Okay, Let's make %2 to be %3 repeat %4 times!     "]],


#delete
  [r'(.*)the last step is wrong (.*)',
  ["delete last1"],["Okay, Let's delete the last command!     "]],

  [r'(.*)delete the last (.*) commands(.*)',
  ["delete last%2"],["Okay, Let's delete the last %2 commands!     "]],
  
#define

  [r'(.*)let (.*) be the following steps',
  ["to %2"],["Okay, Let's make %2 the following steps!    "]],

  [r'(.*)let (.*) be the these steps',
  ["to %2"],["Okay, Let's make %2 the following steps!    "]],

  [r'(.*)end (.*)',
  ["end"],["Okay, Let's make this the end of %2!      "]],

  [r'(.*)let this be the end of (.*)',
  ["end"],["Okay, Let's make this the end of %2!      "]],

  [r'(.*)let (.*) be the last (.*) commands',
  ["to %2 last %3 end"],["Okay, Let's make %2 the last %3 commands!    "]],

  [r'(.*)let (.*) be the last (.*) steps',
  ["to %2 last%3 end"],["Okay, Let's make %2 the last %3 steps!    "]],

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
  [r'(.*)Let the width be (.*)',
  ["setwidth %2"],["Okay, Let's make the width be %2!    "]],

  [r'(.*)make the width be (.*)',
  ["setwidth %2"],["Okay, Let's make the width be %2!    "]],
  
  [r'(.*)Let the width of the (.*) be (.*)',
  ["setwidth %3"],["Okay, Let's make the width of the %2 be %3!    "]],

  [r'(.*)Let the width of the (.*) be (.*)',
  ["setwidth %3"],["Okay, Let's make the width of the %2 be %3!    "]],

#color
  [r'(.*)let the color (.*) blue',
  ["setcolor 1"],["Okay, Let's make the color blue!    "]],

  [r'(.*)let the color of the (.*) be blue',
  ["setcolor 1"],["Okay, Let's make the color of the %2 be blue    "]],

  [r'(.*)the (.*) to be blue',
  ["setcolor 1"],["Okay, Let's make the color blue!    "]],

  [r'(.*)the (.*) be blue',
  ["setcolor 1"],["Okay, Let's make the color blue!    "]],
  
#penup pendown
  [r'(.*)let the pen up(.*)',
  ["penup"],["Okay, Let's make the pen off the paper    "]],

  [r'(.*)let the pen up(.*)',
  ["pendown"],["Okay, Let's make the pen back on the paper    "]],

  [r'(.*)let (.*) be (.*)',
  ["make \"%2 %3"],["Okay, let's make %2 be 3%     "]],

#forward
  [r'(.*)forward the line with length (.*)',
  ["fd %2"],["Okay, Let's draw a line with length %2!     "]],

  [r'(.*)draw a line (.*) units long',
  ["fd %2"],["Okay, Let's draw a line with length %2!     "]],

  [r'(.*)draw a line (.*) units in length',
  ["fd %2"],["Okay, Let's draw a line with length %2!     "]],

  [r'(.*)forward a line (.*) units long',
  ["fd %2"],["Okay, Let's draw a line with length %2!     "]],

  [r'(.*)forward a line (.*) units in length',
  ["fd %2"],["Okay, Let's draw a line with length %2!     "]],

#back
  [r'(.*)draw back a line with length (.*)',
  ["back %2"],["Okay, Let's draw back a line with length %2!      "]],

#turn
  [r'(.*)turn left',
  ["left 90"],["Okay, Let's turn left!     "]],

  [r'(.*)turn left (.*) degree',
  ["left %2"],["Okay, Let's turn left %2 degree[s]"]],

  [r'(.*)rotate (.*) degree clockwise',
  ["right %2"],["Okay, Let's rotate %2 degree clockwise     "]],

  [r'(.*)turn right',
  ["right 90"],["Okay, Let's turn right!     "]],

  [r'(.*)turn right (.*) degree',
  ["right %2"],["Okay, Let's turn right %2 degree"]],

  [r'(.*)rotate (.*) degree anticlockwise',
  ["left %2"],["Okay, Let's rotate %2 degree anticlockwise     "]],


   ]


  


#----------------------------------------------------------------------
#  command_interface
#----------------------------------------------------------------------
def command_interface():
  print "Therapist\n---------"
  print "Talk to the program by typing in plain English, using normal upper-"
  print 'and lower-case letters and punctuation.  Enter "quit" when done.'
  print '='*72
  print "Hello.  What do you want"
  
  s = ""
  
  therapist = eliza();
  while s != "quit":
    try: s = raw_input(">")
    except EOFError:
      s = "quit"
      print s
      k=k+1
    while s[-1] in "!.": s = s[:-1]
    
    print therapist.respond(s)
    

if __name__ == "__main__":
  a=[]
  command_interface()
  
  
    
