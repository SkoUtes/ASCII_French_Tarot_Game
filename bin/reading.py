#!/usr/plocal/bin/python3
import tarotCards
from tarotCards import *
import random as random

#########################################################################
#########################################################################
def r_fool():
    cFool()
    print("""The Fool signifies the start of a journey or a new chapter
in life. While the future is unknown and nothing is 
guaranteed, it is important that you remember that the
uncertain is where opportunities lie, and to not be
troubled by what might go wrong. Be willing to take the
risks and be open-minded to new experiences. Nothing
ventured, nothing gained.
    """)
def r_magician():
    cMagician()
    print("""The Magician is a symbol of willpower and the mind. To make
changes in the world outside, you must have control over
your inner world. Remember that you know yourself best and
what you need for success. If you can strengthen your will 
and mast your thoughts then good things are sure to
follow.
    """)
def r_priestess():
    cPriestess()
    print("""The High Priestess is an image of hidden knowledge and
intuition. You don't need all the answers to make
a decision. If you can't make sense of a problem follow your
instincts and go with your best guess. There are many
things that will remain concealed to you. To avoid being
deceived it's most important to trust in yourself.
    """)
def r_empress():
    cEmpress()
    print("""The Empress is feminine power, nature, and creativity. Be
kind to yourself and nurture your creative pursuits.
Whether you are creating art, a new life, or tending to
family, remember that time and care will be the best policy
for a positive outcome.
    """)
def r_emperor():
    cEmperor()
    print("""The Emperor is a symbol of authority and masculinity. To
build a stable life takes hard work and discipline. Stay
organized and lay out a plan for success. While too much
order can be a bad thing, structure is the foundation for
success. Focus on your core strengths and build a strong
base in your life.
    """)
def r_hierophant():
    cHierophant()
    print("""The Hierophant is tradition, dogma, and obedience. The road
most travelled is sometimes the best one. If you're having
trouble finding a path, conventional wisdom and advice can
be a reliable guide. Listen to people that you can trust
and follow rules that will take you in the right direction.
    """)
def r_lovers():
    cLovers()
    print("""The lovers are an image of partnerships and relationships.
This could mean any sort of relationship whether personal
or for business. Consider your options wisely and take care
when dealing with people. Talk less about yourself and
focus instead on what you can do for others. Make up your
mind about who and what is truly important in your life.
    """)
def r_chariot():
    cChariot()
    print("""The Chariot is a symbol of triumph, control, and direction.
Take action in your life and move forward with confidence.
Focus on your ultimate goals and don't be bothered by the
detours. Carry out your plans and be bold in your approach.
    """)
def r_strength():
    cStrength()
    print("""Strength is bravery and self-control. If you want to
overcome your problems then focus on your inner strength.
Stay calm and be patient. Remember that it's the marathon
and not the hundred-meter dash.
    """)
def r_hermit():
    cHermit()
    print("""The Hermit is a seeker of inner knowledge. To understand who you
are and the steps you need to take is a task that will always fall on you
in the end. To do this one only needs to spend time alone. Make peace with
your fears and be your authentic self.
    """)
def r_wheel():
    cWheel()
    print("""The Wheel of Fortune is about luck and major changes. Things may
be moving in your favor, but the opposite may be true as well. Be aware of
any opportunities that come your way and weigh your options wisely. Make
your long-term happiness a priority and be wary of bad decisions.
    """)
def r_justice():
    cJustice()
    print("""Justice is about balance and consequences. Whether for you or for
others, there will likely come a time when justice is served. This card 
could be about something you've done that you ought to think about and do
right by. Or it could mean justice for others and what has been done to
them. Consider accounting for your actions and make sure others are
treated fairly as best you can.
    """)
def r_hanged():
    cHanged()
    print("""The hanged man is a symbol of sacrifice, surrender, and letting
go. If things aren't going your way then it's okay to take a step backwards
before moving on. It might be necessary to sacrifice your time and
productivity to reassess your situation. Failure is the greatest teacher.
    """)
def r_death():
    cDeath()
    print("""Death is the end of a cycle and transformation. This is perhaps
the most misunderstood and intimidating card. But it's meaning is death in
the abstract. Things in your life will end, and that can be scary, but you
should welcome the changes that come from this. Perhaps it is your old
habits that need to die, or your bad relationships with others. If it's
time for something to end then don't fight it, let things take their
natural course and be optimistic about new things that will come later.
    """)
def r_temperance():
    cTemperance()
    print("""Temperance symbolizes moderation, balance, and patience. Don't
sweat the small things and seek to balance a humble existence. Everything
in moderation, including moderation. It's okay to binge on things
sometimes, but you must maintain a balanced lifestyle and keep your eyes on
what's really important.
    """)
def r_devil():
    cDevil()
    print("""The Devil is materialism, addiction, negativity, and excess. If
you are feeling trapped or unfulfilled then you should reconsider what you
value. The world is full of distraction and pleasures but indulging to
excess is not good for your physical and mental health. Negative
experiences and people are remarkably addictive. It's important to
prioritize your health and slowly but surely replace your bad habits with
good ones.
    """)
def r_tower():
    cTower()
    print("""The Tower is chaos, disruption, and revolution. Disaster can
strike when nobody expects it, and it can happen to anyone. If things are
falling apart sometimes there's nothing you can do don't exhaust yourself
trying to fight it. When things settle down then it's also an opportunity
to start from scratch and build it better this time. Learn from your
mistakes and become better for them.
    """)
def r_star():
    cStar()
    print("""The star represents hope, well being, healing, and success. You've
made it this far on your own and if you haven't lost hope then that's
a good sign. Things will work out if you just maintain your efforts and
have faith in yourself. You may have suffered greatly in the past, but in
a way your pains are also your greatest treasures and can only make life
easier in the future.
    """)
def r_moon():
    cMoon()
    print("""The Moon is the unknown and deception. There is much that we will
never understand and the right path may be hidden to you. Focus on what 
you do know and be aware of situations you should avoid. If you're anxious
about the future or others then do what you can to ground yourself. If it
means leaving a situation or a job you don't like then perhaps it's time to
consider doing so.
    """)
def r_sun():
    cSun()
    print("""The Sun symbolizes joy, happiness, and energy. There's always
something to be grateful for and you should always keep that in mind. If
things are working out then you should feel confident and content. Life
isn't always perfect but hold on to what you have and make the best of it.
    """)
def r_judgement():
    cJudgement()
    print("""Judgement is a reawakening and transformation. You should reflect
on what you've done so far and judge your actions honestly. We are all
faced with choices and sometimes we make the wrong one. Evaluating your
mistakes and triumphs is how we grow as people.
    """)
def r_world():
    cWorld()
    print("""The World is completion, succession, and the universe. There is no
doubt about the cyclicality of life and the universe. Patterns are always
arising and repeating, and our lives our not indepent of this. Perhaps
everything is coming full-circle and you are completing a major project or
milestone. Recognize your true self as part of a much greater pattern and
community. You have a responsibility to make the world a better place as
you yourself are not separate from it, and strive to replace the old
out-dated patterns with new and better ones for everyones benefit.
    """)

#####################################################################################
#####################################################################################

def reading():
    while True:
        a = random.randint(0,21)
        if a == 0:
            r_fool()
        elif a == 1:
            r_magician()
        elif a == 2:
            r_priestess()
        elif a == 3:
            r_empress()
        elif a == 4:
            r_emperor()
        elif a == 5:
            r_hierophant()
        elif a == 6:
            r_lovers()
        elif a == 7:
            r_chariot()
        elif a == 8:
            r_strength()
        elif a == 9:
            r_hermit()
        elif a == 10:
            r_wheel()
        elif a == 11:
            r_justice()
        elif a == 12:
            r_hanged()
        elif a == 13:
            r_death()
        elif a == 14:
            r_temperance()
        elif a == 15:
            r_devil()
        elif a == 16:
            r_tower()
        elif a == 17:
            r_star()
        elif a == 18:
            r_moon()
        elif a == 19:
            r_sun()
        elif a == 20:
            r_judgement()
        elif a == 21:
            r_world()
        contin = input("Press Enter to continue: ")
        b = random.randint(0,21)
        while b == a:
            b = random.randint(0,21)
        if b == 0:
            r_fool()
        elif b == 1:
            r_magician()
        elif b == 2:
            r_priestess()
        elif b == 3:
            r_empress()
        elif b == 4:
            r_emperor()
        elif b == 5:
            r_hierophant()
        elif b == 6:
            r_lovers()
        elif b == 7:
            r_chariot()
        elif b == 8:
            r_strength()
        elif b == 9:
            r_hermit()
        elif b == 10:
            r_wheel()
        elif b == 11:
            r_justice()
        elif b == 12:
            r_hanged()
        elif b == 13:
            r_death()
        elif b == 14:
            r_temperance()
        elif b == 15:
            r_devil()
        elif b == 16:
            r_tower()
        elif b == 17:
            r_star()
        elif b == 18:
            r_moon()
        elif b == 19:
            r_sun()
        elif b == 20:
            r_judgement()
        elif b == 21:
            r_world()
        contin = input("Press Enter to continue: ")
        c = random.randint(0,21)
        while c == a or c == b:
            c = random.randint(0,21)
        if c == 0:
            r_fool()
        elif c == 1:
            r_magician()
        elif c == 2:
            r_priestess()
        elif c == 3:
            r_empress()
        elif c == 4:
            r_emperor()
        elif c == 5:
            r_hierophant()
        elif c == 6:
            r_lovers()
        elif c == 7:
            r_chariot()
        elif c == 8:
            r_strength()
        elif c == 9:
            r_hermit()
        elif c == 10:
            r_wheel()
        elif c == 11:
            r_justice()
        elif c == 12:
            r_hanged()
        elif c == 13:
            r_death()
        elif c == 14:
            r_temperance()
        elif c == 15:
            r_devil()
        elif c == 16:
            r_tower()
        elif c == 17:
            r_star()
        elif c == 18:
            r_moon()
        elif c == 19:
            r_sun()
        elif c == 20:
            r_judgement()
        elif c == 21:
            r_world()
        break

