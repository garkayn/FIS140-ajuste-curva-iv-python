# Ajuste de curvas I–V en Python

Análisis de diez mediciones de corriente y voltaje de un laboratorio universitario. El script ajusta dos modelos logarítmicos con `scipy.optimize.curve_fit`, compara su RMSE dentro de la muestra y grafica las curvas junto a los datos.

## Modelos

- Logarítmico desplazado: `V = a · ln(I + c) + b`.
- Logarítmico simple: `V = a · ln(I) + b`.

El error calculado corresponde a las mismas diez observaciones usadas para ajustar los parámetros. Se presenta como una descripción del ajuste, no como una validación independiente ni como prueba de que el modelo representa un mecanismo físico. El nombre del curso no basta para llamar a estas ecuaciones una validación del modelo de Shockley.

## Ejecución

Se requiere Python 3.10 o posterior.

```bash
python -m venv .venv
python -m pip install -r requirements.txt
python lab6_fis140.py
```

El gráfico aparece en pantalla y la terminal muestra los parámetros estimados y el RMSE de cada curva.

## Datos y alcance

Los diez pares de mediciones están escritos en `lab6_fis140.py`; la fuente disponible es el código del informe de laboratorio original. Antes de publicar una versión final, añade el contexto del montaje, las condiciones experimentales, incertidumbres instrumentales y los créditos de quienes participaron, si corresponde. No se incluye el informe ni una copia de otros materiales del curso.
