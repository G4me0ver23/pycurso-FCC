def add_time(start, duration, day_init=''):
  days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  days_lower = [string.lower() for string in days]
  result_h=0
  result_m=0
  n=0
  n_day=0
  horario_fin=''
  new_time=''
  start1=start.split(':')
  start2=start1[1].split()
  start=[start1[0]]
  start.extend(start2)
  
  duration=duration.split(':')
  if int(duration[1])>59:
      return 'minutes must be less than 60'

  result_m=int(start[1])+int(duration[1])#Calcula os minutos finais (soma do inicial com o periodo)
  if result_m>59: #Os minutos no tempo de duração não são um número inteiro menor que 60?
      result_h+=result_m//60
      result_m%=60

  result_h+=int(start[0])+int(duration[0])#Calcula a hora final (soma da inicial com o periodo)
  n+=result_h//24
  result_h%=24
  if result_h>=12: #Horas restantes completam um turno (AM -> PM/ PM -> AM)? Troca o turno
    if result_h>12:
      result_h-=12
    if start[2]=='AM':
      horario_fin='PM'
    elif start[2]=='PM':
      n+=1
      horario_fin='AM'
  elif result_h<12: #Horas restantes não completam um turno? Pernace o mesmo
    horario_fin=start[2]

  new_time+=str(result_h)+':' #Adiciona a hora ao resultado final
  if result_m<9: #Se minutos forem menos que 10, precisam do 0 à esquerda
    new_time+='0'
  new_time+=str(result_m)+' '+horario_fin #Adiciona os minutos ao resultado final

  day_init=day_init.lower() #Converte para minusculo para evitar erros
  if day_init!='' and (day_init in(days) or day_init in(days_lower)): #Função recebe o parâmetro opcional do dia de início na semana?
    day= days_lower.index(day_init)
    n_day+=n%7
    day+=n_day
    day%=7
    new_time+=', '+str(days[day])

  if n>1: #Resultado é mais de um dia depois?
    new_time+=' ('+str(n)+' days later)'
  elif n==1: #Resultado é no dia seguinte?
    new_time+=' (next day)'
       
  return new_time
