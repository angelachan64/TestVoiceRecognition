#----------------------------------------------------------------------
#  PiE-Programming in Eliza
#  Author: Xiao Liu, Dinghao Wu
#  College of Information Sciences and Technologies
#  The Pennsylvania State University
#  Based on eliza.py
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
import turtle
import rules
import speech_recognition as sr
import text2int
import pyttsx


class eliza:
  global gPats,gReflections

  gPats=rules.gPats
  gReflections=rules.gReflections

   
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
    # find a match among keys
    for i in range(0,len(self.keys)):
      match = self.keys[i].match(str)
      if match:
        # found a match ... stuff with corresponding value
        # chosen randomly from among the available options
        value= random.choice(self.values[i])
        dialog= random.choice(self.dialog[i])
        resp = value

        posi = string.find(dialog,'%')
        while posi > -1:
          numi = string.atoi(dialog[posi+1:posi+2])
            
          dialog = dialog[:posi] + \
            self.translate(match.group(numi),gReflections) + \
            dialog[posi+2:]
          posi = string.find(dialog,'%')
    
        if dialog[-2:] == '?.': dialog = dialog[:-2] + '.'
        if dialog[-2:] == '??': dialog = dialog[:-2] + '?'               
        
       
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
        
        return [resp,dialog]

#----------------------------------------------------------------------
#  To record the wrong case taken in PiE  
#----------------------------------------------------------------------

def Wrongcase(s):
    print "Can you say in another way?"
    
    # This will create a new file or **overwrite an existing file**.
    f2 = open('wrong.txt','r+')
    f2.read()
    f2.write(s)
    f2.write('\n')
    f2.close()

#----------------------------------------------------------------------
#  Six test cases
#----------------------------------------------------------------------

def task_selection():
   turtle.shape("turtle")
   # turtle.seth(270)
   turtle.pencolor("Yellow")
   turtle.pensize(10)


   turtle.bgpic("test/statement.gif")
   # turtle.bgpic("test/circle_loop.gif")
   # turtle.bgpic("test/function_loop_1.gif")
   # turtle.bgpic("test/function_loop_2.gif")
   # turtle.bgpic("test/function_loop_3.gif")
   # turtle.bgpic("test/function_loop_4.gif")


#----------------------------------------------------------------------
#  command_interface
#----------------------------------------------------------------------
def command_interface():
  global fundict
  fundict={}
  global New,n,d
  task_selection()
  a=[]
  program=[]
  s = ""
  test=""
  global loop
  
  therapist = eliza();
 
  program=[]
  Omit=0

  
  while s != "quit":
    try:
      s = raw_input(">")
      # print "SPEAK CLEARLY AND LOUDLY!"
      # r = sr.Recognizer(language = "en-GB")
      # with sr.Microphone() as source:                # use the default microphone as the audio source
      #   audio = r.adjust_for_ambient_noise(source,duration=1)
      #   audio = r.listen(source)
      # s = r.recognize(audio)
      # s = text2int.convert(s)
      # print "Your Command is:" + s

      while s[-1] in "!.": s = s[:-1]

      if s=="quit":
        ts = turtle.getscreen()
        ts.getcanvas().postscript(file="duck.eps")
        # engine = pyttsx.init()
        # engine.say("Okay! Let's quit!")
        # engine.runAndWait()
        print "Okay! Let's quit!"
        print"Program Generated:"


        for item in New:
          if item!="":
            print item
        turtle.mainloop()
        sys.exit()

      if therapist.respond(s)[1]:
        # engine = pyttsx.init()
        # engine.say(therapist.respond(s)[0])
        # engine.runAndWait()
        print therapist.respond(s)[0]

        a.append(therapist.respond(s)[1])
        csvfile = file('regular.csv', 'wb+')
    
        writer = csv.writer(csvfile)
        writer.writerow(a)
        csvfile.close()
    
      New=TurnToList()
      exec(New[-1])
      # New=substitute(List)
      # printNew
    except LookupError:
      command_interface()
    except TypeError:
      Wrongcase(s)
      command_interface()
    except EOFError:
      command_interface()
      Wrongcase(s)
    except UnboundLocalError:
      command_interface()
      Wrongcase(s)
    except IndexError:
      command_interface()
      Wrongcase(s)
    except IndentationError:
      command_interface()
      Wrongcase(s)



    else:
      
      

      
      csvfile = file('program.csv', 'wb+')
    
      writer = csv.writer(csvfile)
      writer.writerow(New)
      csvfile.close()
      # if re.search(r"Omit",New[-1])==None:
      #   exec(New[-1])

      f2 = open('right.txt','r+')
      f2.read()
      f2.write(s+"::"+New[-1])
      f2.write('\n')
      f2.close()

def move_o(direction,number):
  if direction=="Omit":
    print"Please tell me the direction:"
  elif number=="Omit":
    print"Please tell me the length:"
  else:
    exec("turtle."+direction+"("+number+")")
  
def circle_o(number):
  if number=='Omit':
    print"Please tell me the radius:"
  else:
    exec("turtle.circle("+number+")")


def turn_o(direction,number):

  if direction=="Omit":
    print"Please tell me the direction:"
  elif number=="Omit":
    print"Please tell me the degree:"
  else:
    exec("turtle."+direction+"("+number+")")


def O_Num(n):
  exec(re.sub(r'Omit',n,New[-2]))
  print New[-2]

def O_Direction(d):
  
  exec(re.sub(r'Omit',d,New[-2]))     

# def O_commands(cmd):
#   o_cmd.append(cmd)

def polygon(sides,number):
    if number=='Omit':
        print"Please tell me the length:"
    else:
        for x in range(sides):
          turtle.forward(int(number))
          turtle.right(360/sides)

      
def diamond(degree,number):
    if number=='Omit':
        print"Please tell me the length:"
    else:
        for x in range(2):
          turtle.forward(int(number))
          turtle.right(degree)
          turtle.forward(int(number))
          turtle.right(180-degree)





def repeat(direction,number,times):
    if direction=='last':
        for i in range(int(times)):
            for t in range(int(number)):
              # print New
              if re.search(r"repeat", New[t-1-int(number)]):
                  exec(New[t-1-int(number)])
              else:
                  exec(New[t-1-int(number)])

def function(direction,number,name):
    global fundict
    length=len(New)
    funlist=[]
    if direction=='last':
      for i in range(int(number)):
        funlist.append(New[length-number-1+i])
      fundict[name]=funlist
      


def TurnToList():
       reader = csv.reader(file('regular.csv', 'rb'))
       NewList=[]
       for item in reader:
              NewList.append(item)
       NewList=NewList[0]
                           
       return NewList
 

   
def elizalogo():
    print "Eliza-Logo\n---------"
    print "Talk to the program by typing in plain English, using normal upper-"
    print 'and lower-case letters and punctuation.  Enter "quit" when done.'
    print '='*56
    print "Thanks for trying PiE. How can I help you"
    # o_cmd=[]
    # global o_cmd
    # engine = pyttsx.init()
    # engine.say("Thanks for trying PiE. How can I help you")
    # engine.runAndWait()
    command_interface()
    
    
    
'''
if __name__ == "__main__":
  a=[]
  command_interface()

'''  
  
    
