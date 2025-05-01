import streamlit as st
import random
import time
import pandas as pd
from PIL import Image
import base64
import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, expon, binom
from scipy.stats import norm
from scipy.stats import t
from statsmodels.stats.proportion import proportion_confint

#Parte de Informacion Principal de la pagina 
#-------------------------------------------------------------------------------
# Configuración
st.set_page_config(layout="wide")

# Inicializar estado si no existe
if "mostrar_info" not in st.session_state:
    st.session_state.mostrar_info = False

# Función para mostrar info
def mostrar_info_estadistica():
    st.session_state.mostrar_info = True

# Función para volver al inicio
def volver_al_menu():
    st.session_state.mostrar_info = False

# Si NO se está mostrando la ventana emergente, mostrar contenido principal
if not st.session_state.mostrar_info:
    st.title("🎰 Simulador de Ruleta - Estadística Diferencial")
    st.markdown("<h3 style='color:gray;'>Universidad Cooperativa de Colombia</h3>", unsafe_allow_html=True)

    col_espacio, col_contenido, col_boton = st.columns([1, 3, 1])

    with col_contenido:
        col1, col2 = st.columns([1, 3])

        with col1:
            img = Image.open("assets/Logo_Ucc.png")
            st.image(img, width=400)

            img2 = Image.open("assets/Ruleta_Imagen.png")
            st.image(img2, width=550)

        with col2:
            st.header("📘 Justificación")
            st.write(
                "Investigar la dinámica de las ganancias en juegos de azar permite comprender mejor los modelos "
                "matemáticos que rigen estos fenómenos. Esto tiene aplicación en economía, teoría de decisiones y en la regulación "
                "de juegos de azar. Es fundamental analizar las condiciones en que los jugadores jóvenes participan en estos juegos "
                "y el impacto que puede tener la conciencia sobre las probabilidades reales de ganar o perder."
            )

    with col_boton:
        if st.button("📊 Ver Info Estadística Inferencial"):
            mostrar_info_estadistica()
        if st.button("👥 Integrantes del grupo"):
            st.markdown("### 👨‍🎓 Integrantes del Grupo")
            st.markdown("""
            - Miguel Sebastián Colmenares
            - Juan David Vargas 
            - David Quiroga
            """)
       


    st.markdown("---")
    st.subheader("🎯 Objetivo General")
    st.markdown("Analizar la evolución estadística de las ganancias y pérdidas en juegos de azar mediante modelos probabilísticos.")

    st.subheader("📌 Objetivos Específicos")
    st.markdown("""
    - Aplicar distribuciones de probabilidad para modelar los resultados esperados en la ruleta.
    - Implementar pruebas de hipótesis para evaluar estrategias de juego.
    - Estimar intervalos de confianza para las ganancias a largo plazo.
    """)
    
# Si se está mostrando la ventana emergente
else:
    colum1, colum2, colum3 = st.columns([1, 4, 1]) 
     # Columnas para centrar
    with colum2:
        st.markdown("## 📊Aplicacion De La Estadística Inferencial Con El Proyecto")
    
        st.markdown("### 📈 Estadística Inferencial")
        st.write("La estadística inferencial es una rama de la estadística que nos permite hacer conclusiones o predecir resultados sobre un grupo grande de cosas a los que llamamos 'poblacion' usando solo una parte pequeña de ese grupo 'llamada muestra'. En otras palabras, con unos pocos datos, podemos intentar entender lo que sucedería si tuviéramos toda la información disponible.")
    
        img3 = Image.open("assets/Est_Infer.png")
        st.image(img3, width=500)

        st.markdown('<h3 style="color: gray;">📝 ¿Que Metodologia utilizaremos?</h3>', unsafe_allow_html=True)
        st.write("Para este estudio, realizamos una simulación de juegos de azar con un total de 10,000 intentos o 'giros'. Cada uno" \
        " de estos giros representa una apuesta donde el jugador puede ganar o perder según ciertas probabilidades establecidas. Con estos" \
        " datos, analizamos cómo evoluciona el capital del jugador y qué patrones aparecen en las ganancias y pérdidas. Importante mencionar" \
        " que la recolección de datos se realizó mediante simulaciones en Python.")
        st.markdown('<h3 style="color: gray;">Tabla De Variables A utilizar</h3>', unsafe_allow_html=True)

        img3 = Image.open("assets/Tabla_Variables.png")
        st.image(img3, width=800)

        st.markdown('<h3 style="color: white;">Distribuciones</h3>', unsafe_allow_html=True)
        st.markdown('<h3 style="color: Gray;">Distribucion Binomial</h3>', unsafe_allow_html=True)
        
        st.write("Nos sirve para contar cuántas veces se gana y permite calcular la probabilidad de obtener un cierto número de victorias en un número fijo de intentos. ")
        img4 = Image.open("assets/Formula_Bi.png")
        st.image(img4, width=800)

        st.write(" Ejemplo: si un jugador apuesta 10 veces y cada apuesta tiene un 40% de probabilidad de éxito, podemos estimar la probabilidad de que gane exactamente 4 veces. ")
        st.markdown('<h3 style="color: Gray;">Distribucion Exponencial</h3>', unsafe_allow_html=True)
        st.write("Para medir el tiempo entre victorias.")
        img5 = Image.open("assets/Formula_Exp.png")
        st.image(img5, width=800)
        st.write("Ejemplo: Si en promedio se gana cada 5 intentos, la distribución exponencial nos permite calcular la probabilidad de que pasen más de 10 intentos sin ganar.")

        st.markdown('<h3 style="color: Gray;">Distribucion normal</h3>', unsafe_allow_html=True)
        st.write("Para analizar cómo se distribuyen las ganancias totales.")
        st.write("Sirve para estimar rangos en los que es probable que se encuentre la ganancia de un jugador después de muchas apuestas.")
        img6 = Image.open("assets/Formula_Nor.png")
        st.image(img6, width=800)



        st.markdown("### 📉 Estadística descriptiva")
        st.write("La estadística descriptiva nos ayuda a resumir y entender los datos que obtenemos en una investigación. En este proyecto, por ejemplo, usamos la estadística descriptiva para ver cómo se comportan las ganancias y pérdidas en los juegos de azar.")
        st.markdown("""
        - Saber cuántas veces se gana o se pierde.
        - Ver cuál fue la ganancia total.
        - Calcular el promedio de ganancias o pérdidas.
        - Medir qué tanto varían los resultados (si son parecidos o muy diferentes entre sí).
        - Observar patrones o tendencias en los datos.
        """)
        st.markdown("---")
        if st.button("🔙 Volver al menú principal"):
            volver_al_menu()

# Sesiones para mantener el estado
if "capital" not in st.session_state:
    st.session_state.capital = 0
if "historial" not in st.session_state:
    st.session_state.historial = []

#-------------------------------------------------------------------------------------------
#simulador 1 Por 1 ruleta
#---------------------------------------------------------------------------------------------

# Encabezado
st.title("🎲 Simulador de Ruleta - Estadística Diferencial")

# Capital inicial
capital_inicial = st.number_input("💰 Ingresa tu capital inicial:", min_value=100, step=50)
if st.button("🎯 Iniciar sesión"):
    st.session_state.capital = capital_inicial
    st.success(f"¡Comienzas con ${st.session_state.capital}!")

st.markdown("---")

# Apuesta
if st.session_state.capital > 0:
    st.subheader("📌 Haz tu apuesta")

    apuesta_monto = st.number_input("💵 Monto de la apuesta:", min_value=10, step=10, max_value=st.session_state.capital)
    color_apuesta = st.selectbox("🎨 Color a apostar", ["Rojo", "Negro", "Verde"])
    numero_apuesta = st.number_input("🎯 Número a apostar (opcional)", min_value=0, max_value=36, step=1)

    if st.button("🎬 Girar ruleta"):
        st.write("🔄 Girando la ruleta... espera 1 segundos")
        time.sleep(1)

        # Resultado aleatorio
        resultado = random.randint(0, 36)
        rojos = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
        negros = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]

        if resultado == 0:
            color_resultado = "Verde"
        elif resultado in rojos:
            color_resultado = "Rojo"
        else:
            color_resultado = "Negro"

        # Mostrar resultado
        st.info(f"Resultado: {resultado} - {color_resultado}")

        # Cálculo de ganancia
        ganancia = 0
        acierto_color = color_apuesta == color_resultado
        acierto_numero = numero_apuesta == resultado

        if acierto_color and acierto_numero:
            ganancia = apuesta_monto * 36  # prioriza el mayor pago
        elif acierto_numero:
            ganancia = apuesta_monto * 36
        elif acierto_color:
            ganancia = apuesta_monto * 2
        else:
            ganancia = 0

        # Actualizar capital
        neto = ganancia - apuesta_monto
        st.session_state.capital += neto
        st.success(f"Ganancia: ${ganancia} | Capital actual: ${st.session_state.capital}")

        # Registrar en historial
        st.session_state.historial.append({
            "Número": resultado,
            "Color": color_resultado,
            "Apuesta Nº": numero_apuesta,
            "Apuesta Color": color_apuesta,
            "Ganancia": ganancia,
            "Capital restante": st.session_state.capital
        })

        st.markdown("---")

    # Historial
    if st.session_state.historial:
        st.subheader("📊 Historial de Tiradas")
        df = pd.DataFrame(st.session_state.historial)
        st.dataframe(df, use_container_width=True)

else:
    st.warning("Ingresa un capital inicial para comenzar.")

#-----------------------------------------------------------------------------------------------------
#Parte Simulacion Y Graficas
#---------------------------------------------------------------------------------------------------



st.title("🎰 Simulación de Ruleta - Proyecto de Distribuciones")

# Inputs
capital_inicial = st.number_input("Capital inicial", value=1000)
apuesta = st.number_input("Valor de cada apuesta", value=10)
giros = st.number_input("Número de giros (apuestas)", value=1000)

# Botón de simulación
if st.button("Iniciar Simulación"):
    capital = capital_inicial
    historial_capital = []
    victorias = 0
    giros_totales = int(giros)
    resultados = []
    ganancias = []
    intentos_entre_victorias = []

    giros_sin_ganar = 0

    for i in range(giros_totales):
        resultado = random.randint(0, 36)
        eleccion = random.choice(["rojo", "negro"])
        es_rojo = resultado in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
        gano = False

        if (eleccion == "rojo" and es_rojo) or (eleccion == "negro" and not es_rojo and resultado != 0):
            capital += apuesta
            victorias += 1
            gano = True
            if giros_sin_ganar > 0:
                intentos_entre_victorias.append(giros_sin_ganar)
            giros_sin_ganar = 0
        else:
            capital -= apuesta
            giros_sin_ganar += 1

        historial_capital.append(capital)
        resultados.append("Victoria" if gano else "Derrota")
        ganancias.append(capital - capital_inicial)

    # Guardar en session_state para mantener los datos
    st.session_state.df = pd.DataFrame({
        "Giro": list(range(1, giros_totales+1)),
        "Capital": historial_capital,
        "Resultado": resultados,
        "Ganancia acumulada": ganancias
    })
    st.session_state.victorias = victorias
    st.session_state.frecuencia_relativa = victorias / giros_totales
    st.session_state.intentos_entre_victorias = intentos_entre_victorias
    st.session_state.ganancias = ganancias
    st.session_state.historial_capital = historial_capital
    st.session_state.capital_final = capital
    st.session_state.capital_inicial = capital_inicial

# Mostrar resultados solo si ya se generaron
if "df" in st.session_state:

    df = st.session_state.df
    victorias = st.session_state.victorias
    frecuencia_relativa = st.session_state.frecuencia_relativa
    intentos_entre_victorias = st.session_state.intentos_entre_victorias
    ganancias = st.session_state.ganancias
    historial_capital = st.session_state.historial_capital
    capital_inicial = st.session_state.capital_inicial
    capital = st.session_state.capital_final

    st.subheader("📥 Descargar Datos")
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Descargar CSV", csv, "simulacion_ruleta.csv", "text/csv")

    st.subheader("📊 Estadísticas Generales")
    st.write(f"🔢 Número total de apuestas realizadas: {len(historial_capital)}")
    st.write(f"🏆 Número de victorias: {victorias}")
    st.write(f"📈 Frecuencia relativa de éxito: {frecuencia_relativa:.4f}")
    st.write(f"💰 Ganancia final: {capital - capital_inicial}")
    st.write(f"📉 Desviación estándar de ganancias: {np.std(ganancias):.2f}")

    # ➤ Distribución Binomial
    from scipy.stats import binom

    st.subheader("📌 Distribución Binomial - Número de Victorias")
    fig1, ax1 = plt.subplots()

    # Parámetros de la binomial
    n = len(historial_capital)
    p = frecuencia_relativa
    media = n * p
    desviacion = np.sqrt(n * p * (1 - p))

    # Limitar el rango a ±3σ
    x_min = max(0, int(media - 3 * desviacion))
    x_max = min(n, int(media + 3 * desviacion) + 1)
    x = np.arange(x_min, x_max)

    # Gráfico
    ax1.vlines(victorias, 0, 1, colors='r', linestyles='--', label=f"Victorias reales: {victorias}")
    ax1.plot(x, binom.pmf(x, n, p), 'bo', label="PMF Binomial")
    ax1.set_title("Probabilidad de obtener victorias")
    ax1.set_xlabel("Victorias")
    ax1.set_ylabel("Probabilidad")
    ax1.legend()
    st.pyplot(fig1)


    # ➤ Distribución Exponencial - intentos entre victorias
    if intentos_entre_victorias:
        st.subheader("📌 Distribución Exponencial - Intentos entre victorias")
        media_intentos = np.mean(intentos_entre_victorias)
        st.write(f"⏳ Tiempo promedio entre victorias (intentos): {media_intentos:.2f}")
        fig2, ax2 = plt.subplots()
        ax2.hist(intentos_entre_victorias, bins=20, density=True, alpha=0.6, color='orange', edgecolor='black')
        x_exp = np.linspace(0, max(intentos_entre_victorias), 100)
        y_exp = expon.pdf(x_exp, scale=media_intentos)
        ax2.plot(x_exp, y_exp, 'r-', label="Ajuste Exponencial")
        ax2.set_title("Tiempo (intentos) entre victorias")
        ax2.set_xlabel("Intentos entre victorias")
        ax2.set_ylabel("Densidad")
        ax2.legend()
        st.pyplot(fig2)

    # ➤ Distribución Normal - Ganancia acumulada
    st.subheader("📌 Distribución Normal - Ganancia acumulada")
    media_ganancia = np.mean(ganancias)
    std_ganancia = np.std(ganancias)
    fig3, ax3 = plt.subplots()
    ax3.hist(ganancias, bins=30, density=True, alpha=0.6, color='skyblue', edgecolor='black')
    x_norm = np.linspace(min(ganancias), max(ganancias), 100)
    y_norm = norm.pdf(x_norm, media_ganancia, std_ganancia)
    ax3.plot(x_norm, y_norm, 'r-', label="Ajuste Normal")
    ax3.set_title("Distribución de la Ganancia Acumulada")
    ax3.set_xlabel("Ganancia")
    ax3.set_ylabel("Densidad")
    ax3.legend()
    st.pyplot(fig3)

    # ➤ Gráfica de evolución del capital
    st.subheader("📈 Evolución del Capital")
    fig4, ax4 = plt.subplots()
    ax4.plot(historial_capital, label="Capital en el tiempo", color='green')
    ax4.axhline(capital_inicial, color='gray', linestyle='--', label="Capital Inicial")
    ax4.set_xlabel("Giros")
    ax4.set_ylabel("Capital")
    ax4.legend()
    st.pyplot(fig4)

  # ➤ Intervalos de Confianza
    st.subheader("📐 Intervalos de Confianza (95%)")

    # IC proporción poblacional (Wilson)
    li_prop, ls_prop = proportion_confint(victorias, giros_totales, alpha=0.05, method='wilson')
    st.write(f"✅ Intervalo de confianza para la proporción de victorias: [{li_prop:.4f}, {ls_prop:.4f}]")

    # IC media poblacional de la ganancia (Normal)
    z = 1.96  # Z para 95%
    media_ganancia = np.mean(ganancias)
    std_ganancia = np.std(ganancias, ddof=1)
    margen_error = z * std_ganancia / np.sqrt(len(ganancias))
    li_media = media_ganancia - margen_error
    ls_media = media_ganancia + margen_error
    st.write(f"📊 Intervalo de confianza para la media de ganancias: [{li_media:.2f}, {ls_media:.2f}]")

    # ➤ Gráfica de IC para la media
    st.subheader("📉 Visualización del Intervalo de Confianza para la Media de Ganancias")
    fig_ic, ax_ic = plt.subplots()
    ax_ic.hist(ganancias, bins=30, color='lightblue', edgecolor='black', density=True)
    ax_ic.axvline(li_media, color='red', linestyle='--', label=f"LI: {li_media:.2f}")
    ax_ic.axvline(ls_media, color='green', linestyle='--', label=f"LS: {ls_media:.2f}")
    ax_ic.axvline(media_ganancia, color='blue', label=f"Media: {media_ganancia:.2f}")
    ax_ic.set_title("IC para la Media de Ganancias")
    ax_ic.set_xlabel("Ganancia")
    ax_ic.set_ylabel("Densidad")
    ax_ic.legend()
    st.pyplot(fig_ic)

    # Grados de libertad (n-1, donde n es el número de muestras)
    grados_libertad = len(ganancias) - 1

    # Cálculo de la t-Student
    t_value = t.ppf(0.975, grados_libertad)  # Valor t para 95% de confianza

    # Creación del gráfico
    from scipy.stats import t, norm
    import matplotlib.pyplot as plt
    import numpy as np

    from scipy.stats import t
    import matplotlib.pyplot as plt
    import numpy as np

    st.subheader("📊 Distribución t-Student con Intervalos de Confianza")

    # Datos
    n = len(ganancias)
    media_ganancia = np.mean(ganancias)
    std_ganancia = np.std(ganancias, ddof=1)
    error_estandar = std_ganancia / np.sqrt(n)

    # Intervalo de confianza (95%)
    grados_libertad = n - 1
    li_media = t.ppf(0.025, df=grados_libertad, loc=media_ganancia, scale=error_estandar)
    ls_media = t.ppf(0.975, df=grados_libertad, loc=media_ganancia, scale=error_estandar)

    # Rango enfocado alrededor de la media ± 4 errores estándar
    x_min = media_ganancia - 4 * error_estandar
    x_max = media_ganancia + 4 * error_estandar
    x = np.linspace(x_min, x_max, 500)
    y = t.pdf(x, df=grados_libertad, loc=media_ganancia, scale=error_estandar)

    # Crear gráfico
    fig, ax = plt.subplots()
    ax.hist(ganancias, bins=30, density=True, alpha=0.6, color='lightgreen', edgecolor='black')

    # Curva t-Student
    ax.plot(x, y, 'r-', label="Distribución t-Student")

    # Área sombreada entre los límites del IC
    x_sombra = np.linspace(li_media, ls_media, 300)
    y_sombra = t.pdf(x_sombra, df=grados_libertad, loc=media_ganancia, scale=error_estandar)
    ax.fill_between(x_sombra, y_sombra, color='skyblue', alpha=0.5, label="IC 95%")

    # Líneas de referencia
    ax.axvline(li_media, color='blue', linestyle='--', label=f"LI: {li_media:.2f}")
    ax.axvline(ls_media, color='blue', linestyle='--', label=f"LS: {ls_media:.2f}")
    ax.axvline(media_ganancia, color='black', label=f"Media: {media_ganancia:.2f}")

    # Estética
    ax.set_xlim(x_min, x_max)  # Zoom al área útil
    ax.set_title("Distribución t-Student centrada en la media")
    ax.set_xlabel("Ganancia")
    ax.set_ylabel("Densidad")
    ax.legend()

    # Mostrar en Streamlit
    st.pyplot(fig)

    # ➤ Visualización del IC para la Proporción de Victorias
    st.subheader("📉 Visualización del Intervalo de Confianza para la Proporción de Victorias")
    fig_prop, ax_prop = plt.subplots()

    # Barra para la frecuencia relativa observada
    ax_prop.bar(["Proporción Observada"], [frecuencia_relativa], color='mediumseagreen', alpha=0.7, label='Frecuencia Relativa')

    # Líneas para el IC
    ax_prop.errorbar(["Proporción Observada"], [frecuencia_relativa], 
                    yerr=[[frecuencia_relativa - li_prop], [ls_prop - frecuencia_relativa]],
                    fmt='o', color='black', capsize=10, label='IC 95%')

    ax_prop.set_ylim(0, 1)
    ax_prop.set_ylabel("Proporción")
    ax_prop.set_title("Intervalo de Confianza para la Proporción de Victorias")
    ax_prop.legend()
    st.pyplot(fig_prop)



    st.markdown(f"""
    <p style="font-size:20px;">
    Tras simular <strong>{giros_totales} giros</strong> de ruleta, se obtuvo una <strong>frecuencia relativa de victorias</strong> de <strong>{frecuencia_relativa:.4f}</strong>, valor coherente con la probabilidad esperada al apostar aleatoriamente entre "rojo" y "negro" (alrededor de 18/37 ≈ 0.4865). La <strong>ganancia final</strong> fue de <strong>{capital - capital_inicial} unidades</strong>, con una <strong>desviación estándar</strong> de <strong>{np.std(ganancias):.2f}</strong>, lo que refleja la volatilidad del juego.

    📌 <strong>  <p style="font-size:20px;">Distribución Binomial</strong>  
    El comportamiento del número total de victorias sigue una distribución binomial, dado que cada giro puede modelarse como un experimento de Bernoulli (éxito o fracaso). El gráfico mostró que el valor real de victorias se encuentra dentro del rango de mayor probabilidad, indicando que el juego es consistente con la teoría probabilística.

    📌 <strong>  <p style="font-size:20px;">Distribución Exponencial</strong>  
    El tiempo (en intentos) entre victorias se ajustó a una distribución exponencial, lo cual es esperado, ya que en procesos aleatorios la ocurrencia del siguiente éxito es independiente del anterior. El histograma junto a la curva de densidad mostró un buen ajuste visual, y se estimó una media de <strong>{np.mean(intentos_entre_victorias):.2f} intentos</strong> entre cada victoria.

    📌 <strong>  <p style="font-size:20px;">Distribución Normal</strong>  
    La ganancia acumulada a lo largo del tiempo se aproximó a una distribución normal, especialmente gracias al efecto del Teorema Central del Límite, ya que se suman muchas variables aleatorias. El histograma con el ajuste gaussiano reflejó una distribución simétrica con media <strong>{media_ganancia:.2f}</strong> y desviación estándar <strong>{std_ganancia:.2f}</strong>.

    📈 <strong>  <p style="font-size:20px;">Evolución del Capital</strong>  
    La gráfica mostró una trayectoria oscilante del capital a lo largo de los giros, con altibajos naturales en un proceso aleatorio. Aunque hubo rachas de pérdida, el saldo final terminó siendo <strong>{"positivo" if capital - capital_inicial >= 0 else "negativo"}</strong>.

    🔍 <strong>  <p style="font-size:20px;">Intervalos de Confianza</strong>  
    - Para la <strong>  <p style="font-size:20px;">proporción de victorias</strong>, el intervalo del 95% se ubicó entre <strong>[{li_prop:.4f}, {ls_prop:.4f}]</strong>, lo cual encierra la probabilidad real esperada si se repite el experimento muchas veces.
    - Para la <strong>  <p style="font-size:20px;">media de las ganancias</strong>, el intervalo del 95% fue <strong>[{li_media:.2f}, {ls_media:.2f}]</strong>, lo que permite evaluar si en el largo plazo se gana o se pierde de manera consistente.

    📊 <strong>  <p style="font-size:20px;">Aplicación de la Estadística Inferencial</strong>  
    A través del uso de estimaciones puntuales, intervalos de confianza y pruebas de ajuste de distribuciones, esta simulación ejemplifica cómo la estadística inferencial permite generalizar resultados a partir de una muestra aleatoria. Aunque los datos provienen de una simulación específica, se logra extraer conclusiones válidas sobre el comportamiento probabilístico del juego de ruleta, prediciendo tendencias futuras y evaluando la fiabilidad de los resultados observados.

    ✅ En resumen, la simulación muestra que, aunque el azar rige cada giro de la ruleta, los resultados globales tienden a seguir patrones estadísticos previsibles. La presencia de distribuciones teóricas claras y el respaldo de los intervalos de confianza validan el comportamiento simulado. Esto refuerza el valor del análisis probabilístico y estadístico, especialmente desde la óptica de la inferencia, incluso en escenarios dominados por la aleatoriedad.
      <p style="font-size:20px;">
    """, unsafe_allow_html=True)
