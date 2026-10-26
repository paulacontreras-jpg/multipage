import streamlit as st

st.set_page_config(
    page_title="Interfaces Multimodales",
    page_icon="📡",
    layout="wide",
)

# Estilos personalizados
st.markdown(
    """
    <style>
    .hero {
        padding: 2.5rem 2rem;
        border-radius: 18px;
        background: linear-gradient(135deg, #00b09b 0%, #1e3c72 100%);
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 24px rgba(30, 60, 114, 0.35);
    }
    .hero h1 {
        font-size: 2.8rem;
        letter-spacing: 3px;
        margin-bottom: 0.3rem;
        color: white;
    }
    .hero p { font-size: 1.2rem; opacity: 0.9; margin: 0; }

    .badge {
        display: inline-block;
        margin-top: 1rem;
        padding: 0.3rem 0.9rem;
        border-radius: 999px;
        background: rgba(255, 255, 255, 0.18);
        font-size: 0.85rem;
    }

    .card {
        padding: 1.5rem;
        border-radius: 16px;
        background: rgba(128, 128, 128, 0.08);
        border: 1px solid rgba(128, 128, 128, 0.25);
        margin-bottom: 0.8rem;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .card:hover {
        transform: translateY(-6px);
        box-shadow: 0 10px 24px rgba(0, 0, 0, 0.18);
    }
    .card .icon { font-size: 3rem; }
    .card h3 { margin: 0.5rem 0; }
    .card p  { opacity: 0.85; }
    .tag {
        display: inline-block;
        padding: 0.2rem 0.7rem;
        border-radius: 999px;
        font-size: 0.8rem;
        background: #00b09b22;
        color: #00b09b;
        margin-right: 0.3rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Encabezado
st.markdown(
    """
    <div class="hero">
        <h1>📡 INTERFACES MULTIMODALES</h1>
        <p>Control de actuadores por MQTT</p>
        <span class="badge">Voz · Botones · Slider</span>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write(
    "Selecciona una de las aplicaciones en el menú lateral "
    "o usa los accesos directos de abajo."
)

# Tarjetas con accesos directos
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown(
        """
        <div class="card">
            <div class="icon">🎙️</div>
            <h3>Control por voz</h3>
            <p>Da órdenes habladas para activar y desactivar actuadores.</p>
            <span class="tag">Voz</span>
            <span class="tag">Manos libres</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.page_link(
        "pages/1_Control_por_voz.py",
        label="Abrir control por voz",
        icon="🎙️",
        use_container_width=True,
    )

with col2:
    st.markdown(
        """
        <div class="card">
            <div class="icon">🎛️</div>
            <h3>Control con botones y slider</h3>
            <p>Enciende, apaga y ajusta valores de forma manual.</p>
            <span class="tag">Botones</span>
            <span class="tag">Slider</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.page_link(
        "pages/2_Control_MQTT.py",
        label="Abrir control con botones y slider",
        icon="🎛️",
        use_container_width=True,
    )

st.divider()

# Cómo funciona
st.subheader("⚙️ ¿Cómo funciona?")
c1, c2, c3 = st.columns(3)
c1.metric("1. Interfaz", "Voz / Botones")
c2.metric("2. Mensaje", "MQTT")
c3.metric("3. Actuador", "Respuesta")

st.info("💡 Tus órdenes se publican como mensajes MQTT y el actuador reacciona al recibirlos.")

# Barra lateral
with st.sidebar:
    st.header("🧭 Navegación")
    st.caption("Elige una página para controlar tus actuadores.")
    st.markdown("---")
    st.caption("Hecho con ❤️ usando Streamlit")
