'''
eliza.py simulates a therapist

it works by looking for keywords and sending back
randomly chosen responses.
'''
from random import choice


def talk_with_eliza():
    ''' main loop - prompt user and generate responses '''
    user_input = input("eliza: How are you doing today?\n> ")
    while user_input != 'goodbye':
        words = user_input.split()
        computer_response=generate_response(words)
        user_input = input('eliza: '+computer_response+"\n> ")
    print('bye')

def intersects(list1, list2):
    ''' return true if list1 and list2 contain a common element '''
    for word in list1:
        if word in list2:
            return True
    return False

def generate_response(user_words):
    ''' generates random responses based on the user's response '''
    if intersects(user_words,sad_words):
        return choice(sad_responses)
    elif len(user_words)<2:
        return choice(short_responses)
    else:
        return choice(generic_responses)

sad_words = "sad depressed blue down".split()
sad_responses = [
    "I'm sorry to hear that.",
    "Who can you talk to when you are sad?",
    "What is making you feel sad?"]

short_responses =[
    "You'll feel better if you open up to me.",
    "You don't seem to want to talk today",
    "Are you feeling upset today?"
]
generic_responses=[
    "Hmmm. Please go on.",
    "That's interesting.",
    "How is your relationship with your mother?",
    "When was the last time you spoke to your parents?",
    "Thanks for sharing, please tell me more."
]

talk_with_eliza()
