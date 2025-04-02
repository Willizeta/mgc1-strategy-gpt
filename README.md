# 🟡 Estrategia de Trading Short para Micro Gold Futures (MGC1!) + ChatGPT

Este proyecto incluye una estrategia técnica para operar en corto en MGC1 (Micro Gold Futures) con optimización automática de parámetros y asistencia inteligente usando la API de OpenAI (ChatGPT).

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Willizeta/mgc1-strategy-gpt/blob/main/simulador_mgc1_optimizacion_chatgpt.ipynb)

---

## ✅ Características

- Simulación de estrategia short con:
  - EMA de largo plazo
  - RSI con filtro mínimo
  - Supertrend (ATR + factor)
  - Filtros de horario (8:00 a 20:00 UTC)
  - Filtro de volumen y RSI < 30
  - Stop Loss, Take Profit y Trailing Stop
- Datos simulados tipo TradingView
- Optimización de parámetros en múltiples intervalos de tiempo
- Exportación de resultados a LibreOffice `.ods`
- ChatGPT integrado para sugerencias inteligentes

---

## 🤖 ¿Qué puede hacer ChatGPT?

- Analizar los resultados de optimización
- Sugerir combinaciones óptimas
- Responder preguntas como:
  - “¿Qué intervalo tiene el mayor profit factor con al menos 5 trades?”
  - “¿Qué configuración debo ajustar si el winrate es bajo?”

---

## 🧪 Requisitos

```bash
pip install openai pandas numpy
