col1, col2 = st.columns([2, 3])
with col1:
    st.markdown("**Top Investments (₹)**")
    st.dataframe(big_series)

with col2:
    st.markdown("**Top Investments Chart**")
    fig, ax = plt.subplots()
    ax.barh(big_series.index[::-1], big_series.values[::-1])
    ax.set_xlabel("Investment Amount")
    st.pyplot(fig)
