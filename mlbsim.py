# Input/Sim {
import pandas as pd
# }

# Sim {
# t_1: team 1; mlb_cr: mlb simmed season predictions as dictionary; for loop to iterate through team dictionary to predict entire league win/loss record
t_1 = ''
#use below for one team or whole dict for league sim
teams = ['ATL']
#teams = ['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CIN', 'CLE', 'COL', 'CWS', 'DET', 'HOU', 'KC', 'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT', 'SD', 'SEA', 'SF', 'STL', 'TB', 'TEX', 'TOR', 'WSH']
p_score_r = 0
p_score_w = 0
p_score = 0
r_score_r = 0
r_score_w = 0
r_score = 0
f1_score = 0
mlb_cr = {}
for t_1 in teams:

    # Input/Sim {
    # sets the year and prior year for testing
    # s: season length; y/yp: year and year prior used for test
    s = 162

    year = 2019
    y = str(year - 1)
    yp = str(year - 2)
    # }

    # Sim {
    # w/l: win/loss; g: game number of season; r_1/r_2/r_w/r_l: counts from bottom up to find last row with win/loss data, predicts win/loss from the next row to end; for loop sims the season for team selected above
    w = 0
    l = 0
    g = 1
    r_1 = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/MLB_Team_Data/"+t_1+str(year)+".csv",usecols=[10])
    #hide to get full season sim or unhide to get remaining season sim
    #g = r_1.count().get('W-L')
    r_2 = r_1.iat[g-1,0].split(sep='-')
    r_w = int(r_2[0]) 
    r_l = int(r_2[1])
    for g in range(g, s, 1):

        # Sim {
        # t_1_s: team 1's schedule; t_2_l: team 2's raw name pulled from csv; t_2: takes raw name and reformats for test; h_1_s/h/h_1/h_2: checks column for home field advantage attribute and awards extra points to home team
        date = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/MLB_Team_Data/"+t_1+str(year)+".csv",usecols=[1])
        d = date.iat[g-1,0]
        
        t_1_s = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/MLB_Team_Data/"+t_1+str(year)+".csv",usecols=[5])
        t_2_l = t_1_s.iat[g-1,0]

        t_2 = t_2_l.replace("WSN", "WSH").replace("SDP", "SD").replace("SFG", "SF").replace("TBR", "TB").replace("CHW", "CWS").replace("KCR", "KC")

        h_1_s = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/MLB_Team_Data/"+t_1+str(year)+".csv",usecols=[4])
        h = h_1_s.iat[g-1,0]
        if h is "@":
            h_1 = 0
            h_2 = .1
        else:
            h_1 = .1
            h_2 = 0
        # }

        # Input/Sim {
        # reads the csv files and gathers variables for each team(points for and against in current and prior year)
        # pyp/py: points for year prior/current year; oyp/oy: points against year prior/current year
        pyp_1 = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/MLB_Team_Data/"+t_1+yp+".csv",usecols=[7])
        py_1 = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/MLB_Team_Data/"+t_1+y+".csv",usecols=[7])
        oyp_1 = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/MLB_Team_Data/"+t_1+yp+".csv",usecols=[8])
        oy_1 = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/MLB_Team_Data/"+t_1+y+".csv",usecols=[8])
        pyp_2 = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/MLB_Team_Data/"+t_2+yp+".csv",usecols=[7])
        py_2 = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/MLB_Team_Data/"+t_2+y+".csv",usecols=[7])
        oyp_2 = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/MLB_Team_Data/"+t_2+yp+".csv",usecols=[8])
        oy_2 = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/MLB_Team_Data/"+t_2+y+".csv",usecols=[8])

        # takes variables from above and generates mean/median and standard dev for points for and against
        mmpyp_1 = pyp_1.mean() * ((s-g)/s) + pyp_1.median() * (g/s)
        sdpyp_1 = pyp_1.std()
        mmpy_1 = py_1.mean() * ((s-g)/s) + py_1.median() * (g/s)
        sdpy_1 = py_1.std()
        mmoyp_1 = oyp_1.mean() * ((s-g)/s) + oyp_1.median() * (g/s)
        sdoyp_1 = oyp_1.std()
        mmoy_1 = oy_1.mean() * ((s-g)/s) + oy_1.median() * (g/s)
        sdoy_1 = oy_1.std()
        mmpyp_2 = pyp_2.mean() * ((s-g)/s) + pyp_2.median() * (g/s)
        sdpyp_2 = pyp_2.std()
        mmpy_2 = py_2.mean() * ((s-g)/s) + py_2.median() * (g/s)
        sdpy_2 = py_2.std()
        mmoyp_2 = oyp_2.mean() * ((s-g)/s) + oyp_2.median() * (g/s)
        sdoyp_2 = oyp_2.std()
        mmoy_2 = oy_2.mean() * ((s-g)/s) + oy_2.median() * (g/s)
        sdoy_2 = oy_2.std()

        # takes mean/median/standard deviation and calculates a weighted average between current and prior season
        mmp_1 = mmpyp_1 * ((s-g)/s) + mmpy_1 * (g/s)
        sdp_1 = sdpyp_1 * ((s-g)/s) + sdpy_1 * (g/s)
        mmo_1 = mmoyp_1 * ((s-g)/s) + mmoy_1 * (g/s)
        sdo_1 = sdoyp_1 * ((s-g)/s) + sdoy_1 * (g/s)
        mmp_2 = mmpyp_2 * ((s-g)/s) + mmpy_2 * (g/s)
        sdp_2 = sdpyp_2 * ((s-g)/s) + sdpy_2 * (g/s)
        mmo_2 = mmoyp_2 * ((s-g)/s) + mmoy_2 * (g/s)
        sdo_2 = sdoyp_2 * ((s-g)/s) + sdoy_2 * (g/s)

        # combines mean/median/standard deviation so that game can be simulated using these variables
        ms = mmp_1.append(mmo_2).append(sdp_1).append(sdo_2).append(mmp_2).append(mmo_1).append(sdp_2).append(sdo_1)

        # calculates a 'balance' rating between the two teams using scoring differential to give advantage to better team and disadvantage to worse team
        srs = pyp_1.append(oyp_1).append(pyp_2).append(oyp_2).append(py_1).append(oy_1).append(py_2).append(oy_2)
        srsp_1 = (srs.iloc[0] - srs.iloc[1]) / (s - 1)
        srsp_2 = (srs.iloc[2] - srs.iloc[3]) / (s - 1)
        srs_1 = (srs.iloc[4] - srs.iloc[5]) / g
        srs_2 = (srs.iloc[6] - srs.iloc[7]) / g

        m_1 = (srsp_1 * ((s-g)/s) + srs_1 * (g/s))
        m_2 = (srsp_2 * ((s-g)/s) + srs_2 * (g/s))
        mm_sr = m_1.append(m_2)
        m = (mm_sr.iloc[0] - mm_sr.iloc[2]) / 2
        # }

        # Sim {
        msh_1 = (ms.iloc[0] + ms.iloc[2] * 2) * .5 + (ms.iloc[1] + ms.iloc[3] * 2) * .5 + m + h_1
        msl_1 = (ms.iloc[0] - ms.iloc[2] * 2) * .5 + (ms.iloc[1] - ms.iloc[3] * 2) * .5 + m + h_1
        #if msl_1 < 0:
        #    msl_1 = 0
        #else:
        #    msl_1 = (ms.iloc[0] - ms.iloc[2] * 2) * .5 + (ms.iloc[1] - ms.iloc[3] * 2) * .5 + m + h_1
        msh_2 = (ms.iloc[4] + ms.iloc[6] * 2) * .5 + (ms.iloc[5] + ms.iloc[7] * 2) * .5 - m + h_2
        msl_2 = (ms.iloc[4] - ms.iloc[6] * 2) * .5 + (ms.iloc[5] - ms.iloc[7] * 2) * .5 - m + h_2
        #if msl_2 < 0:
        #    msl_2 = 0
        #else:
        #    msl_2 = (ms.iloc[4] - ms.iloc[6] * 2) * .5 + (ms.iloc[5] - ms.iloc[7] * 2) * .5 - m + h_2
        c = (msh_1 - msl_1 + 1) * (msh_2 - msl_2 + 1)
        # }

        # Input/Sim {
        # takes high and low calculated from the average +- 2 standard deviations and simulates 95% of all possible outcomes for the game
        n_1 = 0
        n_2 = 0
        if msh_2 > msh_1:
            n_2 = (msh_2 - msh_1) * (msh_1 - msl_1 + 1) + ((((msh_1 - msl_1 + 1) - 1) / 2) * (msh_1 - msl_1 + 1))
            n_1 = c - n_2 - msh_1
        elif msh_2 < msh_1:
            n_1 = (msh_1 - msh_2) * (msh_2 - msl_2 + 1) + ((((msh_2 - msl_2 + 1) - 1) / 2) * (msh_2 - msl_2 + 1))
            n_2 = c - n_1 - msh_2

        p_1 = (n_1 / c) * 100 / .95
        p_2 = (n_2 / c) * 100 / .95
        if p_1 > 99:
            p_1 = 99
            p_2 = 1
        elif p_2 > 99:
            p_2 = 99
            p_1 = 1

        m_1 = mmp_1.combine(mmo_2, max, fill_value=0)
        m_2 = mmo_1.combine(mmp_2, max, fill_value=0)
        # }

        # Sim {
        mm_1 = m_1.mean() + m + h_1
        mm_2 = m_2.mean() - m + h_2
        mm = - mm_1 + mm_2

        po = - py_1.iat[g-1, 0] + oy_1.iat[g-1, 0]
        if po < 0 and mm < 0:
            p_score_r += 1
        elif po > 0 and mm > 0:
            r_score_r += 1
        elif po < 0 and mm > 0:
            r_score_w += 1
        elif po > 0 and mm < 0:
            p_score_w += 1

        if mm < 0:
            w += .6666
            l += .3434
        elif mm > 0:
            w += .3434
            l += .6666

        print(d, t_1, round(mm_1, 1), int(p_1), round(mm, 2), int(po), t_2, int(p_2), round(mm_1, 1), sep=',')
        g += 1
        # }

    #mlb_cr[str(t_1)] = (int(w) + r_w, int(l) + r_l)
    # }

#print(mlb_cr)
f1_score = (p_score_r / (p_score_r + p_score_w)) * .5 + (r_score_r / (r_score_r + r_score_w)) * .5
print(round(f1_score, 4))
# }