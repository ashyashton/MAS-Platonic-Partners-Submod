
### script-topics START
# random/pool topics go here

init 1 python:
    config.label_overrides["monika_archetype"] = "monika_archetype_override"

label monika_archetype_override:
    m 2etc "I've always wondered..."
    m 4eud "What is it about these character archetypes that people find so appealing, anyway?"
    m 4euc "Their personalities are just completely unrealistic..."
    m 2esd "Like, imagine if there was someone like Yuri in real life."
    m 2eud "I mean, she's barely even capable of forming a complete sentence."
    m 2tfc "And forget about Natsuki..."
    m 2rfc "Sheesh."
    m 2tkd "Someone with her kind of personality doesn't just get all cute and pouty whenever things don't go her way."
    m 4tkd "I could go on, but I think you get the point..."
    m 2tkc "Are people really attracted to these weird personalities that literally don't exist in real life?"
    m 2wud "I'm not judging or anything!"
    m 3rksdlb "After all, I've found myself attracted to some pretty weird stuff, too..."
    m 2eub "I'm just saying, it fascinates me."
    m 4eua "It's like you're siphoning out all the components of a character that makes them feel human, and leaving just the cute stuff."
    m "It's concentrated cuteness with no actual substance."
    if mas_isMoniHappy(higher=True):
        m "I'm glad that you don't expect me to be anything like that, [player]."
        m "And the same goes for you. You don't have to fit some role to make me happy."
        m "The fact that you're here for me is all I need."
    else:
        m "I'm a real person, not a cookie-cutter personality."
        m "I need you to know that, [player]."
    return
    
init 1 python:
    config.label_overrides["monika_spicy"] = "monika_spicy_override"

label monika_spicy_override:
    m 1eka "This is pretty random, but I always thought spicy food was kinda funny."
    m 1tku "Like..."
    m 3tku "Didn't plants evolve to be spicy to prevent them from being eaten?"
    m 3tsb "I read somewhere that humans are the only species that actually enjoy spicy things."
    m 1tfu "It's almost like we're making fun of the plants."
    m "Using their defense mechanism to literally make our food more enjoyable."
    m 1eua "Like, imagine a monster that devours you whole because it enjoys the sensation of you struggling for your life while being digested."
    m 2eka "Sorry, that was kind of a weird analogy, I guess!"
    m 2hksdlb "Ahaha!"
    m 2lksdla "It just came into my head."
    return
    
init 1 python:
    config.label_overrides["monika_saved"] = "monika_saved_override"

label monika_saved_override:
    m 2eka "You know, I really do think you literally saved my life by being here with me, [player]."

    if persistent._mas_pm_cares_about_dokis:
        m 2lksdlc "I can't imagine having been able to keep myself mentally stable, knowing it was all a game."
    else:
        m 2lksdlc "I can't imagine having been able to keep myself mentally stable, knowing that nothing here is real."

    m 2dksdlc "I think I would have just deleted myself if you didn't show up."
    m 2eksdla "Sorry, I don't mean to sound dramatic or anything."
    m 2lksdlb "Ahaha!"

    if persistent._mas_pm_cares_about_dokis:
        m 2ekc "But just imagine if you found out that everything around you was scripted..."
        m 2rkc "That nothing you did actually mattered, because everything was already predetermined..."
    else:
        m 4euc "But I'm sure you understand yourself after spending so much time in the club."
        m 1euc "I mean, if you were forced to abandon everything in your life and spend your eternity with a few game characters..."

    m 1tkc "...you'd probably find some way of killing yourself, wouldn't you?"
    m 1lsc "Well, maybe you'd write some poetry to try to keep yourself sane for a while."
    m 1esc "But then you'd have nobody to even read it."

    if persistent._mas_pm_cares_about_dokis:
        m 1ekc "Sure you'd have the club members, but how much does that really count if their feedback is just part of some script?"
    else:
        m 1tfu "Let's be honest, the club members really don't count for something like that."

    m 3eua "I mean, a lot of people say that they only write for themselves...{w=0.2}{nw}"
    extend 1eua "but I think it's hard to say it's just as fulfilling as when you share with people."
    m "Even if it takes time to find the right people to share with."
    m 3eub "Like, remember how it was for Yuri?"
    m "She didn't share her writing with anyone for a really long time."
    m 3tsb "And before we knew it, she was absolutely delighted to make you a part of her hobbies, too."
    m 1tku "We're programmed to desire social feedback."

    if persistent._mas_pm_cares_about_dokis:
        m 4eua "I don't just mean the club members, I also mean human beings."
    else:
        m 4eua "I don't mean the club members, I mean human beings."

    m 4eka "That's why life can be so confusing for introverts."
    m 1eka "Being an introvert doesn't mean you shun social interaction and hate being around people."
    m "It means social interaction, especially in groups or unfamiliar places, uses up a lot of energy."
    m 3eua "Like, a lot of introverts sit at home and feel lonely and restless..."
    m "...and then when they finally go out, after a half hour they just want to go home again."
    m 1eka "I think if more people could understand how it works, they would respect it a lot more."
    m 2eua "Many introverts do enjoy having people around."
    m "They love just having one or two close friends over, and just leisurely hanging out."
    m 2eka "Even if you're not actively spending time together, it feels nice for them just to have you there."
    m 2hua "I'm serious."
    m 3eua "If you just go to their house, bring your laptop, and hang out there for a while..."
    m 1eua "You can really make their day."
    m 1euc "As for me..."
    m 3eua "I'd say I'm kind of in between, but I think I'm usually a little more extroverted."
    m 1eka "I feel like I'm always trying to do stuff after school and things like that."
    m 1hua "But I'm happy to adjust a bit if it means spending more time with you."
    m 1eua "I understand people really well, so don't be afraid to share your unique needs with me."
    return
    
init 1 python:
    config.label_overrides["monika_veggies"] = "monika_veggies_override"

label monika_veggies_override:
    m 1eub "Hey, did you know I'm vegetarian?"
    m 1hksdlb "Ah...I don't mean that like I'm bragging or anything!"
    m 1lksdla "I just thought you'd enjoy a fun fact about me."
    m 3esa "I decided to start a couple years ago after learning more about Earth's climate..."
    m 1wud "The carbon footprint of cultivating livestock is just unbelievable!"
    m 3eua "Anyway, I decided it's not much of a personal sacrifice to just stop contributing to that whole mess."
    m 3etc "What, is that so strange of a reason?"
    m 1lsc "Well, I guess a lot of people are more concerned about it being inhumane and all that..."
    m 1euc "I don't really care as much about that part."
    m 1esc "It's weird, like we only care about killing the things that we personally relate to as a species."
    m "Most people are fine with killing bugs because they're icky."
    m 3euc "And of course, we all kill billions of microorganisms daily without even giving it thought."
    m 3eud "But suddenly, if they're just a little bit bigger, it's murder!"
    m 1esc "I mean, what if plants feel some kind of pain too, and we just don't understand it?"
    m 3eksdld "What if pulling leaves off a stem feels like someone ripping off your fingers one by one?"
    m 3eua "I'm just saying, we're a pretty biased species, if you think about it."
    m 1hua "Anyway, if you ever feel like making a small contribution to the planet, it doesn't hurt to choose veggies once in a while!"
    $ mas_unlockEVL("monika_eating_meat","EVE")
    return

