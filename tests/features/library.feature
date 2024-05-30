Feature: Biblioteca
  Como usuario de la biblioteca
  Quiero poder consultar, reservar, prestar y devolver libros
  Para poder gestionar mis actividades en la biblioteca

Scenario: Consultar un libro
  Given que hay un libro titulado "Python Programming" en el catálogo
  When busco un libro por título "Python Programming"
  Then debería encontrar al menos un libro con ese título

Scenario: Reservar un libro
  Given que estoy registrado como miembro "John Doe"
  And que el libro "Python Programming" está disponible para reserva
  When reservo el libro "Python Programming"
  Then el libro debería estar reservado para "John Doe"

Scenario: Prestar un libro
  Given que estoy registrado como miembro "John Doe"
  And que el libro "Python Programming" está reservado para mí
  When presto el libro "Python Programming"
  Then el libro debería estar prestado a "John Doe"
  And debería tener un periodo de préstamo de 14 días

Scenario: Devolver un libro
  Given que estoy registrado como miembro "John Doe"
  And que el libro "Python Programming" está prestado a mí
  When devuelvo el libro "Python Programming"
  Then el libro debería estar disponible para otros usuarios
