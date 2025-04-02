
import papermill as pm
import datetime
import os

# Crear carpeta de salida si no existe
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Nombre dinámico con fecha/hora
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_nb = f"{output_dir}/simulador_resultado_{timestamp}.ipynb"

# Ejecutar notebook y guardar copia ejecutada
pm.execute_notebook(
    'simulador_mgc1_optimizacion_chatgpt.ipynb',
    output_nb,
    kernel_name='python3',
    parameters=dict()
)

print(f"✅ Notebook ejecutado correctamente y guardado en: {output_nb}")
