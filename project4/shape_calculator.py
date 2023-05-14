class Rectangle:
  def __init__(self, width, height): #inicializado com atributos largura e altura
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self): #retorna a área (width * height)
    return self.width * self.height

  def get_perimeter(self): #retorna o perímetro (2 * width + 2 * height)
    return 2 * self.width + 2 * self.height

  def get_diagonal(self): #retorna a diagonal ((width ** 2 + height ** 2) ** .5)
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self): # retorna uma string que representa a forma usando as linhas de "*"
    if self.width<=50 and self.height<=50: #largura ou altura é maior do que 50?
      pict=''
      for i in range(self.height): #número de linhas é igual à altura
        pict+='*'*self.width+'\n' #número de "*" em cada linha deve é a largura, com uma nova linha (\n) no final de cada linha
      return pict
    else:
      return 'Too big for picture.'

  def get_amount_inside(self, other): #Retorna o número de vezes que a forma passada como argumento poderia caber dentro da forma (sem rotações)
    if self.width<other.width or self.height<other.height:
      return 0
    else:
      in_w=self.width//other.width
      in_h=self.height//other.height
      return in_w*in_h

  def __str__(self): #se for representada como uma string, ela deve ter a seguinte aparência: Rectangle(width=5, height=10)
    return f'Rectangle(width={self.width}, height={self.height})'
      
      
class Square(Rectangle): #deve ser uma subclasse da classe Rectangle
  def __init__(self, width): #único comprimento lateral é passado
    super().__init__(width, width) #armazena o comprimento do lado nos atributos width e height da classe Rectangle

  def set_width(self, width):
    super().set_width(width)
    self.height=width
  #os métodos set_width e set_height na classe Square devem definir a largura e a altura
  def set_height(self, height):
    super().set_height(height)
    self.width=height

  def get_area(self):
    return super().get_area()

  def get_perimeter(self):
    return super().get_perimeter()

  def get_diagonal(self):
    return super().get_diagonal()

  def get_picture(self):
    return super().get_picture()
    
  def get_amount_inside(self, other):
    return super().get_amount_inside(other)

  def set_side(self, side):
    self.set_width(side)
    self.set_height(side)
    
  def __str__(self): #se for representada como uma string, ela deve ter a seguinte aparência: Square(side=9)
    return f'Square(side={self.width})'
