import datetime

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


df = pd.DataFrame(np.random.randn(200, 3),columns=['a', 'b', 'c'])



def write(s):
    st.write(s)



write("this is altair_chart")
ch = alt.Chart(df).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.altair_chart(ch)


write("this is area chart")
st.area_chart(df)


write("this is mp3 file music")
st.audio(open("./musci.mp3", 'rb').read(), format="audio/mp3")



if st.button("click me and see balloons animation !"):
    st.balloons()


write("this is bar_chart")
st.bar_chart(df)


write("this is bokeh_chart")
from bokeh.plotting import figure
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]
p = figure(title='simple line example',x_axis_label='x',y_axis_label='y')
p.line(x, y, legend_label='Trend', line_width=2)
st.bokeh_chart(p, use_container_width=True)




write("these are buttons")
btns = [st.button("button hello"), st.button("button goodbye")]
txt = st.text("...", )
if btns[0]:
    txt.text("button hello is clicked !")
elif btns[1]:
    txt.text("button goodbye is clicked !")


st.caption("this is caption text")



write("this is camera_input")
pic = st.camera_input("click me and take a photo")
if pic:
    st.image(pic)


write("this is checkbox")
ch = [st.checkbox("i am checkbox1"), st.checkbox("i am checkbox2")]
if ch:
    write(ch)


write("this is code tag !")
st.code("""
print('Hello World !')
""")



write("this columns tag")
col1, col2 = st.columns([3, 1], gap="large")
with col1:
    st.header("image 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")
with col2:
    st.header("image 2")
    st.image("https://static.streamlit.io/examples/cat.jpg")



write("this is tabs tag")
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)



with st.container():
    st.write("This is inside the container")
    st.bar_chart(np.random.randn(50, 3))
st.write("This is outside the container")



write("this is dataframe tag with max-min styles")
st.dataframe(df.style.highlight_max(axis=0, props=f"background-color: green; color: white"), width=1000, height=500, )
st.dataframe(df.style.highlight_min(axis=0, props=f"background-color: red; color: white"), width=1000, height=500, )


write("this is date_input tag")
date = st.date_input("when were you born ?", datetime.date(2005, 8, 8))
st.text(f"you were born in : {date}")


write("this is download_button tag")
st.download_button(label="click me and download csv file",
                   data=df.to_csv().encode('utf-8'),
                   mime="csv")
with open("./mentors.db") as data:
    st.download_button(label="downloading database",
                       data=data,
                       file_name="mentors database",
                       mime="sqlite/db")


write("this is expander tag")
expander = st.expander("See explanation")
expander.write("""this is expander image """)
expander.image("https://static.streamlit.io/examples/dice.jpg")



write("this is empty")
placeholder = st.empty()
import time
with st.empty():
    for seconds in range(60):
        st.write(f"⏳ {seconds} seconds have passed")
    time.sleep(1)
    st.write("✔️ 1 minute over!")


write("this is error")
st.error("this is error ! text", icon="❓")


write("this is file_uploader tag")
file = st.file_uploader("choose file")
if file is not None:
    data = pd.read_csv(file)
    write(data)


write("this is form tag")
with st.form("register"):
    slider = st.slider("this is slider")
    ch = [st.checkbox("i am checkbox1", key="1"), st.checkbox("i am checkbox2", key="2")]
    submit = st.form_submit_button("this is submit button !")
    if submit:
        write(f"slider : {slider}\n"
              f"checkbox : {ch}")


write("this is graphviz_chart tag")
import graphviz as graphviz
graph = graphviz.Digraph()
graph.edge('zulfiya', 'iqrorjon')
graph.edge('zulfiya', 'madina')
graph.edge('zulfiya', 'zeboxon')
graph.edge('iqboljon', 'iqrorjon')
graph.edge('iqboljon', 'madina')
graph.edge('iqboljon', 'zeboxon')
st.graphviz_chart(graph)


write("this is header tag")
st.header("this is header text")


write("this is help tag")
def doc_ed_func():
    """
    this is help text
    """
    pass
st.help(doc_ed_func)


write("this is image tag")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/640px-Image_created_with_a_mobile_phone.png",
         caption="this is an example image")


write("this is info tag")
st.info("this is info text", icon="ℹ")


write("this is json tag")
st.json({
    'a': [1,2,3],
    'b': {1:'a'},
    'c': [['a'], [1,2]]
})


write("this is latex tag")
st.latex(r'''a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =\sum_{k=0}^{n-1} ar^k =a \left(\frac{1-r^{n}}{1-r}\right)''')



write("this is line_chart tag")
arr = np.random.randn(20, 1)
st.line_chart(arr)


write("this is map tag")
df = pd.DataFrame(np.random.randn(10, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon'])
st.map(df, zoom=15)


write("this is markdown tag")
st.markdown('Streamlit is **_really_ cool**.')

write("this is metric tag")
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")


write("this is _main.multiselect tag")
names = st._main.multiselect("what is your name?",
                     ['iqrorjon', 'islomjon', 'asadbek'],
                     ['iqrorjon'])
st.write("your name is : ", names)


write("this is _main.number_input tag")
number = st._main.number_input("enter any number ", min_value=10, max_value=2022)
st.write("you entered number is : ", number)


write("this is _main.progress tag")
import time
pr_bar = st._main.progress(0)
for i in range(100):
    time.sleep(0.1)
    pr_bar.progress(i)


write("this is _main.pyplot tag")
import matplotlib.pyplot as plt
import numpy as np
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
st.pyplot(fig)


write("this is _main.success tag")
st.success('This is a success message!', icon="✅")


write("this is _main.table tag")
df = pd.DataFrame(np.random.randn(10, 5), columns = ('col %d' % i for i in range(5)))
st.table(df)



write("this is _main.text")
st._main.text("this is simple text")


write("this is  _main.text_area tag")
text = st._main.text_area(label="enter any text",
                          value="iqrorjon",
                          height=100,
                          max_chars=1000)
st.write("you entered text is : ", text)



write("this is _main.text_input tag")
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)


write("this is _main.time_input tag")
t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)


write("this is _main.title tag")
st._main.title("this is simple title text")


write("this is _main.vega_lite_chart tag")
df = pd.DataFrame(np.random.randn(200, 3), columns = ['a', 'b', 'c'])
st.vega_lite_chart(df, {'mark': {'type': 'circle', 'tooltip': True}, 'encoding': {'x': {'field': 'a', 'type': 'quantitative'},'y': {'field': 'b', 'type': 'quantitative'},'size': {'field': 'c', 'type': 'quantitative'},'color': {'field': 'c', 'type': 'quantitative'},},})


write("this is _main.video tag")
st._main.video("https://www.youtube.com/watch?v=iVaSEQL8564")


write("this is _main.warning tag")
st._main.warning('This is a warning', icon="⚠️")


write("this is _main.write tag")
st._main.write("this is simple text !")

write("this is _main.color_picker tag")
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)