import streamlit as st

st.set_page_config(
    page_title="Welcome Page",
    page_icon="👋",
)

st.write("# Selamat Datang! 👋")

st.markdown(
    """
    Aplikasi ini dibuat untuk para petani agar memudahkan
    dalam prakiraan waktu tanam demi mendapatkan hasil yang
    maksimal.
    **👈 Pilih menu pada sidebar** untuk melihat grafik sesuai
    rentang waktu yang dibutuhkan!
    

"""
)

crops = ["Padi", "Teh", "Jagung", "Cabai", "Lada", "Kelapa Sawit"]
ideal_rainfall = {
    "Padi": (125, 167),
    "Teh": (166, 209),
    "Jagung": (85, 200),
    "Cabai": (100, 200),
    "Lada": (166, 209),
    "Kelapa Sawit": (150, 167)
}    
st.markdown("### Curah Hujan Bulanan Ideal")

min_rainfall_all = min([range_[0] for range_ in ideal_rainfall.values()])
max_rainfall_all = max([range_[1] for range_ in ideal_rainfall.values()])

col1,col2,col3= st.columns(3)

col1.markdown(f"<div style='text-align: center;font-weight: bold;'>{crops[0]}</div>", unsafe_allow_html=True)
col1.image(f"assets/{crops[0]}.png", caption=f"{ideal_rainfall[crops[0]][0]} mm - {ideal_rainfall[crops[0]][1]} mm")

col2.markdown(f"<div style='text-align: center;font-weight: bold;'>{crops[1]}</div>", unsafe_allow_html=True)
col2.image(f"assets/{crops[1]}.png", caption=f"{ideal_rainfall[crops[1]][0]} mm - {ideal_rainfall[crops[1]][1]} mm")

col3.markdown(f"<div style='text-align: center;font-weight: bold;'>{crops[2]}</div>", unsafe_allow_html=True)
col3.image(f"assets/{crops[2]}.png", caption=f"{ideal_rainfall[crops[2]][0]} mm - {ideal_rainfall[crops[2]][1]} mm")

col4, col5, col6 = st.columns(3)

col4.markdown(f"<div style='text-align: center;font-weight: bold;'>{crops[3]}</div>", unsafe_allow_html=True)
col4.image(f"assets/{crops[3]}.png", caption=f"{ideal_rainfall[crops[3]][0]} mm - {ideal_rainfall[crops[3]][1]} mm")

col5.markdown(f"<div style='text-align: center;font-weight: bold;'>{crops[4]}</div>", unsafe_allow_html=True)
col5.image(f"assets/{crops[4]}.png", caption=f"{ideal_rainfall[crops[4]][0]} mm - {ideal_rainfall[crops[4]][1]} mm")

col6.markdown(f"<div style='text-align: center;font-weight: bold;'>{crops[5]}</div>", unsafe_allow_html=True)
col6.image(f"assets/{crops[5]}.png", caption=f"{ideal_rainfall[crops[5]][0]} mm - {ideal_rainfall[crops[5]][1]} mm")

st.markdown("""
### Referensi
    - Padi (https://d1wqtxts1xzle7.cloudfront.net/82953618/1966-libre.pdf?1648680387=&response-content-disposition=inline%3B+filename%3DINITIAL_VALIDATION_OF_WeRise_TECHNOLOGY.pdf&Expires=1717604516&Signature=bpNWQQEfPdET9vUU3x-jPQW8KRBRuUhJJR6f71lLygRROOWH9NS9ZP-D-4LGaSnqdKuWqvDOxFz8nxtl--rNkUJAXcQ6-VrUBWeE3iOepevDM--q9rVdMk5HTCMHpb7KokYg9bq7MN6vJgSfYxBvu5cZb2n4vEmyy1-BWTpATTas48CCJBZDgiS0oU-hm3NvVGmW5bdHVQWdVGtYL-IMN1-T1QIVwV50XuVcbW7l~VegMHQW443seq5AyrvS5tTRO2mO94a932ii1OtK8evbXF7GbGhPxMVi5NrJvQcfOsxldPiSSAdFXhEnr2oB2IAs2vtOg42SfOLdIqqfHvzi0A__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA)
    - Teh (https://repository.ub.ac.id/id/eprint/179601/)
    - Jagung (https://ejournal.undip.ac.id/index.php/ilmulingkungan/article/download/16198/pdf)
    - Cabai (https://j-ptiik.ub.ac.id/index.php/j-ptiik/article/view/214)
    - Lada (https://repository.ub.ac.id/165306/)
    - Kelapa Sawit (https://ppnp.e-journal.id/agro/article/view/290)
"""
)

