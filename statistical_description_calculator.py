def absol_freq(input_list):
    absol = dict()
    for i in input_list:
        if i in absol:
            absol[i] = absol.get(i) + 1
        else:
            absol[i] = 1
    return(absol)
#---------------------------------------------------
def relat_freq(input_list):
    absolute = absol_freq(input_list)
    relat = dict()
    for j in absolute:
        perc = round(absolute[j] / len(input_list), 2)
        relat[j] = perc
    return relat
#---------------------------------------------------
def mode(input_list):
    dic=absol_freq(input_list)
    big = max(dic, key=dic.get)
    return(big)
#---------------------------------------------------
def average(input_list):
    counter = 0
    for i in input_list:
        counter += i
    counter = counter / len(input_list)
    return(round(counter,2))
#---------------------------------------------------
def median(input_list):
    input_list.sort()
    if len(input_list) % 2 == 0:
        s = input_list[int(len(input_list)/2)] + input_list[int(len(input_list)/2 -1)]
        return(s/2)
    else:
        size= len(input_list)-1
        return(input_list[int(size/2)])
#---------------------------------------------------
def range_calc(input_list):
    dif = max(input_list) - min(input_list)
    return(dif)
#---------------------------------------------------
def Q1(input_list):
    import math
    input_list.sort()
    P_Q1 = (len(input_list) + 1) / 4
    P_Q1_= P_Q1 - 1
    q1 = input_list[math.floor(P_Q1_)] + (P_Q1_ - math.floor(P_Q1_)) * (input_list[math.floor(P_Q1_)+1] - input_list[math.floor(P_Q1_)])
    return(q1)
#---------------------------------------------------
def Q2(input_list):
    import math
    input_list.sort()
    P_Q2 = (len(input_list) + 1) / 2
    P_Q2_= P_Q2 - 1
    q2 = input_list[math.floor(P_Q2_)] + (P_Q2_ - math.floor(P_Q2_)) * (input_list[math.floor(P_Q2_)+1] - input_list[math.floor(P_Q2_)])
    return(q2)
#---------------------------------------------------
def Q3(input_list):
    import math
    input_list.sort()
    P_Q3 = (len(input_list) + 1) * 3 / 4
    P_Q3_= P_Q3 - 1
    q3 = input_list[math.floor(P_Q3_)] + (P_Q3_ - math.floor(P_Q3_)) * (input_list[math.floor(P_Q3_)+1] - input_list[math.floor(P_Q3_)])
    return(q3)
#---------------------------------------------------
def interquart_range(input_list):
    interquartx = Q3(input_list) - Q1(input_list)
    return(interquartx)
#---------------------------------------------------
def variance(input_list):
    mean = average(input_list)
    acumulator = 0
    for i in input_list:
        input_list_i = i - mean
        acumulator += (input_list_i ** 2)
    return(round(acumulator / (len(input_list)-1), 2))
#---------------------------------------------------
def stand_deviation(input_list):
    import math
    return(round(math.sqrt(variance(input_list)),2))
#---------------------------------------------------
def position_mesures(input_list):
    return('min = ',min(input_list), 'Q1= ',Q1(input_list), 'Q2= ',Q2(input_list), 'Q3= ', Q3(input_list), 'max= ' ,max(input_list))
#---------------------------------------------------
def describe_data(input_list):
    print('absolute frequency= ',absol_freq(input_list))
    print('relative frequency= ',relat_freq(input_list))
    
    print('mode= ',mode(input_list))
    print('average/mean= ',average(input_list))
    print('median= ',median(input_list))
    
    print('range= ',range_calc(input_list))
    print('interquartile range= ',interquart_range(input_list))
    print('variance= ',variance(input_list))
    print('standart deviation= ',stand_deviation(input_list))
    
    print('position mesures: ',position_mesures(input_list))
#---------------------------------------------------
def menu():
    print('[1]-frequency mesures' )
    print('[2]-central tendency mesures')
    print('[3]-dispertion mesures')
    print('[4]-position mesures')
    print('[5]-describe data')
    print('[0]-exit')
#---------------------------------------------------
def beginning():
    list_x = list()
    
    def isfloat(num):
        try:
            float(num)
            return(True)
        except ValueError:
            return(False)
    
    while True:
        item=input('add a number for your list, if you are finished, write "stop" ')
        
        if item == 'stop':
            break
        
        else:
            if isfloat(item) == False:
                print('please, insert only numerical values')
            
            else:
                list_x.append(float(item))
    return(list_x)
#---------------------------------------------------
initial_list=beginning()
menu()
while True:
    option=(input('choose an option'))
    if option.isnumeric() == False or int(option) > 5 :
        print('please, choose a number between 0 and 5 as option')
    else:
        option = int(option)
        if option == 0:
            break
        
        elif option == 1:
            print('absolute frequency= ',absol_freq(initial_list))
            print('relative frequency= ',relat_freq(initial_list))
        
        elif option == 2:
            print('average/mean= ', average(initial_list))
            print('median= ',median(initial_list))
            print('mode= ',mode(initial_list))
            
        elif option == 3:
            print('range= ', range_calc(initial_list))
            print('interquartile range= ', interquart_range(initial_list))
            print('variance= ', variance(initial_list))
            print('standart deviation= ', stand_deviation(initial_list))
        
        elif option == 4:
            print('position mesures: ', position_mesures(initial_list))
        
        else:
            describe_data(initial_list)