# Описание
В этом репозитории хранятся библиотеки со структурами данных от Cominta
### Содержание документации:
1. [Массив](#array)
    + [Методы](#arrayMethods)
        + [forEach](#arrayForEach)
        + [insert](#arrayInsert)
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
#### forEach <a name = "arrayForEach"></a>
```python
def forEach(self, callback):
    for i in range(self.__firstElement, self.__lastElement):
        callback(self.__arr[i])
        
```
При вызове этого метода нужно передавать callback функцию в которую будет передаваться элемент массива.
#### insert <a name = "arrayInsert"></a>
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
Этот метод вставляет элемент в нужный индекс. Первый метод это элемент который вы хотите вставить, а второй - индекс в который вы хотите его вставить
