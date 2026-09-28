GRAVITY = 9.81

def calculate_lift(air_dens, velocity, surface, cl):     #Calcula lift en Newtons
    lift = 0.5 * air_dens * velocity**2 * surface * cl
    return lift


def calculate_weight(mass):                                #Calcula weight en Newtons
    weight = mass * GRAVITY
    return weight


def calculate_drag(air_dens, velocity, surface, cd):        #Calcula drag en Newtons
    drag = 0.5 * air_dens * velocity**2 * surface * cd
    return drag


def calculate_vstall(air_dens, surface, weight, cl_max):    #Calcula velocidad de stall en m/s
    vstall = ((2 * weight) / (air_dens * surface * cl_max))**0.5
    return vstall


def calculate_ld_ratio(lift, drag):                         #Calcula el lift to drag ratio
    ld_ratio = lift/drag
    return ld_ratio