import random

R_EATING ="I don't like eating anything, because I can't eat as I'm a bot obviously!  "

def unknow():
    response = ['Could you please re-phrase that?',
                "...",
                "sorry, not ablew to process that",
                "What does that mean?",
                "Sounds about right"][random.randrange(5)]
                

    return response