# Описание
В этом репозитории хранятся библиотеки со структурами данных от Cominta
### Содержание документации:
1. [Массив](#array)
    + [Методы](#arrayMethods)
        + [forEach](#arrayForEach)
        + [insert](#arrayInsert)
		+ [search](#arraySearch)
		+ [delete](#arrayDelete)
        + [append](#arrayAppend)
        + [appendStart](#arrayAppendStart)
        + [pop](#arrayPop)
        + [popStart](#arrayPopStart)
        + [index](#arrayIndex)
        + [setIndex](#arraySetIndex)
    + [Принцип работы](#arrayWork)
2. [Свявзанный список](#linkedlist)
    + [Методы](#linkedlistMethods)
    + [Принцип работы](#linkedlistWork)
#### Содержание репозитория  
+ array.py - файл с массивом
+ linkedlist.py - файл со связанным списком
+ init.py - указывает что это пакет модулей
# Массив <a name = "array"></a>
## Методы <a name = "arrayMethods"></a>
В этом разделе описываються методы массива (как они работают и какие аргмуенты у них есть)
### forEach <a name = "arrayForEach"></a>
```python
def forEach(self, callback):
    for i in range(self.__firstElement, self.__lastElement):
        callback(self.__arr[i])
        
```
При вызове этого метода нужно передавать callback функцию в которую будет передаваться элемент массива. \
\
<b>Как работает</b>\
Запускается цикл в котором вызывается функция и в эту функцию передается каждый элемент массива 
### insert <a name = "arrayInsert"></a>
```python
def insert(self, item, index):
    if index > self.__lastElement + 1 or index < 0:
        raise IndexError('Out of range')
    
    if index == 0 and self.__firstElement != 0:
        self.__firstElement -= 1		
        self.__arr[self.__firstElement] = item
        self.size += 1
        return

    elif len(self.__arr) - 1 == self.__lastElement:
        self.__newArray()

    self.size += 1
    self.__lastElement += 1

    temp = [None] * self.__lastElement
    for i in range(self.__firstElement + index, self.__lastElement):
        temp[i] = self.__arr[i]

    for i in range(self.__firstElement + index + 1, self.__lastElement + 1):
    	self.__arr[i] = temp[i - 1]
		
    del temp
    self.__arr[self.__firstElement + index] = item
```
Этот метод вставляет элемент в нужный индекс. Первый метод это элемент который вы хотите вставить, а второй - индекс в который вы хотите его вставить \
\
<b>Как работает</b>\
В начале производятся проверки на правильность переданого индекса. После мы немного меняем некоторый переменные и запускается 2 цикла. Первый - во временный список добавляются элементы которые нам надо сдвинуть, а второй - добавление элементов со сдвигом на 1 вправо. И в конце удаление временной переменной и вставка нужного элемента
### search <a name = "arraySearch"></a>
```python
def search(self, item):
    for i in range(self.__firstElement, self.__lastElement):
        if self.__arr[i] == item:
            return i
	
    return -1
```
Находит элемент в массиве (этот элемент вы должны передать в функцию) и возвращает его индекс. При неудачной попытке возвращает -1\
\
<b>Как работает</b>\
Запускается цикл который перебирает каждый элемент и сравнивает его с переданным. Если они равны, то возвращает его индекс, а если по окончанию цикла нужный элемент не найден, то возвращается -1
### delete <a name = "arrayDelete"></a>
```python
def delete(self, index):
    if index > self.__lastElement or index < 0:
        raise IndexError('Out of range')

    if index == 0:
        self.size -= 1
        self.__arr[self.__firstElement] = None
        self.__firstElement += 1
        return

    elif index == self.__lastElement:
        self.size -= 1
        self.__arr[self.__lastElement] = None
        self.__lastElement -= 1
        return

    elif self.__sizeOfBuffer > 100 and 0 - self.__firstElement < -100:
        self.__memoryLeak("left")

    elif self.__sizeOfBuffer > 100 and self.__sizeOfBuffer - self.__lastElement > 100:
        self.__memoryLeak("right")

    self.size -= 1
    self.__lastElement -= 1
    self.__arr[self.__firstElement + index] = None

    temp = [None] * (self.__lastElement + 2)
         
    for i in range(self.__firstElement + index, self.__lastElement + 2):	
        temp[i] = self.__arr[i]

    for i in range(self.__firstElement + index - 1, self.__lastElement + 1):
        if i + 1 == self.__firstElement + index:
            continue

        self.__arr[i] = temp[i + 1]

    del temp
    self.__arr[self.__lastElement + 1] = None
```
Удаляет нужный индекс (индекс передается аргументом).\
\
<b>Как работает</b>
В начале несколько проверок похожих на проверки в insert. Производится работа с переменными и запускается 2 цикла. Первый - Добавление в временный список элементы, а второй - смещение элементов.
### append <a name = "arrayAppend"></a>
```python
def append(self, item):
    if self.__lastElement == -1:
        self.__lastElement = 0
        self.__arr[self.__lastElement] = item
        self.size += 1
        return

    if self.__sizeOfBuffer - 1 == self.__lastElement:
        self.__newArray()

    self.__lastElement += 1
    self.size += 1
    self.__arr[self.__lastElement] = item
```
Добавляет элемент (передается как аргумент) в конец массива.\
\
<b>Как работает</b>\
Сначала проверки. Первая проверкка - если массив пустой, то просто добавить элемент. Если такое не произошло, то мы просто добавляем элемент в конец.
### appendStart (можно было бы назвать prepend, но мне кажется что appendStart легче запомнить) <a name = "arrayAppendStart"></a>
```python
def appendStart(self, item):
    if self.__lastElement == -1:
        self.__lastElement = 0
        self.__arr[self.__lastElement] = item
        self.size += 1
        return

    elif self.__firstElement != 0:
        self.__firstElement -= 1
        self.__arr[self.__firstElement] = item
        self.size += 1
        return

    self.insert(item, 0)
```
Добавляет элемент (который вы должны передать как аргумент) в начало массива.\
\
<b>Как работает</b>\
Сначала проверки. Первая - если массив пустой, то просто добавляем в него элемент, а вторая - если перед первым элементом массива в буфере есть место, то просто вставить его туда (для того чтобы понять что я имел ввиду прочтите [Принцип работы массива](#arrayWork))
### pop <a name = "arrayPop"></a>
```python
def pop(self):
    if self.__lastElement == -1:
        raise IndexError("Out of range")
		
    self.__arr[self.__lastElement] = None
    self.size -= 1
    self.__lastElement -= 1

    if self.__sizeOfBuffer > 100 and self.__sizeOfBuffer - self.__lastElement > 100:
        self.__memoryLeak("right")
```
Удаляет элемент в конце массива\
\
<b>Как работает</b>\
Проверка на заполненость. Потом удаление элемента (для того чтобы понять почему я просто заменяю на None прочтите [Принцип работы массива](#arrayWork))
### popStart <a name = "arrayPopStart"></a>
```python 
def popStart(self): 
    if self.__lastElement == -1:
        raise IndexError("Out of range")

    self.size -= 1
    self.__arr[self.__firstElement] = None
    self.__firstElement += 1

    if self.__sizeOfBuffer > 100 and 0 - self.__firstElement < -100:
        self.__memoryLeak("left")
```
Удаляет первый элемент массива\
\
<b>Как работает</b>\
Проверка на заполненость массива. Потом удаление элемента (просто его замена на None. Если не понятно почему, то прочтите [Принцип работы массива](#arrayWork))
### index <a name = "arrayIndex"></a>
```python
def index(self, index):
    if index < self.__firstElement or index > self.__lastElement:
        raise IndexError("Out of range")

    return self.__arr[self.__firstElement + index]
```
Возвращает элемент по указанному в аргументе индексу.\
\
<b>Как работает</b>\
Проверка на правильность индекса. Возврат элемента
### setIndex <a name = "arraySetIndex"></a>
```python
def setIndex(self, index, item):
    if index < self.__firstElement or index > self.__lastElement:
        raise IndexError("Out of range")

    self.__arr[self.__firstElement + index] = item
```
Заменяет элемент по индексу (индекс вы указываете в аргументе) на нужный элемент\
\
<b>Как работает</b>\
Поверка на правильность указанного индекса и замена на нужный элемент 
### arr <a name = "arrayArr"></a>
```python
def arr(self):
    listT = [None] * (self.__lastElement + 1)
    for i in range(self.__firstElement, self.__lastElement + 1):
        listT[i] = self.__arr[i] 

    return listT
```
Возвращает весь массив. Почему для этого сделан отдельный метод? Прочтите [Принцип работы массива](#arrayWork)\
\
<b>Как работает</b>\
Просто запускает цикл в котором добавляет все элементы в временный список и возвращает его
