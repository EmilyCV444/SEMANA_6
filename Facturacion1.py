# Dado el subtotal, calcular el IGV y el total

import financieros
subtotal = 800.5
print(f"Subtotal: {subtotal}")
print(f"IGV: {financieros.obtenerIGVconSubtotal(subtotal): .2f}")
print(f"Total: {financieros.obtenerTotalconSubtotal(subtotal):.2f}")
