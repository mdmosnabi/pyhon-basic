import random

status = {
    'player1':{
        'guti1':0,
        'guti2':0,
        'guti3':0,
        'guti4':0,
    },
    'player2':{
        'guti1':0,
        'guti2':0,
        'guti3':0,
        'guti4':0,
    },
    'player3':{
        'guti1':0,
        'guti2':0,
        'guti3':0,
        'guti4':0,
    },
    'player4':{
        'guti1':0,
        'guti2':0,
        'guti3':0,
        'guti4':0,
    },
}

#================= app functions ===============

def checker():
    for i in range(1,5):
        a= status[f'player{i}'].values()
        if sum(a) > 80:
            return True

def remover(player,number):
    for i in range(1,5):
        if player == i:
            continue
        for guti in range(1,5):
            a = status[f'player{i}'][f'guti{guti}']
            if a%2 == 0 or a >= 20:
                continue
            if a == number:
               status[f'player{i}'][f'guti{guti}'] = 0 
# ================ end app functions ====================

#============== update functuons ========================

def update(next):
    if checker():
        return 'break'
    random_number = random.randint(1,6)
    inputs = int(input(f'payler{next+1} your number is {random_number} enter a guti number: '))

    if inputs <= 0 or inputs > 4:
        return 'continue'
    
    if status[f'player{next+1}'][f'guti{inputs}'] < 20:
        status[f'player{next+1}'][f'guti{inputs}'] += random_number
        remover(next+1,status[f'player{next+1}'][f'guti{inputs}'])

    result = f"""
    player1 ->guti({status['player1']['guti1']})guti({status['player1']['guti2']})guti({status['player1']['guti3']})guti({status['player1']['guti4']})
    player2 ->guti({status['player2']['guti1']})guti({status['player2']['guti2']})guti({status['player2']['guti3']})guti({status['player2']['guti4']})
    player3 ->guti({status['player3']['guti1']})guti({status['player3']['guti2']})guti({status['player3']['guti3']})guti({status['player3']['guti4']})
    player4 ->guti({status['player4']['guti1']})guti({status['player4']['guti2']})guti({status['player4']['guti3']})guti({status['player4']['guti4']})

    """

    print(result)

# ====================== infinity loop ==============================
i=4
while True:
    i %= 4
    a = update(i)
    if a =='break':
        break
    elif a == 'continue':
        print('You should select number between 1-4')
    i+=1
