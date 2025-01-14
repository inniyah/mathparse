# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import math

"""
Utility methods for getting math word terms.
"""

BINARY_OPERATORS = {
    '^', '*', '/', '+', '-'
}

MATH_WORDS = {
        'DUT': {
        'unary_operators': {
            'kwadraat': '^ 2',
            'vierkantswortel van': 'sqrt',
            'wortel van': 'sqrt'
        },
        'binary_operators': {
            'plus': '+',
            'gedeeld door': '/',
            'min': '-',
            'maal': '*',
            'tot de macht': '^',
            'tot de': '^'
        },
        'numbers': {
            'nul': 0,
            'een': 1,
            'één': 1,
            'twee': 2,
            'drie': 3,
            'vier': 4,
            'vijf': 5,
            'zes': 6,
            'zeven': 7,
            'acht': 8,
            'negen': 9,
            'tien': 10,
            'elf': 11,
            'twaalf': 12,
            'dertien': 13,
            'veertien': 14,
            'vijftien': 15,
            'zestien': 16,
            'zeventien': 17,
            'achttien': 18,
            'negentien': 19,
            'twintig': 20,
            'dertig': 30,
            'veertig': 40,
            'vijftig': 50,
            'zestig': 60,
            'zeventig': 70,
            'tachtig': 80,
            'negentig': 90
        },
        'scales': {
            'honderd': 100,
            'duizend': 1000,
            'miljoen': 1000000,
            'miljard': 1000000000,
            'biljard': 1000000000000
        }
    },
    'ENG': {
        'unary_operators': {
            'squared': '^ 2',
            'cubed': '^ 3',
            'square root of': 'sqrt'
        },
        'binary_operators': {
            'plus': '+',
            'divided by': '/',
            'minus': '-',
            'times': '*',
            'to the power of': '^'
        },
        'numbers': {
            'zero': 0,
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9,
            'ten': 10,
            'eleven': 11,
            'twelve': 12,
            'thirteen': 13,
            'fourteen': 14,
            'fifteen': 15,
            'sixteen': 16,
            'seventeen': 17,
            'eighteen': 18,
            'nineteen': 19,
            'twenty': 20,
            'thirty': 30,
            'forty': 40,
            'fifty': 50,
            'sixty': 60,
            'seventy': 70,
            'eighty': 80,
            'ninety': 90
        },
        'scales': {
            'hundred': 100,
            'thousand': 1000,
            'million': 1000000,
            'billion': 1000000000,
            'trillion': 1000000000000
        }
    },
    'FRE': {
        'binary_operators': {
            'plus': '+',
            'divisé par': '/',
            'moins': '-',
            'fois': '*',
            'équarri': '^ 2',
            'en cubes': '^ 3',
            'à la puissance': '^'
        },
        'numbers': {
            'un': 1,
            'deux': 2,
            'trois': 3,
            'quatre': 4,
            'cinq': 5,
            'six': 6,
            'sept': 7,
            'huit': 8,
            'neuf': 9,
            'dix': 10,
            'onze': 11,
            'douze': 12,
            'treize': 13,
            'quatorze': 14,
            'quinze': 15,
            'seize': 16,
            'dix-sept': 17,
            'dix-huit': 18,
            'dix-neuf': 19,
            'vingt': 20,
            'trente': 30,
            'quarante': 40,
            'cinquante': 50,
            'soixante': 60,
            'soixante-dix': 70,
            'septante': 70,
            'quatre-vingts': 80,
            'huitante': 80,
            'quatre-vingt-dix': 90,
            'nonante': 90
        },
        'scales': {
            'cent': 100,
            'mille': 1000,
            'un million': 1000000,
            'un milliard': 1000000000,
            'billions de': 1000000000000
        }
    },
    'GER': {
        'binary_operators': {
            'plus': '+',
            'geteilt durch': '/',
            'geteilt': '/',
            'minus': '-',
            'mal': '*',
            'multipliziert mit': '*',
            'im Quadrat': '^ 2',
            'hoch zwei': '^ 2',
            'quadriert': '^ 2',
            'cubed': '^ 3',
            'hoch': '^'
        },
        'numbers': {
            'eins': 1,
            'zwei': 2,
            'drei': 3,
            'vier': 4,
            'fünf': 5,
            'sechs': 6,
            'sieben': 7,
            'acht': 8,
            'neun': 9,
            'zehn': 10,
            'elf': 11,
            'zwölf': 12,
            'dreizehn': 13,
            'vierzehn': 14,
            'fünfzehn': 15,
            'sechszehn': 16,
            'siebzehn': 17,
            'achtzehn': 18,
            'neunzehn': 19,
            'zwanzig': 20,
            'dreißig': 30,
            'vierzig': 40,
            'fünfzig': 50,
            'sechzig': 60,
            'siebzig': 70,
            'achtzig': 80,
            'neunzig': 90
        },
        'scales': {
            'hundert': 100,
            'tausend': 1000,
            'hunderttausend': 100000,
            'million': 1000000,
            'milliarde': 1000000000,
            'billion': 1000000000000
        }
    },
    'GRE': {
        'unary_operators': {
            'στο τετράγωνο': '^ 2',
            'στον κύβο': '^ 3',
            'τετραγωνική ρίζα του': 'sqrt'
        },
        'binary_operators': {
            'συν': '+', 'και': '+',
            'διά': '/',
            'πλην': '-',
            'επί': '*',
            'στην δύναμη του': '^',
            'εις την': '^'
        },
        'numbers': {
            'μηδέν': 0,
            'ένα': 1,
            'δύο': 2,
            'τρία': 3,
            'τέσσερα': 4,
            'πέντε': 5,
            'έξι': 6,
            'εφτά': 7,
            'οκτώ': 8, 'οχτώ': 8,
            'εννιά': 9, 'εννέα': 9,
            'δέκα': 10,
            'έντεκα': 11,
            'δώδεκα': 12,
            'δεκατρία': 13,
            'δεκατέσσερα': 14,
            'δεκαπέντε': 15,
            'δεκαέξι': 16,
            'δεκαεφτά': 17,
            'δεκαοκτώ': 18, 'δεκαοχτώ': 18,
            'δεκαεννιά': 19, 'δεκαεννέα': 19,
            'είκοσι': 20,
            'τριάντα': 30,
            'σαράντα': 40,
            'πενήντα': 50,
            'εξήντα': 60,
            'εβδομήντα': 70,
            'ογδόντα': 80,
            'ενενήντα': 90
        },
        'scales': {
            'εκατό': 100,
            'χίλια': 1000,
            'εκατομμύρια': 1000000, 'εκ.': 1000000,
            'δισεκατομμύρια': 1000000000,
            'δισ.': 1000000000, 'δις': 1000000000,
            'τρισεκατομμύρια': 1000000000000,
            'τρισ.': 1000000000000, 'τρις': 1000000000000
        }
    },
    'ITA': {
        'binary_operators': {
            'più': '+',
            'diviso': '/',
            'meno': '-',
            'per': '*',
            'al quadrato': '^ 2',
            'cubetti': '^ 3',
            'alla potenza di': '^'
        },
        'numbers': {
            'uno': 1,
            'due': 2,
            'tre': 3,
            'quattro': 4,
            'cinque': 5,
            'sei': 6,
            'sette': 7,
            'otto': 8,
            'nove': 9,
            'dieci': 10,
            'undici': 11,
            'dodici': 12,
            'tredici': 13,
            'quattordici': 14,
            'quindici': 15,
            'sedici': 16,
            'diciassette': 17,
            'diciotto': 18,
            'diciannove': 19,
            'venti': 20,
            'trenta': 30,
            'quaranta': 40,
            'cinquanta': 50,
            'sessanta': 60,
            'settanta': 70,
            'ottanta': 80,
            'novanta': 90
        },
        'scales': {
            'centinaia': 100,
            'migliaia': 1000,
            'milioni': 1000000,
            'miliardi': 1000000000,
            'bilioni': 1000000000000
        }
    },
    'MAR': {
        'binary_operators': {
            'बेरीज': '+',
            'भागाकार': '/',
            'वजाबाकी': '-',
            'गुणाकार': '*',
            '(संख्या)वर्ग': '^ 2',
            'छोटे': '^ 3',
            'गुण्या करण्यासाठी': '^'
        },
        'numbers': {
            'शून्य': '0',
            'एक': '१',
            'दोन': '२',
            'तीन': '३',
            'चार': '४',
            'पाच': '५',
            'सहा': '६',
            'सात': '७',
            'आठ': '८',
            'नऊ': '९',
            'दहा': '१०',
            'अकरा': '११',
            'बारा': '१२',
            'तेरा': '१३',
            'चौदा': '१४',
            'पंधरा': '१५',
            'सोळा': '१६',
            'सतरा': '१७',
            'अठरा': '१८',
            'एकोणीस': '१९',
            'वीस': '२०',
            'तीस': '३०',
            'चाळीस': '४०',
            'पन्नास': '५०',
            'साठ': '६०',
            'सत्तर': '७०',
            'ऐंशी': '८०',
            'नव्वद': '९०',
            'शंभर': '१००'
        },
        'scales': {
            'शंभर': 100,
            'हजार': 1000,
            'दशलक्ष': 1000000,
            'अब्ज': 1000000000,
            'खर्व': 1000000000000
        }
    },
    'RUS': {
        'binary_operators': {
            'плюс': '+',
            'разделить': '/',
            'деленное на': '/',
            'делить на': '/',
            'минус': '-',
            'вычесть': '-',
            'отнять': '-',
            'умножить': '*',
            'умноженное на': '*',
            'умножить на': '*',
            'квадрат': '^ 2',
            'в квадрате': '^ 2',
            'возведенный в куб': '^ 3',
            'степень': '^'
        },
        'numbers': {
            'один': 1,
            'два': 2,
            'три': 3,
            'четыре': 4,
            'пять': 5,
            'шесть': 6,
            'семь': 7,
            'восемь': 8,
            'девять': 9,
            'десять': 10,
            'одинадцать': 11,
            'двенадцать': 12,
            'тринадцать': 13,
            'четырнадцать': 14,
            'пятнадцать': 15,
            'шестнадцать': 16,
            'семнадцать': 17,
            'восемнадцать': 18,
            'девятнадцать': 19,
            'двадцать': 20,
            'тридцать': 30,
            'сорок': 40,
            'пятьдесят': 50,
            'шестьдесят': 60,
            'семьдесят': 70,
            'восемьдесят': 80,
            'девяносто': 90
        },
        'scales': {
            'сто': 100,
            'тысяч': 1000,
            'миллион': 1000000,
            'миллиард': 1000000000,
            'триллион': 1000000000000
        }
    },
    'POR': {
        'unary_operators': {
            'ao quadrado': '^ 2',
            'ao cubo': '^ 3',
            'raiz quadrada de': 'sqrt'
        },
        'binary_operators': {
            'mais': '+',
            'dividido por': '/',
            'menos': '-',
            'vezes': '*',
            'elevado à potência de': '^'
        },
        'numbers': {
            'zero': 0,
            'um': 1,
            'dois': 2,
            'três': 3,
            'quatro': 4,
            'cinco': 5,
            'seis': 6,
            'sete': 7,
            'oito': 8,
            'nove': 9,
            'dez': 10,
            'onze': 11,
            'doze': 12,
            'treze': 13,
            'quatorze': 14,
            'catorze': 14,
            'quinze': 15,
            'dezesseis': 16,
            'dezessete': 17,
            'dezoito': 18,
            'dezenove': 19,
            'vinte': 20,
            'trinta': 30,
            'quarenta': 40,
            'cinquenta': 50,
            'sessenta': 60,
            'setenta': 70,
            'oitenta': 80,
            'noventa': 90
        },
        'scales': {
            'cem': 100,
            'mil': 1000,
            'milhão': 1000000,
            'bilhão': 1000000000,
            'trilhão': 1000000000000
        }
    },
    'UKR': {
        'binary_operators': {
            'додати': '+',
            'розділити': '/',
            'поділити на': '/',
            'ділити на': '/',
            'мінус': '-',
            'відняти': '-',
            'відняти від': '-',
            'помножити': '*',
            'помножене на': '*',
            'помножити на': '*',
            'квадрат': '^ 2',
            'у квадраті': '^ 2',
            'зведений у куб': '^ 3',
            'ступінь': '^'
        },
        'numbers': {
            'один': 1,
            'два': 2,
            'три': 3,
            'чотири': 4,
            'п’ять': 5,
            'шість': 6,
            'сім': 7,
            'вісім': 8,
            'дев’ять': 9,
            'десять': 10,
            'одинадцять': 11,
            'дванадцять': 12,
            'тринадцять': 13,
            'чотирнадцять': 14,
            'п’ятнадцять': 15,
            'шістнадцять': 16,
            'сімнадцять': 17,
            'вісімнадцять': 18,
            'дев’ятнадцять': 19,
            'двадцять': 20,
            'тридцять': 30,
            'сорок': 40,
            'п’ятдесят': 50,
            'шістдесят': 60,
            'сімдесят': 70,
            'вісімдесят': 80,
            'дев’яносто': 90
        },
        'scales': {
            'сто': 100,
            'тисяча': 1000,
            'мільйон': 1000000,
            'мільярд': 1000000000,
            'трильйон': 1000000000000
        }
    },
    'ESP': {
        'unary_operators': {
            'al cuadrado': '^ 2',
            'al cubo': '^ 3',
            'raiz cuadrada de': 'sqrt'
        },
        'binary_operators': {
            'más': '+',
            'entre': '/',
            'menos': '-',
            'por': '*',
            'veces':'*',
            'elevado al': '^'
        },
        'numbers': {
            'cero': 0,
            'uno': 1,
            'dos': 2,
            'tres': 3,
            'cuatro': 4,
            'cinco': 5,
            'seis': 6,
            'siete': 7,
            'ocho': 8,
            'nueve': 9,
            'diez': 10,
            'once': 11,
            'doce': 12,
            'trece': 13,
            'catorce': 14,
            'quince': 15,
            'dieciséis': 16,
            'diecisiete': 17,
            'dieciocho': 18,
            'diecinueve': 19,
            'veinte': 20,
            'treinta': 30,
            'cuarenta': 40,
            'cincuenta': 50,
            'sesenta': 60,
            'setenta': 70,
            'ochenta': 80,
            'noventa': 90
        },
        'scales': {
            'cien': 100,
            'mil': 1000,
            'millon': 1000000,
            'billon': 1000000000,
            'trillon': 1000000000000
        }
    }
}


LANGUAGE_CODES = list(MATH_WORDS.keys())


CONSTANTS = {
    'pi': 3.141693,
    'e': 2.718281
}


UNARY_FUNCTIONS = {
    'sqrt': math.sqrt,

    # Most people assume a log of base 10 when a base is not specified
    'log': math.log10
}


class InvalidLanguageCodeException(Exception):
    """
    Exception to be raised when a language code is given that
    is not a part of the ISO 639-2 standard.
    """
    pass


def word_groups_for_language(language_code):
    """
    Return the math word groups for a language code.
    The language_code should be an ISO 639-2 language code.
    https://www.loc.gov/standards/iso639-2/php/code_list.php
    """

    if language_code not in LANGUAGE_CODES:
        message = '{} is not an available language code'.format(language_code)
        raise InvalidLanguageCodeException(message)

    return MATH_WORDS[language_code]


def words_for_language(language_code):
    """
    Return the math words for a language code.
    The language_code should be an ISO 639-2 language code.
    https://www.loc.gov/standards/iso639-2/php/code_list.php
    """
    word_groups = word_groups_for_language(language_code)
    words = []

    for group in word_groups:
        words.extend(word_groups[group].keys())

    return words
