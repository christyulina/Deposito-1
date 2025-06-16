import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("📊 Dashboard Monitoring Deposito Bulanan")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_excel("TESTING.xlsx", sheet_name="Sheet1")
    df['BULAN'] = pd.Categorical(df['BULAN'], categories=[
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ], ordered=True)
    return df

df = load_data()

# Filter berdasarkan kategori
kategori_terpilih = st.multiselect(
    "Pilih kategori yang ingin ditampilkan:",
    options=df["KATEGORI"].unique(),
    default=list(df["KATEGORI"].unique())
)

df_filtered = df[df["KATEGORI"].isin(kategori_terpilih)]

# Ringkasan
st.subheader("📌 Ringkasan Data")
st.dataframe(df_filtered)

# Plot
st.subheader("📈 Grafik Tren Bulanan")

monthly_summary = df_filtered.groupby(['BULAN', 'KATEGORI'])['AMOUNT'].sum().reset_index()

plt.figure(figsize=(10, 5))
sns.lineplot(data=monthly_summary, x='BULAN', y='AMOUNT', hue='KATEGORI', marker='o')
plt.ylabel("Jumlah (Rp)")
plt.xlabel("Bulan")
plt.title("Tren Deposito dan Bunga per Bulan")
plt.grid(True)
st.pyplot(plt.gcf())

# Footer
st.markdown("---")
st.caption("© 2025 PT ASDP Indonesia Ferry — Dashboard Deposito oleh keuangan perbendaharaan")
