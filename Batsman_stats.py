import numpy as np
import pandas as pd



matches = pd.read_csv('/Users/kunalkoshta/Desktop/Campux_X_DS/datas/IPL_Matches_2008_2022.csv')
ball = pd.read_csv('/Users/kunalkoshta/Desktop/Campux_X_DS/datas/IPL_Ball_by_Ball_2008_2022.csv')

main = pd.merge(matches,ball,how='inner',on='ID')
gp = main.groupby(['Season','bowler'])['isWicketDelivery'].sum().reset_index().sort_values('isWicketDelivery',ascending=False).drop_duplicates(['Season'],keep='first').sort_values('Season',ascending=False)

mask = main[main['overs']>15]
eco = mask.groupby(['bowler'])['isWicketDelivery'].sum().sort_values(ascending=False)

def batsman_name(b_name):
    bat_df = main[main['batter']==b_name]
    bat_df.set_index('Season',inplace=True)
    mask = bat_df.groupby(['Season'])
    total_runs = mask['batsman_run'].sum()
    avg = total_runs/mask['player_out'].count()
    no_of_balls = mask['isWicketDelivery'].count()-mask['isWicketDelivery'].sum()
    strikeRate = (total_runs/no_of_balls)*100
    asd = bat_df.groupby(['Season','ID'])
    wer = asd['batsman_run'].sum().reset_index()
    # print(wer)
    dict1 = {
        'Total Runs':total_runs,
        'Average':avg,
        'Strike Rate':strikeRate
    }
    df1 = pd.DataFrame(dict1)
    print(df1)

batsman_name('JC Buttler')


