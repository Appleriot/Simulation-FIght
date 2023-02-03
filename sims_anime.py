import random

ki_blast = 10
finger_beam = 15
Kamehameha = 25
spirit_bomb = 50
bing_bang = 45
hakai = 100
graivty_bash = 60
normal_punch = 50
Consecutive_Normal_Punches = 20 * random.randint(3, 10)
seroius_punch = 400
Shockwave_Generation = 100

goku_health = 100
goku = {}
Saitama_health = 100
Saitama = {}
transform = 0

attacks = [ki_blast, finger_beam, Kamehameha, spirit_bomb, bing_bang]
special_attacks = [hakai,graivty_bash]
states = ['ultra_insiticst', 'Kaio_ken', 'Kaio_kenx20','super_sayian1', 'super_sayian2', 'super_sayian3', 'super_sayian_god', 'great_ape','super_sayian_blue','super_sayian_red']

Saitama_attacks = [normal_punch, Consecutive_Normal_Punches, seroius_punch, Shockwave_Generation]

def action_goku():
    global Saitama_health
    global goku_health
    global state
    global dodge
    global attack
    global transform
    dodge = random.randint(1, 6)
    attack = random.choice(attacks)
    number = random.randint(1, 10)
    if dodge == 5:
        saitama_attack = 0
    Saitama_health = Saitama_health - attack
    if number == 10:
        attack = random.choice(special_attacks)
    Saitama_health = Saitama_health - attack
    state = None
    special_number = random.randint(1, 25)
    if special_number == 25:
        state = random.choice(states)
        print(f'Goku went {state}')
        transform = transform+1
        if state == 'ultra_insiticst':
            goku_health = goku_health * 9
        if state == 'super_sayian1':
            goku_health = goku_health * 2
        if state == 'super_sayian2':
            goku_health = goku_health * 3
        if state == 'super_sayian3':
            goku_health = goku_health * 4
        if state == 'Kaio_ken':
            for attack in attacks:
                attack = attack * 1.5
        if state == 'Kaio_kenx20':
            for attack in attacks:
                attack = attack * 2
        if state == 'super_sayian_god':
            goku_health =  goku_health * 5
        if state == 'super_sayian_blue':
            goku_health = goku_health * 6
        if state == 'super_sayian_red':
            goku_health = goku_health * 7
        if state == 'great_ape':
            goku_health = goku_health * 1.5


def action_saitama():
    global goku_health
    global saitama_dodge
    saitama_dodge = random.randint(1,10)
    if saitama_dodge == 9:
        attack = 0
    saitama_attack = random.choice(Saitama_attacks)
    goku_health = goku_health - saitama_attack

goku_win = 0
saitama_win = 0

def run():
    global goku_win
    global saitama_win
    global goku_health
    global Saitama_health
    action_saitama()
    action_goku()

    if goku_health <= 0:
        goku_win = goku_win+1
        goku_health = 100
        Saitama_health = 100
        print('They took a little break.')
        state = None

    if Saitama_health <= 0:
        saitama_win = saitama_win+1
        goku_health = 100
        Saitama_health = 100
        print('They took a little break.')
        state = None

domation = False
while domation == False:
    run()
    print(f'Goku has won {goku_win} times.')
    print(f'Saimatma has won {saitama_win} times.')
if goku_win or saitama_win >= 1000:
    domation = True
