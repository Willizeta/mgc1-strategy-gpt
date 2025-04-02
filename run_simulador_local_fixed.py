
import papermill as pm
import datetime
import os

# 🔐 Define aquí tu API Key de OpenAI de forma segura (opcional: usar .env o gestor de secretos)
os.environ["OPENAI_API_KEY"] = "sk-REEMPLAZA_CON_TU_API_KEY"

# Crear carpeta de salida si no existe
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Nombre dinámico del archivo
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_nb = f"{output_dir}/simulador_resultado_{timestamp}.ipynb"

# Ejecutar el notebook
pm.execute_notebook(
    'simulador_mgc1_optimizacion_chatgpt_FINAL_OK.ipynb',
    output_nb,
    kernel_name='python3'
)

print(f"✅ Notebook ejecutado y guardado en: {output_nb}")
