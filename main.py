import dash

app = dash.Dash(__name__)
server = app.server
from visual import layout_all
from visual import plot_all
from data.preprocess import data4q1, data4q2, data4q3, data4q4, data4q5

q1_op, q1_df = data4q1()
q2_op, q2_df = data4q2()
q3_op, q3_df = data4q3()
q4_op, q4_df = data4q4()
q5_op = data4q5()

app.layout = layout_all.create_layout_all(q1_op, q2_op, q3_op, q4_op, q5_op)

plot_all.Plot_all(app, q1_df, q2_df, q3_df, q4_df)

del q1_op, q2_op, q3_op, q4_op, q1_df, q2_df, q3_df, q4_df, q5_op

if __name__ == '__main__':
    app.run_server(debug=True, port=8080)
