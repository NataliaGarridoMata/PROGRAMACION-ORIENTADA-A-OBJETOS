# ABSTRACCION - PROGRAMACION ORIENTADA A OBJETOS (POO)
## Natalia Yamile Garrido Mata 

# Descripcion:

@abstractmethod en Python es un decorador que se usa para indicar que un método es abstracto, es decir, 
debe ser implementado obligatoriamente por las clases hijas.

Se utiliza dentro de clases abstractas del módulo abc (Abstract Base Classes).

Idea básica

Cuando una clase tiene un método con @abstractmethod:

La clase define el método pero no lo implementa completamente.
Las clases que heredan de esa clase están obligadas a crear su propia implementación de ese método.
Si no lo hacen, no podrán crear objetos de esa clase hija.



