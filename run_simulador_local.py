import papermill as pm

input_path = "simulador_resultado_VALIDADO_FINAL_con_api.ipynb"
output_path = "output/simulador_resultado_EJECUTADO.ipynb"

# Ejecutar el notebook
pm.execute_notebook(
    input_path,
    output_path,
    parameters={}
)

print("✅ Simulación completada. Resultado guardado en:", output_path)