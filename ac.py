import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from PIL import Image

#=======================================================================================================================

df = pd.read_csv('./function11_1.csv')
df2 = pd.read_csv('./function11_1.csv',parse_dates=['Start_Date'],index_col='Start_Date')
df3 = pd.read_csv('./function11_2.csv',parse_dates = ['Start_Date'])

image = Image.open('aladay.jpg')

#====================================================================================================================
print(df2.index) 
df2['day_of_week']=df2.index.day_of_week
df2['day_of_month']=df2.index.day
df2['month']=df2.index.month
print(df2['day_of_week'])
print(df2)


df4 = df2
df4_week = df4.groupby('day_of_week')['Total_kWh','carpark','home','other','street','work'].sum().reset_index()
print(df4_week)


days = {0:'Mon',1:'Tues',2:'Weds',3:'Thurs',4:'Fri',5:'Sat',6:'Sun'}
df4_week['day_of_week'] = df4_week['day_of_week'].apply(lambda x: days[x])
print(df4_week)
df2['day_of_week'] = df2['day_of_week'].apply(lambda x: days[x])

df_by_month = df2.resample('M').sum()


st.subheader("Electric Vehicle Charging Energy Consumption Analysis")
chart_visual = 'bar chart'

df_s = pd.DataFrame([[3,'spring'],[4,'spring'],[5,'spring'],[6,'summer'],[7,'summer'],[8,'summer'],[9,'autumn'],[10,'autumn'],[11,'autumn'],[12,'winter'],[1,'winter'],[2,'winter']],columns=['month','season'])
# df_s.set_index('month',inplace=True)
print(df_s)
df2.reset_index(inplace=True)

df22 = pd.merge(df2,df_s)
print(df22)


df_spring = df22[df22['month'].between(3,5)]
df_summer = df22[df22['month'].between(6,8)]
df_autumn = df22[df22['month'].between(9,11)]

t = df22['month']==12
tt = df22['month']==1
ttt = df22['month']==2

df_winter = df22[t|tt|ttt]
print(df_winter)

labels = ['carpark','home','street','work','other']
vc1 = df_spring['carpark'].values.sum()
vc2 = df_summer['carpark'].values.sum()
vc3 = df_autumn['carpark'].values.sum()
vc4 = df_winter['carpark'].values.sum()
print(vc1)
vh1 = df_spring['home'].values.sum()
vh2 = df_summer['home'].values.sum()
vh3 = df_autumn['home'].values.sum()
vh4 = df_winter['home'].values.sum()
print(vh1)
vs1 = df_spring['street'].values.sum()
vs2 = df_summer['street'].values.sum()
vs3 = df_autumn['street'].values.sum()
vs4 = df_winter['street'].values.sum()
print(vs1)
vw1 = df_spring['work'].values.sum()
vw2 = df_summer['work'].values.sum()
vw3 = df_autumn['work'].values.sum()
vw4 = df_winter['work'].values.sum()
print(vw1)
vo1 = df_spring['other'].values.sum()
vo2 = df_summer['other'].values.sum()
vo3 = df_autumn['other'].values.sum()
vo4 = df_winter['other'].values.sum()

pie_spring = [vc1,vh1,vs1,vw1,vo1]
pie_summer = [vc2,vh2,vs2,vw2,vo2]
pie_autumn = [vc3,vh3,vs3,vw3,vo3]
pie_winter = [vc4,vh4,vs4,vw4,vo4]
print(pie_winter)

st.sidebar.header(":triangular_flag_on_post: Adjustment Function Sidebar")
selected_status_2 = st.sidebar.selectbox('Select time interval', options = ['day', 'week','month','season'])
if selected_status_2 =='season':
    selected_status_6 = st.sidebar.selectbox('Select season', options = ['spring', 'summer','autumn','winter'])
    selected_status_7 = st.sidebar.selectbox('Select Chart type', options = ['bar chart', 'pie chart','box chart'])

    if selected_status_7 =='bar chart':
        if selected_status_6 =='spring':
            fig = go.Figure(data=[
            go.Bar(name='carpark', x=df_spring['season'], y=df_spring['carpark']),
            go.Bar(name='home', x=df_spring['season'], y=df_spring['home']),
            go.Bar(name='street', x=df_spring['season'], y=df_spring['street']),
            go.Bar(name='work', x=df_spring['season'], y=df_spring['work']),
            go.Bar(name='other', x=df_spring['season'], y=df_spring['other'])
            ])
            # Change the bar mode
            fig.update_layout(barmode='group', width=800, height=500,legend=dict(font=dict(size= 19)))
            # set x axis label
            fig.update_xaxes( title_text = "Charging piles in different regions", title_font = {"size": 20},tickfont_size=17)
            fig.update_yaxes( title_text = "Charging times", title_font = {"size": 20},tickfont_size=15)
            fig.update_layout(
                title=dict(
                    text="The number of times charging piles are used in "+ selected_status_6+" in different regions" ,
                    x=0.5,
                    y=0.93,
                    font=dict(
                        family="Arial",
                        size=22,
                        color='#000000'
                    )
                ))

        elif selected_status_6 =='summer':
            fig = go.Figure(data=[
            go.Bar(name='carpark', x=df_summer['season'], y=df_summer['carpark']),
            go.Bar(name='home', x=df_summer['season'], y=df_summer['home']),
            go.Bar(name='street', x=df_summer['season'], y=df_summer['street']),
            go.Bar(name='work', x=df_summer['season'], y=df_summer['work']),
            go.Bar(name='other', x=df_summer['season'], y=df_summer['other'])
            ])
            # Change the bar mode
            fig.update_layout(barmode='group', width=800, height=500,legend=dict(font=dict(size= 19)))
            # set x axis label
            fig.update_xaxes( title_text = "Charging piles in different regions", title_font = {"size": 20},tickfont_size=17)
            fig.update_yaxes( title_text = "Charging times", title_font = {"size": 20},tickfont_size=15)
            fig.update_layout(
                title=dict(
                    text="The number of times charging piles are used in "+ selected_status_6+" in different regions" ,
                    x=0.5,
                    y=0.93,
                    font=dict(
                        family="Arial",
                        size=22,
                        color='#000000'
                    )
                ))
        elif selected_status_6 =='autumn':
            fig = go.Figure(data=[
            go.Bar(name='carpark', x=df_autumn['season'], y=df_autumn['carpark']),
            go.Bar(name='home', x=df_autumn['season'], y=df_autumn['home']),
            go.Bar(name='street', x=df_autumn['season'], y=df_autumn['street']),
            go.Bar(name='work', x=df_autumn['season'], y=df_autumn['work']),
            go.Bar(name='other', x=df_autumn['season'], y=df_autumn['other'])
            ])
            # Change the bar mode
            fig.update_layout(barmode='group', width=800, height=500,legend=dict(font=dict(size= 19)))
            # set x axis label
            fig.update_xaxes( title_text = "Charging piles in different regions", title_font = {"size": 20},tickfont_size=17)
            fig.update_yaxes( title_text = "Charging times", title_font = {"size": 20},tickfont_size=15)
            fig.update_layout(
                title=dict(
                    text="The number of times charging piles are used in "+ selected_status_6+" in different regions" ,
                    x=0.5,
                    y=0.93,
                    font=dict(
                        family="Arial",
                        size=22,
                        color='#000000'
                    )
                ))
        elif selected_status_6 =='winter':
            fig = go.Figure(data=[
            go.Bar(name='carpark', x=df_winter['season'], y=df_winter['carpark']),
            go.Bar(name='home', x=df_winter['season'], y=df_winter['home']),
            go.Bar(name='street', x=df_winter['season'], y=df_winter['street']),
            go.Bar(name='work', x=df_winter['season'], y=df_winter['work']),
            go.Bar(name='other', x=df_winter['season'], y=df_winter['other'])
            ])
            # Change the bar mode
            fig.update_layout(barmode='group', width=800, height=500,legend=dict(font=dict(size= 19)))
            # set x axis label
            fig.update_xaxes( title_text = "Charging piles in different regions", title_font = {"size": 20},tickfont_size=17)
            fig.update_yaxes( title_text = "Charging times", title_font = {"size": 20},tickfont_size=15)
            fig.update_layout(
                title=dict(
                    text="The number of times charging piles are used in "+ selected_status_6+" in different regions" ,
                    x=0.5,
                    y=0.93,
                    font=dict(
                        family="Arial",
                        size=22,
                        color='#000000'
                    )
                ))
    elif selected_status_7 =='pie chart':
        if selected_status_6 =='spring':
            fig = go.Figure(data=[go.Pie(labels=labels, values=pie_spring, textinfo='label+percent',insidetextorientation='radial',textfont=dict(size=25))])
            fig.update_layout(width=800, height=600,legend=dict(font=dict(size= 19)))
            fig.update_layout(
                title=dict(
                    text="The number of times charging piles are used in "+ selected_status_6+" in different regions" ,
                    x=0.5,
                    y=0.93,
                    font=dict(
                        family="Arial",
                        size=22,
                        color='#000000'
                    )
                ))
        elif selected_status_6 =='summer':
            fig = go.Figure(data=[go.Pie(labels=labels, values=pie_summer, textinfo='label+percent',insidetextorientation='radial',textfont=dict(size=25))])
            fig.update_layout(width=800, height=600,legend=dict(font=dict(size= 19)))
            fig.update_layout(
                title=dict(
                    text="The number of times charging piles are used in "+ selected_status_6+" in different regions" ,
                    x=0.5,
                    y=0.93,
                    font=dict(
                        family="Arial",
                        size=22,
                        color='#000000'
                    )
                ))
        elif selected_status_6 =='autumn':
            fig = go.Figure(data=[go.Pie(labels=labels, values=pie_autumn, textinfo='label+percent',insidetextorientation='radial',textfont=dict(size=25))])
            fig.update_layout(width=800, height=600,legend=dict(font=dict(size= 19)))
            fig.update_layout(
                title=dict(
                    text="The number of times charging piles are used in "+ selected_status_6+" in different regions" ,
                    x=0.5,
                    y=0.93,
                    font=dict(
                        family="Arial",
                        size=22,
                        color='#000000'
                    )
                ))
        elif selected_status_6 =='winter':
            fig = go.Figure(data=[go.Pie(labels=labels, values=pie_winter, textinfo='label+percent',insidetextorientation='radial',textfont=dict(size=25))])
            fig.update_layout(width=800, height=600,legend=dict(font=dict(size= 19)))
            fig.update_layout(
                title=dict(
                    text="The number of times charging piles are used in "+ selected_status_6+" in different regions" ,
                    x=0.5,
                    y=0.93,
                    font=dict(
                        family="Arial",
                        size=22,
                        color='#000000'
                    )
                ))
    elif selected_status_7 =='box chart':
        if selected_status_6 =='spring':
            fig = go.Figure()

            fig.add_trace(go.Box(
                y=df_spring['carpark'],
                x=df_spring['season'],
                name='carpark',
                marker_color='#C48888'
            ))
            fig.add_trace(go.Box(
                y=df_spring['home'],
                x=df_spring['season'],
                name='home',
                marker_color='#B9B973'
            ))
            fig.add_trace(go.Box(
                y=df_spring['street'],
                x=df_spring['season'],
                name='street',
                marker_color='#81C0C0'
            ))
            fig.add_trace(go.Box(
                y=df_spring['work'],
                x=df_spring['season'],
                name='work',
                marker_color='#A6A6D2'
            ))
            fig.add_trace(go.Box(
                y=df_spring['other'],
                x=df_spring['season'],
                name='other',
                marker_color='#C07AB8'
            ))

            fig.update_layout(
                boxmode='group', # group together boxes of the different traces for each value of x
                width=800, height=500,legend=dict(font=dict(size= 19))
            )
            # set x axis label
            fig.update_xaxes( title_text = "Charging piles in different regions", title_font = {"size": 20},tickfont_size=17)
            fig.update_yaxes( title_text = "Charging times", title_font = {"size": 20},tickfont_size=15)
            fig.update_layout(
                title=dict(
                    text="The number of times charging piles are used in "+ selected_status_6+" in different regions" ,
                    x=0.5,
                    y=0.93,
                    font=dict(
                        family="Arial",
                        size=22,
                        color='#000000'
                    )
                ))
        elif selected_status_6 =='summer':
            fig = go.Figure()

            fig.add_trace(go.Box(
                y=df_summer['carpark'],
                x=df_summer['season'],
                name='carpark',
                marker_color='#C48888'
            ))
            fig.add_trace(go.Box(
                y=df_summer['home'],
                x=df_summer['season'],
                name='home',
                marker_color='#B9B973'
            ))
            fig.add_trace(go.Box(
                y=df_summer['street'],
                x=df_summer['season'],
                name='street',
                marker_color='#81C0C0'
            ))
            fig.add_trace(go.Box(
                y=df_summer['work'],
                x=df_summer['season'],
                name='work',
                marker_color='#A6A6D2'
            ))
            fig.add_trace(go.Box(
                y=df_summer['other'],
                x=df_summer['season'],
                name='other',
                marker_color='#C07AB8'
            ))

            fig.update_layout(
                boxmode='group', # group together boxes of the different traces for each value of x
                width=800, height=500,legend=dict(font=dict(size= 19))
            )
            # set x axis label
            fig.update_xaxes( title_text = "Charging piles in different regions", title_font = {"size": 20},tickfont_size=17)
            fig.update_yaxes( title_text = "Charging times", title_font = {"size": 20},tickfont_size=15)
            fig.update_layout(
                title=dict(
                    text="The number of times charging piles are used in "+ selected_status_6+" in different regions" ,
                    x=0.5,
                    y=0.93,
                    font=dict(
                        family="Arial",
                        size=22,
                        color='#000000'
                    )
                ))
        elif selected_status_6 =='autumn':
            fig = go.Figure()

            fig.add_trace(go.Box(
                y=df_autumn['carpark'],
                x=df_autumn['season'],
                name='carpark',
                marker_color='#C48888'
            ))
            fig.add_trace(go.Box(
                y=df_autumn['home'],
                x=df_autumn['season'],
                name='home',
                marker_color='#B9B973'
            ))
            fig.add_trace(go.Box(
                y=df_autumn['street'],
                x=df_autumn['season'],
                name='street',
                marker_color='#81C0C0'
            ))
            fig.add_trace(go.Box(
                y=df_autumn['work'],
                x=df_autumn['season'],
                name='work',
                marker_color='#A6A6D2'
            ))
            fig.add_trace(go.Box(
                y=df_autumn['other'],
                x=df_autumn['season'],
                name='other',
                marker_color='#C07AB8'
            ))

            fig.update_layout(
                boxmode='group', # group together boxes of the different traces for each value of x
                width=800, height=500,legend=dict(font=dict(size= 19))
            )
            # set x axis label
            fig.update_xaxes( title_text = "Charging piles in different regions", title_font = {"size": 20},tickfont_size=17)
            fig.update_yaxes( title_text = "Charging times", title_font = {"size": 20},tickfont_size=15)
            fig.update_layout(
                title=dict(
                    text="The number of times charging piles are used in "+ selected_status_6+" in different regions" ,
                    x=0.5,
                    y=0.93,
                    font=dict(
                        family="Arial",
                        size=22,
                        color='#000000'
                    )
                ))
        else:
            fig = go.Figure()

            fig.add_trace(go.Box(
                y=df_winter['carpark'],
                x=df_winter['season'],
                name='carpark',
                marker_color='#C48888'
            ))
            fig.add_trace(go.Box(
                y=df_winter['home'],
                x=df_winter['season'],
                name='home',
                marker_color='#B9B973'
            ))
            fig.add_trace(go.Box(
                y=df_winter['street'],
                x=df_winter['season'],
                name='street',
                marker_color='#81C0C0'
            ))
            fig.add_trace(go.Box(
                y=df_winter['work'],
                x=df_winter['season'],
                name='work',
                marker_color='#A6A6D2'
            ))
            fig.add_trace(go.Box(
                y=df_winter['other'],
                x=df_winter['season'],
                name='other',
                marker_color='#C07AB8'
            ))

            fig.update_layout(
                boxmode='group', # group together boxes of the different traces for each value of x
                width=800, height=500,legend=dict(font=dict(size= 19))
            )
            # set x axis label
            fig.update_xaxes( title_text = "Charging piles in different regions", title_font = {"size": 20},tickfont_size=17)
            fig.update_yaxes( title_text = "Charging times", title_font = {"size": 20},tickfont_size=15)
            fig.update_layout(
                title=dict(
                    text="The number of times charging piles are used in "+ selected_status_6+" in different regions" ,
                    x=0.5,
                    y=0.93,
                    font=dict(
                        family="Arial",
                        size=22,
                        color='#000000'
                    )
                ))
    st.plotly_chart(fig)

    if selected_status_7 =='bar chart':
        if selected_status_6 =='spring':
            st.markdown("""
            -------------------------------------------------------------------------------------
            :round_pushpin:Simple Description:
            """)
            st.markdown("""
            In spring, the usage of charging piles in different locations in Dundee, Scotland, 
            the charging piles in the home location are used the most, and the charging piles 
            in the park location are used the least.
            """)
            st.markdown("""
            -------------------------------------------------------------------------------------
            """)
        elif selected_status_6 =='summer':
            st.markdown("""
            -------------------------------------------------------------------------------------
            :round_pushpin:Simple Description:
            """)
            st.markdown("""
            In summer, the usage of charging piles in different locations in Dundee, Scotland, 
            the charging piles in the home location are used the most, and the charging piles 
            in the park location are used the least.
            """)
            st.markdown("""
            -------------------------------------------------------------------------------------
            """)
        elif selected_status_6 =='autumn':
            st.markdown("""
            -------------------------------------------------------------------------------------
            :round_pushpin:Simple Description:
            """)
            st.markdown("""
            In autumn, the usage of charging piles in different locations in Dundee, Scotland, 
            the charging piles in the home location are used the most, and the charging piles 
            in the park location are used the least.
            """)
            st.markdown("""
            -------------------------------------------------------------------------------------
            """)
        elif selected_status_6 =='winter':
            st.markdown("""
            -------------------------------------------------------------------------------------
            :round_pushpin:Simple Description:
            """)
            st.markdown("""
            In winter, the usage of charging piles in different locations in Dundee, Scotland, 
            the charging piles in the home location are used the most, and the charging piles 
            in the park location are used the least.
            """)
            st.markdown("""
            -------------------------------------------------------------------------------------
            """)
    elif selected_status_7 =='pie chart':
        if selected_status_6 =='spring':
            st.markdown("""
            -------------------------------------------------------------------------------------
            :round_pushpin:Simple Description:
            """)
            st.markdown("""
            The use of charging piles at different locations in Dundee, Scotland, in the spring. The 
            charging pile in the home location was used the highest by 25.8%, and the charging pile 
            in the park location was used the lowest by 10.4%.
            """)
            st.markdown("""
            -------------------------------------------------------------------------------------
            """)
        elif selected_status_6 =='summer':
            st.markdown("""
            -------------------------------------------------------------------------------------
            :round_pushpin:Simple Description:
            """)
            st.markdown("""
            The use of charging piles at different locations in Dundee, Scotland, in the summer. 
            The charging pile in the home location was used the highest by 28.7%, and the charging 
            pile in the park location was used the lowest by 10.8%.
            """)
            st.markdown("""
            -------------------------------------------------------------------------------------
            """)
        elif selected_status_6 =='autumn':
            st.markdown("""
            -------------------------------------------------------------------------------------
            :round_pushpin:Simple Description:
            """)
            st.markdown("""
            The use of charging piles at different locations in Dundee, Scotland, in the autumn. 
            The charging pile in the home location was used the highest by 27.4%, and the charging 
            pile in the park location was used the lowest by 10.8%.
            """)
            st.markdown("""
            -------------------------------------------------------------------------------------
            """)
        elif selected_status_6 =='winter':
            st.markdown("""
            -------------------------------------------------------------------------------------
            :round_pushpin:Simple Description:
            """)
            st.markdown("""
            The use of charging piles at different locations in Dundee, Scotland, in the winter. 
            The charging pile in the home location was used the highest by 26.8%, and the charging 
            pile in the park location was used the lowest by 9.35%.
            """)
            st.markdown("""
            -------------------------------------------------------------------------------------
            """)
    elif selected_status_7 =='box chart':
        if selected_status_6 =='spring':
            st.markdown("""
            -------------------------------------------------------------------------------------
            :round_pushpin:Simple Description:
            """)
            st.markdown("""
            The use of charging piles at different locations in Dundee, Scotland, in the spring. 
            The charging pile in the home location has the largest frequency range, and the charging 
            pile in the park location has the smallest frequency range.
            """)
            st.markdown("""
            -------------------------------------------------------------------------------------
            """)
        elif selected_status_6 =='summer':
            st.markdown("""
            -------------------------------------------------------------------------------------
            :round_pushpin:Simple Description:
            """)
            st.markdown("""
            The use of charging piles at different locations in Dundee, Scotland, in the summer. 
            The charging pile in the home location has the largest frequency range, and the charging 
            pile in the park location has the smallest frequency range.
            """)
            st.markdown("""
            -------------------------------------------------------------------------------------
            """)
        elif selected_status_6 =='autumn':
            st.markdown("""
            -------------------------------------------------------------------------------------
            :round_pushpin:Simple Description:
            """)
            st.markdown("""
            The use of charging piles at different locations in Dundee, Scotland, in the autumn. 
            The charging pile in the home location has the largest frequency range, and the charging 
            pile in the park location has the smallest frequency range.
            """)
            st.markdown("""
            -------------------------------------------------------------------------------------
            """)
        elif selected_status_6 =='winter':
            st.markdown("""
            -------------------------------------------------------------------------------------
            :round_pushpin:Simple Description:
            """)
            st.markdown("""
            The use of charging piles at different locations in Dundee, Scotland, in the winter. 
            The charging pile in the home location has the largest frequency range, and the charging 
            pile in the park location has the smallest frequency range.
            """)
            st.markdown("""
            -------------------------------------------------------------------------------------
            """)


else:
    selected_status_3 = st.sidebar.selectbox('Select object', options = ['carpark', 'home','street','work','other','Total_kWh'])
    selected_status_5 = st.sidebar.selectbox('Select Chart type', options = ['bar chart', 'line chart','box chart'])


    if selected_status_5 == 'bar chart':
        
        if selected_status_2 == 'day':
            fig = px.bar(df, x='Start_Date', y= selected_status_3, width=750, height=450)
            fig.update_traces(marker_color='rgb(166, 204, 227)', marker_line_color='rgb(166, 204, 227)', marker_line_width=1.5)
            # set x axis label
            fig.update_xaxes( title_text = "Days of charging per day", title_font = {"size": 20},tickfont_size=15)
            fig.update_yaxes( title_text = "Charging times("+selected_status_3+")", title_font = {"size": 20},tickfont_size=15)
            fig.update_layout(
                title=dict(
                    text="Daily charging pile usage ("+ selected_status_3 + ")" ,
                    x=0.5,
                    y=0.93,
                    font=dict(
                        family="Arial",
                        size=22,
                        color='#000000'
                    )
                ))
        elif selected_status_2 == 'week':
            fig = px.bar(df4_week, x='day_of_week', y=selected_status_3, width=750, height=450)
            fig.update_traces(marker_color='rgb(161, 178, 133)', marker_line_color='rgb(161, 178, 133)', marker_line_width=1.5)
            # set x axis label
            fig.update_xaxes( title_text = "Charging days a week", title_font = {"size": 20},tickfont_size=15)
            fig.update_yaxes( title_text = "Charging times("+selected_status_3+")", title_font = {"size": 20},tickfont_size=15)
            fig.update_layout(
                title=dict(
                    text="Weekly charging pile usage ("+ selected_status_3 + ")" ,
                    x=0.5,
                    y=0.93,
                    font=dict(
                        family="Arial",
                        size=22,
                        color='#000000'
                    )
                ))
        else:
            fig = px.bar(df_by_month, x=df_by_month .index, y=selected_status_3, width=750, height=450 )
            fig.update_traces(marker_color='rgb(200, 138, 113)', marker_line_color='rgb(200, 138, 113)', marker_line_width=1.5)
            # set x axis label
            fig.update_xaxes( title_text = "Charging days per month", title_font = {"size": 20},tickfont_size=15)
            fig.update_yaxes( title_text = "Charging times("+selected_status_3+")", title_font = {"size": 20},tickfont_size=15)
            fig.update_layout(
                title=dict(
                    text="Monthly charging pile usage ("+ selected_status_3 + ")" ,
                    x=0.5,
                    y=0.93,
                    font=dict(
                        family="Arial",
                        size=22,
                        color='#000000'
                    )
                ))

    elif selected_status_5 == 'line chart':
        
        if selected_status_2 == 'day':
            fig = px.line(df, x='Start_Date', y= selected_status_3, width=750, height=450)
            fig.update_traces(line_color='rgb(166, 204, 227)', marker_line_width=1.5)
            # set x axis label
            fig.update_xaxes( title_text = "Days of charging per day", title_font = {"size": 20},tickfont_size=15)
            fig.update_yaxes( title_text = "Charging times("+selected_status_3+")", title_font = {"size": 20},tickfont_size=15)
            fig.update_layout(
                title=dict(
                    text="Daily charging pile usage ("+ selected_status_3 + ")" ,
                    x=0.5,
                    y=0.93,
                    font=dict(
                        family="Arial",
                        size=22,
                        color='#000000'
                    )
                ))
        elif selected_status_2 == 'week':
            fig = px.line(df4_week, x='day_of_week', y=selected_status_3, width=750, height=450)
            fig.update_traces(line_color='rgb(161, 178, 133)', marker_line_width=1.5)
            # set x axis label
            fig.update_xaxes( title_text = "Charging days a week", title_font = {"size": 20},tickfont_size=15)
            fig.update_yaxes( title_text = "Charging times("+selected_status_3+")", title_font = {"size": 20},tickfont_size=15)
            fig.update_layout(
                title=dict(
                    text="Weekly charging pile usage ("+ selected_status_3 + ")" ,
                    x=0.5,
                    y=0.93,
                    font=dict(
                        family="Arial",
                        size=22,
                        color='#000000'
                    )
                ))
        else:
            fig = px.line(df_by_month, x=df_by_month .index, y=selected_status_3, width=750, height=450)
            fig.update_traces(line_color='rgb(200, 138, 113)', marker_line_width=1.5)
            # set x axis label
            fig.update_xaxes( title_text = "Charging days per month", title_font = {"size": 20},tickfont_size=15)
            fig.update_yaxes( title_text = "Charging times("+selected_status_3+")", title_font = {"size": 20},tickfont_size=15)
            fig.update_layout(
                title=dict(
                    text="Monthly charging pile usage ("+ selected_status_3 + ")" ,
                    x=0.5,
                    y=0.93,
                    font=dict(
                        family="Arial",
                        size=22,
                        color='#000000'
                    )
                ))

    elif selected_status_5 == 'box chart':
        if selected_status_2 == 'day':
            fig = px.box(df2, x='day_of_month', y= selected_status_3, width=750, height=450)
            fig.update_traces(line_color='rgb(166, 204, 227)', marker_line_width=1.5)
            # set x axis label
            fig.update_xaxes( title_text = "Days of charging per day", title_font = {"size": 20},tickfont_size=15)
            fig.update_yaxes( title_text = "Charging times("+selected_status_3+")", title_font = {"size": 20},tickfont_size=15)
            fig.update_layout(
                title=dict(
                    text="Daily charging pile usage ("+ selected_status_3 + ")" ,
                    x=0.5,
                    y=0.93,
                    font=dict(
                        family="Arial",
                        size=22,
                        color='#000000'
                    )
                ))
        elif selected_status_2 == 'week':
            fig = px.box(df2, x='day_of_week', y=selected_status_3, width=750, height=450)
            fig.update_traces(line_color='rgb(161, 178, 133)', marker_line_width=1.5)
            # set x axis label
            fig.update_xaxes( title_text = "Charging days a week", title_font = {"size": 20},tickfont_size=15)
            fig.update_yaxes( title_text = "Charging times("+selected_status_3+")", title_font = {"size": 20},tickfont_size=15)
            fig.update_layout(
                title=dict(
                    text="Weekly charging pile usage ("+ selected_status_3 + ")" ,
                    x=0.5,
                    y=0.93,
                    font=dict(
                        family="Arial",
                        size=22,
                        color='#000000'
                    )
                ))
        else:
            fig = px.box(df2, x='month', y=selected_status_3, width=750, height=450)
            fig.update_traces(line_color='rgb(200, 138, 113)', marker_line_width=1.5)
            # set x axis label
            fig.update_xaxes( title_text = "Charging days per month", title_font = {"size": 20},tickfont_size=15)
            fig.update_yaxes( title_text = "Charging times("+selected_status_3+")", title_font = {"size": 20},tickfont_size=15)
            fig.update_layout(
                title=dict(
                    text="Monthly charging pile usage ("+ selected_status_3 + ")" ,
                    x=0.5,
                    y=0.93,
                    font=dict(
                        family="Arial",
                        size=22,
                        color='#000000'
                    )
                ))


    
    st.plotly_chart(fig)



    if selected_status_5 == 'bar chart':
        if selected_status_2 == 'day':    
            df_max = df[selected_status_3].max()
            df_min = df[selected_status_3].min()
            df_mean = df[selected_status_3].mean()
            st.write('Max value: {:.2f}'.format(df_max))
            st.write('Min value: {:.2f}'.format(df_min))
            st.write('Mean value: {:.2f}'.format(df_mean))
            st.image(image,width=700)
        elif selected_status_2 == 'week':
            df_max = df4_week[selected_status_3].max()
            df_min = df4_week[selected_status_3].min()
            df_mean = df4_week[selected_status_3].mean()
            st.write('Max value: {:.2f}'.format(df_max))
            st.write('Min value: {:.2f}'.format(df_min))
            st.write('Mean value: {:.2f}'.format(df_mean))
        else:
            df_max = df_by_month[selected_status_3].max()
            df_min = df_by_month[selected_status_3].min()
            df_mean = df_by_month[selected_status_3].mean()
            st.write('Max value: {:.2f}'.format(df_max))
            st.write('Min value: {:.2f}'.format(df_min))
            st.write('Mean value: {:.2f}'.format(df_mean))
    elif selected_status_5 == 'line chart':
        if selected_status_2 == 'day':    
            df_max = df[selected_status_3].max()
            df_min = df[selected_status_3].min()
            df_mean = df[selected_status_3].mean()
            st.write('Max value: {:.2f}'.format(df_max))
            st.write('Min value: {:.2f}'.format(df_min))
            st.write('Mean value: {:.2f}'.format(df_mean))
        elif selected_status_2 == 'week':
            df_max = df4_week[selected_status_3].max()
            df_min = df4_week[selected_status_3].min()
            df_mean = df4_week[selected_status_3].mean()
            st.write('Max value: {:.2f}'.format(df_max))
            st.write('Min value: {:.2f}'.format(df_min))
            st.write('Mean value: {:.2f}'.format(df_mean))
        else:
            df_max = df_by_month[selected_status_3].max()
            df_min = df_by_month[selected_status_3].min()
            df_mean = df_by_month[selected_status_3].mean()
            st.write('Max value: {:.2f}'.format(df_max))
            st.write('Min value: {:.2f}'.format(df_min))
            st.write('Mean value: {:.2f}'.format(df_mean))

    if selected_status_5 == 'bar chart':
        if selected_status_3 == 'carpark':
            if selected_status_2 == 'day':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                At the charging pile in the park in Dundee, Scotland, the number of times 
                the electric vehicle charging pile is used every day is up to 15 times, the 
                lowest is 0 times, and the average is about 7 times.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            elif selected_status_2 == 'week':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                Charging piles at park locations in Dundee, Scotland, gradually increased 
                usage from Monday to Thursday, and dropped significantly from Friday to Sunday. 
                The weekly use of electric vehicle charging piles reached a maximum of 386 times, 
                a minimum of 241 times, and an average of about 348 times.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            else:
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                Charging piles at a park site in Dundee, Scotland, UK. The highest usage was in 
                November and the lowest in July. The maximum number of electric vehicle charging 
                piles used per month is 234 times, the minimum is 163 times, and the average is 
                about 203 times.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
        elif selected_status_3 == 'home':
            if selected_status_2 == 'day':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                At the home charging point in Dundee, Scotland, the number of electric vehicle 
                charging points used per week reached 44 times at the highest and 0 times at the 
                minimum, with an average of about 18 times.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            elif selected_status_2 == 'week':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                In the home location of Dundee, Scotland, the usage of charging piles from Monday 
                to Friday is significantly different from that from Saturday to Sunday. The weekly 
                use of electric vehicle charging piles reached a maximum of 1,264 times and a minimum 
                of 225 times, with an average of about 916 times.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            else:
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                Charging piles at home in Dundee, Scotland, UK. The highest usage was in November 
                and the lowest in May. The maximum number of electric vehicle charging piles 
                used per month is 625 times, the minimum is 437 times, and the average is about 
                534 times.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
        elif selected_status_3 == 'street':
            if selected_status_2 == 'day':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                In Dundee, Scotland, the street location charging piles, the maximum number of 
                electric vehicle charging points is 25 times a day, the minimum is 1 time, and 
                the average is about 12 times.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            elif selected_status_2 == 'week':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                In the street location of Dundee, Scotland, the use of charging piles gradually increases 
                from Monday to Friday, and decreases from Saturday to Sunday. The weekly use of electric 
                vehicle charging piles reached a maximum of 710 times, a minimum of 412 times, and an average 
                of about 624 times.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            else:
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                A charging pile at a street location in Dundee, Scotland, UK. From November to April, 
                the number of times of use gradually decreased, and the number of times of use increased 
                in May. The maximum number of electric vehicle charging piles used per month is 420 times 
                and the minimum is 300 times, with an average of about 364 times.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
        elif selected_status_3 == 'work':
            if selected_status_2 == 'day':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                In the charging piles at the workplace in Dundee, Scotland, the maximum number of 
                electric vehicle charging piles used every day is 58 times, and the minimum is 1 time, 
                with an average of about 16 times.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            elif selected_status_2 == 'week':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                At the workplace in Dundee, Scotland, the usage is highest on Thursday and lowest from Saturday 
                to Sunday. The weekly use of electric vehicle charging piles reached a maximum of 1,055 times, 
                a minimum of 336 times, and an average of about 817 times.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            else:
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                Charging piles at the workplace in Dundee, Scotland, UK. The highest usage is in November 
                and the lowest in July to August. The maximum number of electric vehicle charging piles used 
                per month is 617 times, the minimum is 364 times, and the average is about 476 times.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
        elif selected_status_3 == 'other':
            if selected_status_2 == 'day':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                In other locations in Dundee, Scotland, the number of electric vehicle charging points 
                used per day reaches 29 times at the highest and 0 times at the lowest, with an average 
                of about 13 times.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            elif selected_status_2 == 'week':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                In other locations in Dundee, Scotland, the number of charging points is high from Monday to Friday, 
                and the usage is significantly lowest from Saturday to Sunday. The weekly use of electric vehicle 
                charging piles reached a maximum of 813 times and a minimum of 378 times, with an average of about 
                671 times.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            else:
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                Charging piles at other locations in Dundee, Scotland, UK. The highest usage was in March and 
                the lowest in July. The monthly usage of electric vehicle charging piles reaches a maximum of 
                502 times, a minimum of 267 times, and an average of about 392 times.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
        elif selected_status_3 == 'Total_kWh':
            if selected_status_2 == 'day':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                The charging energy consumption of electric vehicle charging piles in Dundee, Scotland, 
                UK, the highest daily usage is 818.86, the lowest is 20.25, and the average is about 404.38.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            elif selected_status_2 == 'week':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                The charging energy consumption of electric vehicle charging piles in Dundee, Scotland, is very high 
                from Monday to Friday, and the consumption is obviously the lowest from Saturday to Sunday. The weekly 
                usage of electric vehicle charging piles reached a maximum of 25,302.91, a minimum of 11,235.46, and 
                an average of about 20,969.75.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            else:
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                Energy consumption for charging an electric vehicle charging point at a location in Dundee, 
                Scotland, UK. The usage has gradually decreased since January, and the number of usage has 
                increased since September. The monthly usage of electric vehicle charging piles reached a maximum 
                of 15,954.35, a minimum of 8,052.67, and an average of about 12,232.35.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)

    elif selected_status_5 == 'line chart':
        if selected_status_3 == 'carpark':
            if selected_status_2 == 'day':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                At the charging pile in the park in Dundee, Scotland, the number of times 
                the electric vehicle charging pile is used every day is up to 15 times, the 
                lowest is 0 times, and the average is about 7 times.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            elif selected_status_2 == 'week':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                Charging piles at park locations in Dundee, Scotland, gradually increased 
                usage from Monday to Wednesday, and dropped significantly from Thursday to Sunday. 
                The weekly use of electric vehicle charging piles reached a maximum of 386 times, 
                a minimum of 241 times, and an average of about 348 times.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            else:
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                Charging piles at a park site in Dundee, Scotland, UK. The highest usage was in 
                November and the lowest in July. The maximum number of electric vehicle charging 
                piles used per month is 234 times, the minimum is 163 times, and the average is 
                about 203 times.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
        elif selected_status_3 == 'home':
            if selected_status_2 == 'day':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                At the home charging point in Dundee, Scotland, the number of electric vehicle 
                charging points used per week reached 44 times at the highest and 0 times at the 
                minimum, with an average of about 18 times.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            elif selected_status_2 == 'week':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                In the home location of Dundee, Scotland, the usage of charging piles from Monday 
                to Friday is significantly different from that from Saturday to Sunday. The weekly 
                use of electric vehicle charging piles reached a maximum of 1,264 times and a minimum 
                of 225 times, with an average of about 916 times.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            else:
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                Charging piles at home in Dundee, Scotland, UK. The highest usage was in November 
                and the lowest in May. The maximum number of electric vehicle charging piles 
                used per month is 625 times, the minimum is 437 times, and the average is about 
                534 times.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
        elif selected_status_3 == 'street':
            if selected_status_2 == 'day':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                In Dundee, Scotland, the street location charging piles, the maximum number of 
                electric vehicle charging points is 25 times a day, the minimum is 1 time, and 
                the average is about 12 times.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            elif selected_status_2 == 'week':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                In the street location of Dundee, Scotland, the use of charging piles gradually increases 
                from Monday to Friday, and decreases from Saturday to Sunday. The weekly use of electric 
                vehicle charging piles reached a maximum of 710 times, a minimum of 412 times, and an average 
                of about 624 times.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            else:
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                A charging pile at a street location in Dundee, Scotland, UK. From November to April, 
                the number of times of use gradually decreased, and the number of times of use increased 
                in May. The maximum number of electric vehicle charging piles used per month is 420 times 
                and the minimum is 300 times, with an average of about 364 times.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
        elif selected_status_3 == 'work':
            if selected_status_2 == 'day':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                In the charging piles at the workplace in Dundee, Scotland, the maximum number of 
                electric vehicle charging piles used every day is 58 times, and the minimum is 1 time, 
                with an average of about 16 times.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            elif selected_status_2 == 'week':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                At the workplace in Dundee, Scotland, the usage is highest on Thursday and lowest from Saturday 
                to Sunday. The weekly use of electric vehicle charging piles reached a maximum of 1,055 times, 
                a minimum of 336 times, and an average of about 817 times.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            else:
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                Charging piles at the workplace in Dundee, Scotland, UK. The highest usage is in November 
                and the lowest in July to August. The maximum number of electric vehicle charging piles used 
                per month is 617 times, the minimum is 364 times, and the average is about 476 times.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
        elif selected_status_3 == 'other':
            if selected_status_2 == 'day':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                In other locations in Dundee, Scotland, the number of electric vehicle charging points 
                used per day reaches 29 times at the highest and 0 times at the lowest, with an average 
                of about 13 times.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            elif selected_status_2 == 'week':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                In other locations in Dundee, Scotland, the number of charging points is high from Monday to Friday, 
                and the usage is significantly lowest from Saturday to Sunday. The weekly use of electric vehicle 
                charging piles reached a maximum of 813 times and a minimum of 378 times, with an average of about 
                671 times.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            else:
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                Charging piles at other locations in Dundee, Scotland, UK. The highest usage was in March and 
                the lowest in July. The monthly usage of electric vehicle charging piles reaches a maximum of 
                502 times, a minimum of 267 times, and an average of about 392 times.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
        elif selected_status_3 == 'Total_kWh':
            if selected_status_2 == 'day':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                The charging energy consumption of electric vehicle charging piles in Dundee, Scotland, 
                UK, the highest daily usage is 818.86, the lowest is 20.25, and the average is about 404.38.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            elif selected_status_2 == 'week':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                The charging energy consumption of electric vehicle charging piles in Dundee, Scotland, is very high 
                from Monday to Friday, and the consumption is obviously the lowest from Saturday to Sunday. The weekly 
                usage of electric vehicle charging piles reached a maximum of 25,302.91, a minimum of 11,235.46, and 
                an average of about 20,969.75.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            else:
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                Energy consumption for charging an electric vehicle charging point at a location in Dundee, 
                Scotland, UK. The usage has gradually decreased since January, and the number of usage has 
                increased since September. The monthly usage of electric vehicle charging piles reached a maximum 
                of 15,954.35, a minimum of 8,052.67, and an average of about 12,232.35.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
    elif selected_status_5 == 'box chart':
        if selected_status_3 == 'carpark':
            if selected_status_2 == 'day':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                In the park location of Dundee, Scotland, in the UK, there are seven extreme 
                values ​​in the box plot of the number of times of use of electric vehicle charging 
                piles per day in each month of the year.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            elif selected_status_2 == 'week':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                In the charging pile in the park of Dundee, Scotland, the use of electric vehicle 
                charging piles per week shows that there are eight extreme values ​​in the box chart, 
                and the range of use times on Sunday is the smallest, and the range of use times on 
                Friday is the largest.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            else:
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                In the charging pile at the park site in Dundee, Scotland, the monthly usage of 
                electric vehicle charging piles can be seen in the box chart with four extreme values, 
                and the usage range is the smallest in July and August, and the usage range in November. 
                maximum.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
        elif selected_status_3 == 'home':
            if selected_status_2 == 'day':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                At home charging piles in Dundee, Scotland, the use of electric vehicle charging 
                piles per day in each month of the year shows three extreme values in the box plot.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            elif selected_status_2 == 'week':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                At home charging piles in Dundee, Scotland, the weekly use of electric vehicle charging 
                piles shows twelve extreme values in the box chart, and the range of use times is the smallest
                 on Friday and the largest on Monday.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            else:
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                At home charging piles in Dundee, Scotland, the monthly usage of electric vehicle 
                charging piles can be seen in the box chart with four extreme values, and the range 
                of usage is the smallest in September and the largest in April and June.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
        elif selected_status_3 == 'street':
            if selected_status_2 == 'day':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                Using a box plot of the number of electric vehicle charging points used per day 
                for each month of the year at a charging pile at a street location in Dundee, 
                Scotland, it can be seen that there are seven extreme values.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            elif selected_status_2 == 'week':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                In the charging piles in the streets of Dundee, Scotland, the weekly use of electric vehicle 
                charging piles shows ten extreme values in the box chart, and the use frequency range is the 
                smallest on Sunday and the largest range on Saturday, Tuesday and Thursday.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            else:
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                At the charging piles in the streets of Dundee, Scotland, the monthly usage of electric vehicle 
                charging piles shows that there are twelve extreme values. The maximum number of times of use.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
        elif selected_status_3 == 'work':
            if selected_status_2 == 'day':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                In the charging pile at the workplace in Dundee, Scotland, the number of times of use 
                of the electric vehicle charging pile per day in each month of the year can be seen to 
                have an extreme value using the box plot.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            elif selected_status_2 == 'week':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                In the charging pile at the workplace in Dundee, Scotland, the use of electric vehicle charging 
                piles per week shows that there are six extreme values in the box chart, and the range of use times
                 is the smallest on Saturday and the largest range on Thursday.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            else:
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                In the charging pile at the workplace in Dundee, Scotland, the monthly usage of electric vehicle 
                charging piles shows an extreme value in the box chart, and the range of usage is the smallest in 
                August and the largest in January.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
        elif selected_status_3 == 'other':
            if selected_status_2 == 'day':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                In other locations in Dundee, Scotland, in the UK, there are five extreme values in the 
                box plot of the number of electric vehicle charging points used per day in each month of 
                the year.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            elif selected_status_2 == 'week':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                For charging piles in other locations in Dundee, Scotland, the weekly use of electric vehicle charging 
                piles shows seven extreme values in the box chart, and the range of use times is the smallest on Saturday 
                and the largest on Friday.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            else:
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                In the charging piles in other locations in Dundee, Scotland, the monthly use of electric vehicle 
                charging piles shows an extreme value in the box chart, and the range of use times is the smallest 
                in October and the largest in May.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
        elif selected_status_3 == 'Total_kWh':
            if selected_status_2 == 'day':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                In the charging energy demand of charging piles in Dundee, Scotland, there are six 
                extreme values.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            elif selected_status_2 == 'week':
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                In the charging energy consumption demand of charging piles in Dundee, Scotland, the weekly usage of 
                electric vehicle charging piles can be seen in a box-like chart with three extreme values, and the usage 
                range is the smallest on Sunday and the largest on Monday.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)
            else:
                st.write(' ')
                st.markdown("""
                -------------------------------------------------------------------------------------
                :round_pushpin:Simple Description:
                """)
                st.markdown("""
                In the charging energy consumption demand of charging piles in Dundee, Scotland, the monthly usage
                 of electric vehicle charging piles can be seen in the box chart with zero extreme values, and the 
                 usage range in July is the smallest, and the usage range in January maximum.
                """)
                st.markdown("""
                -------------------------------------------------------------------------------------
                """)

   











