def isPathCrossing( path: str) -> bool:
        list_of_visits=[[0,0]]
        start_x=0
        start_y=0
        if "NS" in path:
            return True
        if "SN" in path:
            return True
        if "WE" in path:
            return True
        if "EW" in path:
            return True
        for i in path:
            if i == "N":
                start_y+=1
            elif i =="E":
                start_x+=1
            elif i=="S":
                start_y-=1
            elif i=="W":
                start_x-=1
            if [start_x,start_y] in list_of_visits:
                return True
            list_of_visits.append([start_x,start_y] )
        print(list_of_visits)
        return False
print(isPathCrossing("NES"))
