from urllib import response
import numpy as np
import os
import cv2
from tensorflow import keras
from PIL import Image
import requests
import random


class Model: 
    def load_model(self):
        model = keras.models.load_model('PokeModel.h5')
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model

    def predict(self, model, url):
        data = []
        url = url
        filename = url.split("/")[-1]
        
        if not self.is_valid_format(filename):
            supported_formats = 'Formatos suportados: jpg, jpeg, png, etc.'
            return f"{random.choice(self.rude_responses)} `" + supported_formats + "`"

        self.save_image(url, filename)

        try: 
            data.append(self.prepare_image(filename))
        except:
            print("Error preparing image")

        result, percentage = self.test_image(data, model)
        response = f"{self.random_response()} `" + self.classes[result[0]] + " | certeza: " +  str(np.round(percentage, 2)) + "%"+ "`"
        return response
         
    def save_image(self, url, filename):
        img_data = requests.get(url).content
        with open(filename, 'wb') as handler:
            handler.write(img_data)

    def prepare_image(self, filename):
        image = cv2.imread(filename)
        image_fromarray = Image.fromarray(image, 'RGB')
        resize_image = image_fromarray.resize((30, 30))
        os.remove(filename)
        return np.array(resize_image)
    
    def test_image(self, data, model):
        test = np.array(data) / 255

        pred = model.predict(test)
        classes_x=np.argmax(pred,axis=1)
        return classes_x, np.amax(pred) * 100

    def is_valid_format(self, filename): 
        format = filename.split(".")[-1]
        return format == "jpg" or format == 'png' or format == "jpeg"
    
 
    
    rude_responses = [
        'Parece que alguém comprou a carteira.',
        'Manda a mãe para ver se classifica.',
        'Leio, não nego. Classifico se eu quiser..',
        'Você não vai me pegar tão fácil.',
        'Que feio, mandando imagem nada a ver para tirar nota de aluno'
    ]

   

    classes = { 0:'Abra',
    1:'Aerodactyl',
    2:'Alakazam',
    3:'Alolan Sandslash',
    4:'Arbok',
    5:'Arcanine',
    6:'Articuno',
    7:'Beedrill',
    8:'Bellsprout',
    9:'Blastoise',
    10:'Bulbasaur',
    11:'Butterfree',
    12:'Caterpie',
    13:'Chansey',
    14:'Charizard',
    15:'Charmander',
    16:'Charmeleon',
    17:'Clefable',
    18:'Clefairy',
    19:'Cloyster',
    20:'Cubone',
    21:'Dewgong',
    22:'Diglett',
    23:'Ditto',
    24:'Dodrio',
    25:'Doduo',
    26:'Dragonair',
    27:'Dragonite',
    28:'Dratini',
    29:'Drowzee',
    30:'Dugtrio',
    31:'Eevee',
    32:'Ekans',
    33:'Electabuzz',
    34:'Electrode',
    35:'Exeggcute',
    36:'Exeggutor',
    37:'Farfetchd',
    38:'Fearow',
    39:'Flareon',
    40:'Gastly',
    41:'Gengar',
    42:'Geodude',
    43:'Gloom',
    44:'Golbat',
    45:'Goldeen',
    46:'Golduck',
    47:'Golem',
    48:'Graveler',
    49:'Grimer',
    50:'Growlithe',
    51:'Gyarados',
    52:'Haunter',
    53:'Hitmonchan',
    54:'Hitmonlee',
    55:'Horsea',
    56:'Hypno',
    57:'Ivysaur',
    58:'Jigglypuff',
    59:'Jolteon',
    60:'Jynx',
    61:'Kabuto',
    62:'Kabutops',
    63:'Kadabra',
    64:'Kakuna',
    65:'Kangaskhan',
    66:'Kingler',
    67:'Koffing',
    68:'Krabby',
    69:'Lapras',
    70:'Lickitung',
    71:'Machamp',
    72:'Machoke',
    73:'Machop',
    74:'Magikarp',
    75:'Magmar',
    76:'Magnemite',
    77:'Magneton',
    78:'Mankey',
    79:'Marowak',
    80:'Meowth',
    81:'Metapod',
    82:'Mew',
    83:'Mewtwo',
    84:'Moltres',
    85:'MrMime',
    86:'Muk',
    87:'Nidoking',
    88:'Nidoqueen',
    89:'Nidorina',
    90:'Nidorino',
    91:'Ninetales',
    92:'Oddish',
    93:'Omanyte',
    94:'Omastar',
    95:'Onix',
    96:'Paras',
    97:'Parasect',
    98:'Persian',
    99:'Pidgeot',
    100:'Pidgeotto',
    101:'Pidgey',
    102:'Pikachu',
    103:'Pinsir',
    104:'Poliwag',
    105:'Poliwhirl',
    106:'Poliwrath',
    107:'Ponyta',
    108:'Porygon',
    109:'Primeape',
    110:'Psyduck',
    111:'Raichu',
    112:'Rapidash',
    113:'Raticate',
    114:'Rattata',
    115:'Rhydon',
    116:'Rhyhorn',
    117:'Sandshrew',
    118:'Sandslash',
    119:'Scyther',
    120:'Seadra',
    121:'Seaking',
    122:'Seel',
    123:'Shellder',
    124:'Slowbro',
    125:'Slowpoke',
    126:'Snorlax',
    127:'Spearow',
    128:'Squirtle',
    129:'Starmie',
    130:'Staryu',
    131:'Tangela',
    132:'Tauros',
    133:'Tentacool',
    134:'Tentacruel',
    135:'Vaporeon',
    136:'Venomoth',
    137:'Venonat',
    138:'Venusaur',
    139:'Victreebel',
    140:'Vileplume',
    141:'Voltorb',
    142:'Vulpix',
    143:'Wartortle',
    144:'Weedle',
    145:'Weepinbell',
    146:'Weezing',
    147:'Wigglytuff',
    148:'Zapdos',
    149:'Zubat',

            }   