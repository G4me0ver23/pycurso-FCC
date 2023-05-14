import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs): #um número variável de argumentos que especificam o número de bolas de cada cor que estão no chapéu
    if any(kwargs): #pelo menos uma bola?
      self.contents = []
      for color, quantity in kwargs.items(): #Os argumentos passados para o objeto de chapéu após a criação devem ser convertidos em uma variável de instância contents
        self.contents.extend([color] * quantity) #um item para cada bola no chapéu
      self.contents_o=self.contents.copy()
    else:
      raise ValueError('at least one ball')

  def draw(self, num_balls_drawn): #remove bolas aleatoriamente de contents e retorna essas bolas como uma lista de strings
    self.contents=self.contents_o.copy() #bolas só voltam ao chapéu "depois" da retirada
    if num_balls_drawn>len(self.contents): #número de bolas a serem retiradas exceder a quantidade disponível?
      num_balls_drawn=len(self.contents)
    drawed_list=[]
    for n in range(num_balls_drawn):
      len_ctt=len(self.contents)-1
      pop_item=self.contents.pop(random.randint(0,len_ctt))
      drawed_list.append(pop_item)
    return drawed_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments): #retorna uma probabilidade
  m=0 #resultados favoráveis
  for e in range(num_experiments): #cada experimento
    draweds=hat.draw(num_balls_drawn)
    condition=False
    for k in expected_balls.keys(): #cada cor experada
      if draweds.count(k)>=expected_balls[k]: #quantidade retirada de bolas com essa cor é maior ou igual quantidade esperada?
        condition=True
      else: #quantidade não satifaz a condição
        condition=False
        break
    if condition: #condição é satisfeita?
      m+=1
  return m/num_experiments #probabilidade(casos favoráveis/casos totais)
