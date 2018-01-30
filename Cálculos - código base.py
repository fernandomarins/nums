#!/usr/bin/env python

def letters(text):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'I', 'E', 'O', 'U')
    # create two arrays to store the characters
    text_vowel = ''
    text_consonant = ''
    # remove the white space
    text = text.replace(' ', '')
    for char in text:
        # if the char is in vowels, then it's a vowel
        if char in vowels:
            text_vowel += char
        else:
            text_consonant += char
    # return only the vowels and only the consonants in lowercase
    return text_vowel.lower(), text_consonant.lower()

def convert_to_number(text):
    # make sure the text is lowercased
    text = text.lower()
    # remove the white space
    text = text.replace(' ', '')
    # check all the elements in the array
    for char in text:
        # replace the letters with numbers
        if char == 'a' or 'j' or 's':
            text = text.replace('a', '1')
            text = text.replace('j', '1')
            text = text.replace('s', '1')
        if char == 'b' or 'k' or 't':
            text = text.replace('b', '2')
            text = text.replace('k', '2')
            text = text.replace('t', '2')
        if char == 'c' or 'l' or 'u':
            text = text.replace('c', '3')
            text = text.replace('l', '3')
            text = text.replace('u', '3')
        if char == 'd' or 'm' or 'v':
            text = text.replace('d', '4')
            text = text.replace('m', '4')
            text = text.replace('v', '4')
        if char == 'e' or 'n' or 'w':
            text = text.replace('e', '5')
            text = text.replace('n', '5')
            text = text.replace('w', '5')
        if char == 'f' or 'o' or 'x':
            text = text.replace('f', '6')
            text = text.replace('o', '6')
            text = text.replace('x', '6')
        if char == 'g' or 'p' or 'y':
            text = text.replace('g', '7')
            text = text.replace('p', '7')
            text = text.replace('y', '7')
        if char == 'h' or 'q' or 'z':
            text = text.replace('h', '8')
            text = text.replace('q', '8')
            text = text.replace('z', '8')
        if char == 'i' or 'r':
            text = text.replace('i', '9')
            text = text.replace('r', '9')
    return text

def sum_numbers(x):
    # check if x is a string
    if type(x) == str:
        x = x.replace('/', '')
    total = 0
    for letter in str(x):
        total+= ord(letter) - 48
    # return the sum of the characters
    return total

def numbers(name, birthday):
    # create an array with the full name
    names = name.split()
    # remove the white spaces
    name = name.replace(' ', '')
    print('Base da pirâmide invertida:', convert_to_number(name))
    # remove the slashes from the birthday
    birthday_no_slash = birthday.replace('/', '')
    # check if the birthday has 8 elements
    if len(birthday_no_slash) == 8:
        # convert the name to numbers
        name_converted = convert_to_number(name)
        # get the vowels and consonants
        name_vowels, name_consonants = letters(name)
        # convert the vowels to numbers
        vowels_converted = convert_to_number(name_vowels)
        # convert the consonants to numbers
        consonants_converted = convert_to_number(name_consonants)
        # reduce the birthday to one number = destiny path
        destiny_path = sum_numbers(birthday)
        
        # get the birthday day
        day = int(birthday_no_slash[0:2])
        # get the birthday month
        month = int(birthday_no_slash[2:4])
        # get the birthday year
        year = int(birthday_no_slash[4:])
        # calculate the daily work
        daily_work = int(day) + int(month)
        # calculate the daily virtude
        daily_virtude = int(day) + int(year)
        
        expression = sum_numbers(name_converted)
        impression = sum_numbers(consonants_converted)
        motivation = sum_numbers(vowels_converted)
        
        # print the expression, the impression, the motivation ahd the destiny path
        print('Expressão: ' + str(expression))
        print('Impressão: ' + str(impression))
        print('Motivação: ' + str(motivation))
        
        # print the vibration of the day
        print('Vibração do dia de nascimento:', day)
        # print the number of the name
        print('Número do nome:', sum_numbers(convert_to_number(names[0])))
        
        # convert the name to string
        name_str = str(name_converted)
        
        #print the skills
        print ('Talentos:')
        print('1:', name_str.count('1'))
        print('2:', name_str.count('2'))
        print('3:', name_str.count('3'))
        print('4:', name_str.count('4'))
        print('5:', name_str.count('5'))
        print('6:', name_str.count('6'))
        print('7:', name_str.count('7'))
        print('8:', name_str.count('8'))
        print('9:', name_str.count('9'))
        
        # print the destiny path
        print('Caminho do destino: ' + str(destiny_path))
        
        # print the daily work
        print('Trabalho diário: ', daily_work)
        # print the daily virtude
        print('Atividade ou virtude diária: ', sum_numbers(daily_virtude))
        # calculate the powerful number
        powerful_number = sum_numbers(expression) + sum_numbers(destiny_path)
        
        # print the powerful name
        print('Número poderoso:', (powerful_number))
        
        # sum the motivation, expression, day of birth and the destiny path
        spiritual_initiation = sum_numbers(motivation) + sum_numbers(expression) + sum_numbers(day) + sum_numbers(destiny_path)
        print('Iniciação espiritual:', spiritual_initiation)
        
        # first pinnacle = day of birth + month of birty (both reduced)
        pinnacle_1 = day + month
        # the duration is calculated subtracting the reduced destiny path from 36
        pinnacle_1_duration = 36 - (sum_numbers(sum_numbers(destiny_path)))
        # second pinnacle = day of birth + year of birty (both reduced)
        pinnacle_2 = (sum_numbers(day) + sum_numbers(year))
        # it's the first pinnacle plus 9
        pinnacle_2_duration = pinnacle_1_duration + 9
        # third pinnacle = sum of the first and second pinnacles
        pinnacle_3 = (pinnacle_1) + (pinnacle_2)
        # it's the second pinnacle plus 9
        pinnacle_3_duration = pinnacle_2_duration + 9
        # fourth pinnacle = month of birth + year of birty (both reduced)
        pinnacle_4 = ((sum_numbers(month) + sum_numbers(year)))
        # it's after the third pinnacle is finished
        pinnacle_4_duration = pinnacle_3_duration + 1
        
        # print pinnacle 1
        print('Pináculo 1:', pinnacle_1, 'de 0 aos', pinnacle_1_duration, 'anos') 
        # print pinnacle 2
        print('Pináculo 2:', pinnacle_2, 'de', pinnacle_1_duration + 1, 'aos', pinnacle_2_duration + 1, 'anos')
        # print pinnacle 3
        print('Pináculo 3:', pinnacle_3, 'de', pinnacle_2_duration + 2, 'aos', pinnacle_3_duration + 2, 'anos')
        # print pinnacle 4
        print('Pináculo 4:', pinnacle_4, 'de', pinnacle_3_duration + 3, 'até o fim da vida')
        
        # the magical numbers added from line #164 until here are just a calibration
        
        # substract the reduced destiny path from 36
        cycle_number = 36 - (sum_numbers(sum_numbers(destiny_path)))
        # the year of birth plus the cycle number
        first_cycle = int(year) + cycle_number
        # the year after the first cycle + cycle number
        second_cycle = first_cycle + 1 + cycle_number
        # the year after the second cycle + cycle number
        third_cycle = second_cycle + 1
        
        # print forming cycle
        print('Ciclo formador: de', year, 'até', first_cycle, 'na vibração do', (month))
        # print productive cycle
        print('Ciclo produtivo: de', first_cycle + 1, 'até ', second_cycle, 'na vibração do', (day))
        # print mature cycle
        print('Ciclo de maturidade:', third_cycle, 'na vibração do', ((sum_numbers(year))))
        
        # it's the reduced day minus the reduced month
        first_challenge = day - month
        # the reduced month minus the reduced year
        second_challenge = (sum_numbers(month)) - sum_numbers((sum_numbers(sum_numbers(year))))
        # the difference between the first and the second
        third_challenge = first_challenge - second_challenge
        
        # print the first challenge
        print('Primeiro desafio:', abs(first_challenge))
        # print the second challenge
        print('Segundo desafio:', abs(second_challenge))
        # print the third challenge
        print('Terceiro desafio:', abs(third_challenge))

    else:
        print('A data de nascimento precisa ter 8 caracteres.')
        
def personal_numbers(birthday, current_date):
    birthday = birthday.replace('/', '')
    current_date = current_date.replace('/', '')
    day = birthday[0:2]
    # get the birthday month
    month = birthday[2:4]
    # get the birthday year
    year = birthday[4:]
    
    current_day = current_date[0:2]
    # get the current month
    current_month = current_date[2:4]
    # get the current year
    current_year = current_date[4:]
    
    day_reduced = sum_numbers(sum_numbers(day))
    current_day_reduced = sum_numbers(sum_numbers(current_day))
    month_reduced = sum_numbers(sum_numbers(month))
    current_month_reduced = sum_numbers(sum_numbers(current_month))
    current_year_reduced = sum_numbers(sum_numbers(sum_numbers(current_year)))
    personal_year = day_reduced + month_reduced + current_year_reduced
    personal_year_reduced = sum_numbers(sum_numbers(personal_year))
    personal_month_reduced = personal_year_reduced + current_month_reduced
    personal_day_reduced = personal_month_reduced + current_day_reduced
    print('Ano pessoal:', personal_year_reduced)
    print('Mês pessoal:', personal_month_reduced)
    print('Dia pessoal:', personal_day_reduced)

name = str(input('Qual o nome? '))
birthday = str(input('Qual a data de nascimento? '))
numbers(name, birthday)