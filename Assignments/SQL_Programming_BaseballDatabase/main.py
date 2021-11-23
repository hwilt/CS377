import sqlite3

def query(con, stmt, params=None):
    cur = con.cursor()
    if params is None:
        result = cur.execute(stmt)
    else:
        result = cur.execute(stmt, params)
    con.commit()
    return result




def problem1(con):
    selectTeams = "SELECT W FROM teams where name = \"Philadelphia Phillies\" AND  YEARID = \"2019\";"
    res = query(con, selectTeams)
    phillywins = str(res.fetchall()[0][0])
    print("1. The Philadeplhia Phillies had " + phillywins + " in 2019")


def problem2(con):
    select = "SELECT H, name FROM teams WHERE YEARID = \"2019\" ORDER BY H desc ;"
    res = query(con, select)
    mostHits = str(res.fetchall()[0][1])
    print("\n2. " + mostHits + " had the most hits in 2019")


def problem3(con):
    select = "SELECT playerID FROM salaries where yearid = 2016 ORDER BY salary DESC;"
    res = query(con, select)
    highestplayer = res.fetchall()[0][0]
    select = "SELECT nameFirst, nameLast FROM people WHERE playerID = \"" + highestplayer + "\"; "
    res = query(con, select)
    names = res.fetchall()
    playerName = names[0][0] + " " + names[0][1]
    print("\n3. The highest player in 2016 was " + playerName)
    

def problem4(con):
    select = "SELECT nameFirst, nameLast FROM AllstarFull INNER JOIN People ON AllstarFull.playerID = PEOPLE.playerID WHERE yearID = 2019 AND GP = 1;"
    res = query(con, select)
    names = res.fetchall()
    print("\n4. Players who played in 2016 Allstar Game: ")
    for name in names:
        print("Name: " + name[0] + " " + name[1])

    
def problem5(con):
    select = "SELECT nameFirst, nameLast, name_full FROM CollegePlaying INNER JOIN Appearances ON CollegePlaying.playerID = Appearances.playerID INNER JOIN People ON CollegePlaying.playerID = People.playerID INNER JOIN Schools ON CollegePlaying.schoolID = Schools.schoolID WHERE Appearances.yearID = 2019;"
    res = query(con, select)
    players = res.fetchall()
    print("\n5. Players who played in the major leagues in 2019 that also played in college: ")
    print(players)
    # Uncomment this to see it formatted
    #for player in players:
        #print("Name: " + player[0] + " " + player[1] + ", School: " + player[2])
    
def problem6(con):
    select = "SELECT name, yearID FROM teams WHERE teams.WSWin = \"Y\" ORDER BY yearID ASC;"
    res = query(con, select)
    teams = res.fetchall()
    print("\n6. Every team that has won the world series from 1884")
    for team in teams:
        print("Team: " + team[0] + ", Year: " + str(team[1]))

def main():
    con = sqlite3.connect("lahmansbaseballdb.sqlite")
    problem1(con) 
    problem2(con)
    problem3(con)
    problem4(con)
    # There are so many results for problem 5 that it fills up the terminal so
    # only uncomment the problem when to check it.
    #problem5(con)
    problem6(con)

    con.close()



if __name__ == "__main__":
    main()
