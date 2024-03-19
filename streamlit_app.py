# Import necessary libraries
import pandas as pd
import streamlit as st
import plotly.graph_objs as go

# df = pd.read_csv("data.csv")

def update_plot(x_axis, y_axis):
    fig = go.Figure(data=go.Scatter(x=df[x_axis],
                                    y=df[y_axis],
                                    mode='markers',
                                    text=df['Song'] + " by " + df['Artist'],
                                    marker=dict(color='LightSkyBlue', size=10, opacity=0.5)))
    
    fig.update_layout(title=f'{x_axis} vs. {y_axis}',
                      xaxis_title=x_axis,
                      yaxis_title=y_axis,
                      hovermode='closest')
    
    st.plotly_chart(fig)

# Create Streamlit widgets for selecting the X and Y axis data
x_axis = st.selectbox('Select X-axis:', options=df.columns, index=0)
y_axis = st.selectbox('Select Y-axis:', options=df.columns, index=1)

# Add a button to update the plot
st.button('Update Plot', on_click=update_plot, args=(x_axis, y_axis))
