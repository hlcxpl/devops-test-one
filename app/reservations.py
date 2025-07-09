def check_availability(reservations, new):
    for reservation in reservations:
        
        if (new["room"]== reservation["room"] and new["time"] == reservation["time"]):
            return False
    
    return True