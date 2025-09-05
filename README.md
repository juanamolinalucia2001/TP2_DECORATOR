---

<div align="center">

# **Criterios de evaluación: Decisiones de diseño**

☕️ **Mensita UNSAM — Patrón Decorator**

</div>

---


### **Size**
La clase **`Size`** implementa un **Enum** para definir cada tamaño con un *label* y un factor de precio.  
Esta decisión se tomó para **centralizar la lógica de tamaños y factores de costo en un único lugar**.  
De esta manera, añadir un nuevo tamaño o cambiar un precio implica modificar solo esta clase, **reduciendo el acoplamiento y mejorando la extensibilidad** del sistema.   

---

### **Decisiones de diseño de los tests**
Los test unitarios se escribieron con **pytest** para validar el patrón Decorator aplicado a la simulación del servicio de café *Mensita UNSAM*.  

Los objetivos fueron:
- Que las **descripciones** de las bebidas reflejen correctamente la composición de los condimentos.  
- Que los **precios** coincidan con la suma esperada de bebida base + condimentos × factor de tamaño.  
- Que la **propagación de tamaños** en la cadena de decoradores funcione de manera consistente.  

---

### **Usos**

#### **Cobertura de casos representativos**
- Se incluyeron combinaciones simples (*Espresso solo*) y más complejas (doble Mocha con Crema, bebidas con Caramel, etc.).  
- Se probó tanto la descripción como el costo de la bebida final, asegurando que la lógica de composición funcione correctamente.  

#### **Consistencia de tamaños**
- Se verificó que los tamaños (**Tall, Grande y Venti**) se propaguen en toda la cadena de decoradores.  
- Los test comparan el `Size` esperado y validan que el precio de los condimentos cambie según el factor definido.  

#### **Uso del builder**
- Se agregó un test a **`build_beverage`** para comprobar que la función construya correctamente una bebida con lista de condimentos y tamaño, evitando errores manuales en la composición.  

#### **PrettyPrint**
- Se añadió una capa de presentación que transforma descripciones repetitivas en un formato más legible  
  *(ejemplo: “Mocha, Mocha, Mocha” → “Triple Mocha”)*.  
- Los test confirman que esta presentación **no altera el cálculo de costos**, solo la descripción textual.  

---

### **Resultados de las pruebas**
Todas las pruebas pasaron exitosamente con **pytest**, confirmando que:  
- Las clases base y los decoradores mantienen el **principio de abierto/cerrado (OCP)**.  
- Es posible **extender el sistema** con nuevas bebidas o condimentos sin modificar el código existente.  

---

### **OCP aplicado**
- **Beverage**: abstracción base; todas las bebidas concretas (*Espresso, HouseBlend, etc.*) heredan de ella.  
- **CondimentDecorator**: decorador abstracto que envuelve cualquier `Beverage`.  
- **Condimentos clásicos**: *Mocha, Whip, Soy, Caramel, Milk* heredan de `CondimentDecorator`.  
- **Topping**: clase genérica que hereda de `CondimentDecorator` y maneja lógica común (precio y tamaño).  
- **Toppings concretos**: *Honey, Cacao, Cinnamon, Vanilla*, etc., heredan de `Topping`, definiendo solo nombre y precio.  

✅ Cumplimiento de OCP:
- Se pueden agregar **nuevos toppings** sin modificar ninguna clase existente.  
- El cliente programa siempre contra la abstracción **Beverage**.  
- Los decoradores se pueden **encadenar dinámicamente**  
  *(ejemplo: `Cacao(Honey(Espresso()))`)*.  

---

### **Diagrama simplificado**

```text
Beverage (abstract)
   ↑
   |-----------------------------
   |            |               |
Espresso    HouseBlend       DarkRoast
   |
   | (puede ser envuelto por decoradores)
   ↓
CondimentDecorator (abstract)  <-- hereda de Beverage
   |
   |--------------------------------------------------
   |           |            |       |        |        
Mocha      Whip         Soy    Caramel    Milk      Topping (abstract)
                                                 |
                                                 |-----------------------------------------------
                                                 |            |               |                |
                                               Honey        Cacao         Cinnamon         Vanilla


