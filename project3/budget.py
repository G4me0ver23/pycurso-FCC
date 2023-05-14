class Category:
  def __init__(self, name):
    self.name = name
    self.ledger=[]

  def deposit(self, amount, description=''): #acrescenta um objeto à lista ledger na forma de:
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=''): #quantia passada deve ser armazenada no ledger como um número negativo
    if self.check_funds(amount): #tem  fundos suficientes?
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False

  def get_balance(self): #retorna o saldo atual da categoria de orçamento com base nos depósitos e retiradas que ocorreram
    saldo=0
    for oper in self.ledger:
      saldo+=oper['amount']
    return saldo

  def transfer(self, amount, category): #adicionar uma retirada
    if self.check_funds(amount): #tem  fundos suficientes?
      description="Transfer to "+ category.name
      self.withdraw(amount, description)
      description="Transfer from "+ self.name
      category.deposit(amount, description) #adiciona um depósito à outra categoria do orçamento
      return True
    return False

  def check_funds(self, amount): #verifica se o valor é maior que o saldo da categoria do orçamento
    value=0
    for oper in self.ledger:
      value+=oper['amount']
    if amount>value:
      return False
    else:
      return True

  def __str__(self):
    space_max=30
    space_r=round((space_max-len(self.name)+0.1)/2)
    space_l=(space_max-len(self.name))//2
    imprint= '*'*space_r+self.name+'*'*space_l+'\n'
    for oper in self.ledger:
      am="{:.2f}".format(oper['amount'])
      imprint+=oper['description'][:23].ljust(23) + am[:7].rjust(7) + '\n'
    imprint+='Total: '+str(round(self.get_balance(),2))
      
    return imprint

def create_spend_chart(categories): #retorna uma string, que é um gráfico de barras
  if len(categories)<=4: #até quatro categorias
    names=[]
    catgs=[]
    a_bars={}
    plot='Percentage spent by category\n' #título no topo
    all=0
    for catg in categories:
      a_bars[catg.name]=0
      for oper in catg.ledger:
        if oper['amount']<0: #é uma retirada?
          all+=abs(oper['amount'])
          a_bars[catg.name]+=abs(oper['amount'])
    for catg in categories: #calcula a pocentagem de cada categoria
      percentile=int(a_bars[catg.name]/all*100)
      bars=percentile//10
      catgs.append({'percentile':percentile, 'bars':bars})
      names.append(list(catg.name))
  
    for i in range(10,-1,-1): #rótulos de 0 a 100
      if i!=0:
        plot+=str(i*10)+'| '
      else:
        plot+=' 0| '
      for catg in catgs:
        if catg['bars']<i:
          plot+='   '
        else:
          plot+='o  '
      plot+='\n '
  
    plot+='   '+'-'*len(categories)*3+'-\n     '
  
    while any(names): #nome de cada categoria deve ser escrito verticalmente abaixo da barra
      for name_n in names:
        if len(name_n)!=0:
          plot+=name_n[0]+'  '
          name_n.pop(0)
        else:
          plot+='   '
      if any(names):
        plot+='\n     '
    
    return plot
  return 'only up to 4 categories'
