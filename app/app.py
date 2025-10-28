# app/app.py
import io
from pathlib import Path

import pandas as pd
import streamlit as st

# ---------------------------
# Configuração geral da página
# ---------------------------
st.set_page_config(page_title="Totem IA – Educacional", layout="wide")

# ---------------------------
# Estado de sessão
# ---------------------------
if "interacoes" not in st.session_state:
    st.session_state.interacoes = []  # lista de dicts: {"pergunta": ..., "resposta": ...}

# ---------------------------
# Banner (opcional)
# ---------------------------
banner_path = Path("../assets/banner-totem-ia.png")
if banner_path.exists():
    st.markdown(
        f"""
        <div style="text-align:center">
          <img src="{banner_path.as_posix()}" style="max-width:100%; border-radius:12px;" />
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------------------------
# Cabeçalho
# ---------------------------
st.title("Totem IA – Protótipo (Sprint 1)")
st.caption("FIAP + FlexMidia • Educação inteligente em escolas públicas e privadas")

# ---------------------------
# Sidebar / Navegação
# ---------------------------
st.sidebar.header("Menu")
page = st.sidebar.radio(
    "Navegação",
    ["Início", "Interações (demo)", "Relatórios (simulado)", "Sobre"],
)

# ---------------------------
# Página: Início
# ---------------------------
if page == "Início":
    st.subheader("Objetivo do Totem IA")
    st.write(
        "- Interação por **voz/texto** com IA em um totem físico.\n"
        "- Coleta de dados **anonimizados** para apoiar decisões pedagógicas.\n"
        "- Integração com **sensores (presença/ultrassom, ESP32-CAM)** e nuvem."
    )
    st.info("Versão demo: interface e dados simulados para validar UX e arquitetura.")

# ---------------------------
# Página: Interações (demo)
# ---------------------------
elif page == "Interações (demo)":
    st.subheader("Faça uma pergunta ao Totem (demo)")

    pergunta = st.text_input("Ex.: 'Qual é o horário da biblioteca?'")
    if st.button("Enviar"):
        resp = (
            "Resposta (demo): em breve este módulo usará um modelo de IA com base educacional."
        )
        st.success(resp)
        st.session_state.interacoes.append(
            {"pergunta": pergunta or "", "resposta": resp}
        )

    st.divider()
    st.write("📈 Métricas rápidas (simuladas)")

    c1, c2, c3 = st.columns(3)
    c1.metric(
        "Interações nesta sessão",
        len(st.session_state.interacoes),
        "+1" if st.session_state.interacoes else "0",
    )
    c2.metric("Tempo médio (s)", "18", "-2")
    c3.metric("Satisfação (NPS)", "76", "+3")

    # Persistência simples em CSV (na pasta ../data)
    data_dir = Path("../data")
    data_dir.mkdir(parents=True, exist_ok=True)
    csv_path = data_dir / "interacoes.csv"

    if st.session_state.interacoes:
        df_save = pd.DataFrame(st.session_state.interacoes)
        df_save.to_csv(csv_path, index=False, encoding="utf-8")
        st.caption(f"💾 Interações salvas em: {csv_path.as_posix()}")

        # Download direto do CSV
        buff = io.StringIO()
        df_save.to_csv(buff, index=False, encoding="utf-8")
        st.download_button(
            label="⬇️ Baixar CSV das interações desta sessão",
            data=buff.getvalue(),
            file_name="interacoes_sessao.csv",
            mime="text/csv",
        )

# ---------------------------
# Página: Relatórios (simulado)
# ---------------------------
elif page == "Relatórios (simulado)":
    st.subheader("Fluxo de visitação / Interações")

    csv_path = Path("../data/interacoes.csv")
    if csv_path.exists():
        st.success("Dados carregados de interações salvas (CSV).")
        df = pd.read_csv(csv_path)
        st.dataframe(df, use_container_width=True)

        # Gráfico simples: contagem cumulativa de interações
        st.line_chart(
            pd.DataFrame({"qtd_interacoes": [i + 1 for i in range(len(df))]})
        )
    else:
        st.warning("Ainda não há CSV de interações. Exibindo dados simulados.")
        df = pd.DataFrame(
            {
                "hora": [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                "interacoes": [2, 4, 8, 12, 15, 10, 9, 7, 6, 5, 3],
            }
        )
        st.line_chart(df.set_index("hora"))

# ---------------------------
# Página: Sobre
# ---------------------------
elif page == "Sobre":
    st.write("**Totem IA – Educacional** • FIAP + FlexMidia")
    st.write("- Protótipo em **Streamlit (Python)**")
    st.write("- Próximos passos: sensores/ESP32-CAM, APIs em nuvem e dashboards reais.")
