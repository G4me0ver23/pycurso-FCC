def arithmetic_arranger(problems, result=False):
  if len(problems)>5: #Tem até 5 problemas?
      return 'Error: Too many problems.'
    
  line1=''
  line2=''
  line3=''
  resps=''
  arranged_problems=''
  for problem in problems:
    problem=problem.split()
    if problem[1] not in('+', '-'): #O operador é válido?
      return 'Error: Operator must be \'+\' or \'-\'.'
    for number in range(0,3,2):
      if len(problem[number])>4: #Numero tem mais de 4 digitos?
        return 'Error: Numbers cannot be more than four digits.'
      for n in problem[number]:
        if not n.isdigit(): #Algum caractere do numero não é um digito?
          return 'Error: Numbers must only contain digits.'
    lens=[len(problem[0]),len(problem[2])]
    spacemax=max(lens)+2 #Acha o tamanho máximo dessa linha
    space1=spacemax-len(problem[0]) #Acha o tamanho dos espaços da linha 1
    space2=spacemax-len(problem[2])-1 #Acha o tamanho dos espaços da linha 2

    if problem==problems[-1].split():
      line1+=' '*space1+str(problem[0])
      line2+=problem[1]+' '*space2+str(problem[2])
      line3+='-'*spacemax
    else:
      line1+=' '*space1+str(problem[0])+'    '
      line2+=problem[1]+' '*space2+str(problem[2])+'    '
      line3+='-'*spacemax+'    '
      
    if result: #Se result for True, salva o resultado
      if problem[1]=='+':
        resp=int(problem[0])+int(problem[2])
      elif problem[1]=='-':
        resp=int(problem[0])-int(problem[2])
      spaceresp=spacemax-len(str(resp))

      if problem==problems[-1].split():
        resps+=' '*spaceresp+str(resp)
      else:
        resps+=' '*spaceresp+str(resp)+'    '
      
  if result:
    arranged_problems+=line1+'\n'+line2+'\n'+line3+'\n'+resps
  else:
    arranged_problems+=line1+'\n'+line2+'\n'+line3
    
  return arranged_problems
