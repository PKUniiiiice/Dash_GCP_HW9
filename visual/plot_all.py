from visual import plot_q1, plot_q2, plot_q3, plot_q4, plot_q5

def Plot_all(app,
             df1, df2, df3, df4):
    
    plot_q1.Plot_Q1(app, df1)
    plot_q2.Plot_Q2(app, df2)
    plot_q3.Plot_Q3(app, df3)
    plot_q4.Plot_Q4(app, df4)
    plot_q5.Plot_Q5(app)
    return
