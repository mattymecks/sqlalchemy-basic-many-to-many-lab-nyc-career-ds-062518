from models import *


def return_christian_bales_roles(session):
    bale = session.query(Actor).filter(Actor.name == "Christian Bale").one().roles
    return bale
    # Return a list of Christian Bale role instances

def return_catwoman_actors(session):
    catwomen = session.query(Role).filter(Role.character == "Catwoman").one().actors
    return catwomen
    #  Return a list of actor instances that have played Catwoman

def return_number_of_batman_actors(session):
    batmen = session.query(Role).filter(Role.character == "Batman").one().actors
    num_of_batmen = len(batmen)
    return num_of_batmen
    # Return the number of actors that have played Batman
